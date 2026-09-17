#!/usr/bin/env python3
"""
pdftext.py — minimal dependency-free PDF text extractor, plus a claim checker.

Written because no pdftotext/pypdf is available in this environment. Handles the
common case for journal PDFs: FlateDecode content streams and the standard text
operators (Tj, TJ, ', "), including hex strings and basic ToUnicode mapping.

It is not a general PDF renderer. It will not read scanned images, and it makes
no attempt at layout — words come out in content-stream order, which is fine for
searching but not for reading tables.

Usage:
    python3 pdftext.py paper.pdf                     # dump text
    python3 pdftext.py paper.pdf --grep "84%" -C 120 # search with context
    python3 pdftext.py --check claims.tsv papers/    # verify figures in bulk

claims.tsv format (tab separated):
    doi <TAB> regex-to-find <TAB> human description of the claim
"""

import argparse, pathlib, re, sys, zlib


# ---------------------------------------------------------------- extraction

def _streams(data: bytes):
    """Yield decompressed content streams."""
    for m in re.finditer(rb"stream\r?\n", data):
        start = m.end()
        end = data.find(b"endstream", start)
        if end < 0:
            continue
        raw = data[start:end].rstrip(b"\r\n")
        for attempt in (raw, raw.lstrip(b"\r\n")):
            try:
                yield zlib.decompress(attempt)
                break
            except zlib.error:
                continue
        else:
            # some streams are stored uncompressed
            if b"Tj" in raw or b"TJ" in raw:
                yield raw


def _unescape(s: bytes) -> str:
    out, i = [], 0
    while i < len(s):
        c = s[i:i + 1]
        if c == b"\\" and i + 1 < len(s):
            nxt = s[i + 1:i + 2]
            mapping = {b"n": "\n", b"r": "", b"t": "\t", b"b": "", b"f": "",
                       b"(": "(", b")": ")", b"\\": "\\"}
            if nxt in mapping:
                out.append(mapping[nxt]); i += 2; continue
            oct_m = re.match(rb"[0-7]{1,3}", s[i + 1:i + 4])
            if oct_m:
                out.append(chr(int(oct_m.group(), 8)))
                i += 1 + len(oct_m.group()); continue
            i += 2; continue
        out.append(c.decode("latin-1", "replace")); i += 1
    return "".join(out)


def _hexstr(h: bytes) -> str:
    h = re.sub(rb"[^0-9A-Fa-f]", b"", h)
    if len(h) % 2:
        h += b"0"
    b = bytes.fromhex(h.decode())
    # UTF-16BE is common in hex strings; fall back to latin-1
    if len(b) >= 2 and b[0:1] == b"\x00":
        try:
            return b.decode("utf-16-be", "replace")
        except Exception:
            pass
    return b.decode("latin-1", "replace")


def extract(path: pathlib.Path) -> str:
    data = path.read_bytes()
    if not data.startswith(b"%PDF"):
        raise ValueError(f"{path.name} is not a PDF")
    chunks = []
    for st in _streams(data):
        # TJ arrays:  [ (Wor) -20 (d) ] TJ
        for m in re.finditer(rb"\[(.*?)\]\s*TJ", st, re.S):
            parts = []
            for piece in re.finditer(rb"\((.*?)(?<!\\)\)|<([0-9A-Fa-f\s]+)>", m.group(1), re.S):
                parts.append(_unescape(piece.group(1)) if piece.group(1) is not None
                             else _hexstr(piece.group(2)))
            chunks.append("".join(parts))
        # simple shows: (text) Tj   |   <hex> Tj   |   (text) '   |   (text) "
        for m in re.finditer(rb"\((.*?)(?<!\\)\)\s*(?:Tj|'|\")|<([0-9A-Fa-f\s]+)>\s*Tj", st, re.S):
            chunks.append(_unescape(m.group(1)) if m.group(1) is not None
                          else _hexstr(m.group(2)))
        if re.search(rb"\bT\*|\bTd\b|\bTD\b", st):
            chunks.append("\n")
    text = " ".join(chunks)
    text = text.replace("ﬁ", "fi").replace("ﬂ", "fl")
    text = re.sub(r"[ \t]+", " ", text)
    return re.sub(r"\n\s*\n+", "\n", text)


# ---------------------------------------------------------------- claim check

def check(claims_file: pathlib.Path, papers_dir: pathlib.Path):
    rows, found, missing, unreadable = [], 0, 0, 0
    for line in claims_file.read_text().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        doi, pattern, desc = (line.split("\t") + ["", ""])[:3]
        stem = re.sub(r"[^A-Za-z0-9._-]", "_", doi.strip())
        cand = [papers_dir / f"{stem}.pdf", papers_dir / f"{stem}.xml"]
        path = next((c for c in cand if c.exists()), None)
        if path is None:
            rows.append(("NO FILE", doi, desc, "")); unreadable += 1; continue
        try:
            text = (extract(path) if path.suffix == ".pdf"
                    else re.sub(r"<[^>]+>", " ", path.read_text(errors="replace")))
        except Exception as e:
            rows.append(("UNREADABLE", doi, desc, str(e)[:50])); unreadable += 1; continue
        m = re.search(pattern, text, re.I)
        if m:
            i = max(0, m.start() - 100)
            ctx = re.sub(r"\s+", " ", text[i:m.end() + 100]).strip()
            rows.append(("FOUND", doi, desc, ctx)); found += 1
        else:
            rows.append(("NOT FOUND", doi, desc, f"{len(text)} chars searched")); missing += 1

    w = max((len(r[1]) for r in rows), default=10)
    for status, doi, desc, ctx in rows:
        print(f"{status:11} {doi:<{w}}  {desc}")
        if ctx:
            print(f"            …{ctx}…\n")
    print(f"\n  confirmed {found} · not found {missing} · unreadable {unreadable}")
    return 0 if missing == 0 and unreadable == 0 else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target", type=pathlib.Path, nargs="?")
    ap.add_argument("--grep", help="regex to search for")
    ap.add_argument("-C", "--context", type=int, default=100)
    ap.add_argument("--check", type=pathlib.Path, metavar="CLAIMS.TSV")
    a = ap.parse_args()

    if a.check:
        return check(a.check, a.target or pathlib.Path("papers"))

    text = extract(a.target)
    if not a.grep:
        print(text)
        return 0
    hits = list(re.finditer(a.grep, text, re.I))
    if not hits:
        print(f"no match for {a.grep!r} in {len(text)} chars of extracted text")
        return 1
    for m in hits:
        i = max(0, m.start() - a.context)
        print("…" + re.sub(r"\s+", " ", text[i:m.end() + a.context]).strip() + "…\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
