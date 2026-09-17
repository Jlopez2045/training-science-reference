#!/usr/bin/env python3
"""
fetch-papers.py — download open-access full text for a list of DOIs, and
produce a request list for whatever is left.

Sources, in order of preference (all legal, all publisher-sanctioned):
  1. Unpaywall      — locates author manuscripts and publisher OA copies
  2. Europe PMC     — PMC open-access subset, full text as PDF or XML
  3. bioRxiv/medRxiv preprints via Crossref relations

Whatever has no OA copy is written to requests.csv, formatted for an
interlibrary-loan form, plus an author-email template per paper.

Usage:
    python3 fetch-papers.py dois.txt --email you@example.com [--out pdfs/]
    python3 fetch-papers.py dois.txt --email you@example.com --dry-run
"""

import argparse, csv, json, pathlib, re, sys, time, urllib.parse, urllib.request

UA = "fetch-papers/1.0 (mailto:%s)"
TIMEOUT = 30


def get_json(url, email):
    req = urllib.request.Request(url, headers={"User-Agent": UA % email,
                                               "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
        return json.load(r)


def safe_name(doi):
    return re.sub(r"[^A-Za-z0-9._-]", "_", doi) + ".pdf"


def unpaywall(doi, email):
    """Return (is_oa, pdf_url, meta) from Unpaywall."""
    j = get_json(f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={email}", email)
    meta = {
        "title": (j.get("title") or "").strip(),
        "journal": (j.get("journal_name") or "").strip(),
        "year": j.get("year"),
        "first_author": "",
        "publisher": (j.get("publisher") or "").strip(),
    }
    auth = j.get("z_authors") or []
    if auth:
        meta["first_author"] = (auth[0].get("family") or "").strip()
    if not j.get("is_oa"):
        return False, None, meta
    # prefer a direct PDF; fall back to the landing page
    for loc in filter(None, [j.get("best_oa_location")] + (j.get("oa_locations") or [])):
        if loc.get("url_for_pdf"):
            return True, loc["url_for_pdf"], meta
    loc = j.get("best_oa_location") or {}
    return True, loc.get("url"), meta


def europepmc_pdf(doi, email):
    """Find a PMC open-access PDF for this DOI, if one exists."""
    q = urllib.parse.quote(f'DOI:"{doi}"')
    j = get_json(f"https://www.ebi.ac.uk/europepmc/webservices/rest/search"
                 f"?query={q}&resultType=core&format=json", email)
    for res in j.get("resultList", {}).get("result", []):
        if res.get("isOpenAccess") == "Y" and res.get("pmcid"):
            return (f"https://www.ebi.ac.uk/europepmc/webservices/rest/"
                    f"{res['pmcid']}/fullTextPdf")
    return None


def _fetch(url, email, tries=3):
    """GET with polite retry/backoff. Some publishers reject bare API agents."""
    last = None
    for n in range(tries):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": UA % email,
                "Accept": "application/pdf,text/xml,*/*",
            })
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (429, 500, 502, 503):      # transient — wait and retry
                time.sleep(2 ** n * 3)
                continue
            raise
        except Exception as e:
            last = e
            time.sleep(2 ** n)
    raise last


def europepmc_xml(doi, email):
    """Europe PMC full-text XML — available for some records with no PDF."""
    q = urllib.parse.quote(f'DOI:"{doi}"')
    j = get_json(f"https://www.ebi.ac.uk/europepmc/webservices/rest/search"
                 f"?query={q}&resultType=core&format=json", email)
    for res in j.get("resultList", {}).get("result", []):
        if res.get("pmcid") and res.get("hasTextMinedTerms") is not None:
            return (f"https://www.ebi.ac.uk/europepmc/webservices/rest/"
                    f"{res['pmcid']}/fullTextXML")
    return None


def download(url, dest, email, doi=None):
    data = _fetch(url, email)
    if data.startswith(b"%PDF"):
        dest.write_bytes(data)
        return True, f"{len(data)//1024} KB"
    # not a PDF — try Europe PMC full-text XML, which is just as readable
    if doi:
        try:
            x = europepmc_xml(doi, email)
            if x:
                xd = _fetch(x, email)
                if b"<article" in xd[:4000]:
                    dest.with_suffix(".xml").write_bytes(xd)
                    return True, f"{len(xd)//1024} KB (full-text XML)"
        except Exception:
            pass
    return False, "not a PDF (landing page or HTML)"


EMAIL_TEMPLATE = """\
Subject: Request for a copy of your paper — {title}

Dear Dr {author},

I am reading around {topic} and would like to consult your paper:

    {citation}
    doi:{doi}

My institution does not have access. Would you be willing to send a copy
of the accepted manuscript? Authors are normally permitted to share their
own work directly.

Thank you for your time.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("doi_file", type=pathlib.Path)
    ap.add_argument("--email", required=True, help="required by the Unpaywall API")
    ap.add_argument("--out", type=pathlib.Path, default=pathlib.Path("papers"))
    ap.add_argument("--topic", default="exercise physiology and energy metabolism")
    ap.add_argument("--dry-run", action="store_true", help="classify only, download nothing")
    ap.add_argument("--delay", type=float, default=1.0, help="seconds between API calls")
    a = ap.parse_args()

    dois = [l.strip() for l in a.doi_file.read_text().splitlines()
            if l.strip() and not l.startswith("#")]
    a.out.mkdir(parents=True, exist_ok=True)

    got, closed, failed = [], [], []

    for i, doi in enumerate(dois, 1):
        print(f"[{i}/{len(dois)}] {doi}", end=" … ", flush=True)
        try:
            is_oa, url, meta = unpaywall(doi, a.email)
        except Exception as e:
            print(f"lookup failed: {e}")
            failed.append((doi, str(e)))
            time.sleep(a.delay)
            continue

        if not is_oa:
            url = None
            try:
                url = europepmc_pdf(doi, a.email)     # Unpaywall occasionally misses PMC
            except Exception:
                pass
            if not url:
                print("paywalled")
                closed.append((doi, meta))
                time.sleep(a.delay)
                continue
            print("OA via Europe PMC", end=" … ")

        # Unpaywall's "OA" link is often a landing page; prefer a real PMC PDF
        pmc = None
        try:
            pmc = europepmc_pdf(doi, a.email)
        except Exception:
            pass
        alt = [u for u in (pmc, url) if u]      # try PMC first, fall back to Unpaywall

        if a.dry_run:
            print("OA (dry run)")
            got.append((doi, meta))
            time.sleep(a.delay)
            continue

        dest = a.out / safe_name(doi)
        if dest.exists() or dest.with_suffix(".xml").exists():
            print("already have it")
            got.append((doi, meta))
            continue
        try:
            ok, note = False, "no usable link"
            for cand in alt:
                try:
                    ok, note = download(cand, dest, a.email, doi)
                    if ok:
                        break
                except Exception as e:
                    note = str(e)[:60]
            print("saved " + note if ok else f"skipped — {note}")
            (got if ok else closed).append((doi, meta))
        except Exception as e:
            print(f"download failed: {e}")
            failed.append((doi, str(e)))
        time.sleep(a.delay)

    # ---- request list for everything that stayed closed ----
    if closed:
        req = a.out / "requests.csv"
        with req.open("w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["doi", "first_author", "year", "title", "journal", "publisher"])
            for doi, m in closed:
                w.writerow([doi, m["first_author"], m["year"], m["title"],
                            m["journal"], m["publisher"]])

        tpl = a.out / "author-emails.txt"
        with tpl.open("w") as f:
            for doi, m in closed:
                cite = f"{m['first_author']} et al. {m['title']}. {m['journal']}. {m['year']}."
                f.write(EMAIL_TEMPLATE.format(
                    title=m["title"][:70], author=m["first_author"] or "[author]",
                    citation=cite, doi=doi, topic=a.topic))
                f.write("\n" + "-" * 72 + "\n\n")

    print(f"\n  open access, retrieved : {len(got)}")
    print(f"  paywalled              : {len(closed)}")
    print(f"  lookup/download errors : {len(failed)}")
    if closed:
        print(f"\n  → {a.out/'requests.csv'}      paste into an interlibrary-loan form")
        print(f"  → {a.out/'author-emails.txt'}  one drafted request per paper")
        print("\n  Interlibrary loan is free at most public and university libraries")
        print("  and usually turns these around in 1–3 days.")


if __name__ == "__main__":
    sys.exit(main())
