# House Style — strength-and-body-composition.md

Binding for all reviewers. Rewrites that violate any rule below are rejected at merge, not negotiated.

## 1. Inline citations

Cite in running text, never in a footnote, never as a bare URL, never as a numbered reference list.

- Named study: **`(Author year)`** — `(Alfredson et al., 1998)`, `(Hall, 2019)`. First author + `et al.` above two authors.
- Named trial or cohort: use its name in bold, no parenthetical — **MATADOR trial**, **STEP-1**, **SURMOUNT-1**, **CALERIE**, **NWCR**. If the name is not self-explanatory, it gets a glossary entry.
- Named model or protocol: name + originator in parentheses — `Continuum model of tendon pathology (Cook & Purdam, 2009)`.
- Never cite a claim you cannot name. Write `several recent trials`, `metabolic ward studies`, `replicated across cohorts` instead of inventing a citation.
- One citation per claim. Do not stack.

## 2. Confidence labels

Every empirical claim carries exactly one of four labels, written as running prose, in bold, at the point of the claim. Do not invent synonyms.

| Label | Written as | Means |
|---|---|---|
| strong | *(unmarked — the default)* | Replicated, consistent, direct evidence. State it plainly with no hedge. |
| moderate | **Moderate evidence** / **well-supported** | Consistent direction, limited replication or indirect measures. |
| limited | **Promising but under-replicated** / **evidence remains limited and inconsistent** | Mechanistically plausible; outcome data thin. |
| contested | **Contested** / **weak and contested** / **not supported** | Actively disputed, or tested and failed. |

Rules: the same finding carries the **same** label everywhere it appears — body text and glossary must agree. A caveat attached to a finding (`**Caveat:** …`, `**Interpretive caution:** …`, `**Validity caveat:** …`) is bolded and placed *after* the claim, never before it. Never bury a downgrade: if the glossary says "contested", the body text may not state it flatly.

## 3. Plain-English lead, then technical sentence

Every glossary entry is exactly three moves, in this order, in one paragraph unless a formula forces a break:

1. **Lead sentence — plain English.** One sentence a 16-year-old reads once and understands. No jargon, no abbreviation, no term that itself needs the glossary. Concrete before abstract. It must define, not describe: say what the thing *is*, never only what it does or why it is interesting.
2. **Formal definition**, opened with `Formally:` (or a colon before a display formula). Full technical precision, plus formula and units wherever the quantity is physically or operationally defined. Formulas go in a blockquote on their own line with units in parentheses.
3. **Why it matters**, only if not already obvious from (1) and (2).

Hard constraints: the lead sentence must stand alone if the rest of the entry is deleted. `See [X](#x)` is never a definition — an entry that defers must still define. No entry may be reconstructible only by someone who already knows the term.

## 4. Tables and dosing cards

**Tables.** Pipe tables, header row mandatory, `|---|` separator, no alignment colons. Column 1 is the thing; the last column is the verdict, note, or consequence. Cells are fragments, not sentences — no terminal full stop. Bold the operative word in a verdict cell (`**False.**`, `**Avoid.**`). A table replaces prose only when every row shares the same columns; otherwise write prose.

**Dosing cards.** Fenced code blocks, no language tag. Label column padded to a common width, values left-aligned in a second column. Order is always: load → tempo → sets/reps → rest → total dose → frequency → timeline. Ranges use an en dash with no spaces (`3–4`), units follow the number with a space except for `%` and `°`. A dosing card states doses only; justification lives in the surrounding prose.

## 5. First mention links to the glossary

- The **first** occurrence of a technical term **in each Part** links to its glossary entry: `[term](#slug)`. Subsequent mentions in that Part are plain text.
- Link text is the term as it reads in the sentence; the target is the slug. Link text and target must denote the **same concept** — never link a general term to a specific protocol (`[tendon adaptation](#hsr)` is a defect), and never link a practice to a principle (`[resistance training](#progressive-overload)` is a defect).
- Glossary headings are written already in slug form: lowercase ASCII, hyphens for spaces, no punctuation. The human-readable term is the bold lead-in of the entry. Headings never change — they are load-bearing link targets.
- Entries stay in strict ASCII-sorted order by slug.
- Links are same-file anchors only. No HTML anchors, no relative file links, no external links.
- Cross-references between Parts are written `Part II §B.1` — never `above`, `below`, or a bare `§1`.

## 6. Ambiguous words — mandatory disambiguation

These words carry more than one sense in this document. Every use must make the sense unambiguous, by qualifier or by link.

| Word | Senses | Rule |
|---|---|---|
| intensity | intensity of load (%1RM) / intensity of effort (RIR) / high-intensity plyometrics | Always qualified. Bare "intensity" in a programming context means **load**. |
| load | the weight lifted / cumulative training dose | Bare "load" = weight. Cumulative sense is written "training load". |
| volume | sets per muscle / volume load / total reps | Name the operationalization on first use in each Part. |
| stiffness | mechanical property (N·mm⁻¹) / morning stiffness (symptom) | The symptom is always written "morning stiffness". |
| strain | mechanical deformation (ε) / muscle-strain injury | The injury is always written "muscle-strain injury". |
| failure | momentary failure / technical failure / volitional termination | Always qualified. "Clean technique" criteria mean technical failure. |
| adaptation | training gain (Parts I–II) / defensive expenditure reduction (Part III) | In Part III always written "metabolic adaptation" or "adaptive thermogenesis". |
| CSA | tendon / muscle / anatomical vs PCSA | Name the tissue. |
| deload vs taper | recovery within a block / peaking for a date | Never used interchangeably. |

## 7. Numbers and units

SI unless field convention dictates otherwise (tendon stiffness in N·mm⁻¹, GCT in ms, energy in kcal). Ranges use en dashes. Approximations carry `~`. Never change a number during a language edit — report a suspected error to the numbers reviewer instead.
