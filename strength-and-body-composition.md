# Strength, Hypertrophy, Tendon Science and Fat Loss — Complete Reference

> A single self-contained reference covering resistance-training progression, tendon and
> connective-tissue science, and the energetics of fat loss. Part IV is a master glossary
> defining every term used.
>
> **General education only — not medical, physiotherapeutic, or dietetic advice.** Persistent or
> acute pain, existing injury, endocrine or metabolic disease, pregnancy, adolescence, and any
> history of disordered eating all require professional guidance rather than a self-directed
> program.

## Contents

1. **Part I — Exercise Progression**
2. **Part II — Tendon Strength**
3. **Part III — Fat Loss and Metabolic Adaptation**
   - Read the **STOP — read before you start** block at the head of Part III before using any protocol in it.
   - **[When this stops being a programming problem](#when-this-stops-being-a-programming-problem)** — eating-disorder warning signs and where to get help. If you read one section of Part III, read that one.
4. **Part IV — Master Glossary** (278 entries)
5. **Part V — Bibliography** (105 sources, 58 open access)

**How to read this.** The first occurrence of a technical term in each section links to its
glossary entry in Part IV.

**Anchor convention.** Markdown has no standard for heading anchors — VS Code slugifies headings
(GitHub rules), pandoc uses its own `auto_identifiers`, and Obsidian matches the literal heading
text. The three disagree. Glossary headings are therefore written **already in slug form**
(lowercase ASCII, hyphens for spaces), which is the fixed point of all three algorithms: every
renderer maps it to itself. The human-readable term is the bold lead-in of each entry. Links are
same-file only — no HTML anchors, no relative file links, nothing renderer-specific.

---
# Part I Exercise Progression

> Evidence-based reference for beginner/intermediate hypertrophy training, progression models, and dose–response.
> General guidance only — not a substitute for a physician or physiotherapist if you have pain, injury, or medical conditions.


---

### 0. Two prerequisites that gate everything below

Training is the signal. Food is the raw material. Get these wrong and nothing in §1–§9 rescues you.

**Protein — eat ~1.6 g per kg of bodyweight per day.** Pooling 49 trials and 1,863 participants, gains in fat-free mass stopped improving above ~1.62 g·kg⁻¹·day⁻¹ (Morton et al., 2018). More than that is not harmful, merely not useful.

**Calories — you can build muscle in a deficit, but slowly.** Across controlled trials of ≥3 weeks, training in an energy deficit substantially blunted lean-mass gains while leaving strength gains essentially intact (Murphy & Koehler, 2022). Practical reading: below maintenance, expect your lifts to keep climbing while the tape measure stalls — that is the diet, not the program. Sustained low [energy availability](#energy-availability) lowers the ceiling further.

Sleep and non-training stress also move that ceiling, but the effect has not been quantified precisely enough to give a number [consensus — no single source].

---

### 1. The core principle

**[Progressive overload](#progressive-overload)** = the training stimulus must keep exceeding what the tissue has already adapted to. That is the only non-negotiable. *How* you overload appears to be largely interchangeable: when [volume](#training-volume) — counted here as [hard sets](#hard-set) per muscle per week — and [proximity to failure](#proximity-to-failure) are equated, different schemes produce similar [hypertrophy](#hypertrophy). **Caveat:** that conclusion is assembled from trials comparing *periodization models* (Grgic et al., 2017), *loads*, and *rep tempos* — no trial has ever compared progression *rules* head to head, so the claim is an extrapolation [UNVERIFIED — could not confirm a direct trial of progression schemes].

**Overload variables (ranked by practical usefulness for hypertrophy):**

| Variable | Notes |
|---|---|
| [Load](#load) (weight) | Most obvious; limited by strength gains, which are slower than you'd like |
| [Reps](#repetition) | Primary beginner lever; cheap and precise |
| [Sets](#set) (volume) | Strongest single [dose–response](#dose-response-relationship) signal for hypertrophy, with diminishing returns and recovery cost (Pelland et al., 2026) |
| Proximity to failure ([RIR](#rir)) | Real but small effect; *spends* recovery — not a lever you can pull forever (Robinson et al., 2024) |
| [ROM](#rom) / exercise variant | Fuller ROM, especially [lengthened position](#lengthened), is a real progression (Pallarés et al., 2021) |
| [Density](#training-density) (rest reduction) | Mostly a conditioning lever; can *hurt* hypertrophy if it cuts load (Schoenfeld et al., 2016) |
| [Frequency](#training-frequency) | Mostly a way to distribute volume, not an independent stimulus (Schoenfeld et al., 2019) |
| [Tempo](#tempo) / eccentric control | Minor for hypertrophy; more relevant for [heavy slow tendon loading](#hsr) (Schoenfeld et al., 2015) |

**Underlying mechanism:** hypertrophy is driven principally by **[mechanical tension](#mechanical-tension)** — force pulling along the fiber — sensed by [mechanosensors](#mechanotransduction) in muscle fibers, which raises [muscle protein synthesis](#mps-mpb) via [mTOR](#mtor-mtorc1) signaling (Wackerhage et al., 2019). [Metabolic stress](#metabolic-stress) and [muscle damage](#muscle-damage) are secondary and largely act *through* tension rather than independently of it. **Moderate evidence** for the tension-primacy framing; which sensor dominates in human muscle is still unresolved (Roberts et al., 2023).

---

### 2. Double progression (the "8–12" model)

The default for beginners and the most robust scheme in practice.

**Rules:**
1. Pick a [rep range](#rep-range) (e.g. 8–12) and a target [set](#set) count.
2. Start at a [load](#load) you can do for the **bottom** of the range with ~2 [RIR](#rir).
3. Each session, add reps where you can.
4. When **all sets** hit the **top** of the range with clean technique (i.e. no rep past [technical failure](#technical-failure)), increase load.
5. The load jump drops you back near the bottom of the range. Repeat.

**Example (3 sets):**

```
Wk 1   60 kg × 9, 8, 8
Wk 2   60 kg × 10, 9, 9
Wk 3   60 kg × 11, 10, 10
Wk 4   60 kg × 12, 12, 12   ← top of range, all sets
Wk 5   62.5 kg × 9, 8, 8    ← reload (+4.2%), cycle restarts
```

**Load increment guidance:** aim for ~2.5–5% of the working weight. The absolute jumps below are what standard gym equipment actually offers:
- Lower-body [compounds](#compound) → 2.5–5 kg, which on a 60–150 kg lift *is* the 2.5–5% target
- Upper-body [isolation](#isolation) → 1–2.5 kg, which on a 10–25 kg lift is **4–25%** — far above target, and the reason these lifts stall first
- [Micro-loading](#micro-loading) (0.5–1.25 kg) exists to close exactly that gap: it is not an optional refinement on light lifts but the only way to hit the percentage rule on them

Read the percentage as the goal and the plate as the constraint. Where the smallest available plate exceeds ~5%, add reps or a set instead of load until micro-plates are available. *These increments are gym convention; no trial has compared increment sizes* [UNVERIFIED — could not confirm].

**Why a rep *range* rather than fixed reps:** it decouples progression from daily readiness. Bad sleep? You still progress at the low end. It also keeps you inside the hypertrophy-effective zone.

**Rep-range evidence:** roughly **5–30 reps** produces similar hypertrophy *if sets are taken close to failure*. Pooling 21 studies, loads at or below 60% [1RM](#one-rep-max) and loads above it produced statistically indistinguishable muscle growth, while maximal strength clearly favored heavy loads (Schoenfeld et al., 2017b). **Caveat:** most of those trials ran 8–12 weeks in untrained or lightly trained participants, and the light-load arms were typically taken to failure while the heavy arms often were not — so the comparison is not perfectly clean.

Below ~5 reps, hypertrophy per set drops and joint/tendon cost rises; above ~30, [effort tolerance](#effort-tolerance) becomes the limiter. 6–15 is the practical sweet spot: enough load for tension, low enough discomfort to actually reach failure proximity. **8–12 is popular because it balances all of this — not because it is a privileged range.**

---

### 3. Progression models, ranked by training age

#### [Linear progression (LP)](#linear-progression) — beginners
Add load every session or every week. Works only because [novice adaptation](#novice-effect) is fast, and early strength gain is substantially [neural](#neural-adaptation) rather than structural (Del Vecchio et al., 2019). **Caveat:** that study tracked motor units over 4 weeks of isometric ankle training in a small sample, so treat the timeline as indicative, not as a boundary.

The three variants below run out at different times, which is why a single "LP lasts *N* months" figure is meaningless:

- **Session-to-session LP** — 2.5–5 kg/session on compounds. Exhausts itself in **8–16 weeks**.
- **Weekly LP** — same increments, applied one-seventh as often; commonly stretches to **6–12 months**.
- **[Double progression](#double-progression)** — see §2; the most durable form, and the one that can persist for years.

*All three durations are coaching convention, not measured outcomes* [UNVERIFIED — could not confirm].

**When it [stalls](#stall):** repeat the weight, then reduce load ~10% and re-climb (a **[reset](#reset)**). Two failed resets = graduate to a different model.

#### [Undulating periodization](#undulating) — intermediates
Vary reps/intensity within the week ([DUP](#dup)) or across weeks ([WUP](#undulating)).

```
DUP example, same lift 3×/wk:
Mon  4 × 5   heavy
Wed  3 × 12  light
Fri  3 × 8   medium
```

Evidence: DUP ≈ [linear periodization](#linear-periodization) for hypertrophy when volume is equated — a meta-analysis found the two produce likely-similar muscle growth (Grgic et al., 2017). Its real benefit is **variety, joint-stress distribution, and [adherence](#adherence)**, not a superior growth signal. **Caveat:** the pooled trials were mostly short and mostly in untrained participants, and several individual studies have favored DUP for *strength*, so a small real difference could still be hiding in the noise.

#### [Block periodization](#block-periodization) — advanced / strength-focused
Sequential emphasis: **accumulation** (high volume, moderate load) → **intensification** (lower volume, higher load) → **realization/peak**. Meaningful for powerlifting; largely unnecessary for pure hypertrophy.

#### [Autoregulation](#autoregulation) — any level, best for intermediates and above
Progression driven by *daily readiness* rather than a fixed script.

- **RIR/[RPE](#rpe)-based:** prescribe "3 sets @ RPE 8 (2 RIR)" and let load float.
  **Validity caveat:** people are simply bad at judging how many reps they have left, and the error runs toward stopping earlier than they believe. Across 12 studies and 414 participants, accuracy improved as the set approached failure and as loads got heavier — but resistance-training *experience* did **not** measurably improve it (Halperin et al., 2022). So the familiar claim that beginners are inaccurate while trained lifters are reliable is **not supported**; everyone is inaccurate far from failure. The fix is the same for both: periodically take a set to real [momentary failure](#momentary-failure) on a safe machine exercise to learn what your own estimates actually mean.
- **[Velocity-based training (VBT)](#vbt):** terminate the set when bar velocity drops a set percentage below the first rep ([velocity loss threshold](#velocity-loss-threshold)). **Moderate evidence** for strength applications, from small trials confined largely to squat and bench press (Pareja-Blanco et al., 2017); requires equipment and is overkill for beginners, whose technical variability makes the velocity signal noisy.
- **[AMRAP](#amrap)-driven:** the last set is an AMRAP; if reps exceed a threshold, load increases next session.

#### [Volume progression](#volume-progression) (set progression)
Instead of adding load, add sets across a [mesocycle](#mesocycle):

```
Wk 1  3 sets/exercise
Wk 2  4 sets
Wk 3  5 sets
Wk 4  6 sets   ← approaching the recovery ceiling
Wk 5  deload (~half volume, load maintained)
```

Evidence: a real [dose–response](#dose-response-relationship) exists between weekly [sets per muscle group](#sets-per-muscle-group-per-week) and hypertrophy, roughly **~4 up to ~20+ sets/muscle/week**, with clearly diminishing returns past ~10–20 (Pelland et al., 2026). That meta-regression also found that *how you count* matters: crediting indirect involvement as a fraction of a set predicts outcomes better than counting direct sets alone.

**Interpretive caution:** the measured curve rises with diminishing returns and **no clear plateau was identified** within the volumes studied — the best fit was a square-root model, and the authors state the data support diminishing returns but not an inverted-U. Nor does it turn downward: no meta-analysis has observed a group-level decline, so the familiar inverted-U is an expectation, not a finding. Two caveats belong with that. Uncertainty grows at the top of the range, because few studies have examined beyond ~25 fractional sets per week. And the asymmetry matters — in that same meta-regression the *functional plateau* belongs to **strength**, not to hypertrophy. Individual [MRV](#mrv) is still the practical limiter and varies widely. **Do not add sets and load in the same week** — you lose the ability to attribute the result to either [consensus — no single source].

---

### 4. Proximity to failure

- Training to [failure](#momentary-failure) and stopping a few reps short produce nearly the same hypertrophy. Pooling 15 studies, sets to failure held only a trivial advantage over non-failure sets (Refalo et al., 2023). Going to failure adds [fatigue](#fatigue) cost without proportional benefit.
- **The relationship is not flat, though, and it is worth stating precisely.** A meta-regression across the literature found hypertrophy improving *slightly* as sets are taken closer to failure — the slope was negative and its confidence interval excluded the null (Robinson et al., 2024). So "**0–3 [RIR](#rir)** is all equivalent" overstates it: the growth penalty for stopping 1–3 reps short is small but real. **For strength the same analysis found nothing.** Every best-fit strength model's interval contained the null, and the two models pointed in *opposite* directions, so no direction is claimable — strength gains were similar across a wide range of RIR. **Validity caveat:** these regressions rest on *estimated* RIR, which §3 has already shown to be unreliable.
- Failure matters more for **light loads (>20 reps)**, where [motor-unit recruitment](#motor-unit-recruitment) is otherwise incomplete. The parallel claim for **[isolation](#isolation)/single-joint** work is reasoning from [SFR](#sfr) rather than direct evidence [consensus — no single source].
- On heavy [compounds](#compound) (squat, deadlift), failure is costly and technically risky — stay 1–3 RIR.
- **Practical:** on isolation work, take the last set to 0–1 RIR and earlier sets to 2–3 RIR. On heavy compounds, hold every set at 1–3 RIR, including the last one — the bullet above overrides the general rule rather than being an exception to it.

**Mechanistic reason failure isn't required:** by the [size principle](#size-principle), high-threshold [motor units](#motor-unit) are recruited once force demand is high enough (Henneman et al., 1965) — which occurs several reps before failure with moderate-to-heavy loads. The final reps add fatigue faster than they add stimulus, worsening the [stimulus-to-fatigue ratio](#sfr).

---

### 5. Range of motion as a progression variable

- **Full [ROM](#rom) ≥ [partial ROM](#partial-rom)** for hypertrophy in most comparisons. Pooling 16 studies, full ROM produced greater strength and greater lower-limb hypertrophy than partial ROM (Pallarés et al., 2021).
- **That average hides the important detail: "partials" is not one thing.** **[Lengthened partials](#lengthened-partials)** (repetitions restricted to the stretched half of the range) produced adaptations similar to full-ROM training in trained individuals (Wolf et al., 2025a), whereas partials in the shortened half are the ones dragging the pooled average down. **Promising but under-replicated** — a legitimate progression tool once full ROM is exhausted, not a replacement for establishing full ROM first.
- Training at [long muscle lengths](#lengthened) shifts *where* growth occurs along a muscle ([regional hypertrophy](#regional-hypertrophy)) and gives better ROM carryover. The further claim that it adds [fascicle length](#fascicle-length-adaptation) is **weak and contested**: a systematic review of exactly this question found the evidence suggestive but inconclusive, because nearly every study estimated fascicle length by linear extrapolation from ultrasound — a method of questionable validity — and none has counted serial sarcomeres in humans (Wolf et al., 2025b).
- ROM should be *established first, then loaded*. Adding load by shortening ROM is not progression — it is [load cheating](#load-cheating).

---

### 6. Realistic rates of progress

| Training age | Muscle gain (male, approximate) | Strength progression cadence |
|---|---|---|
| 0–1 yr | ~0.7–1 kg/month | Session-to-session |
| 1–3 yr | ~0.3–0.5 kg/month | Weekly to monthly |
| 3–5 yr | ~0.1–0.25 kg/month | Monthly to quarterly |
| 5+ yr | ~1–2 kg/year | Yearly |

**Interpretive caution:** these are circulated coaching heuristics, not measured outcomes. No longitudinal study has tracked muscle gain stratified by training age over the years this table spans [UNVERIFIED — could not confirm a primary source]. Use them to set expectations, not to judge a program.

Women gain a similar *relative* amount of muscle from the same program and less in absolute terms, because they start from a smaller base — a meta-analysis found no significant sex difference in hypertrophy, and women actually gained relatively *more* upper-body strength (Roberts et al., 2020). These are population averages; genetics, starting point, and [responder variability](#responder-variability) move them substantially.

---

### 7. Deloads and when progression must stop

Progression is not monotonic. Signals to [deload](#deload) or [reset](#reset):
- Performance drops across 2+ consecutive sessions on multiple lifts ([overreaching](#overreaching-overtraining))
- Joint or tendon ache persisting >24 h after training
- Sleep disruption, elevated resting heart rate, motivation collapse

**Typical deload:** every 4–8 weeks, reduce volume ~40–60% while holding [intensity of load](#intensity) high — ~80–90% of usual, and higher if you can manage it. Cutting *volume* rather than *load* is the conventional lever, and one trial establishes the volume half of that: with [intensity of load](#intensity) held constant at 8–12RM throughout, young adults retained their hypertrophy on as little as one-third — and even one-ninth — of their original training dose across 32 weeks (Bickel et al., 2011). **Validity caveat:** that trial never varied load, so it cannot show that load matters *more* than volume; it shows only that volume can be cut a long way when load is held. It also splits by age — older adults lost muscle size at *both* reduced doses while retaining their strength gains, so the one-ninth figure is a young-adult result and the study measured knee extensors only. The ~80–90% figure is a floor set by fatigue tolerance, not a target [consensus — no single source].

**The strongest evidence against deloading on a schedule.** In a randomized trial, 39 trained men and women took a full week off at the midpoint of a 9-week program. The deload group gained no more muscle and did somewhat *worse* on lower-body strength (Coleman et al., 2024). One small short trial does not settle it, but the confident "deload every 4–6 weeks regardless" prescription is **not supported**. Deload when the signals above appear; do not deload out of superstition.

---

### 8. What the evidence does **not** support

- That any one [periodization](#periodization) model is meaningfully superior for hypertrophy when volume and effort are matched (Grgic et al., 2017)
- That "[muscle confusion](#muscle-confusion)" / constant exercise rotation drives growth (it impedes progression tracking) [consensus — no single source]
- That [eccentric](#eccentric-contraction)-only work is uniquely required for tendon health (see Part II §B.1)
- That [DOMS](#doms) indicates a productive session — soreness tracks novelty, and in the very week damage markers peak, the muscle-building signal is *unrelated* to eventual growth (Damas et al., 2016)
- That there is a narrow "hypertrophy rep range" outside of which growth does not happen (Schoenfeld et al., 2017b)
- That [metabolic stress](#metabolic-stress) / pump-focused training beats [mechanical tension](#mechanical-tension) as a primary driver (Wackerhage et al., 2019)
- That a scheduled [deload](#deload) reliably improves outcomes (Coleman et al., 2024)

---

### 9. The one-paragraph version

Eat ~1.6 g of protein per kg of bodyweight daily, and accept that an energy deficit slows muscle gain without slowing strength gain. Then: pick 4–8 exercises per session covering all major muscles, 2–4 sets each, 6–15 reps, 1–3 RIR, 2–3×/week per muscle. Use **double progression**: add reps until you top the range on every set, then add ~2.5–5% load and restart. Add a set per exercise every few weeks up to your recovery ceiling, then deload. Progress loads on compounds more slowly than your strength allows, because your tendons adapt more slowly than your muscles and nerves do (see Part II §B.1). Log every set. That is ~90% of the available benefit.

---

---

# Part II Tendon Strength

> Three scopes: **(A)** injury recovery & tendinopathy treatment, **(B)** building resilience in healthy tendon, **(C)** elite athletic tendon development for jumping and sprinting.
>
> **General education only — not medical advice.** Everything in Part A assumes a clinician has examined you and told you what is wrong. Persistent, sharp, or acute-onset tendon pain needs a physician or physiotherapist, especially to rule out tears and ruptures. **Read the red flags in §A.3 before applying anything else here** — several of the conditions that masquerade as tendinopathy are *not* especially painful, which is exactly why a pain-based rule cannot detect them.
>
> **How to read this Part.** Claims that are replicated and consistent are stated plainly. Anything weaker is labelled at the point of the claim — **moderate evidence**, **evidence remains limited and inconsistent**, or **contested** — and a **Caveat** or **Interpretive caution** follows the claim it qualifies. Where a number is a practitioner convention rather than a research finding, it says so. The failure mode of tendon writing is confidence outrunning evidence; this Part tries to mark the boundary rather than blur it.


---

## PART 0 — The Biology You Have to Know First

### 0.1 What a tendon is

| Component                                                                         | Share               | Role                                                                                               |
| --------------------------------------------------------------------------------- | ------------------- | -------------------------------------------------------------------------------------------------- |
| [Type I collagen](#collagen-type-i)                                             | ~60–85% of dry mass | Tensile strength; hierarchically arranged [fibrils](#fibril) → fibers → [fascicles](#fascicle) |
| [Elastin](#elastin)                                                             | ~1–2%               | Recoil, [crimp](#crimp) recovery                                                                 |
| [Proteoglycans](#proteoglycan) ([decorin](#decorin), [aggrecan](#aggrecan)) | small               | Water binding, fibril spacing, [viscoelasticity](#viscoelasticity)                               |
| [Tenocytes](#tenocyte) / tenoblasts                                             | ~90–95% of cells    | [Mechanosensing](#mechanotransduction), collagen turnover                                        |
| Water                                                                             | ~55–70% wet mass    | Viscoelastic behavior                                                                              |

**Structure:** collagen molecules → fibrils → fibers → fascicles (surrounded by [endotenon](#endotenon-epitenon-paratenon)) → tendon ([epitenon/paratenon](#endotenon-epitenon-paratenon)). The **crimp** pattern gives the characteristic "toe region" of the [stress](#stress)–[strain](#strain) curve.

**Stress–strain curve:**

| Region | Strain (ε) | Behavior |
|---|---|---|
| **[Toe region](#toe-region)** | 0–2% | Crimp straightening; low, rising [stiffness](#stiffness) |
| **Linear (elastic)** | 2–4% | Normal functional loading; the adaptive zone; [Young's modulus](#youngs-modulus) is measured here |
| **Microfailure** | >4–5% | Fibril slippage, damage begins |
| **Rupture** | ~8–10% | Complete structural failure |

**⚠ These figures are *ex-vivo*.** They come from cadaveric tendon pulled to failure in one continuous loading ramp, and they are **not directly comparable to the in-vivo strain figures used for training prescription** in §B.2. Living tendon operates at only about **4.0–4.9% strain during walking and running** — the best-controlled in-vivo measurement, which corrects for the tendon's curved path and for skin-to-bone movement (Kharazi et al., 2021) **[strong]**. Higher in-vivo figures of roughly 6–10% come from **maximal one-legged hopping**, not running (Lichtwark & Wilson, 2005). An earlier version of this document said running reaches 6–9%; that was wrong, and it came from applying hopping data to running. The two are not measuring the same thing: whole-tendon elongation measured by ultrasound in a living person includes [fascicle sliding](#fascicle-sliding) and slack take-up that an isolated-fibre failure test does not capture. **So: whenever you meet a strain percentage in this document, check its basis.** This table is a material-failure curve; the training targets in §B.2 are ultrasound measurements on intact, living tendon. Treating them as one scale makes the training target appear to fall inside the damage zone, which it does not.

**And the corrected numbers explain *why* the training window works.** Habitual running sits at ~4–5% strain — which Kharazi et al. explicitly call insufficient to drive adaptation. The adaptive target of 4.5–6.5% sits just **above** habitual loading, which is the whole point: to make a tendon adapt you must exceed what it already does every day. Ex-vivo failure begins around 7.5–9.9% (Wren et al., 2001), so the window is above habit and below failure. **Moderate evidence** for the in-vivo operating range, which is method-dependent and varies between laboratories.

Tendon [ultimate tensile strength](#uts) ≈ **50–100 [MPa](#pa-mpa-gpa)**; Young's modulus ≈ **1–2 [GPa](#pa-mpa-gpa)** [consensus — no single source]. **Caveat:** direct measurement of human Achilles tendon gives a modulus of ~**0.82 GPa** (Wren et al., 2001), below the textbook range quoted here — treat 1–2 GPa as a generic tendon figure, not an Achilles-specific one.
Achilles tendon peak loads: ~2–3× [BW](#bw) walking, ~6–8× BW running, **up to ~9–12× BW** in sprinting/jumping. Patellar tendon in landing: ~4–7× BW.

### 0.2 Two functional tendon types

- **[Energy-storing tendons](#energy-storing-tendon)** (Achilles, patellar) — long, compliant, act as biological springs; high strain during locomotion; **high injury rate**; adapt strongly to training.
- **[Positional tendons](#positional-tendon)** (finger flexors, tibialis anterior) — short, stiff, low strain, low injury rate.

The Achilles is not one rope but three twisted together. It exhibits **[fascicle sliding](#fascicle-sliding)** — neighbouring bundles shearing past one another — and a helical [sub-tendon](#sub-tendon) architecture, with separate contributions from soleus, medial gastrocnemius and lateral gastrocnemius. Load is not shared evenly between them. That non-uniformity is a proposed injury mechanism, but the supporting work is cross-sectional and mechanical rather than prospective: **evidence remains limited and inconsistent** [consensus - no single source].

### 0.3 Mechanotransduction — how loading becomes adaptation

Load → tenocyte deformation → [integrins](#integrin), [primary cilia](#primary-cilium), stretch-activated cation channels (**[Piezo1/2](#piezo1-piezo2)**), cytoskeletal signaling → **[IGF-1](#igf-1), [TGF-β](#tgf-beta)**, [ERK/MAPK](#mapk-erk-pathway), [YAP/TAZ](#yap-taz) → type I collagen gene expression → procollagen synthesis → [cross-linking](#collagen-cross-linking) via [lysyl oxidase](#lysyl-oxidase) → increased [CSA](#csa) and stiffness.

**Key kinetics:**
- Collagen synthesis in human patellar tendon **rises by 6 h post-exercise, peaks ~24 h, and is still elevated at ~72 h** (Miller et al., 2005), measured via [PINP](#pinp) and [microdialysis](#microdialysis). **Moderate evidence** — one well-conducted stable-isotope study in eight healthy adults.
- Collagen *degradation* (via [MMPs](#mmps)) also rises early, so the balance is thought to run **negative for roughly the first 24–36 h** before turning positive. **Evidence remains limited and inconsistent:** the synthesis half is measured, but no human study has measured net collagen balance across that window directly [consensus - no single source].
- **Practical:** every-other-day is a sensible default for tendon-targeted work, on the reasoning that it lands the next stimulus inside the synthesis window rather than on top of the catabolic one. **This is a rationale, not a demonstrated superiority. Contested:** the [Alfredson protocol](#alfredson-protocol) loads the Achilles twice daily, seven days a week, for 12 weeks and works (Alfredson et al., 1998). Daily heavy tendon loading has not been shown to impair adaptation in humans.

### 0.4 Turnover — the hard constraint

The middle of an adult tendon is largely the tissue you grew as a teenager, and you do not replace much of it. Above-ground nuclear testing in 1955–63 spiked atmospheric carbon-14, which then declined along a known curve; because a protein is built from the carbon available when it is made, its carbon-14 content dates it. [Radiocarbon bomb-pulse dating](#radiocarbon-bomb-pulse-dating) of 28 forensic human Achilles samples found core collagen carrying carbon fixed decades earlier — the core appears to be laid down **during height growth and then essentially not renewed** (Heinemeier et al., 2013). The **peripheral/paratenon regions turn over much faster**.

**Interpretive caution — three limits on that finding.** First, the study reports *very limited* turnover inferred from dating; it does not publish a measured half-life, so any specific "half-life of decades" figure is extrapolation and is not stated here. Second, "formed by ~age 17" is shorthand for "formed during height growth", which finishes at different ages in different people. Third, the same method applied to *diseased* tendon found the opposite pattern — years of abnormally high collagen turnover preceding symptoms (Heinemeier et al., 2018). So the low-turnover picture describes healthy tendon, not tendinopathic tendon. **Moderate evidence**: a single cross-sectional cohort of 28, one tendon, one laboratory, not independently replicated.

**Consequence:** most trainable adaptation is **material-property change (cross-linking, stiffness), peripheral CSA growth, and neuromuscular regulation of [musculotendinous unit](#mtu) stiffness** — not wholesale rebuilding of the core. This explains why:
- Adaptation is slow (8–12+ weeks minimum to measure) (Bohm et al., 2015)
- Adolescence is plausibly a high-leverage window — but see §C.5, where that claim is bounded
- Damaged core tissue is unlikely to "heal back to new" — you build capacity *around* it

---

## PART A — Injury Recovery & Tendinopathy Treatment

### A.1 What tendinopathy actually is

**[Tendinopathy](#tendinopathy) is not a simple inflammation.** "[Tendinitis](#tendinitis)" is an obsolete term for the chronic presentation. What histology shows instead is a **failed healing response**: disorganized collagen, increased [ground substance](#ground-substance) (proteoglycans, water), [neovascularization](#neovascularization), ingrowth of nerves alongside the new vessels (a source of pain), and tenocyte proliferation with rounded morphology.

**Caveat — a correction the field has made to itself.** The slogan "tendinopathy has *nothing* to do with inflammation" was an overcorrection to the old term "tendinitis", and it is no longer accurate. Classic acute inflammatory cells are largely absent in chronic disease, but inflammatory signalling and resident immune cells do participate throughout, including chronically (Millar et al., 2021). The right statement is the narrow one: this is not an acute inflammatory condition, and treating it as one has failed.

#### The [Continuum Model](#continuum-model-of-tendon-pathology) (Cook & Purdam)

| Stage | State | Reversible? | Treatment focus |
|---|---|---|---|
| **1. Reactive** | Non-inflammatory cell/matrix swelling from acute overload | Highly | **Reduce load spikes**, [isometrics](#isometric-contraction) for pain, relative rest (days) |
| **2. Dysrepair** | Matrix breakdown, some neovascularity | Partly | Begin progressive loading, correct volume errors |
| **3. Degenerative** | Cell death, disorganized matrix, "holes" | Largely not | Load the *surrounding healthy tissue*; build capacity around the lesion |

**Interpretive caution on the model itself.** This is a staging framework built by synthesising clinical and laboratory observation (Cook & Purdam, 2009) — it is not a validated staging system, the stages cannot be reliably assigned from imaging, and its own authors have since revisited it. It earns its place because it makes good treatment decisions, not because the three boxes have been shown to be real, separable states. **Moderate evidence.** Use it the way you use the [ACWR](#acwr): keep the principle, discard the false precision.

Crucially: **imaging severity correlates poorly with pain.** Many asymptomatic athletes have abnormal tendon imaging ([asymptomatic imaging abnormality](#asymptomatic-imaging-abnormality)), and such findings carry only modest prospective risk with poor positive predictive value (Docking et al., 2015). Treat the person, not the ultrasound.

**Reactive-on-degenerative** — a worn tendon that flares — is described as the most common athletic presentation (Cook & Purdam, 2009). **Moderate evidence.**

### A.2 Common tendinopathies

| Condition | Site | Distinguishing features |
|---|---|---|
| **Achilles [midportion](#midportion-tendinopathy)** | 2–6 cm above calcaneus | Best loading evidence; [HSR](#hsr) and eccentrics both work and are equivalent (Beyer et al., 2015) |
| **Achilles [insertional](#insertional-tendinopathy)** | At calcaneal [enthesis](#enthesis) | **Avoid deep [dorsiflexion](#dorsiflexion-plantarflexion)** — [compression](#tendon-compression) against calcaneus; work 0° to plantarflexion. **Moderate evidence** — mechanistic rationale, thinner trial base than midportion |
| **Patellar ("jumper's knee")** | Inferior pole of patella | Decline squat and HSR both used (Kongsgaard et al., 2009); very common in volleyball/basketball |
| **Gluteal (greater trochanteric pain syndrome)** | Glute medius/minimus insertion | **Avoid sustained hip adduction** — crossing legs, hanging on one hip, side-lying on the sore side. The **LEAP trial** found education + exercise beat both corticosteroid injection and wait-and-see at 8 and 52 weeks |
| **Lateral elbow ("tennis elbow")** | Common extensor origin (extensor carpi radialis brevis, ECRB) | Often self-limiting over ~12 months; corticosteroid injection is **worse than placebo** at 1 year (Coombes et al., 2013) |
| **Rotator cuff related** | Supraspinatus etc. | Loading ≈ surgery for most non-traumatic cases. **Moderate evidence** [consensus - no single source] |
| **Proximal hamstring** | Ischial tuberosity | Compressive in deep hip flexion; avoid deep stretch early. **Evidence remains limited and inconsistent** |
| **Tibialis posterior** | Medial ankle | Progressive; watch for acquired flatfoot deformity. **Get this one assessed early rather than self-managed** — untreated, it deforms the foot permanently |

**Compression is a key concept:** where a tendon wraps a bony prominence, squeezing is added on top of pulling. Insertional tendinopathies are aggravated by that compression, so **stretching an insertional tendinopathy usually makes it worse** — one of the most common self-treatment errors. **Moderate evidence:** the mechanism is well described and clinically consistent, but no trial has compared stretching against not stretching in these presentations.

### A.3 Treatment — ranked by evidence

#### Tier 1: Progressive mechanical loading

**Read the whole tier list with one caveat first.** The largest synthesis of Achilles tendinopathy treatment — a living network meta-analysis of 29 randomised trials — found that **doing something active beats wait-and-see at 3 months, but no active treatment was clearly better than any other** at 3 or 12 months (van der Vlist et al., 2021). Exercise is recommended first because it is cheap, safe and easy to prescribe, not because it has beaten the alternatives head-to-head. The ranking below is therefore partly a judgement call: strong evidence that active loading beats waiting, **contested** ordering within the active options.

| Protocol | Prescription | Evidence |
|---|---|---|
| **[Heavy Slow Resistance (HSR)](#hsr)** | 3–4 sets, **15[RM](#rm) → 6RM** over 12 weeks, **3 s [concentric](#concentric-contraction) / 3 s [eccentric](#eccentric-contraction)**, 3×/wk. Prescribed in repetition maximum, not %1RM — that is how the trials were run | **Equal to eccentrics, not superior.** Both produced equally good, lasting results in Achilles; HSR patients were more satisfied at 12 weeks, a difference gone by 52 weeks (Beyer et al., 2015). **Moderate evidence.** The adherence advantage is real; claims of **better structural normalization are not supported** — findings are inconsistent between trials and sites |
| **[Eccentric (Alfredson protocol)](#alfredson-protocol)** | 3 × 15 twice daily, 7 days/wk, 12 weeks, straight- and bent-knee, load added via backpack | Historic reference standard for **midportion Achilles**; large effect sizes, poor adherence; **not** superior to HSR. **Caveat:** the founding study was 15 patients with no control group (Alfredson et al., 1998) — its reputation outruns its design. Later controlled work supports eccentric loading here. **Moderate evidence** |
| **[Isometrics](#isometric-contraction)** | 5 × 30–45 s at a hard but sustainable effort, 2–3 min rest, 1–2×/day | Useful for in-season loading when dynamic work is irritable. **The pain-relief claim is weaker than it is usually presented.** The influential finding came from six volleyball players in a crossover study (Rio et al., 2015); a meta-analysis of 10 randomised trials, 7 of them poor quality, found short-term pain reduction but **no consistent advantage over other exercise** (Clifford et al., 2020). **Contested** — try it, drop it if it does nothing for you |
| **[Combined/graded (Silbernagel protocol)](#silbernagel-combined-graded-protocol)** | Pain-guided progression through 4 phases; permits continued running | Continuing to run and jump under the pain rule did not worsen outcomes versus stopping (Silbernagel et al., 2007). **Moderate evidence** — one 38-patient randomised trial |

**The universal progression logic:** isometric → heavy slow isotonic → [energy-storage loading](#energy-storage-loading) → sport-specific [plyometric](#plyometrics) / return to play. Advance when the current stage is tolerated within the pain rule below. **Moderate evidence** for the individual stages; the *ordering* is standard clinical practice that has not been tested against alternatives [consensus - no single source].

**⚠ Do not import the healthy-tendon dose into week 1 of rehab.** Part II §B.2 argues that building tendon *material* properties needs roughly 70–90% [MVC](#mvc). HSR starts at 15RM, well below that, and this is not an inconsistency. Early rehab targets symptoms, tolerance and muscle capacity; it *progresses into* the high-load zone across 12 weeks. Starting an irritable tendon at 90% MVC is how people flare themselves.

#### The [pain-monitoring rule](#pain-monitoring-model) (Silbernagel)
- Pain **≤ 5/10** on a [Numeric Rating Scale](#nrs) during loading is acceptable
- Pain must **return to baseline within 24 h**
- **Morning stiffness must not progressively worsen** week over week
- Meeting these criteria → the loading is **producing outcomes as good as resting would**, and you may progress

The rule comes from a randomised trial of 38 patients with midportion Achilles tendinopathy, in which continuing to run and jump within these limits did not worsen outcomes (Silbernagel et al., 2007). **Moderate evidence** — validated once, in one tendon, and now applied far more widely than it was tested.

**⚠ Two limits on this rule, both important.**

**It does not prove absence of tissue damage.** Silbernagel's framework is validated as a *symptom-guided rehabilitation* method that produces outcomes at least as good as avoiding load. No study has shown that tissue is undamaged while you follow it. To say "the loading is not causing damage" overstates what the evidence shows.

**It applies only once tendinopathy has been diagnosed.** It is not a general gate for any painful tendon. A bone stress injury, a partial tendon tear, and an early rupture can all sit under 5/10 and settle within 24 hours — and this rule would tell you to keep loading all three. If your problem has not been assessed by a clinician, read the red flags below first.

#### ⚠ Red flags — stop and get assessed

Everything above assumes you have a diagnosed tendinopathy. These are the situations where self-management is the wrong tool, and several of them defeat the pain rule because they are **not especially painful**.

**Suspect an Achilles rupture if:** you felt or heard a sudden pop or snap, or felt as though you were kicked in the back of the calf; you cannot push off, go up on tiptoe, or perform a **single-leg heel raise**; there is a palpable gap in the tendon. A rupture is frequently *not* severe pain, which is exactly why roughly a quarter are missed at first presentation.

**The calf-squeeze test (Thompson / Simmonds).** Lie face down with the foot hanging off the end of a bed. Have someone squeeze the calf muscle. The foot should point downward. **If it does not move, that suggests a rupture — go to urgent care the same day.** This test takes ten seconds and is the single most useful thing in this section.

**Also seek assessment for:**
- **A swollen, warm, red or tender calf**, especially one-sided, or pain out of proportion to what you did — a blood clot (DVT) must be excluded *before* anyone loads it.
- **Pain that came on suddenly during a single movement** rather than building over weeks — that pattern suggests a tear, not tendinopathy.
- **Pain at night or at complete rest**, unexplained weight loss, or fever.
- **Several tendon attachment points hurting at once**, especially with more than 30 minutes of morning stiffness or inflammatory back pain — that suggests [enthesitis](#enthesitis), an inflammatory-arthritis problem needing different treatment.
- **A growing child or adolescent with an acute limp, or hip or knee pain** — do not assume [apophysitis](#apophysitis).
- **Tendon pain during or after a course of [fluoroquinolone](#fluoroquinolone) antibiotics** — see §B.5.
- **Inner-ankle pain with a flattening arch** ([tibialis posterior](#tendinopathy)) — this one changes treatment if caught late, so get it looked at early rather than loading it for three months.

**A note on sustained hard isometrics.** Holding 70–90% of maximum for 30–45 seconds raises blood pressure sharply. Breathe throughout rather than holding your breath, and talk to a clinician first if you have uncontrolled high blood pressure or known heart disease.

#### Tier 2: Adjuncts — modest or situational evidence

| Intervention | Verdict |
|---|---|
| **Education & [load management](#load-management)** | Essential. Most tendinopathy follows a **training-load spike**. **Moderate evidence** [consensus - no single source] |
| **[ESWT](#eswt) (shockwave)** | **Weaker than commonly claimed.** A systematic review reported moderate effects in greater trochanteric, patellar and Achilles tendinopathy but rated most included trials low quality (Mani-Babu et al., 2015), and the Achilles network meta-analysis found no clear advantage over other active treatments (van der Vlist et al., 2021). **Evidence remains limited and inconsistent.** Reasonable adjunct if loading stalls; not a replacement |
| **[NSAIDs](#nsaid)** | Short-term analgesia only. Blunt the prostaglandin-mediated part of load-induced collagen synthesis and tenocyte proliferation — **avoid routine or prolonged use**, especially during adaptation phases. **Moderate evidence** for the analgesia; **evidence remains limited and inconsistent** on how much real-world adaptation is lost |
| **[GTN patches](#gtn)** | Some positive trials, inconsistent overall; headaches common |
| **Manual therapy / soft-tissue work** | Short-term symptom relief; no structural effect |
| **Orthoses / heel lifts** | Situational offloading; useful early in insertional Achilles |

#### Tier 3: Weak, mixed, or negative evidence

| Intervention | Verdict |
|---|---|
| **[Corticosteroid](#corticosteroid) injection** | **Better short-term, worse long-term.** In lateral elbow tendinopathy, 1-year recovery was 83% with injection vs 96% with placebo and recurrence 54% vs 12% (Coombes et al., 2013); in gluteal tendinopathy the **LEAP trial** beat it with education plus exercise. Raised rupture risk in weight-bearing tendons rests on mechanism and case series, not trials — **moderate evidence** for that part. **Generally avoid** |
| **[PRP](#prp) (platelet-rich plasma)** | **Not supported.** Two well-conducted placebo-controlled trials found no benefit: PRP vs saline, double-blind, n = 54 (de Vos et al., 2010), and PRP vs sham, n = 240 (Kearney et al., 2021) |
| **[Orthobiologics](#orthobiologics) / stem cell** | Experimental; **evidence remains limited and inconsistent** |
| **Dry needling / [prolotherapy](#prolotherapy)** | Low-quality evidence; **evidence remains limited and inconsistent** |
| **Therapeutic ultrasound, low-level laser** | Minimal to no meaningful effect [consensus - no single source] |
| **Static stretching (insertional cases)** | Often **harmful** — adds compression. **Moderate evidence** (mechanistic and clinical, no trial) |
| **Indefinite complete rest as a treatment** | **Not supported.** Wait-and-see was inferior to every active treatment at 3 months (van der Vlist et al., 2021); prolonged unloading deconditions tendon and muscle, and symptoms return on resumption |

**⚠ "Rest is harmful" is a slogan, and it needs bounding.** What the evidence supports is that *indefinite, complete, undirected* rest is a poor treatment for diagnosed tendinopathy. It does **not** mean rest is always wrong. **Short relative rest of a few days is the correct first move in a reactive flare** (see the continuum table above), and **complete unloading is the correct move** for a suspected rupture or partial tear, a suspected [bone stress injury](#bone-stress-injury), a possible DVT, or [fluoroquinolone](#fluoroquinolone)-associated tendon pain. The accurate version: *active loading beats waiting — once you know what you are loading.*

#### Surgery
Reserved for failure of ≥6 months of well-executed loading. Tendinopathy surgery outcomes are **not clearly superior to continued conservative care** [consensus - no single source]; **evidence remains limited and inconsistent**. Frank ruptures are a separate problem with their own pathways.

### A.4 Acute rupture (a different problem)

- **Achilles rupture — get the outcome right, because the two are commonly swapped.** The equivalence is in **function**, not in re-rupture rate. A three-arm randomised trial of 526 patients found **no significant difference in function at 12 months** between non-operative treatment, open repair and minimally invasive surgery (Myhrvold et al., 2022). Re-rupture, by contrast, is **modestly higher without surgery**: 3.9% non-operative vs 2.3% operative in a meta-analysis of 29 studies — while complications ran the other way, 1.6% non-operative vs 4.9% operative, the main surgical complication being infection and the main non-surgical one deep vein thrombosis (Ochen et al., 2019). So: non-operative management with functional bracing and early weight-bearing is a legitimate default for most people, and you are trading a small increase in re-rupture risk against a larger decrease in complication risk. Surgery may still be favoured in elite athletes and delayed presentations — that part is **contested**. Early controlled mobilization beats prolonged casting either way.
- Return to sport: **6–12 months**; many athletes never fully regain pre-injury performance, and sprint and jump deficits often persist for years. **Moderate evidence** [consensus - no single source].
- **Rehab principle:** protect repair length early ([tendon elongation](#tendon-elongation) = permanent mechanical deficit), then load progressively and aggressively.

### A.5 Realistic timelines

| Condition | Meaningful improvement | Full return |
|---|---|---|
| Reactive tendinopathy | 1–3 weeks | 4–8 weeks |
| Chronic midportion Achilles | 6–12 weeks | 3–6 months |
| Patellar tendinopathy | 8–12 weeks | 3–6 months, often longer in jumpers |
| Gluteal tendinopathy | 8–12 weeks | 3–6 months |
| Lateral elbow | Highly variable | Often 6–12 months (much resolves naturally) |
| Achilles rupture | — | 6–12 months |

**Recurrence is common.** The endpoint of rehab is not "no pain" — it is **restored capacity**: strength, power, endurance, and tolerance to sport-specific load.

---

## PART B — Building Resilient Tendon in Healthy Tissue

### B.1 The core problem: muscle outruns tendon

| Tissue | Detectable adaptation |
|---|---|
| Neural / strength | 2–4 weeks |
| Muscle [CSA](#csa) | 6–8 weeks |
| **Tendon [stiffness](#stiffness) / CSA** | **8–12+ weeks** (Bohm et al., 2015) |

Your ability to *produce* force improves faster than your tendon's ability to *transmit* it. Strength — especially early, neurally driven strength — rises within weeks, while tendon needs months. The ordering of those three rows is well established; the specific week ranges for the first two are conventional [consensus - no single source]. The further claim that this mismatch is the dominant cause of tendinopathy in months **2–5** of a new lifter's career is a plausible working model, **not** a measured finding [UNVERIFIED - could not confirm]. **Evidence remains limited and inconsistent.**

Additional risk multiplier: **[muscle–tendon imbalance](#muscle-tendon-imbalance)**. Athletes with very high plantarflexor strength but disproportionately low Achilles stiffness experience higher tendon strain per contraction. This is the one part with prospective support: in adolescent athletes tracked longitudinally, high patellar tendon strain preceded tendinopathy (Mersmann et al., 2023). **Moderate evidence.** A review of this literature reports the pattern in roughly **1 in 5** athletes studied (Mersmann et al., 2017) — **Interpretive caution:** that figure comes from small, sport-specific samples and is not a population rate.

### B.2 The four loading parameters that matter

| Parameter | Effective dose | Notes |
|---|---|---|
| **[Strain](#strain) magnitude** ← *primary driver* | **~70–90% [MVC](#mvc)**, producing roughly **4.5–6.5% tendon strain** | The single most important variable. In a meta-analysis of loading interventions in healthy adults, above 70% MVC/RM gave a large effect on tendon stiffness (effect size 0.90) while below 70% gave essentially nothing (0.04) (Bohm et al., 2015). Manipulating strain directly confirms it: ~4.6% raised Achilles stiffness, ~2.8% did not (Arampatzis et al., 2007). **Caveat:** the lower end of the strain window is directly supported; the ~6.5% upper end is extrapolation |
| **Strain duration** | **~3 s per contraction**; **~60 s total high-strain time** per session for the isometric protocol (4–5 sets × 4 reps × 3 s = 48–60 s). The heavier, slower [HSR](#hsr) protocol accumulates more — 3–4 sets × 6–8 reps × 6 s ≈ 1.8–3.2 min | Short/ballistic contractions (<1 s) are markedly less effective for stiffness gains at equal load. **Evidence remains limited and inconsistent** for the 3 s figure specifically: it is a property of the protocols that worked, not the output of a trial comparing 3 s against 1 s at matched strain, and contraction duration was reported too inconsistently across studies to pool (Bohm et al., 2015) |
| **Frequency** | **3–4×/week**, ideally every other day | Lands the next stimulus inside the ~72 h synthesis window. **Contested:** across the pooled studies, frequencies from ~2 to 7×/week all produced adaptation (Bohm et al., 2015), and the twice-daily [Alfredson protocol](#alfredson-protocol) works. There is no human evidence that more frequent loading impairs tendon adaptation — treat every-other-day as a sensible default, not a rule |
| **Contraction type** | [Isometric](#isometric-contraction) ≈ [concentric](#concentric-contraction) ≈ [eccentric](#eccentric-contraction) ≈ combined, **when strain is equated** | Eccentric-only superiority is **not supported**: effect sizes were isometric 0.95, concentric–eccentric 0.82, eccentric-only 1.04, differences not statistically significant (Bohm et al., 2015). Choose by tolerance and adherence |

**Volume is NOT the driver.** High-volume, low-load work builds muscular endurance without supplying a meaningful tendon stimulus — loading below 70% MVC produced no tendon adaptation regardless of how much of it was done (Bohm et al., 2015). The further claim that it *worsens* the muscle-to-tendon capacity ratio by raising muscle force output without a matching tendon stimulus is an inference from that plus the imbalance literature: **evidence remains limited and inconsistent.**

**⚠ %MVC and %1RM are different numbers and do not convert.** [MVC](#mvc) is a maximal voluntary *isometric* contraction, measured on a dynamometer at one fixed joint angle. [1RM](#one-rep-max) is the heaviest load moved once through a full range on a specific lift. 90% MVC on an isometric calf press is not 90% of your squat. Where a protocol below specifies one, do not substitute the other.

### B.3 Practical protocols for healthy tendon

These are for **healthy, asymptomatic tendon in people cleared to train hard**. They are not rehab prescriptions — for that, see §A.3, which starts at 15RM. Breathe throughout every hold; see the pressor caution in §A.3.

**Heavy isometric** (highest strain per unit of fatigue), modelled on Arampatzis et al. (2007):
```
Load       ~90% MVC
Tempo      3 s ramp-up → 3 s hold → controlled release
Sets/reps  4–5 × 3–4
Rest       2–3 min
Total      ~60 s high-strain time per muscle group
Frequency  3×/week, every other day
```

**Heavy Slow Resistance** (dual muscle + tendon stimulus), as prescribed in the trials (Kongsgaard et al., 2009; Beyer et al., 2015):
```
Load       a true 6–8RM
Tempo      3 s eccentric / 3 s concentric (6 s per rep)
Sets/reps  3–4 × 6–8
Rest       2–3 min
Total      ~1.8–3.2 min high-strain time per muscle group
Frequency  2–3×/week
```
**Prescribed in [RM](#rm), not %[1RM](#one-rep-max), and that is deliberate.** The original trials dosed HSR this way, and the conversion does not survive the tempo: 6–8 reps at a genuine 80–85% 1RM is not achievable at a 6-second tempo, because the slow tempo itself costs you reps. Pick a load you could not exceed by more than one or two reps at that tempo. Loosely, that tends to land near 70–80% of a conventionally tested 1RM, but the mapping varies enough by exercise and by person that RM is the safer instruction.

**Regional targeting:** tendon strain varies by joint angle. Train through the range and include long-[muscle-length](#muscle-length) positions — bent-knee calf work biases soleus/deep Achilles, straight-knee biases gastrocnemius.

### B.4 Rules for the developing or beginner lifter

1. **Cap load progression at ~2.5–5%/week on lower-body compounds**, even when you could add more. Tendon injuries are a *rate-of-progression* problem. **Note the two different quantities:** this rule caps **bar weight** on a single lift. The separate ≤~10–15%/week figure in the Quick-Reference Dosing Card caps **training load** — cumulative weekly dose across sets, tonnage and foot contacts. They are not in conflict and neither is a validated threshold; both are practitioner heuristics [consensus - no single source]. **Evidence remains limited and inconsistent** for the specific percentages; **moderate evidence** for the underlying principle that rate of increase matters more than absolute load.
2. **Never increase bar load and volume in the same week.** Heuristic [consensus - no single source].
3. **[Acute:Chronic Workload Ratio](#acwr)** — keep this week's training load near the rolling 4-week average, conventionally **~0.8–1.3×**. **Contested, leaning negative:** the ACWR framework has been substantively criticised for mathematical coupling of numerator and denominator, arbitrary category boundaries and spurious correlation, and an acute-to-*random* workload ratio proved about as associated with injury as the genuine one (Impellizzeri et al., 2020). Keep the principle — avoid sudden spikes — and discard the arithmetic precision. Do not treat 1.3 or 1.5 as thresholds.
4. **Establish full [ROM](#rom) first, then load it.**
5. **The first 12 weeks are about tissue tolerance, not records.**
6. **[Deload](#deload) every 4–8 weeks:** cut volume 40–60%, keep load moderate. Volume reduction preserves adaptation better than load reduction.
7. **Never train through worsening [morning stiffness](#morning-stiffness)** — the earliest reliable warning sign.

### B.5 Modifiers of tendon health

| Factor | Effect |
|---|---|
| **Age** | Stiffness and cross-link quality decline; healing slows. **Older tendons still adapt** — the dose must be adequate and the progression slower |
| **Sex** | Women show **lower tendon stiffness and a smaller collagen-synthesis response** to loading; **estrogen reduces tendon stiffness** (elevated laxity around ovulation). A reason to train stiffness deliberately, not to train lighter |
| **Genetics** | [*COL5A1*, *COL1A1*, *TNC*, *MMP3*](#tendinopathy-associated-genes) polymorphisms associate with tendinopathy/rupture risk. Family history is a genuine risk factor |
| **Metabolic health** | **Type 2 diabetes and obesity substantially raise tendinopathy risk** — [AGEs](#ages) stiffen and embrittle collagen. Insulin resistance is an independent risk factor |
| **Hypercholesterolemia** | Associated with tendon [xanthomas](#tendon-xanthoma) and tendinopathy |
| **[Fluoroquinolone](#fluoroquinolone) antibiotics** | Documented tendon rupture risk, especially Achilles, in older adults and with concurrent corticosteroids. Risk persists weeks-to-months after the course. **If tendon pain, swelling or inflammation develops during or after a course, stop the drug and contact the prescriber immediately, and unload that tendon completely — not merely "train lighter" — until it has been assessed.** Rupture can occur with little or no warning pain. Avoid heavy tendon loading during and for some weeks after the course |
| **Systemic corticosteroids** | Impair collagen synthesis; raise rupture risk |
| **Statins** | Weak and inconsistent association with tendinopathy |
| **Smoking** | Impairs tendon healing and microcirculation |
| **Sleep deprivation** | Impairs connective-tissue remodeling; raises injury rates in athletes |
| **Inflammatory arthropathies** | Spondyloarthritis presents as [enthesitis](#enthesitis) — consider if multiple entheses hurt |

### B.6 Nutrition for tendon

| Intervention | Evidence |
|---|---|
| **[Hydrolyzed collagen](#hydrolyzed-collagen-collagen-peptides-gelatin) / gelatin + vitamin C, timed pre-load** | ~15 g + ~50 mg [ascorbate](#ascorbate), **30–60 min before** loading. Shaw et al. (2017) raised circulating glycine/proline/[hydroxyproline](#hydroxyproline) and [PINP](#pinp), and increased collagen content in an *engineered ligament* construct — not in a human tendon, in 8 participants. **Countervailing evidence:** a stable-isotope tracer study measuring the outcome that actually matters found collagen protein ingestion during recovery from exercise **did not increase muscle connective tissue protein synthesis rates** (Aussieker et al., 2023). **Evidence remains limited and inconsistent** — a biomarker and bench finding with a direct tracer null against it, and no human tendon outcome trial either way. Low cost, low risk |
| **Vitamin C** | Required cofactor for [prolyl/lysyl hydroxylase](#prolyl-lysyl-hydroxylase). Deficiency clearly impairs collagen; supplementing beyond sufficiency has no proven added benefit |
| **Protein (total)** | 1.6–2.2 g/kg/day supports the whole [musculotendinous unit](#mtu) |
| **Vitamin D** | Deficiency associates with musculoskeletal injury; correct if low |
| **Omega-3** | Anti-inflammatory; no clear tendon-specific benefit |
| **[Blood-flow restriction (BFR)](#bfr)** | Useful for *muscle* when heavy load is contraindicated; **does not reliably build tendon stiffness** — at 20–30% 1RM it is low-strain by design, well under the ~70% MVC threshold below which tendon adaptation effectively vanishes (Bohm et al., 2015). A bridge tool, not a substitute. **Moderate evidence** — the inference is sound but direct BFR-on-tendon trials are few |

**Timing rationale:** tendon is poorly vascularized, so the pre-load window exists to get substrate amino acids circulating when peritendinous blood flow peaks.

---

## PART C — Elite Athletic Tendon Development (Jumping & Sprinting)

### C.1 Why tendon stiffness equals performance

In the **[stretch-shortening cycle (SSC)](#ssc)**, the muscle contracts near-isometrically while the **tendon stretches and recoils**, returning stored elastic strain energy. Tendon recoil is far faster and more efficient than muscle shortening.

- Achilles recoil supplies a large share of the mechanical work in sprinting and jumping [consensus - no single source]
- Tendons return **~90–93%** of stored energy ([hysteresis](#hysteresis) loss ~7–10%). **Moderate evidence** [consensus - no single source]
- **Stiffer tendon → faster force transmission, shorter [electromechanical delay](#emd), higher [RFD](#rfd)**. **Moderate evidence** [consensus - no single source]
- Achilles and patellar tendon stiffness correlate with **jump height, sprint velocity, and [running economy](#running-economy)**. **Interpretive caution:** these are cross-sectional correlations. They do not establish that raising an individual's stiffness raises their performance. **Evidence remains limited and inconsistent**

**Documented elite tendon characteristics.** Two of these are commonly stated backwards, and both corrections point the same way — sprinters are built for *speed of shortening*, not for leverage.

- **Sprinters have LONGER muscle fascicles, not shorter.** Among 37 male 100 m sprinters, the faster group had longer vastus lateralis and gastrocnemius fascicles than the slower group (Kumagai et al., 2000). Longer fascicles mean more sarcomeres in series, hence higher shortening velocity. **Moderate evidence.**
- **Sprinters have SMALLER Achilles [moment arms](#moment-arm), not larger.** Sprinters' Achilles moment arms averaged **25% smaller** than non-sprinters', and simulation showed that shorter moment arms plus longer toes let the athlete generate more forward impulse in the push-off (Lee & Piazza, 2009; n = 12). The mechanism is a trade-off: a bigger moment arm converts force into more joint torque, but forces the muscle to shorten faster for the same joint rotation, which costs force. **Moderate evidence.**
- **"Sprinters have stiffer Achilles tendons" is contested.** Findings vary with measurement method and with which tendon region is assessed, and no consistent primary source supports it as stated [UNVERIFIED - could not confirm].
- Jumpers: greater patellar and Achilles CSA and stiffness. **Moderate evidence** [consensus - no single source]
- Distance runners: high tendon stiffness correlates with **better running economy** — again cross-sectional. **Evidence remains limited and inconsistent**

### C.2 The optimal-stiffness paradox

Stiffness is **not monotonically good**.

| Too compliant | Optimal | Too stiff |
|---|---|---|
| Energy lost, slow force transmission, higher strain per contraction → injury risk | Efficient SSC, high RFD, tolerable strain | Higher peak force transmitted to muscle and bone, reduced energy-storage capacity, potential muscle-strain and [bone stress injury](#bone-stress-injury) |

The optimum is **task- and athlete-specific**. Sprint/jump favors higher stiffness; distance running favors a balance weighted toward economy; change-of-direction sports need stiffness *plus* tolerance to varied loading vectors.

### C.3 The elite training model — three layers, in order

#### Layer 1 — Foundation: heavy slow loading (build the material)
Year-round base. This is what actually increases stiffness and CSA.
```
Heavy isometrics:       4–5 × 3–4 reps, 3 s ramp + 3 s hold @ ~90% MVC, 3×/wk
Heavy slow resistance:  3–4 × 6 at a true 6RM, 3-0-3 tempo, 2–3×/wk
Key lifts: back squat, trap-bar deadlift, seated + standing calf raise (both knee
           angles), Nordic hamstring curl, hip thrust, split squat
```
> **You cannot skip this and jump straight to plyometrics.** Plyometric-only programs improve SSC *function* (neural control, MTU stiffness regulation) far more than they improve tendon *material properties*. **Moderate evidence** — this follows from the loading meta-analysis, in which fast ballistic contractions spend too little time at high strain to drive material change (Bohm et al., 2015), rather than from a trial that sequenced the two layers.

**Interpretive caution on the three-layer model as a whole.** It is a coherent synthesis of the loading literature, not a tested training system. No trial has compared "Layer 1 first" against "plyometrics first" in elite athletes, and the foot-contact volumes and box heights below are coaching convention rather than derived doses [consensus - no single source]. **Evidence remains limited and inconsistent** for the prescription; **moderate evidence** for the physiology it rests on.

#### Layer 2 — Bridge: energy-storage loading
```
Slow-to-moderate SSC: countermovement jumps, box jumps (concentric emphasis),
                      submaximal bounding, hurdle hops with soft landings
Volume: 60–100 foot contacts/session, 2×/wk
```

#### Layer 3 — Expression: high-intensity plyometrics & sprinting
```
Depth jumps (30–60 cm; higher boxes only for advanced athletes, and only while
             [ground contact time](#gct) stays short — long contact = wrong stimulus)
Drop jumps, alternate-leg bounding, stiff-leg pogos, single-leg hops
Maximal-velocity sprinting  ← the highest-strain Achilles activity in sport
Volume: 40–120 foot contacts, 1–3×/wk, always fresh, never fatigued
Rest: full recovery between reps — this is a [CNS](#cns)/elastic quality, not conditioning
```

**Critical rule: high-intensity plyometrics and sprinting are NOT tendon-building tools — they are tendon-*taxing* tools that express the capacity built in Layer 1.** The most common elite error is high plyometric and sprint load on an underbuilt tendon base, especially after a layoff.

#### [Reactive Strength Index (RSI)](#rsi) as the monitoring metric
```
RSI = jump height (m) / ground contact time [GCT](#gct) (s)
```
- Track weekly with a jump mat or [force plate](#force-plate), under standardised conditions — same box height, same instruction, same footwear, same surface, same time of day
- **Declining RSI at stable body mass and training load** is a reasonable signal of accumulated neuromuscular fatigue. **Moderate evidence** for that use. The stronger claim — that RSI decline specifically precedes *tendon* pain — has not been demonstrated prospectively for tendinopathy and should be treated as a hypothesis [UNVERIFIED - could not confirm]
- **⚠ Mind the noise floor.** RSI is a ratio of two small, variable numbers, and it moves with instruction, footwear, surface, warm-up and motivation as much as with fatigue. A single session tells you nothing. Establish your own week-to-week variation over several stable weeks first, and only act on a decline that persists across at least two or three sessions and exceeds that variation. Chasing single-session dips will have you deloading noise
- Also track: [CMJ](#cmj) height, [drop-jump](#drop-jump-vs-depth-jump) contact time, morning stiffness/pain report

### C.4 Programming architecture for professional athletes

| Phase | Tendon emphasis | Plyometric / sprint volume |
|---|---|---|
| **Off-season ([GPP](#gpp))** | Heavy isometrics + HSR, 3–4×/wk. Build CSA and stiffness | Low; extensive, low-intensity |
| **Pre-season** | Maintain heavy loading 2×/wk | Rising — introduce intensive plyometrics and max-velocity work |
| **In-season** | 1–2×/wk heavy maintenance (isometrics ideal — low fatigue cost) | Sport-dictated; monitor [ACWR](#acwr) |
| **[Taper](#taper)/peak** | 1×/wk low-volume heavy | Sharp, low volume, high quality |
| **Post-season** | Continue *some* loading — [detraining](#detraining) loses stiffness in weeks | Minimal |

**Detraining:** tendon stiffness declines measurably within **~2–8 weeks** of unloading — faster than it was gained (Kubo et al., 2012). **Bed rest and immobilization cause rapid, large stiffness loss** (Kubo et al., 2004). **Moderate evidence** — these are small-sample studies. In-season maintenance is non-negotiable. Isometrics are the best maintenance tool: high strain, minimal fatigue and soreness cost.

**Return from layoff is the highest-risk window in the athletic calendar.** Re-establish Layer 1 before re-introducing Layer 3. The classic injury is the returning athlete whose muscular and neural capacity return in 3 weeks while tendon capacity needs 10. **Moderate evidence** for the asymmetry in adaptation rates (Bohm et al., 2015); the specific week numbers are illustrative [consensus - no single source].

### C.5 The adolescent window

Because healthy adult tendon core turns over very little (Heinemeier et al., 2013), adolescence — when that core is actually being laid down — is plausibly the highest-leverage period for building tendon CSA and material quality. **Moderate evidence** for the underlying biology.

**⚠ Two corrections to how this is usually stated.**

**It is a leverage point, not a deadline.** Adults adapt perfectly well: in the pooled loading interventions, healthy adults aged 18–50 showed large gains in tendon stiffness (Bohm et al., 2015). Missing the adolescent window costs you an advantage; it does not close a door. Describing it as "non-recoverable" contradicts the adults-still-adapt finding stated in Part II §B.5 and is dropped here. And the specific claim that youth loading produces *measurably superior adult* tendon properties has not been demonstrated by following athletes from adolescence into adulthood [UNVERIFIED - could not confirm]: **evidence remains limited and inconsistent.**

**Adolescents are simultaneously the highest-risk group.** Adolescent athletes show high patellar tendon strain that prospectively precedes tendinopathy (Mersmann et al., 2023), and are at peak risk of **[apophysitis](#apophysitis)** (Osgood–Schlatter at the tibial tuberosity, Sever's at the calcaneus) during growth spurts, when bone lengthens faster than the MTU adapts. Manage volume around [peak height velocity](#phv) — moderate the loading, don't stop it. And note the red flag from §A.3: **a limping adolescent, or one with hip, groin or knee pain, needs medical assessment**, because hip pathology in this age group presents as knee pain and is time-critical.

### C.6 Elite-specific risk factors

- **Surface and footwear changes** — hard surfaces and low-[drop](#shoe-drop) shoes increase Achilles load; abrupt transitions are a classic trigger
- **[Carbon-plated shoes](#carbon-plated)** — alter Achilles vs. knee load distribution; evidence points to changed injury patterns. Transition gradually
- **Sprinting is the peak-strain activity** — schedule max-velocity sessions as heavy CNS *and* tendon load, not as "just running"
- **[Bilateral asymmetry](#lsi) >10–15%** on jump/hop testing is a recognized risk marker
- **Travel, sleep debt, and fixture congestion** measurably raise soft-tissue injury rates
- Elite jumpers show **very high rates of asymptomatic patellar tendon abnormality on imaging** — do not chase imaging findings in a pain-free, performing athlete

---

## PART D — Synthesis: Rules That Hold Across All Three Scopes

0. **Know what you are loading before you load it.** A rupture, a partial tear, a [bone stress injury](#bone-stress-injury), a DVT and inflammatory [enthesitis](#enthesitis) all present as "tendon pain", and the pain rule will wave three of them through. The red flags in §A.3 come before everything else on this list.
1. **For diagnosed tendinopathy, active loading beats waiting** (van der Vlist et al., 2021). But short relative rest in a reactive flare, and complete unloading for a suspected tear or drug-associated tendon pain, are correct treatment — not weakness.
2. **Strain magnitude is the driver — ~70–90% MVC.** Volume, novelty, and modality are secondary. Light work does not build tendon (Bohm et al., 2015).
3. **~3 s contractions, ~60 s of high-strain time for isometrics (or ~1.8–3.2 min for HSR), most sessions spaced a day apart.** The 3 s figure and the spacing are the weakest-supported parts of the dose: **evidence remains limited and inconsistent.**
4. **Tendon adaptation takes 8–12+ weeks** and is measured in months, not sessions (Bohm et al., 2015).
5. **Tendon lags muscle and neural adaptation.** Every injury-prevention decision follows from this. The ordering — nerves, then muscle, then tendon — is solid. The size of the gap is not: the table it came from implies roughly 4–10 weeks behind neural adaptation depending on which comparator you pick, and the older "6–12 weeks" figure was never independently measured [UNVERIFIED - could not confirm]. Note also that the 8-week floor for tendon partly reflects a meta-analysis inclusion criterion of ≥8-week studies (Bohm et al., 2015), not a measured onset.
6. **Most tendon injury is a rate-of-progression error**, not an exercise-selection error. **Moderate evidence** — widely believed, hard to demonstrate cleanly, and the ACWR arithmetic used to formalise it is **contested** (Impellizzeri et al., 2020).
7. **For diagnosed tendinopathy only: pain ≤5/10 during load, settled within 24 h, no worsening morning stiffness = acceptable** (Silbernagel et al., 2007).
8. **Compression aggravates insertional tendinopathy.** Do not stretch it.
9. **Eccentric-only is not special.** All contraction types work at sufficient strain (Bohm et al., 2015).
10. **Plyometrics and sprinting express tendon capacity; heavy slow loading builds it.** Never invert the order.
11. **Detraining loses stiffness faster than training gains it** (Kubo et al., 2012). Maintain year-round.
12. **Injections are mostly not the answer.** PRP is no better than placebo (de Vos et al., 2010; Kearney et al., 2021); corticosteroid helps short-term and harms long-term (Coombes et al., 2013).
13. **Imaging findings ≠ pain** (Docking et al., 2015). Treat capacity and symptoms, not pictures.
14. **Systemic health is tendon health** — diabetes, obesity, smoking, sleep debt, and fluoroquinolones all degrade tendon.
15. **The adolescent window is real, and it is also the highest-risk window.** A leverage point, not a deadline — adults still adapt.

---

### Quick-Reference Dosing Card

```
TENDON-BUILDING SESSION — HEALTHY, ASYMPTOMATIC TENDON ONLY
  Not a rehab prescription. For diagnosed tendinopathy use Part II §A.3,
  which starts at 15RM and progresses over 12 weeks. Do not start an
  irritable tendon at 90% MVC.
  %MVC and %1RM are different quantities and do not convert. Use whichever
  the line specifies.

  Load       isometric: 70–90% MVC   /   slow heavy: a true 6–8RM
  Tempo      3 s per phase  (isometric: 3 s ramp + 3 s hold)
  Sets/reps  4–5 × 3–6      (isometric: 4–5 × 3–4 holds)
  Rest       2–3 min
  Total      ~60 s high-strain time isometric / ~1.8–3.2 min HSR
  Frequency  3×/week, every other day
  Timeline   8–12 wks to measurable change; ~6 months to meaningful change
  Breathe throughout every hold. Never hold your breath. See §A.3 if you
  have uncontrolled hypertension or known heart disease.

REHAB PROGRESSION LADDER — requires a diagnosis of tendinopathy first
  Isometric (load and tolerance; analgesia is inconsistent)
    → Heavy slow resistance, 15RM progressing to 6RM over ~12 weeks
      → Energy storage (moderate SSC)
        → Fast / plyometric (high SSC)
          → Sport-specific / return to play
  Advance when: stage tolerated, pain ≤5/10, settles <24 h, no AM regression
  Stop and get reassessed for: a sudden pop or snap, a palpable gap,
  inability to do a single-leg heel raise, a swollen or warm calf,
  night or rest pain, or symptoms worsening week on week

LOAD MANAGEMENT — heuristics, not validated thresholds
  Weekly training-load change:  ≤ ~10–15%   (cumulative dose, not bar weight)
  Weekly bar-load change:       ≤ ~2.5–5%   (a single lift)
  Acute:chronic ratio:  ~0.8–1.3   (contested — a spike detector, not a score)
  Never add bar load + volume in the same week
  Deload every 4–8 wks: −40–60% volume, load held near-normal
```

---

---

# Part III Fat Loss and Metabolic Adaptation

> Scope: the energetics of fat loss, how to size and run a deficit, what actually happens metabolically when you do, and why weight loss decelerates and reverses.
> **General education only — not medical or dietetic advice.** Very-low-calorie dieting, dieting with any history of disordered eating, dieting in adolescence or pregnancy, and dieting alongside metabolic or endocrine disease require professional supervision. If food, weight, or body image thoughts feel compulsive or distressing, that is a clinical matter, not a programming one — see [when this stops being a programming problem](#when-this-stops-being-a-programming-problem).

---

## STOP — read before you start

**Do not run any protocol in this part if any of the following apply. This is not a caution. It is a stop.**

- You have, or have ever had, an eating disorder — anorexia, bulimia, binge-eating disorder, ARFID, or a diagnosis of "other specified feeding or eating disorder". Deliberate restriction is the single most reliable trigger for relapse.
- You are at or below a healthy weight for your height, or your weight is falling without you intending it to.
- You are under 18. Growth, bone accrual, and puberty are energy-expensive, and the deficits described here are calibrated for adults. Adolescents who need to change body composition need a paediatrician or a registered dietitian, not a spreadsheet.
- You are pregnant or breastfeeding.
- You have type 1 or type 2 diabetes on insulin or sulfonylureas, chronic kidney disease, liver disease, an untreated thyroid disorder, or a history of cardiac arrhythmia.
- Food, weight, or your body already occupies more of your thinking than you would like.

**If you are already restricting and things are going wrong** — periods have stopped, morning erections have stopped, you are always cold, you keep getting ill, you have picked up a bone injury, or you are losing control around food — the answer is **not** a better deficit. The answer is to return to maintenance calories and get assessed. Full list in §7.2, and in [when this stops being a programming problem](#when-this-stops-being-a-programming-problem).

**Medication note.** Losing a substantial amount of weight changes how much medicine you need. Blood-pressure drugs, thyroid replacement, and especially insulin and sulfonylureas commonly need their doses reduced during weight loss, and getting this wrong causes hypotension or hypoglycaemia. If you take any of these, your prescriber needs to know you are dieting before you start [consensus — no single source].

**How confidence is labelled below.** Every substantive claim carries one of **[strong]** (replicated experiments or meta-analysis), **[moderate]** (consistent but limited or indirect evidence), **[limited]** (one study, small samples, or a theoretical model), or **[contested]** (competent researchers actively disagree).

---

## PART 1 — The Energetics

### 1.1 The first law, stated correctly

To lose fat you must take in less energy than you burn, and keep doing it. That is a **[sustained energy deficit](#energy-deficit)**: [energy intake](#ei) below [total daily energy expenditure](#tdee). Nobody disputes this; it is bookkeeping, not biology.

> ΔE_stored = [EI](#ei) − [EE](#ee)
> (change in stored energy = energy in − energy out)

The part people get wrong is that **both sides of that equation move, and they move together.** Energy out is not a fixed number you subtract from. It falls as you get lighter, falls again because you are eating less, and falls a third time because your nervous system quietly turns down how much you move without asking you. Meanwhile hunger goes up. So "calories in, calories out" is a true accounting identity and a nearly useless plan, because the two terms are coupled through [metabolic adaptation](#metabolic-adaptation) and [energy compensation](#energy-compensation) **[strong]**.

**Every diet that works, works through a deficit.** Keto, fasting, low-fat, carnivore, paleo, [IIFYM](#iifym) — when [energy and protein are equated](#isocaloric), outcomes converge. In tightly controlled inpatient studies where every meal is weighed, cutting fat and cutting carbohydrate at matched calories produce near-identical fat loss, with a small edge to fat restriction (Hall et al., 2015; n = 19, 2 × 6-day inpatient periods) **[moderate — small n, short duration]**. Diets differ in how easy they are to stick to, not in their thermodynamics.

### 1.2 The components of expenditure

Your daily burn is four things added together.

| Component | Share of [TDEE](#tdee) | Variability | Notes |
|---|---|---|---|
| **[BMR/RMR](#bmr-rmr)** — what it costs to stay alive at rest | ~60–70% | Low between individuals (±10% after correcting for [fat-free mass](#ffm-lbm)) | Driven mainly by fat-free mass, and disproportionately by organs (brain, liver, kidney, heart) rather than muscle (Wang et al., 2010) **[strong]** |
| **[TEF](#tef)** — the cost of digesting food | **~10% of TDEE** | Low | Protein 20–30%, carbohydrate 5–10%, fat 0–3%, alcohol ~10–30% [consensus — no single source] |
| **[EAT](#eat) + [NEAT](#neat)** — all physical activity | **~15–50% together** | **Extremely high** | See the warning below: no source splits these two numerically |
| — of which **[EAT](#eat)** — deliberate exercise | the smaller share for most people | High, by choice | The bit you schedule |
| — of which **[NEAT](#neat)** — everything else you do | the larger share for most people | **Extremely high** | Fidgeting, posture, walking to things, standing up. **The largest single source of unexplained variance in expenditure, and the main site of adaptive suppression** (Levine, 2004) **[moderate]** |

**⚠ Why activity is given as one combined band.** The 15–50% figure is the authoritative one (NASEM, *Dietary Reference Intakes for Energy*, 2023), but in the source it describes **total physical activity — exercise and non-exercise together** — ranging from 15% in sedentary people to 50% in very active ones. **No source splits EAT from NEAT as separate percentages of TDEE.** Earlier versions of this document assigned the whole 15–50% band to NEAT alone and then added a separate 0–30% for EAT, which double-counted: the four upper bounds summed to 165% of a total that cannot exceed 100%. The qualitative point stands — NEAT dominates the band for anyone who is not an athlete, and it is the part that quietly collapses when you diet — but the split is not a measured quantity. Note also that these are independent central tendencies, not a partition, so they are not meant to sum to exactly 100%.

**On the "NEAT varies by ~2000 kcal/day between people" figure.** This is a review estimate that spans occupational activity — a roofer versus a call-centre worker — not a controlled measurement of two similar people (Levine, 2004) **[limited]**. The best controlled number comes from an overfeeding experiment: when 16 adults were fed 1000 kcal/day above maintenance for 8 weeks, the change in NEAT ranged from **−98 to +692 kcal/day** between individuals, and that range predicted who got fat (Levine et al., 1999) — *verified against the paper's Table 2 and text, not just the abstract* **[strong for the mechanism, limited for the 2000 kcal figure]**.

**Consequence:** the component you consciously control (exercise) is small, and the component that quietly changes the most (NEAT) is invisible to you.

### 1.3 Sizing the deficit

| Deficit size | Rate | Use case | Cost |
|---|---|---|---|
| **~10–15%** below TDEE | ~0.25–0.5% BW/wk | Lean individuals, athletes in-season, [body recomposition](#body-recomposition) attempts | Slow; high adherence; minimal [LBM](#lbm) loss |
| **~20–25%** | ~0.5–0.75% BW/wk | Standard, most people | Good balance; the default |
| **~30–40%** | ~1%+ BW/wk | Higher body fat, medical urgency, time-limited | Rising LBM loss, [adaptive thermogenesis](#adaptive-thermogenesis), hunger, performance decline. Not for lean people |
| **[VLCD](#vlcd)** (<800 kcal/day) | 1.5%+ BW/wk | **Clinical settings only, medically supervised** | Substantial LBM loss, gallstones, electrolyte disturbance, cardiac arrhythmia, micronutrient deficiency, **and refeeding syndrome on coming off it** — see the warning below |

> **⚠ REFEEDING SYNDROME.** After prolonged severe restriction, reintroducing food — especially carbohydrate — pulls phosphate, potassium, magnesium and thiamine into cells fast enough to cause dangerously low blood levels, and can precipitate cardiac failure, arrhythmia, seizures and death. It is a recognised, preventable, and occasionally fatal complication (Mehanna et al., 2008) **[strong]**. Anyone coming off a VLCD, a prolonged severe deficit, or a period of very low intake for any reason needs **medical electrolyte monitoring and graded reintroduction of food**, not a "diet break". Do not self-manage this.

**The governing rule — rate scales to fat mass.** The leaner you are, the less of the deficit your fat can supply, and the more has to come from lean tissue.

#### The fat-oxidation ceiling, stated correctly

There is a theoretical upper limit on how fast stored fat can release energy.

> **Alpert's limit ≈ 290 ± 25 kJ per kg of fat mass per day**
> **= ~69 kcal per kg of fat mass per day (range ~63–75)**
> **= ~31 kcal per *pound* of fat mass per day**
> (Alpert, 2005)

**⚠ Correction of a common error.** The figure "31 kcal" is **per pound**, not per kilogram. Sources that state "31 kcal per kg of fat mass" — including earlier versions of this document — understate the limit by a factor of 2.2. The published value is 290 ± 25 kJ·kg⁻¹·d⁻¹ (Alpert, 2005, *J Theor Biol* 233:1–13); 290 ÷ 4.184 = 69.3 kcal·kg⁻¹·d⁻¹, and 69.3 × 0.4536 = 31.4 kcal·lb⁻¹·d⁻¹.

Worked examples, corrected:

| Person | Fat mass | Theoretical ceiling |
|---|---|---|
| 100 kg at 30% body fat | 30 kg | ~2,080 kcal/day |
| 70 kg at 10% body fat | 7 kg | ~485 kcal/day |
| 60 kg at 6% body fat | 3.6 kg | ~250 kcal/day |

**What this rule is actually worth — read this before using it.** Alpert derived the number by fitting a mathematical model to the [Minnesota Starvation Experiment](#persistent-adaptive-thermogenesis) data — 32 semi-starved young men in 1944–45 — plus a handful of other underfeeding datasets. It has **never been prospectively tested**: no trial has assigned people to deficits above and below the ceiling and measured whether lean-mass loss behaves as predicted **[limited]**. Treat it as a physical upper bound and a useful intuition pump, **not** as a validated prescription, and certainly not as permission to diet harder. It is not "the single most useful quantitative rule in deficit design"; it is one constraint among several, and usually not the binding one.

Specifically:
- **At high body fat the ceiling never binds.** A 100 kg person at 30% fat could theoretically supply ~2,080 kcal/day from fat. No sane deficit approaches that. What limits them is lean-mass loss, hunger, micronutrient adequacy, gallstone risk and adherence — not fat mobilisation.
- **At low body fat it binds hard.** A 60 kg man at 6% fat has a ceiling near 250 kcal/day, which is roughly a 10% deficit. Below about 8–10% body fat in men, any meaningful deficit is partly funded by lean tissue by arithmetic, not by bad programming.
- **For most women the ceiling is not the relevant limit at all.** A 60 kg woman at 20% fat has a ceiling around 830 kcal/day — far above any deficit she should run. Her binding constraint is **energy availability** and the reproductive axis, described below, which is disrupted at intakes nowhere near the fat-oxidation ceiling.

#### Forbes' curve — the better-supported version of the same idea

The empirically grounded relationship is **Forbes' curve**: the proportion of weight lost that comes from fat-free mass falls as starting fat mass rises, following a roughly logarithmic relationship derived from body-composition data across underfeeding and overfeeding studies (Forbes, 2000) **[moderate]**. Practically: a person with a lot of fat loses mostly fat; a lean person loses a much larger share of lean tissue at the same rate of weight loss. This is the same qualitative message as Alpert's ceiling, but it comes from measured body composition rather than a fitted model, and it predicts a smooth gradient rather than a cliff edge.

#### Three ceilings, and you take the lowest

Before you set a number, check it against all three:

1. **Muscle-preservation ceiling — about 500 kcal/day.** A meta-analysis and meta-regression of resistance-training trials found that lean-mass gains were impaired in an energy deficit, and that a deficit of roughly **500 kcal/day was the point at which lean-mass gain stopped altogether** (Murphy & Koehler, 2022) **[moderate]**. If you are training to build or hold muscle, do not exceed it.
2. **Fat-oxidation ceiling — 69 kcal per kg of fat mass per day** (Alpert, 2005) **[limited]**. Binds only when you are already lean.
3. **[Energy availability](#energy-availability) floor — 30 kcal per kg of fat-free mass per day.** This one protects your endocrine system and is the one people ignore.

> **Energy availability (EA) = (calories eaten − calories burned in exercise) ÷ kg of fat-free mass**
>
> Below ~30 kcal·kg FFM⁻¹·day⁻¹, luteinising-hormone pulsatility — the pituitary signal that drives the menstrual cycle — is measurably disrupted within five days (Loucks & Thuma, 2003; n = 29 regularly menstruating, sedentary women of normal body composition) **[strong for the mechanism; limited for the exact threshold]**. Sustained low energy availability is the causal basis of **[RED-S](#red-s)** — impaired bone, immune, endocrine, cardiovascular and reproductive function across all sexes (Mountjoy et al., 2023, IOC consensus statement) **[strong]**.
>
> Worked example. A 60 kg woman with 45 kg of fat-free mass who trains hard enough to burn 400 kcal must eat at least (30 × 45) + 400 = **1,750 kcal/day** to stay above the floor. A 1,400 kcal "diet" plus a spin class puts her at EA ≈ 22 — deep into the disruption zone — even though she is nowhere near "too lean" on any body-fat chart.
>
> **The 30 kcal/kg figure is an indicator, not a switch.** The IOC's own 2023 consensus cautions that EA is difficult to measure accurately in free-living people and that a single threshold oversimplifies; some people show problems above it and some do not below it (Mountjoy et al., 2023) **[contested at the level of the exact number]**. Use it as a floor, not as a target to sit on.

**Practical targets by starting body fat** — read these together with the energy-availability floor, which overrides them:

| Body fat | Recommended rate |
|---|---|
| >30% (M) / >40% (F) | 0.75–1.0% BW/week |
| 20–30% (M) / 30–40% (F) | 0.5–0.75% BW/week |
| 12–20% (M) / 22–30% (F) | 0.5% BW/week |
| <12% (M) / <22% (F) | 0.25–0.5% BW/week — bottom of that range below ~10% (M) / ~20% (F), protein high, [resistance training](#resistance-training) non-negotiable, and **first ask whether more weight loss is actually indicated at all** |

Sanity-check on the last row: a 75 kg man at 8% body fat has 6 kg of fat and a ceiling near 415 kcal/day; 0.5% BW/week is about 410 kcal/day. He is at the ceiling. That is why the recommendation collapses to the bottom of the range as leanness increases.

**A note on the female column that most sources get wrong.** These body-fat brackets do **not** describe endocrine safety. Menstrual disruption is driven by energy availability, not by body-fat percentage, and it routinely appears in women at 20–25% body fat — far above the ~10–13% "[essential fat](#essential-body-fat)" figure — when intake minus training load drops too low (Loucks & Thuma, 2003; Mountjoy et al., 2023) **[strong]**. There is no body-fat percentage above which you are safe. If you are in the bottom bracket and periods become irregular, the correct response is **not to lose more slowly**. It is to stop losing, return to maintenance, and reassess whether further loss is indicated at all — with a clinician.

### 1.4 The arithmetic that is wrong

**The "3500 kcal = 1 lb" rule is obsolete.** It assumes your expenditure never changes, and therefore predicts that a 500 kcal/day deficit yields 52 lb in a year, forever. That never happens. The **[dynamic energy balance models](#dynamic-energy-balance-model)** (Hall et al., NIH Body Weight Planner) replace it by letting expenditure fall as mass falls. Real one-year outcomes typically land near **half** the static prediction **[strong]**.

Corollary: **weight loss is inherently decelerating.** A plateau is the *expected* endpoint of any fixed calorie target, not a sign of failure.

---

## PART 2 — Metabolic Adaptation

### 2.1 What actually changes

[Metabolic adaptation](#metabolic-adaptation) is the umbrella term for the coordinated defence of body mass during energy restriction. It has four components. Only one of them is mysterious.

| Component | Magnitude | Mechanism |
|---|---|---|
| **1. Reduced mass** | Largest | Less tissue costs less to run, and less mass costs less to move. Entirely predictable; not "adaptation" in the interesting sense **[strong]** |
| **2. Reduced [TEF](#tef)** | Small | You are eating less food, so you burn less digesting it **[strong]** |
| **3. Reduced [NEAT](#neat)** ← *the big behavioural one* | **Plausibly up to a few hundred kcal/day** | Less fidgeting, slower walking, more sitting. Largely unconscious **[moderate — the often-quoted "up to 500 kcal/day" is an upper-end estimate, not a typical value]** |
| **4. [Adaptive thermogenesis](#adaptive-thermogenesis)** | **~50–150 kcal/day typically** | A genuine reduction in resting metabolic rate *beyond* what mass loss predicts **[moderate]** |

**Mechanism, stated honestly.** Adaptive thermogenesis is *defined* as a statistical residual — measured resting metabolic rate minus the rate predicted from your new body composition. That definition is agnostic about cause. The mechanisms usually invoked — falling [leptin](#leptin), falling [T3](#thyroid-hormones), reduced [sympathetic](#sns) tone, and increased skeletal-muscle work efficiency — are supported, but they are hypotheses about what fills the residual, not part of its definition, and a share of any measured residual is simply error in the prediction equation **[moderate]**. The strongest causal evidence is the leptin work in §2.3.

**Anchor value.** In CALERIE — 53 non-obese adults, 2 years, ~15% calorie restriction achieved, 8.7 kg mean weight loss — 24-hour and sleeping energy expenditure ran **80–120 kcal/day below** what the weight loss predicted, alongside reduced thyroid-axis activity (Redman et al., 2018) **[strong for this population]**. That is the realistic magnitude for a moderate, sustained deficit.

**The gap between perception and measurement.** People who report "eating 1200 calories and not losing" are frequently under-recording intake and over-reporting activity. The famous demonstration: 10 subjects who described themselves as diet-resistant were measured by [doubly labeled water](#dlw) and found to under-report intake by ~47% and over-report exercise by ~51% (Lichtman et al., 1992) **[limited — n = 10, deliberately selected for treatment failure, so this is the extreme case, not the average]**. Across the broader literature the typical figures are around **20% under-reporting in lean people and 30–50% in people with obesity** [consensus — no single source] **[moderate]**. This is a measurement phenomenon, not dishonesty; it happens to dietitians recording their own intake.

> **⚠ The exception that matters clinically.** All of the above applies to someone with substantial fat to lose who has been dieting for a few weeks. It does **not** apply to a lean person, an athlete, or someone who has already been restricting for months. In that person, a reported intake of 1200 kcal is more likely to be accurate than not — and the correct response is to **stop dieting and eat more**, not to audit harder and cut further. Chronically low intake in an already-lean person is a clinical finding, not a tracking error.

### 2.2 The evidence base — three landmark datasets

| Study | Finding | Interpretation and limits |
|---|---|---|
| **Minnesota Starvation Experiment (Keys et al., 1944–45)** | 32 conscientious-objector volunteers, 24 weeks at roughly half of maintenance intake → ~25% body-weight loss; resting metabolic rate fell far more than mass alone predicted. Profound food preoccupation, depression, apathy, social withdrawal, hypothermia, bradycardia. Post-refeeding [hyperphagia](#hyperphagia) and fat overshoot (Kalm & Semba, 2005, historical review) | Still the definitive description of semi-starvation physiology **and psychology**. **This is where we learned that binge behaviour is a *physiological consequence* of restriction, not a character defect.** Limits: 32 young, healthy, initially lean men; no control group; the exact percentage figures vary between secondary sources, so treat them as approximate **[strong for the qualitative findings, limited for precise numbers]** |
| **The Biggest Loser 6-year follow-up (Fothergill et al., 2016)** | 14 of 16 contestants followed up. Six years on, 41 ± 31 kg of the lost weight had been regained, yet resting metabolic rate was still **499 ± 207 kcal/day below prediction** | The headline evidence for **[persistent adaptive thermogenesis](#persistent-adaptive-thermogenesis)**. **Read the caveats.** (a) n = 14, no control group, and the "predicted" RMR comes from a regression fitted at baseline, so some of the residual is model error. (b) The intervention was extreme: ~40% body-weight loss in 30 weeks via very-low-calorie dieting plus several hours of daily exercise. (c) Hall himself later reinterpreted the result: the contestants who sustained the largest *increases in physical activity* showed the largest adaptation, which fits a **constrained-expenditure** explanation — the body trading resting expenditure against activity expenditure — rather than "damage" caused by dieting per se (Hall, 2022) **[contested]**. Not generalisable to a 20% deficit |
| **CALERIE (Redman et al., 2018; Kraus et al., 2019)** | 2 years of calorie restriction in healthy non-obese adults (n = 218 randomised in the main trial; ~11.9% restriction actually achieved) → sustained ~10% weight loss, of which 71% was fat; metabolic adaptation of 80–120 kcal/day; improved cardiometabolic markers and reduced oxidative damage | The realistic case: a **moderate** deficit in healthy adults produces modest, tolerable adaptation **[strong]**. Note the honest detail — participants were prescribed 25% restriction and achieved about 12%. Prescribed deficits and achieved deficits are different things, in trials and in your kitchen |

**Synthesis:** adaptation scales with **how aggressive the deficit was, how much total weight was lost, how lean you ended up, and how much sustained activity you added.** A moderate deficit produces small, largely reversible adaptation. An extreme one produces large adaptation that may persist for years **[moderate]**.

### 2.3 The hormonal defence system

| Signal | Change in deficit | Effect |
|---|---|---|
| **[Leptin](#leptin)** | ↓↓ — falls faster and further than fat mass itself | The master signal. Falling leptin drives hunger, lowers [T3](#thyroid-hormones), lowers [SNS](#sns) tone, and suppresses the reproductive axis. **Giving low-dose leptin back to weight-reduced people reverses much of the adaptation — the strongest causal evidence that this is leptin deficiency, not damage** (Rosenbaum et al., 2005) **[strong for the mechanism; note n = 10 and an experimental infusion protocol, so this is proof of cause, not a treatment]** |
| **[Ghrelin](#ghrelin)** | ↑ and **stays elevated ~1 year** post-diet | Hunger drive (Sumithran et al., 2011) **[moderate — see caveat below]** |
| **[GLP-1](#glp-1), [PYY](#pyy), [CCK](#cck)** | ↓ | Reduced fullness per meal (Sumithran et al., 2011) **[moderate]** |
| **[Thyroid: T3](#thyroid-hormones)** | ↓ (T4 typically stable) | Lowered cellular metabolic rate (Redman et al., 2018) **[strong]** |
| **[Cortisol](#cortisol)** | ↑ | Catabolic; promotes water retention that masks fat loss **[moderate]** |
| **[Testosterone](#testosterone)** (M) | ↓ at low body fat / large deficit | Reduced anabolism, libido, mood **[moderate]** |
| **[LH/FSH, estrogen](#hpg-axis)** (F) | ↓ | Menstrual dysfunction, [RED-S](#red-s) risk. **The most sensitive early warning of excessive restriction** (Loucks & Thuma, 2003) **[strong]** |
| **[Insulin](#insulin)** | ↓ | Permits [lipolysis](#lipolysis) **[strong]** |

**The critical asymmetry:** these signals **do not simply normalise once you stop dieting.** In the key study, 50 adults with overweight or obesity did 10 weeks on a very-low-energy diet (~550 kcal/day); at 62 weeks — a year after the diet ended, and despite partial regain — ghrelin was still elevated and satiety hormones still suppressed, in proportion to the weight lost (Sumithran et al., 2011).

> **Caveat, because this claim gets over-used.** Only 34 of the 50 completed. There was no control group. And the diet was a **VLCD**, which is the most aggressive protocol in this document and one you should not self-administer. Whether a moderate 20% deficit produces the same year-long hormonal persistence has not been shown to the same standard **[limited]**. The honest statement is: after aggressive weight loss, appetite signalling stays shifted toward regain for at least a year; after moderate weight loss, probably to a lesser degree.

### 2.4 "Starvation mode" — what is true and what is not

| Claim | Verdict |
|---|---|
| "Eating too little stops fat loss entirely" | **False.** A deficit always produces loss; adaptation *slows* it, never reverses it. Metabolic ward studies confirm this without exception **[strong]** |
| "Metabolism is permanently damaged" | **Mostly false.** Adaptation is largely reversible on refeeding and weight restoration in typical dieters. After extreme loss a residual persists — but "reduced" ≠ "damaged", and even the Biggest Loser residual has a competing constrained-expenditure explanation (Hall, 2022) **[moderate]** |
| "You must eat more to lose weight" | **False as stated.** What *is* true: eating adequately preserves [LBM](#lbm), [NEAT](#neat), performance and adherence, so a moderate deficit often out-performs an aggressive one **over months** **[moderate]** |
| "Adaptive thermogenesis is real" | **True.** ~50–150 kcal/day typically (Redman et al., 2018); larger after extreme loss; persists longest after the largest losses **[strong]** |
| "Your plateau is metabolic damage" | **Almost always false.** It is nearly always intake creep, NEAT suppression and reduced mass compounding **[moderate]** — but see the exception in §2.1 for lean, chronically restricting people, where the plateau may be real and dieting further is the wrong move |

### 2.5 The [constrained total energy expenditure model](#constrained-total-energy-expenditure-model)

Pontzer's work suggests **total daily burn does not simply scale with how much you move.** Hadza hunter-gatherers, who walk many kilometres a day, expend about the same total energy as sedentary Westerners once you correct for body size (Pontzer et al., 2012; n = 30 Hadza adults measured by [DLW](#dlw)) **[moderate]**, and across a large multi-country sample total expenditure rises with activity but flattens out rather than climbing linearly (Pontzer et al., 2016; n = 332) **[moderate]**.

**Narrowing the claim, because it is routinely overstated.** The Hadza result is a comparison of *populations*, not an experiment: it shows total expenditure is similar after size correction, which is consistent with compensation but does not by itself prove it, and body-composition correction across very different populations is contested **[contested]**. The defensible version is **partial** compensation, not full.

The best quantification: across 1,754 adults with [doubly labeled water](#dlw) measurements, energy compensation via reduced basal expenditure averaged **~28%** — meaning roughly 72% of the calories burned in extra activity actually show up as extra daily burn — and compensation was **greater in people with more body fat** (Careau et al., 2021) **[strong for the average; the adiposity link is correlational]**. Add compensation through increased eating and reduced spontaneous movement, and total offsets of ~20–50% are a reasonable working range **[moderate]**.

**Consequence:** *"just add more cardio"* is a weaker lever than it looks — but it is not a broken one. Roughly seven-tenths of what you burn still counts. Exercise is a mediocre *deficit-creation* tool and an excellent *tissue-protection* tool: it preserves [LBM](#lbm), improves cardiometabolic health, and is the single most consistent behaviour among long-term maintainers. **Diet creates most of the deficit; training protects the tissue.**

### 2.6 Refeeds, diet breaks, and reverse dieting

| Strategy | Definition | Evidence |
|---|---|---|
| **[Refeed](#refeed)** | 1–2 days at maintenance, carbohydrate-led | Restores muscle glycogen and training performance; transiently raises leptin. **Effect on fat-loss outcomes is small and inconsistent**; the performance and psychological benefits are the better justification **[limited]** |
| **[Diet break](#diet-break)** | 1–2 weeks at maintenance, periodically | **MATADOR** (Byrne et al., 2018): 51 men with obesity randomised to 16 weeks continuous restriction vs. the same 16 weeks of restriction broken up by 2-week maintenance blocks. The intermittent group lost more weight (14.1 vs 9.1 kg) and more fat. **Read the caveats:** only 36 of 51 completed per protocol and results are per-protocol, not intention-to-treat; the intermittent arm ran 30 calendar weeks vs 16; and it was men with obesity only. **The replication is null:** ICECAP randomised 61 resistance-trained adults (32 women) to intermittent vs continuous restriction and found **no difference** in fat mass, body weight or fat-free mass (Peos et al., 2021). Broader meta-analysis of intermittent vs continuous restriction also finds no consistent advantage (Cioffi et al., 2018; 11 RCTs) **[contested]**. Claims that diet breaks improve *adherence* are plausible but, as far as I could verify, **untested** — MATADOR did not measure adherence as an outcome and had substantial dropout |
| **[Reverse dieting](#reverse-dieting)** | Gradual post-diet calorie increases to "rebuild metabolism" | **Popular, essentially unevidenced.** No controlled trial supports the metabolic-rebuilding claim [UNVERIFIED — could not confirm any trial either way]. What it plausibly does provide is a *structured* return to maintenance, which aids adherence and limits overshoot — value it for that, not the stated mechanism **[limited]** |
| **[Intermittent fasting](#intermittent-fasting) / [TRE](#tre)** | Restricted eating windows | **No metabolic advantage over continuous restriction when calories and protein are equated** (Cioffi et al., 2018, meta-analysis of RCTs) **[strong]**. It is an adherence tool that suits some people and not others. Caution: narrow windows make adequate protein intake harder, which matters for LBM retention **[moderate]** |

---

## PART 3 — Preserving Lean Mass (the actual objective)

Fat loss, not weight loss, is the goal. In an unmanaged deficit, roughly **20–30% of the weight lost is [lean body mass](#lbm)** [consensus — no single source; the true fraction varies strongly with starting fat mass, per Forbes, 2000] **[moderate]**. That fraction is highly modifiable.

**The four levers, in order of effect size:**

| Lever | Prescription | Why |
|---|---|---|
| **1. [Resistance training](#resistance-training)** | 2–4×/wk, maintain [load](#load), reduce [volume](#training-volume) if recovery falters | **The single most effective intervention.** It supplies the mechanical signal that tells the body to keep the muscle. Maintain *intensity* — heavy loads, even at reduced volume [consensus — no single source] **[moderate]** |
| **2. Protein** | **1.6–2.4 g/kg body weight**; up to **2.3–3.1 g/kg [FFM](#ffm-lbm)** when lean and in a large deficit | Requirements rise during restriction. 1.6 g/kg is where the dose–response for training-induced muscle gain plateaus in a meta-analysis of 49 RCTs, n = 1,863 (Morton et al., 2018) **[strong]**; the higher lean-athlete figure comes from a systematic review of dieting resistance-trained athletes (Helms et al., 2014) **[moderate]**. Protein is also the most [satiating](#satiety-vs-satiation) macronutrient and highest in [TEF](#tef) |
| **3. Deficit moderation** | ≤~0.5–0.75% BW/wk, and **≤~500 kcal/day if you want to hold or build muscle** | Rate of loss is the strongest modifiable predictor of how much lean mass you lose. Elite athletes losing at ~0.7%/wk gained lean mass and strength; those losing at ~1.4%/wk did not (Garthe et al., 2011; n = 24 elite athletes, 8–12 weeks) **[moderate — small n]**. Meta-regression puts the point where lean-mass gain stops at about a 500 kcal/day deficit (Murphy & Koehler, 2022) **[moderate]**. See also the [Alpert ceiling](#maximum-fat-oxidation-ceiling) and Forbes' curve in §1.3 |
| **4. Sleep** | 7–9 h | **Nedeltcheva et al. (2010):** 10 adults with overweight, randomised crossover, 14 days of identical moderate restriction with 8.5 h vs 5.5 h sleep opportunity. Both conditions lost ~3.0 kg. With adequate sleep, 1.4 kg of that was fat; with restricted sleep, only 0.6 kg — so the fat share of loss fell from roughly **half to about a fifth**, and fat-free-mass loss rose by 60%. Sleep restriction also raised hunger and ghrelin **[limited — n = 10, 14 days, one lab; directionally consistent with other work but the effect size should not be quoted as precise]** |

**[Body recomposition](#body-recomposition)** — losing fat and gaining muscle at the same time — is genuinely achievable in novices, returning trainees ([muscle memory](#muscle-memory)), people with higher body fat, and people correcting from very low protein **[moderate]**. It is slow and largely unavailable to lean, trained people in a substantial deficit — they should run fat-loss and muscle-gain phases separately.

---

## PART 4 — Diet Composition

### 4.1 The hierarchy

```
1. Energy balance          → determines weight change            (dominant)
2. Protein intake          → determines composition of that change
3. Fiber / food selection  → determines satiety, adherence, micronutrients
4. Fat/carb split          → determines preference, performance, adherence
5. Meal timing/frequency   → determines convenience; minimal independent effect
6. Supplements             → marginal
```

### 4.2 Macronutrients in a deficit

| Macronutrient | Target | Rationale |
|---|---|---|
| **Protein** | 1.6–2.4 g/kg BW (higher when lean) | LBM retention, [satiety](#satiety-vs-satiation), [TEF](#tef) ~20–30%. Diminishing returns above ~1.6 g/kg for muscle gain (Morton et al., 2018); the case for 2.4 g/kg and above is specific to lean dieters (Helms et al., 2014) **[moderate]** |
| **Fat** | ≥0.5–0.8 g/kg, floor ~20% of calories | Essential fatty acids, fat-soluble vitamins. **Note on the sex-hormone claim:** low dietary fat is associated with lower testosterone, but in dieting athletes the dominant driver of falling sex hormones is low *energy availability*, not the fat percentage as such (Mountjoy et al., 2023). Do not assume that eating more fat at the same low intake protects your hormones — it does not **[moderate; a common misattribution]** |
| **Carbohydrate** | Remainder | Fuels training intensity, and therefore the LBM-preserving stimulus. Not required for fat loss, but low-carb diets typically degrade high-intensity performance **[moderate]** |
| **Fiber** | 14 g per 1000 kcal (≈25–38 g/day) | Satiety, glycaemic control, gut microbiome, [energy density](#energy-density) reduction [consensus — no single source; US Dietary Reference Intake] |
| **Alcohol** | Minimize | 7 kcal/g, no satiety value, acutely suppresses fat oxidation and [MPS](#mps-mpb), impairs sleep, disinhibits eating **[moderate]** |

**On the carbohydrate–insulin model.** The strong version — that carbohydrate-driven insulin secretion causes fat gain more or less independently of energy balance — has been tested directly under metabolic-ward conditions and not supported: at matched calories, cutting fat produced slightly *more* body-fat loss than cutting carbohydrate (Hall et al., 2015), and an isocaloric ketogenic diet produced only a small, transient rise in expenditure that did not accelerate fat loss (Hall et al., 2016; n = 17, 8 weeks inpatient) **[strong against the strong version]**.

**But do not flatly reject the model, because that overstates the evidence.** Proponents have published a substantially weaker and more defensible formulation — that high-glycaemic-load diets shift substrate partitioning and appetite in ways that promote positive energy balance *through intake* (Ludwig et al., 2021) — and the dispute is live in the peer-reviewed literature (Hall et al., 2018; Ludwig & Ebbeling, 2018) **[contested]**. The correct statement is narrow: **insulin regulates where nutrients go; energy balance regulates how much fat you carry.** Carbohydrate quality still matters, via appetite and food choice, which is exactly where the ultra-processed-food evidence below lives.

### 4.3 Why "which diet" barely matters

Head-to-head trials consistently show **no clinically meaningful difference between low-carb and low-fat diets** at 12 months:

- **DIETFITS** (Gardner et al., 2018): 609 adults, 12 months, healthy low-fat vs healthy low-carbohydrate. Mean loss 5.3 vs 6.0 kg — no significant difference. Neither insulin-secretion status nor a three-SNP genotype pattern predicted who did better on which diet **[strong]**.
- **A TO Z** (Gardner et al., 2007): 311 premenopausal women, 12 months, Atkins vs Zone vs LEARN vs Ornish. Atkins lost more (−4.7 kg) than Zone (−1.6 kg), with LEARN and Ornish in between; the Atkins-vs-Zone difference was statistically significant **[strong]**.

> **Correction to a claim this document previously made.** Neither trial equated calories or protein — both were free-living, ad libitum, with no prescribed calorie target. So they do **not** show "no difference when protein and calories are controlled." They show something more useful: *assigning* a macronutrient pattern does not reliably change one-year outcomes, and A TO Z shows the differences that do appear are small and not always zero. Within-group variance dwarfs between-group variance in both.

**What genuinely predicts success:**
1. **Adherence** — by a wide margin the dominant variable **[strong]**
2. Protein adequacy **[strong]**
3. Low [energy density](#energy-density) and high fiber ([satiety per calorie](#satiety-vs-satiation)) **[moderate]**
4. Minimising [hyper-palatable](#hyperpalatable-food) [ultra-processed foods](#upf) — **Hall et al. (2019): 20 adults, 4 weeks as inpatients, randomised crossover, ultra-processed vs unprocessed diets matched for presented calories, energy density, macronutrients, sugar, sodium and fibre, both eaten ad libitum. Participants ate ~500 kcal/day more on the ultra-processed arm and gained weight on it while losing weight on the other** **[strong for internal validity; limited for generalisability — n = 20, 4 weeks, one facility]**
5. Self-monitoring (food logging, regular weighing) **[moderate; observational]**
6. Sleep and stress management **[moderate]**

### 4.4 Supplements — honest accounting

| Supplement | Verdict |
|---|---|
| **Caffeine** | Small, real effect on expenditure and performance. In lean volunteers, ordinary caffeine doses raised daily energy expenditure by roughly 3–5% (Dulloo et al., 1989; n = 10) **[limited — small, old, and tolerance develops to the thermogenic component]** |
| **Protein powder** | Not special — a convenient way to hit protein. That is genuinely useful **[strong]** |
| **Creatine** | No fat-loss effect; supports strength and LBM retention. Causes ~1–2 kg of water-weight gain — do not misread the scale [consensus — no single source] **[strong]** |
| **Green tea / EGCG, capsaicin, synephrine, CLA, L-carnitine, raspberry ketone, garcinia** | Effects range from trivially small to zero. Not worth the money **[moderate]** |
| **Fiber supplements (glucomannan, psyllium)** | Modest satiety benefit; real food is better **[limited]** |
| **Nicotine, DNP, clenbuterol, unregulated "fat burners"** | Range from harmful to lethal. **DNP causes hyperthermia and death at doses close to those taken for weight loss, and there is no antidote** (Grundlingh et al., 2011) **[strong]**. Not recommended in any circumstance |

---

## PART 5 — Adipose Tissue Biology

### 5.1 Fat cells

- **[Adipocyte](#adipocyte) hypertrophy** — existing cells getting bigger — is the main way adults gain fat **[strong]**.
- **[Adipocyte hyperplasia](#adipocyte-hyperplasia-vs-hypertrophy)** — making new fat cells — happens mainly in childhood and adolescence, and in severe adult obesity **[strong]**.
- **Fat-cell *number* is essentially fixed in adulthood.** Radiocarbon dating of adipocyte DNA shows roughly 10% of fat cells are replaced each year while the total stays constant, in both lean and obese adults (Spalding et al., 2008) **[strong]**. Dieting **shrinks** cells; it does not remove them. This is one mechanistic contributor to why maintaining loss after prolonged obesity is hard.
- **[Brown adipose tissue (BAT)](#bat)** generates heat via [UCP1](#ucp1) and is present in adults, but in quantities too small to be a realistic weight-loss target with current interventions. **[Beige/brite adipocytes](#beige)** ("browning") are an active research area, not a usable strategy **[moderate]**.

### 5.2 Fat mobilization

[Lipolysis](#lipolysis) → hormone-sensitive lipase and [ATGL](#atgl-hsl) break stored triacylglycerol apart → free fatty acids and glycerol are released → carried to tissues → **[β-oxidation](#beta-oxidation)** burns them. Stimulated by [catecholamines](#catecholamines) (adrenaline and noradrenaline) and low [insulin](#insulin); inhibited by insulin **[strong]**.

**Where the fat physically goes:** oxidised fat leaves the body mostly **as CO₂ through your lungs (~84%)**, with the rest as water (~16%) (Meerman & Brown, 2014) **[strong — this is stoichiometry, not an experiment]**. Fat is not sweated out, not "burned off" as heat, and not converted into muscle. You exhale it.

The split comes straight from the atoms in a fat molecule, so you can check it yourself. Tripalmitin, a typical triglyceride, weighs 861 daltons. The part that leaves as carbon dioxide is its 55 carbon atoms plus four oxygens: (661 + 64) ÷ 861 = **84%**. The part that leaves as water is its hydrogens plus the remaining two oxygens: (105 + 32) ÷ 861 = **16%**. *Verified against the full text at bmj.com, not just the abstract.*

### 5.3 Three durable myths

| Myth | Reality |
|---|---|
| **[Spot reduction](#spot-reduction)** | Training a muscle does not preferentially strip the fat sitting on top of it. In a controlled trial, 12 weeks of localised single-leg endurance resistance training produced fat loss in the *upper body*, not the trained leg (Ramírez-Campillo et al., 2013; n = 11) **[moderate — small n, but consistent with the wider literature]**. Regional fat-loss order is largely genetic, mediated by α₂- vs β-adrenergic receptor density and blood flow |
| **The "[fat-burning zone](#fat-burning-zone)"** | Low intensity burns a higher *percentage* of energy from fat but fewer *total* calories. **Fat balance over 24 hours, not substrate use during the session, determines fat loss** **[strong]** |
| **Fat turns into muscle (or vice versa)** | Distinct tissues, no conversion pathway. They change independently and only appear coupled **[strong]** |

### 5.4 Body fat reference ranges

| Category | Male | Female |
|---|---|---|
| **[Essential fat](#essential-body-fat)** | 3–5% | 10–13% |
| Athletic | 6–13% | 14–20% |
| Fitness | 14–17% | 21–24% |
| Average | 18–24% | 25–31% |
| Obese ([BF%](#bf) criterion) | ≥25% | ≥32% |

**Provenance, honestly.** The "athletic / fitness / average" rows are conventional textbook categories with no single primary source [consensus — no single source] **[limited]**. The health-linked thresholds are better grounded: BMI-anchored healthy body-fat ranges derived from a multi-ethnic sample of 1,626 adults put the obesity-equivalent cut-point near 25% in men and 35–38% in women depending on age (Gallagher et al., 2000) **[moderate]** — note that this is *higher* than the 32% figure in the table above, which is one reason not to treat any of these numbers as precise.

> **⚠ Do not read this table as a safety map.** Being above "essential fat" does **not** mean your endocrine system is fine. Endocrine and immune function are compromised below essential fat, but they are also commonly compromised well above it, because the operative variable is [energy availability](#energy-availability), not body-fat percentage (Mountjoy et al., 2023) **[strong]**.
>
> Competitive physique athletes reach 4–6% (M) transiently and pay for it in hormonal, psychological and performance terms. It is not a maintainable state, it is not a health state, and the photographs that make it look otherwise are taken on one day of a multi-year cycle. If you are chasing it, the [RED-S](#red-s) warning signs in §7.2 are for you specifically.

---

## PART 6 — Plateaus, Regain & Maintenance

### 6.1 Why the scale stops moving

Ranked by how often each is actually the answer:

1. **Intake creep** — portions drift, untracked bites accumulate, [under-reporting](#under-reporting) worsens as a diet lengthens. **The most common cause by a wide margin** **[moderate]**
2. **Reduced mass** — a smaller body costs less to run; your original deficit is now your maintenance **[strong]**
3. **[NEAT](#neat) suppression** — unconscious, and the largest *behavioural* term **[moderate]**
4. **[Water retention masking fat loss](#water-retention)** — [cortisol](#cortisol), sodium, glycogen, menstrual phase and post-training inflammation can hide weeks of genuine fat loss. Fat loss is continuous; scale weight is not **[strong]**
5. **[Adaptive thermogenesis](#adaptive-thermogenesis)** — real, and the smallest of these terms **[moderate]**

**Diagnostic order:** measure intake accurately for 7–10 days → check step count and daily activity → assess the 2–4 week weight *trend*, not daily readings → only then consider adjusting. **Reflexively cutting calories at every plateau produces a downward spiral toward an unmaintainable intake, and is one of the most common routes from ordinary dieting into disordered eating.** If your maintenance-adjusted intake is drifting below roughly 30 kcal/kg fat-free mass, stop and reread §1.3.

### 6.2 The regain problem

- **The honest version of the regain statistic.** The widely quoted "80% regain within 5 years" is a folk statistic. Its most likely origin is the finding that **about 20% of people with overweight succeed at long-term weight loss, defined as losing ≥10% of starting weight and keeping it off for ≥1 year** (Wing & Phelan, 2005) — a one-year definition, not five, and a definitional estimate rather than a cohort followed to 5 years **[moderate]**. The counter-evidence is worth knowing: a meta-analysis of 80 trials with ≥1-year follow-up found a mean 5–8.5 kg loss at 6 months and **3–6 kg still maintained at 48 months, with no intervention group regaining all the way to baseline on average** (Franz et al., 2007) **[strong]**. So: most people do not maintain a large loss, but "everyone regains everything" is false, and partial maintenance is the normal outcome.
- The **[National Weight Control Registry](#nwcr)** (entry criteria: ≥13.6 kg kept off for ≥1 year; members average 33 kg lost and >5 years maintained. The often-quoted ">10,000 members" is a registry website figure — the largest peer-reviewed sample is 3,683) reports the common behaviours of successful maintainers: high physical activity (~1 h/day, largely walking), regular self-weighing, a consistent eating pattern including weekends, eating breakfast, and limited television (Wing & Phelan, 2005). **Observational and self-selected by construction — it enrols only successes, so these are correlates, not proven causes, and it cannot tell you what the people who failed did differently** **[limited]**.
- **[Weight cycling](#weight-cycling)** ("yo-yo dieting") is common. Evidence that it independently *harms* metabolism or worsens future outcomes is weak and contested (Mackie et al., 2017, systematic review) **[contested]**. The better-supported concerns are psychological cost and cumulative LBM loss if resistance training is absent during each cycle.

### 6.3 The maintenance principle

**Maintenance is an active state, not the absence of dieting.** Because [ghrelin](#ghrelin) stays elevated and [leptin](#leptin) suppressed, a weight-reduced person has to sustain deliberate behaviours indefinitely to hold the new [settling point](#settling-point-theory) (Sumithran et al., 2011; Rosenbaum et al., 2005) **[moderate]**.

Practical implications:
- Plan the exit before starting the diet. An unplanned exit is a regain.
- Return to maintenance calories deliberately over 2–4 weeks, accepting a small water/glycogen rebound as normal rather than as fat regain. **If you are coming off a VLCD or any prolonged severe restriction, this is a medical process, not a self-managed one — see the refeeding syndrome warning in §1.3** (Mehanna et al., 2008).
- Maintain resistance training. Restored muscle is the metabolic and behavioural anchor of maintenance.
- **Diet in finite blocks** (8–16 weeks) separated by genuine maintenance phases, rather than dieting perpetually.
- Keep the behaviours that produced the loss. The diet was the tool; the habits are the result.

### 6.4 Pharmacology

**These are prescription medicines with real contraindications. This section is here so you can have an informed conversation with a doctor, not so you can source them yourself.**

**[GLP-1 receptor agonists](#glp-1-receptor-agonist)** and **[dual GIP/GLP-1 agonists](#tirzepatide)** work by slowing gastric emptying and acting centrally to suppress appetite. They make a deficit easy to sustain; they do not bypass energetics.

| Drug | Trial | Mean weight loss |
|---|---|---|
| Liraglutide 3.0 mg daily | SCALE, 56 weeks, n = 3,731 (Pi-Sunyer et al., 2015) | **8.4 kg vs 2.8 kg on placebo (~8%)** **[strong]** |
| Semaglutide 2.4 mg weekly | STEP-1, 68 weeks, n = 1,961 (Wilding et al., 2021) | **~14.9%** (86% lost ≥5%) **[strong]** |
| Tirzepatide 5 / 10 / 15 mg weekly | SURMOUNT-1, 72 weeks, n = 2,539 (Jastreboff et al., 2022) | **~15% / ~19.5% / ~21%** (up to 22.5% on the efficacy estimand) **[strong]** |

**Discontinuation.** One year after semaglutide and lifestyle support were withdrawn, participants had **regained about two-thirds of the weight they had lost**, with cardiometabolic markers reverting in parallel (Wilding et al., 2022) **[strong]**. These are treatments for a chronic condition, not a course of antibiotics.

**Contraindications and cautions — the part usually left out:**

- **Personal or family history of medullary thyroid carcinoma, or multiple endocrine neoplasia syndrome type 2 (MEN2): contraindicated.** This is a boxed warning on the GLP-1 agonist and tirzepatide labels, based on rodent thyroid C-cell tumours [consensus — regulatory labelling; human relevance unestablished].
- **History of pancreatitis:** caution; pancreatitis is a recognised adverse event.
- **Gallbladder disease:** rapid weight loss of any cause raises gallstone risk, and cholelithiasis is reported with these drugs.
- **Anaesthesia and sedation:** delayed gastric emptying means the stomach may still contain food after standard fasting, creating a **pulmonary aspiration risk**. Tell any anaesthetist or endoscopist that you are taking one of these drugs; current practice is to extend fasting or hold doses before procedures [consensus — professional society guidance].
- **Gastrointestinal side effects** (nausea, vomiting, constipation, diarrhoea) are common and are the main reason people stop.
- **Diabetes medication:** combining with insulin or sulfonylureas requires dose reduction to avoid hypoglycaemia.
- **Eating-disorder history:** appetite-suppressing drugs interact badly with restrictive eating pathology, and their use as a way to reach or hold a low weight for cosmetic reasons is a recognised and growing clinical concern. If restriction is already a problem for you, these drugs are not a fix for it.
- **Use for cosmetic leanness, in people who are not clinically indicated, is not what these trials studied.** The efficacy and safety data above come from adults with obesity or overweight-plus-comorbidity. None of it transfers to a lean person trying to get leaner.
- **Compounded and grey-market "semaglutide"** bought online is not the studied product. Dosing errors, wrong salt forms, and contamination have caused documented harm. Do not.
- **Lean mass.** A substantial fraction of the weight lost on these drugs is lean tissue unless resistance training and high protein are maintained. Figures around 25–40% circulate widely [UNVERIFIED — could not confirm a primary body-composition source]; treat the direction as established and the number as unreliable, and train and eat protein accordingly.

**[Bariatric surgery](#bariatric-surgery)** remains the most durable intervention for severe obesity. In the Swedish Obese Subjects study — 2,010 surgical patients matched to 2,037 controls, followed a mean of ~11 years — surgery produced large sustained weight loss and reduced overall mortality (Sjöström et al., 2007) **[strong; prospective matched cohort, not randomised]**. It works partly through mechanical restriction and substantially through altered gut-hormone signalling (elevated [GLP-1](#glp-1) and [PYY](#pyy)), which is why its effect exceeds what restriction alone predicts.

---

## PART 7 — Practice

### 7.1 Setting up

**Age guard: this protocol is written for adults (18+). It is not appropriate for adolescents, whose energy needs are elevated by growth and bone accrual and who require paediatric or dietetic supervision for any deliberate weight change.**

```
0. SCREEN OUT
     Do not start if any item in the STOP block at the top of Part III applies.
     If you take antihypertensives, thyroid replacement, insulin or a
     sulfonylurea, tell your prescriber before you begin — doses commonly
     need reducing as you lose weight.

1. ESTIMATE TDEE
     Track intake + weight for 10-14 days at stable weight.
     Observed maintenance beats any prediction equation
     ([Mifflin-St Jeor](#mifflin-st-jeor) is the best of them, +/-10-15% error).

2. SET THE DEFICIT
     20-25% below TDEE for most people.
     Cross-check against ALL THREE ceilings:
       - target rate 0.5-0.75% BW/week
       - <= ~500 kcal/day if holding or building muscle
       - energy availability >= 30 kcal per kg fat-free mass per day
     Take the smallest number the three give you.

3. SET PROTEIN FIRST
     1.6-2.4 g/kg BW.  Fat floor >= 0.5 g/kg.  Carbs fill the remainder.

4. TRAIN
     Resistance training 2-4x/wk, load maintained.
     Steps: 8-10k/day as a NEAT guardrail against unconscious suppression.

5. MEASURE
     Daily weigh-in, same conditions; act only on the 7-day rolling average.
     Waist circumference weekly.  Photos every 2-4 weeks.
     Training performance log - the earliest signal of an excessive deficit.
     Menstrual cycle log (F) - the earliest signal of an excessive deficit.

6. ADJUST
     Only after 2-3 weeks of no trend movement, and only after auditing
     intake accuracy and step count first.
     Prefer adding activity to cutting calories, WITHIN LIMITS - see note.

7. EXIT
     Plan it in advance. 8-16 week blocks, then a genuine maintenance phase.
```

> **Note on step 6, reconciling it with §2.5.** Section 2.5 says exercise is a poor tool for *creating* a deficit. Step 6 says prefer adding activity to cutting calories. Both are right, for different reasons, and here is how they fit together. Adding activity is the preferred *first* adjustment because it does not further reduce food volume, fibre, micronutrients or satiety, and because it protects lean mass — not because it is an efficient way to burn calories. But size it honestly: expect roughly **70% of the nominal burn** to show up in your daily total (Careau et al., 2021), and expect that fraction to be worse the more body fat you carry. Activity also has a low ceiling before recovery and joints object. Once you are at 10–12k steps and your training is already as much as you recover from, the next adjustment has to come from food.

### 7.2 When to stop the diet

**"Stop" here means: return to maintenance calories now, and seek professional assessment. It does not mean "push through", "diet more slowly", or "take a diet break and resume".**

Stop if any of these appear:

- Training performance declining across multiple sessions and lifts
- Sleep disruption, persistent cold intolerance, low libido
- **Menstrual irregularity or amenorrhoea** — stop; this is [RED-S](#red-s) territory (Mountjoy et al., 2023)
- **Loss of morning erections, or a sustained drop in libido, in males** — the male equivalent early signal of [HPG-axis](#hpg-axis) suppression
- **A bone stress injury, or bone pain that worsens with impact** — low energy availability impairs bone; a stress fracture during a diet is a red flag, not bad luck
- **Recurrent infections, or wounds and injuries healing unusually slowly**
- Persistent mood disturbance, food preoccupation, or emerging binge behaviour
- Your calculated energy availability has fallen below ~30 kcal per kg fat-free mass per day
- Reaching a planned target, or 16 weeks elapsed

If you find you cannot stop when these appear — that the idea of eating more is more frightening than the symptoms — that is itself the finding. Go to [when this stops being a programming problem](#when-this-stops-being-a-programming-problem).

### 7.3 What matters, ranked

Note that "run a sustained deficit" and "keep the deficit moderate" are the same variable pointing in opposite directions, so they are shown together rather than at opposite ends of the list.

```
1.  A sustained deficit, moderately sized            ████████████  dominant
2.  Adherence over months                            ███████████
3.  Protein intake                                   ████████
4.  Resistance training                              ████████
5.  Sleep 7-9 h                                      ██████
6.  Fiber / food quality / energy density            █████
7.  Steps / NEAT preservation                        █████
8.  Meal timing, fasting windows                     ██
9.  Supplements                                      ▌
```

### 7.4 Rate-of-loss reality check

| Timeframe | Realistic fat loss (moderate deficit) |
|---|---|
| Per week | 0.5–0.75% of body weight |
| Per month | 2–3% of body weight |
| 12-week block | 6–9% of body weight, and realistically less |
| Per year (with maintenance phases) | 10–20% of body weight |

The yearly figure assumes genuine maintenance phases between blocks and is an upper expectation, not a plan. Against real trial data it is optimistic: pooled across 80 trials, mean loss at 6 months was 5–9% and at 4 years 3–6% (Franz et al., 2007). If you are hitting the top of this table you are doing better than almost everyone in the literature; if you are at the bottom you are normal.

### 7.5 The one-paragraph version

Work out your maintenance calories by tracking for two weeks, then eat about 20–25% below that. Check that number against three limits and take the smallest: roughly 0.5–0.75% of body weight lost per week, no more than about a 500 kcal/day deficit if you want to keep your muscle, and never less than 30 kcal per kg of fat-free mass after subtracting what you burn training. Set protein at 1.6–2.4 g/kg and a fat floor, then fill the rest with whatever you will actually eat. Lift 2–4 times a week keeping the loads heavy, walk 8–10k steps so your body cannot quietly stop moving, and sleep 7–9 hours. Weigh daily, act only on the weekly average, and when the scale stalls, audit your food and your steps *before* cutting anything. Expect real adaptation of perhaps 50–150 kcal/day — not metabolic damage. Diet in 8–16 week blocks and plan the exit in advance, because the biology defending your old weight persists for a year or more after you finish. And stop early, without negotiating with yourself, if your periods stop, your morning erections stop, you break a bone, you keep getting ill, or food starts occupying your thoughts.

## when-this-stops-being-a-programming-problem

**§7.6 — When this stops being a programming problem.** *(This heading is written in slug form, following the anchor convention stated in the Contents. It is the most safety-critical link target in the document and must resolve identically in every renderer, so it does not get a prose heading.)*

**Restriction is a recognised trigger for eating disorders.** The physiology described throughout this part — food preoccupation, post-restriction [hyperphagia](#hyperphagia), binge behaviour — is a **predictable consequence of restriction itself**, documented since the Minnesota experiment in men with no prior eating pathology (Kalm & Semba, 2005). It is not a character failing, and it is not solved by more discipline. More discipline is how it gets worse.

**Seek professional help if any of these are true:**

- Eating or weight thoughts are intrusive, frequent, or distressing
- You experience loss of control around food, or eat in a way that feels like it is not a choice
- You compensate for eating with vomiting, laxatives, diuretics, fasting, or punitive exercise
- You avoid eating with other people, or arrange your social life around food rules
- You check your body — mirrors, pinching, measuring, weighing — frequently
- Your weight is below a healthy range and still falling
- You cannot stop dieting when the warning signs in §7.2 appear
- Other people who know you have said they are worried

**Who to contact:** a physician, a registered dietitian, or an eating-disorder specialist. In most countries there is a national eating-disorder charity with a free helpline; searching "eating disorder helpline" plus your country will find it faster than any list printed here can stay current. Eating disorders have among the highest mortality of any psychiatric illness and they respond well to early treatment — early is the operative word.

**A training program is not the right resource for this, and neither is this document.**

---

---
# Part IV Master Glossary

Every technical term used anywhere in this document, defined formally with formula and units where the quantity is physically or operationally defined. Entries are alphabetical; the tag under each heading gives its domain. Every entry follows the same three-part pattern: a plain-English opening sentence, then the formal definition, then why it matters in practice. Every in-text mention links here, and every link is a plain same-file heading anchor — no HTML anchors, no cross-file references.

## acwr

*Training, Loading & Contraction*

**ACWR (acute:chronic workload ratio)** — A number that compares how much you trained this week against how much you have been training lately. Formally, the ratio of short-term to long-term accumulated [training load](#training-load):

> ACWR = acute load (rolling 7 days) / chronic load (rolling 28-day average)

A value of 1.0 means this week matched your recent norm; 1.5 means you did half again as much. Proposed "sweet spot" ≈ 0.8–1.3; values >1.5 associate with elevated injury risk. **Methodological caveat:** the ACWR framework has been substantively criticized (mathematical coupling of numerator and denominator, arbitrary binning, spurious-correlation artifacts). Use as a heuristic for detecting load spikes, not as a validated risk score.

## adaptive-thermogenesis

*Metabolic Adaptation & Endocrine Regulation*

**Adaptive thermogenesis (metabolic adaptation, narrow sense)** — When you diet, your body burns slightly less energy than its new, smaller size alone would explain. That extra slowdown is adaptive thermogenesis: a reduction in energy expenditure **beyond** that predicted by the loss of metabolically active tissue. Quantified as the residual:

> AT = measured RMR − RMR predicted from post-diet body composition

Typical magnitude: **~50–150 kcal·day⁻¹**; up to ~300 kcal·day⁻¹ after large or rapid losses. The best-controlled anchor is CALERIE: 2 years of ~15% restriction in 53 non-obese adults left 24-hour and sleeping expenditure **80–120 kcal·day⁻¹ below prediction** (Redman et al., 2018).

**A definitional caution.** AT is *defined* as a statistical residual, and that definition says nothing about cause. The mechanisms usually invoked — falling [leptin](#leptin), reduced [T3](#thyroid-hormones), reduced [sympathetic](#sns) tone, and increased skeletal-muscle work efficiency — are supported hypotheses about what fills the residual, not part of what AT *is*, and some of any measured residual is simply error in the prediction equation. **Real, measurable, and considerably smaller than popular discourse claims.** Distinguish from the *broad* sense of [metabolic adaptation](#metabolic-adaptation), which includes mass loss, reduced [TEF](#tef), and [NEAT](#neat) suppression.

## adherence

*Appetite, Behavior & Adherence*

**Adherence** — Whether you actually do the thing the plan says. Formally: the degree to which actual behavior matches the prescribed intervention, over the full duration of the intervention. **The dominant predictor of weight-loss outcome, exceeding every dietary composition variable in effect size.** Consequence: the best diet for an individual is the adequately structured one they will actually follow, and comparative diet trials largely measure adherence differences dressed as metabolic ones.

## adipocyte

*Body Composition & Adipose Biology*

**Adipocyte** — A fat cell. Formally: the lipid-storing cell of adipose tissue, containing a single large triacylglycerol droplet that displaces the nucleus to the cell edge (white adipocyte). It is also an endocrine cell, secreting [leptin](#leptin), adiponectin, and inflammatory cytokines — which is why adipose tissue is correctly described as an endocrine organ rather than inert storage.

## adipocyte-hyperplasia-vs-hypertrophy

*Body Composition & Adipose Biology*

**Adipocyte hyperplasia vs. hypertrophy** — Fat mass can rise two ways: existing fat cells get bigger, or new ones appear. **Hypertrophy** = existing adipocytes enlarging; the dominant mechanism of adult fat gain. **Hyperplasia** = increase in adipocyte *number*, from preadipocyte differentiation; occurs principally during childhood and adolescence and in severe adult obesity. **Adipocyte number is approximately fixed in adulthood** (~10% annual turnover with constant total, established by radiocarbon dating of adipocyte DNA; Spalding et al., 2008), so weight loss shrinks cells without eliminating them. Practical reading: you can empty fat cells but not delete them, which is one mechanistic contributor to the difficulty of maintaining loss after prolonged obesity.

## ages

*Cell & Molecular Biology*

**AGEs (advanced glycation end-products)** — Sugar molecules can stick to proteins without any enzyme directing the process, gluing neighbouring protein strands together; the products of that reaction are AGEs. Formally: compounds formed by non-enzymatic reaction of reducing sugars with protein amino groups (Maillard chemistry), producing irreversible non-enzymatic collagen [cross-links](#collagen-cross-linking) such as pentosidine. Because tendon core collagen turns over extremely slowly ([bomb-pulse dating](#radiocarbon-bomb-pulse-dating)), AGEs accumulate over decades. Effect: increased stiffness with **decreased** toughness and increased brittleness. Accelerated by hyperglycemia — the mechanistic link between diabetes and tendinopathy.

## aggrecan

*Anatomy & Composition*

**Aggrecan** — A large, heavily sugar-coated matrix molecule that holds water and lets tissue resist being squashed. Formally: a large aggregating chondroitin-sulfate [proteoglycan](#proteoglycan). In tendon it is concentrated in regions subjected to compression (fibrocartilaginous zones, e.g. where a tendon wraps a bony pulley). Its high fixed negative charge binds water, conferring compressive resistance. Elevated aggrecan expression is a marker of compressive loading and of tendinopathic matrix change.

## alfredson-protocol

*Training, Loading & Contraction*

**Alfredson protocol** — The original heavy heel-drop program for Achilles pain: two sessions a day, every day, for three months. Formally: the classical heavy-load **[eccentric](#eccentric-contraction)** regimen for midportion Achilles tendinopathy (Alfredson et al., 1998) — 3 × 15 eccentric heel drops, performed with the knee straight and again with the knee bent, **twice daily, 7 days per week, for 12 weeks**, with external load added progressively via a backpack; performed *into* pain. Historically the reference standard; produces large effect sizes but has poor adherence and is **not superior to [HSR](#hsr)** (Beyer et al., 2015). **Caveat:** the founding study was 15 patients with no control group, so its reputation outruns its design; later controlled work supports eccentric loading for this condition. **Moderate evidence.** It is also the standing counter-example to the every-other-day rule — it loads the tendon twice daily, seven days a week, and works.

## amrap

*Loading Variables & Prescription*

**AMRAP (as many repetitions as possible)** — A set where you keep going until you cannot do another good rep. Formally: a set performed to [momentary failure](#momentary-failure) or to a specified [RIR](#rir), used either as a training method or as an [autoregulation](#autoregulation) probe of current capacity. Its practical value is as a measurement: the rep count on a known load tells you what today's readiness actually is.

## aponeurosis

*Anatomy & Composition*

**Aponeurosis** — A flat, sheet-like tendon that spreads across the surface of a muscle instead of forming a rope. Formally: a broad, thin sheet of dense collagenous connective tissue into which muscle fibers insert, mechanically continuous with the free tendon and forming part of the [MTU](#mtu). It matters because measured "tendon" stiffness in vivo usually includes the aponeurosis, so tendon and aponeurosis stretch in series and share the [strain](#strain) applied to the unit.

## apophysitis

*Pathology & Clinical*

**Apophysitis** — A growing-plate injury at the spot where a tendon pulls on a child's or teenager's bone. Formally: traction-induced injury at an **apophysis** (a secondary ossification center serving as a tendon attachment) in the skeletally immature, occurring when the apophyseal growth plate is the mechanically weakest link. Named forms: **Osgood–Schlatter** (tibial tuberosity / patellar tendon), **Sever's disease** (calcaneus / Achilles), **Sinding-Larsen–Johansson** (inferior patellar pole). Risk peaks around [peak height velocity](#phv). Self-limiting with skeletal maturity; managed by load modulation, not cessation.

## ascorbate

*Pharmacology, Nutrition & Medical*

**Ascorbate (vitamin C)** — Vitamin C, which collagen-building enzymes cannot work without. Formally: an essential cofactor for [prolyl and lysyl hydroxylases](#prolyl-lysyl-hydroxylase); it maintains the enzymes' Fe²⁺ in the reduced state. Deficiency prevents stable collagen triple-helix formation (the mechanism of scurvy). Supplementation above sufficiency has no demonstrated additional collagen benefit; ~50 mg is used alongside collagen peptides in the pre-load protocol.

## asymptomatic-imaging-abnormality

*Pathology & Clinical*

**Asymptomatic imaging abnormality** — A scan that looks abnormal in a person whose tendon does not hurt and works fine. Formally: structural change on ultrasound or MRI (hypoechogenicity, thickening, [neovascularization](#neovascularization), intrasubstance signal change) in a pain-free individual. Highly prevalent in jumping and running athletes (Docking et al., 2015). Its existence is the basis for the clinical rule that **imaging findings must not be treated in the absence of symptoms or capacity deficit**; such findings do carry modestly elevated prospective risk but poor positive predictive value.

## atgl-hsl

*Body Composition & Adipose Biology*

**ATGL / HSL (adipose triglyceride lipase / hormone-sensitive lipase)** — The two enzymes that chop stored fat into pieces small enough to leave the fat cell. Formally: the principal enzymes of [lipolysis](#lipolysis). ATGL catalyzes the first hydrolysis step (triacylglycerol → diacylglycerol); HSL the second, and is the step regulated by [catecholamine](#catecholamines)-driven PKA phosphorylation and inhibited by [insulin](#insulin).

## autoregulation

*Programming & Progression*

**Autoregulation** — Letting today's training be decided by how you actually perform today, rather than by a number written weeks ago. Formally: any prescription method in which the day's actual training dose is determined by the athlete's measured or reported readiness rather than fixed in advance. Implementations: [RPE](#rpe)/[RIR](#rir)-based load selection, [velocity-based training](#vbt), [AMRAP](#amrap)-driven load adjustment, and readiness-questionnaire-gated volume. Rationale: day-to-day variation in maximal strength is substantial (commonly ±5–10% of [1RM](#one-rep-max)), so a fixed percentage prescription is systematically wrong on most days.

## bariatric-surgery

*Pharmacology & Clinical*

**Bariatric surgery** — Weight-loss operations that reshape the stomach or gut. Formally: surgical intervention for severe obesity (sleeve gastrectomy, Roux-en-Y gastric bypass, gastric band). Produces the most durable long-term weight loss of any intervention (typically 25–30% total body weight at 2 years for bypass); in the Swedish Obese Subjects study — 2,010 surgical patients matched to 2,037 controls, followed a mean of ~11 years — it also reduced overall mortality (Sjöström et al., 2007; prospective matched cohort, not randomised). Mechanism is **not primarily mechanical restriction**: profound alterations in gut hormone signaling — markedly elevated post-prandial [GLP-1](#glp-1) and [PYY](#pyy), reduced [ghrelin](#ghrelin) — reset appetite regulation, which is why outcomes exceed what restriction alone predicts.

## bat

*Body Composition & Adipose Biology*

**BAT (brown adipose tissue)** — A rare kind of fat that burns energy to make heat instead of storing it. Formally: thermogenic adipose tissue, dense in mitochondria and expressing [UCP1](#ucp1), which dissipates the mitochondrial proton gradient as heat instead of capturing it as ATP. Abundant in infants; present in adults (supraclavicular, paravertebral) and activated by cold exposure. **Quantitatively too small in adults to be a practical weight-loss target with current interventions.**

## beige

*Body Composition & Adipose Biology*

**Beige (brite) adipocyte** — Ordinary white fat cells that can be coaxed into behaving a bit like heat-producing brown fat. Formally: [UCP1](#ucp1)-expressing thermogenic adipocytes that appear within white adipose depots in response to cold or β-adrenergic stimulation ("browning"). An active pharmacological research target; not currently a usable intervention.

## beta-oxidation

*Body Composition & Adipose Biology*

**β-oxidation** — The step where fat is actually burned, inside the cell's mitochondria. Formally: the mitochondrial catabolic pathway that sequentially cleaves two-carbon acetyl-CoA units from fatty acyl-CoA, feeding the citric acid cycle. The terminal step of fat "burning." Long-chain fatty acids require the [carnitine shuttle](#carnitine-shuttle) to enter the mitochondrion. Practical point: releasing fat from a fat cell ([lipolysis](#lipolysis)) is not the same as burning it — β-oxidation is the step that removes it for good.

## bf

*Body Composition & Adipose Biology*

**BF% (body fat percentage)** — What share of your body mass is fat. Formally: fat mass as a proportion of total body mass. Measurement methods, in descending order of accuracy: **4-compartment models** (reference standard), DXA (±3–4% absolute error, good for tracking change), ADP/BodPod, hydrostatic weighing, [BIA](#bia) (poor absolute accuracy, hydration-sensitive), skinfolds (technician-dependent), visual estimation (unreliable). **Every method is more reliable for tracking change over time than for absolute value** — use one method consistently under standardized conditions and ignore the absolute number.

## bfr

*Training, Loading & Contraction*

**BFR (blood-flow restriction training)** — Lifting light weights with a cuff around the top of the limb that partly restricts blood flow, so light loads feel and act heavy. Formally: resistance training with a proximal cuff inflated to a fraction of [limb occlusion pressure](#lop) (typically 40–80% LOP), permitting hypertrophy and strength gains at 20–30% 1RM. Valuable when heavy loading is contraindicated. **Important limitation:** because it is low-load and therefore low-[strain](#strain) by design, it does **not** provide the ~70–90% [MVC](#mvc) stimulus tendon adaptation requires — loading below 70% MVC produced an effect size of 0.04 on tendon stiffness, against 0.90 above it (Bohm et al., 2015). **Moderate evidence:** the inference from that threshold is sound, but direct trials of BFR on tendon properties are few.

## bia

*Body Composition & Adipose Biology*

**BIA (bioelectrical impedance analysis)** — The body-fat reading on a bathroom scale or handheld gripper, produced by passing a tiny current through you. Formally: estimation of body composition from the electrical impedance of body tissues, exploiting the higher conductivity of hydrated lean tissue. Highly sensitive to hydration status, meal timing, exercise, and skin temperature, producing large day-to-day variation independent of any real compositional change. Suitable for population screening; poor for individual precision.

## block-periodization

*Programming & Progression*

**Block periodization** — Training in consecutive phases, each of which does one job and sets up the next. Formally: a [periodization](#periodization) structure in which consecutive [mesocycles](#mesocycle) ("blocks") each concentrate on a small number of compatible training targets, sequenced so each block's [residual training effect](#residual-training-effect) supports the next. Canonical sequence: **accumulation** (high volume, moderate intensity) → **transmutation/intensification** (reduced volume, high intensity) → **realization** ([taper](#taper) and peak). Developed for sports with discrete competitions; of limited relevance to continuous hypertrophy training.

## bmr-rmr

*Energetics & Balance*

**BMR / RMR (basal / resting metabolic rate)** — The energy your body uses just staying alive and doing nothing. Formally: the energy expended at complete rest, in kcal·day⁻¹. **BMR** is measured under strict conditions: post-absorptive (12+ h fasted), fully rested, thermoneutral, immediately on waking, supine. **RMR** is measured under relaxed conditions and runs ~3–10% higher; it is what is actually measured in practice, and the two terms are used interchangeably in the literature despite not being identical. Accounts for ~60–70% of [TDEE](#tdee). Predicted primarily by [fat-free mass](#ffm-lbm) — and disproportionately by high-metabolic-rate organ mass (brain, liver, kidney, heart), which is why RMR does not scale linearly with muscle mass. **Muscle tissue expends only ~13 kcal·kg⁻¹·day⁻¹ at rest** (Wang et al., 2010) — the widely repeated claim of 50–100 kcal per kg of muscle is false by roughly an order of magnitude.

## body-recomposition

*Body Composition & Adipose Biology*

**Body recomposition** — Losing fat and gaining muscle at the same time, so the scale barely moves while your shape changes. Formally: simultaneous fat loss and lean mass gain, producing little net weight change. Reliably achievable in: untrained individuals, returning trainees (via [muscle memory](#muscle-memory)), individuals with high body fat, and individuals correcting from inadequate protein. (Adolescents recompose readily during growth, but **deliberate energy restriction in under-18s requires paediatric or dietetic supervision and is outside the scope of this document.**) Slow and largely unavailable to lean, well-trained individuals in a meaningful deficit — for whom sequential fat-loss and muscle-gain phases are more efficient.

## bone-stress-injury

*Pathology & Clinical*

**Bone stress injury (BSI)** — Bone damage from repeated loading, ranging from irritated bone to an actual crack. Formally: a continuum from accelerated bone remodeling ("stress reaction") to frank stress fracture, arising when repetitive loading exceeds bone's remodeling capacity. Relevant here because excessive [MTU](#mtu) stiffness shifts load-attenuation demand onto bone: a very stiff spring passes more shock through to what it is attached to.

## bw

*Units, Abbreviations & Conventions*

**BW (body weight)** — Your own weight, used as the measuring stick for a force. Formally: the gravitational force of the person's body mass, used as a normalizing unit for tendon and joint loads. "6× BW" means the tendon transmits a force six times the person's body weight. Normalizing by BW permits comparison of tendon loads across individuals of different mass, and is also used in this document to express rates of weight change (e.g. "0.5% BW/week").
## calorimetry-direct-and-indirect

*Measurement & Research Methods*

**Calorimetry, direct and indirect** — Two ways of measuring how much energy a person burns: catch the heat they give off, or measure the gases they breathe. **Direct**: measurement of heat production in a sealed chamber; the reference method, rarely used. **Indirect**: calculation of energy expenditure from respiratory gas exchange (O₂ consumed, CO₂ produced), the practical standard. Yields the [RER](#rer-rq), from which substrate utilization is inferred. Whole-room indirect calorimetry ("metabolic chambers") permits precise [TDEE](#tdee) measurement but constrains normal activity — which is precisely why it systematically underestimates free-living [NEAT](#neat).

## carbon-plated

*Training, Loading & Contraction*

**Carbon-plated ("super") shoe** — A racing shoe with a stiff plate embedded in a bouncy foam midsole. Formally: footwear combining a stiff, curved carbon-fiber plate with a high-compliance, high-resilience midsole foam. Improves running economy by roughly 2–4%. It redistributes joint kinetics — typically reducing ankle/Achilles work and increasing knee and hip demand — which changes, rather than uniformly reduces, injury exposure. Introduce gradually.

## carnitine-shuttle

*Body Composition & Adipose Biology*

**Carnitine shuttle (CPT-1/CPT-2)** — The doorway that lets fat molecules into the part of the cell that burns them. Formally: the transport system moving long-chain fatty acyl groups across the inner mitochondrial membrane for [β-oxidation](#beta-oxidation). Frequently invoked to justify L-carnitine supplementation; in practice the shuttle is not rate-limiting in healthy, carnitine-replete individuals, which is why supplementation does not increase fat loss.

## catecholamines

*Metabolic Adaptation & Endocrine Regulation*

**Catecholamines (adrenaline, noradrenaline, dopamine)** — The "fight-or-flight" chemicals your body releases under stress, exercise, or fasting. Formally: a family of signaling molecules derived from tyrosine, released from the adrenal medulla and from sympathetic nerve endings, acting on α- and β-adrenergic receptors. Relevant here as the principal *stimulators* of [lipolysis](#lipolysis) (via β-adrenergic receptors) and as the chemical output of [sympathetic nervous system](#sns) tone — which is why falling SNS tone in a deficit reduces fat mobilization as well as [NEAT](#neat).

## cck

*Metabolic Adaptation & Endocrine Regulation*

**CCK (cholecystokinin)** — A gut hormone that tells your brain to stop eating this meal. Formally: a hormone released from the duodenum in response to fat and protein, producing short-term meal-terminating [satiety](#satiety-vs-satiation) signals and slowing gastric emptying. Declines with energy restriction — one reason a given meal feels less filling once you have been dieting for a while.

## cmj

*Testing & Monitoring*

**CMJ (countermovement jump)** — A standing vertical jump where you dip down quickly and then jump straight up. Formally: a vertical jump initiated from standing with a rapid downward countermovement immediately preceding the upward drive; a **slow-[SSC](#ssc)** task ([ground contact](#gct) typically >250 ms). Standard measure of lower-limb explosive capacity and a sensitive index of neuromuscular [fatigue](#fatigue) — a drop in CMJ height at unchanged body mass usually means accumulated fatigue rather than lost ability.

## cns

*Units, Abbreviations & Conventions*

**CNS (central nervous system)** — The brain and spinal cord. Formally: the division of the nervous system comprising the brain and spinal cord, as distinct from the peripheral nerves. In this document "CNS load" is shorthand for training that heavily taxes voluntary neural drive and coordination — maximal sprints, heavy singles, high-intensity [plyometrics](#plyometrics) — and therefore requires full recovery between efforts rather than conditioning-style short rests. Note that "CNS fatigue" is a loose practical label, not a precisely measured quantity; see [fatigue](#fatigue) for the measurable components.

## collagen-cross-linking

*Cell & Molecular Biology*

**Collagen cross-linking** — Chemical bonds that tie neighbouring collagen strands together, like rungs between ropes. Formally: covalent bonding between collagen molecules that determines matrix tensile strength. Two classes: **(1) enzymatic**, initiated by [lysyl oxidase](#lysyl-oxidase), producing mature, mechanically favorable cross-links; **(2) non-enzymatic ([AGEs](#ages))**, accumulating with age and hyperglycemia, producing brittleness. Training increases enzymatic cross-linking — one of the main ways an adult tendon gets stronger without being rebuilt.

## collagen-type-i

*Anatomy & Composition*

**Collagen, type I** — The rope-like protein that tendon is mostly made of. Formally: a right-handed triple helix of three polypeptide α-chains (two α1(I), one α2(I)) in a repeating Gly-X-Y motif, where X is frequently proline and Y frequently [hydroxyproline](#hydroxyproline). Molecules self-assemble into quarter-staggered [fibrils](#fibril) with a characteristic 67 nm D-period banding. Constitutes ~60–85% of tendon dry mass, and carries essentially all of its tensile strength.

## compound

*Exercise Mechanics*

**Compound (multi-joint) exercise** — A lift that moves more than one joint and uses several muscles at once. Formally: an exercise producing motion at two or more joints, recruiting multiple muscle groups (squat, deadlift, bench press, row, pull-up). Advantages: high absolute load, time efficiency, systemic strength transfer. Disadvantages: high systemic [fatigue](#fatigue) cost (poorer [SFR](#sfr) for any single muscle), higher technical demand, and the possibility of a non-target muscle limiting the set. Contrast [isolation](#isolation).

## concentric-contraction

*Training, Loading & Contraction*

**Concentric contraction** — The lifting half of a rep, where the muscle shortens. Formally: active muscle shortening, occurring when the muscle's force exceeds the external load. Net positive mechanical work.

## constrained-total-energy-expenditure-model

*Energetics & Balance*

**Constrained total energy expenditure model** — The idea that your body holds daily energy use within a fairly narrow band, so extra exercise does not simply add to the total. Formally: the hypothesis (Pontzer) that [TDEE](#tdee) is metabolically constrained within a relatively narrow range rather than scaling additively with physical activity: as activity energy rises, the body reduces expenditure in other domains ([NEAT](#neat), immune activity, reproductive function, stress-axis activity) to defend total expenditure. Evidence: [DLW](#dlw) comparisons showing Hadza hunter-gatherers (n = 30) expend little more total energy than sedentary Westerners after size correction (Pontzer et al., 2012), plus a large multi-country sample in which TDEE rises with activity but flattens rather than climbing linearly (Pontzer et al., 2016; n = 332). **Status: partial compensation is well supported; full constraint is not.** The Hadza comparison is between populations rather than an experiment, and body-composition correction across very different populations is contested, so it is consistent with compensation without demonstrating it. The best quantification comes from 1,754 adults measured by DLW: compensation via reduced basal expenditure averaged **~28%**, meaning roughly 72% of the energy burned in extra activity still shows up in the daily total, with greater compensation in people carrying more body fat (Careau et al., 2021). **Contested at the level of magnitude and mechanism.**

## continuum-model-of-tendon-pathology

*Pathology & Clinical*

**Continuum model of tendon pathology (Cook & Purdam, 2009)** — A map of tendon trouble in three stages, from an irritable but recoverable tendon to one with permanent structural damage. Formally: a three-stage framework — **reactive tendinopathy → tendon dysrepair → degenerative tendinopathy** — describing tendon pathology as a continuum of cell and matrix response to load, in which movement in either direction is possible at earlier stages but limited once degeneration is established. Introduces the clinically important **reactive-on-degenerative** presentation: a chronically degenerated tendon that flares acutely. Practical value: it tells you what recovery to expect and where to aim the loading. **Interpretive caution:** this is a framework built by synthesising clinical and laboratory observation, not a validated staging system — the stages cannot be reliably assigned from imaging, and its own authors have revisited it. **Moderate evidence.** Use it as you use the [ACWR](#acwr): keep the principle, discard the false precision.

## corticosteroid

*Pharmacology, Nutrition & Medical*

**Corticosteroid (glucocorticoid)** — A powerful anti-inflammatory drug, often injected near a painful tendon. Formally: a synthetic analogue of [cortisol](#cortisol) with potent anti-inflammatory action. In tendon: inhibits [tenocyte](#tenocyte) proliferation and collagen synthesis and reduces mechanical strength. Injection yields **short-term analgesia but inferior long-term outcomes** relative to loading or even to wait-and-see. Best evidenced in lateral elbow tendinopathy, where 1-year recovery was 83% with injection versus 96% with placebo and recurrence 54% versus 12% (Coombes et al., 2013); in gluteal tendinopathy the **LEAP trial** found education plus exercise superior at 8 and 52 weeks. The raised rupture risk in weight-bearing tendons rests on mechanism and case series rather than trials — **moderate evidence** for that part.

## cortisol

*Metabolic Adaptation & Endocrine Regulation*

**Cortisol** — The body's main stress hormone, which rises when you are under-fed, under-slept, or over-trained. Formally: the principal glucocorticoid, secreted by the adrenal cortex under [HPA-axis](#hpa-axis) control. Effects relevant here: promotes proteolysis ([LBM](#lbm) cost), promotes renal sodium and water retention (masking scale progress — see [water retention](#water-retention)), and interacts with appetite. Chronically elevated cortisol from an over-aggressive diet plus over-training is a common, self-inflicted cause of stalled visible progress.

## creep

*Mechanics & Material Properties*

**Creep** — Tissue slowly stretching further and further when a steady load is left on it. Formally: progressive increase in [strain](#strain) over time under a constant applied load; a [viscoelastic](#viscoelasticity) behavior. Practically relevant to sustained-load activity and to post-surgical [tendon elongation](#tendon-elongation), where creep before healing consolidates leaves a permanently longer tendon.

## crimp

*Anatomy & Composition*

**Crimp** — The tiny wavy zig-zag pattern in relaxed tendon fibers, which pulls flat before the tendon itself starts to stretch. Formally: the regular planar zig-zag waveform of collagen [fibrils](#fibril) in unloaded tendon, with a wavelength on the order of tens of micrometres. Straightening of crimp under low load produces the [toe region](#toe-region) of the stress–strain curve. Crimp angle decreases with age and with degeneration, which is part of why older tendon has less initial give.

## csa

*Anatomy & Composition*

**CSA (cross-sectional area)** — How thick something is, measured as the area of a slice cut straight across it. Formally: the area of a plane section taken perpendicular to the tendon's or muscle's line of action. Units: mm² or cm². Distinguishes *structural* from *material* properties: [stiffness](#stiffness) scales with CSA, whereas [Young's modulus](#youngs-modulus) is CSA-normalized and does not. For pennate muscle, see [PCSA](#pcsa). Practical consequence: a tendon can get stiffer simply by getting thicker, without its material improving at all.

## decorin

*Anatomy & Composition*

**Decorin** — A small molecule that coats collagen fibrils, controls how thick they grow, and helps them slide against each other. Formally: a small leucine-rich dermatan-sulfate [proteoglycan](#proteoglycan) that binds the surface of type I collagen fibrils, regulating fibril diameter and lateral spacing and mediating interfibrillar shear transfer. Central to tendon [viscoelasticity](#viscoelasticity).

## deload

*Programming & Progression · Training, Loading & Contraction*

**Deload** — A planned easy week, taken to shed accumulated fatigue without losing what you built. Formally: a planned, temporary reduction in training stress intended to dissipate accumulated [fatigue](#fatigue) while preserving adaptation. Typical implementation: reduce [volume](#training-volume) 40–60%, hold [intensity of load](#intensity) at ~80–90% of normal, for 5–7 days, every 4–8 weeks. Volume-reduction is preferred over load-reduction by convention, and the volume half of that is demonstrated: with load held constant at 8–12RM, young adults retained hypertrophy on one-third, and even one-ninth, of their original dose across 32 weeks (Bickel et al., 2011). **Validity caveat:** load was never varied in that trial, so it cannot rank load against volume; and older adults lost muscle size at both reduced doses while keeping their strength, making the low-dose result a young-adult, knee-extensor finding. Read the ~80–90% figure as a fatigue-imposed floor rather than a target [consensus — no single source]. **Contested:** whether a *scheduled* deload improves anything is unclear — in a randomized trial, 39 trained adults given a 1-week deload mid-program gained no extra muscle and lost some lower-body strength relative to continuous training (Coleman et al., 2024). Distinguish from a [taper](#taper), which has the same shape but a different purpose (peaking for a competition rather than recovering within an ongoing block), and from a [reset](#reset), which is a load reduction triggered by a [stall](#stall) rather than scheduled.

## detraining

*Training, Loading & Contraction*

**Detraining** — Losing adaptations because you stopped training. Formally: partial or complete loss of training-induced adaptations following cessation or marked reduction of the stimulus. Tendon [stiffness](#stiffness) declines measurably within ~2–8 weeks of unloading — appreciably faster than the 8–12+ weeks required to gain it (Kubo et al., 2012). Immobilization and bed rest produce rapid, large losses (Kubo et al., 2004). **Moderate evidence** — the underlying studies are small. The asymmetry is the reason returning from a layoff is the highest-risk phase in training. See also [reversibility](#reversibility).

## diet-break

*Appetite, Behavior & Adherence*

**Diet break** — A deliberate week or two of eating at maintenance in the middle of a longer diet. Formally: a planned period of **1–2 weeks at maintenance calories** interrupting a longer deficit, intended to attenuate [adaptive thermogenesis](#adaptive-thermogenesis), restore [leptin](#leptin) and [thyroid](#thyroid-hormones) signaling, and relieve psychological load. Principal evidence: the **MATADOR trial** (Byrne et al., 2018; 51 men with obesity randomised, 2 weeks on / 2 weeks off vs. continuous restriction at equal total *weeks of restriction*) found greater weight loss (14.1 vs 9.1 kg) and less adaptation in the intermittent arm. **Read the caveats:** only 36 of 51 completed per protocol and the analysis is per-protocol; the intermittent arm ran 30 calendar weeks against the continuous arm's 16; men with obesity only. **The replication is null** — ICECAP randomised 61 resistance-trained adults and found no difference in fat mass, body weight or fat-free mass (Peos et al., 2021) — and meta-analysis of intermittent vs continuous restriction finds no consistent advantage (Cioffi et al., 2018). **Status: contested.** The often-repeated claim that diet breaks improve *adherence* is plausible but, as far as could be verified, untested — MATADOR did not measure adherence as an outcome and had substantial dropout. Longer than a [refeed](#refeed), shorter than a maintenance phase.

## disinhibition

*Appetite, Behavior & Adherence*

**Disinhibition (dietary restraint theory)** — The "I've blown it, so I may as well keep going" reaction after breaking a food rule. Formally: the tendency for a rigidly restrained eater to abandon control entirely following a perceived violation ("what-the-hell effect"). Explains why **rigid** dietary restraint predicts binge episodes and poorer long-term outcomes, whereas **flexible** restraint predicts better weight maintenance and lower psychological distress. Practical implication: build the diet to tolerate imperfection rather than to require perfection.

## dlw

*Measurement & Research Methods*

**DLW (doubly labeled water)** — A method that measures how much energy someone really burns while living normally, by tracking specially labeled water leaving the body. Formally: the gold-standard method for free-living [TDEE](#tdee) measurement. Participants ingest water labeled with ²H and ¹⁸O; deuterium is lost as water alone while ¹⁸O is lost as both water and CO₂, so the divergence in elimination rates yields CO₂ production and hence energy expenditure over 1–3 weeks. Accuracy ~±5%. **DLW is the method that established the scale of self-reported intake [under-reporting](#under-reporting)** — the finding that reshaped how energy-balance research is interpreted.

## doms

*Effort, Fatigue & Recovery*

**DOMS (delayed-onset muscle soreness)** — The stiffness and soreness that shows up a day or two after unfamiliar training. Formally: muscle pain and tenderness peaking approximately **24–72 h** after unaccustomed or eccentric-biased exercise, arising from a combination of mechanical microdamage, inflammatory signaling, and sensitization of nociceptors. **Not a marker of stimulus quality, training efficacy, or [hypertrophy](#hypertrophy).** It reflects *novelty* more than effectiveness, and it attenuates with repeated exposure (the **repeated-bout effect**) without any loss of hypertrophic response. Distinguish from [fatigue](#fatigue) (lost force capacity) and from [morning stiffness](#morning-stiffness) (a tendon warning sign).

## dorsiflexion-plantarflexion

*Anatomy & Composition*

**Dorsiflexion / plantarflexion** — Two directions of ankle movement: pulling the toes up toward the shin, and pointing them away. Formally: **dorsiflexion** decreases the angle between foot and shin (toes toward shin); **plantarflexion** increases it (toes away, as in rising onto the balls of the feet). Neutral (0°) is the standing foot-flat position. Clinically load-bearing here because deep dorsiflexion presses the Achilles against the calcaneus ([tendon compression](#tendon-compression)) and therefore aggravates [insertional tendinopathy](#insertional-tendinopathy) — the reason those cases are worked from 0° into plantarflexion rather than stretched.

## dose-response-relationship

*Measurement & Research Terms*

**Dose–response relationship** — How the size of the result changes as you give more of the thing. Formally: the functional relationship between the quantity of a stimulus and the magnitude of the adaptive response. For [volume](#training-volume) and hypertrophy the measured relationship is **monotonic with diminishing returns**: it rises, and no clear plateau was identified within the volumes studied (Pelland et al., 2026). Strength behaves differently in the same dataset — there the diminishing returns are strong enough to produce a functional plateau. **Interpretive caution:** it is conventionally drawn as an inverted-U turning downward beyond [MRV](#mrv), but no meta-analysis has observed that downturn at the group level — it is a theoretical expectation and an individual clinical observation, and remains **contested**. Practical reading: more sets help, then help progressively less; whether they eventually hurt is not something the group data can currently show.

## double-progression

*Programming & Progression*

**Double progression** — Add reps until you hit the top of your rep range on every set, then add weight and start again at the bottom. Formally: a progression scheme operating on two variables sequentially within a fixed [rep range](#rep-range): **(1)** repetitions are increased at constant load until the top of the range is reached on all prescribed sets; **(2)** load is then increased by a defined increment, returning repetitions toward the bottom of the range. Formally: hold *L* constant while *r* → *r_max* across all sets, then set *L* ← *L*(1 + Δ) with Δ ≈ 0.025–0.05, where *L* is [load](#load) and *r* is repetitions per set. Contrast **single progression** (load only) and **triple progression** (reps → sets → load).

## drop-jump-vs-depth-jump

*Training, Loading & Contraction*

**Drop jump vs. depth jump** — Two exercises that both start by stepping off a box, distinguished only by what you are told to do on landing. **Drop jump**: instruction emphasizes minimizing [ground contact time](#gct), typically for [RSI](#rsi) assessment. **Depth jump**: instruction emphasizes maximizing subsequent jump height, accepting longer contact. The distinction matters because the two impose different [SSC](#ssc) demands — fast vs. slow — and are trained for different purposes.

## dup

*Programming & Progression*

**DUP (daily undulating periodization)** — Varying heavy, medium, and light days for the same lift within a single week. Formally: [undulating periodization](#undulating) in which the [rep range](#rep-range) and [intensity](#intensity) vary between sessions *within* a single [microcycle](#microcycle) (e.g. heavy Monday / light Wednesday / medium Friday for the same lift). Contrast **WUP** (weekly undulating), where the same kind of variation occurs week-to-week instead of session-to-session.
## dynamic-energy-balance-model

*Energetics & Balance*

**Dynamic energy balance model** — A weight-prediction model that accounts for the fact that a smaller body burns less, so weight loss slows down and eventually stops. Formally: a mathematical model of body-weight change that treats energy expenditure as a *function of* changing body mass and composition, rather than as a constant. Supersedes the static "3500 kcal = 1 lb" rule. Implemented in the NIH Body Weight Planner (Hall et al.). Key prediction: weight loss for a fixed intake is **curvilinear and asymptotic** — a new equilibrium is approached over ~1–3 years, rather than loss continuing indefinitely.

## eat

*Energetics & Balance*

**EAT (exercise activity thermogenesis)** — The calories you burn in deliberate workouts. Formally: energy expended in deliberate, structured exercise. Units: kcal·day⁻¹. Typically ~0–30% of [TDEE](#tdee). Note that the *net* cost of exercise is less than the gross figure, since it displaces resting expenditure that would have occurred anyway, and is further reduced by [energy compensation](#energy-compensation). One of the four components of [TDEE](#tdee), alongside [BMR](#bmr-rmr), [TEF](#tef), and [NEAT](#neat).

## eccentric-contraction

*Training, Loading & Contraction*

**Eccentric contraction** — The lowering half of a rep, where the muscle is producing force while being stretched. Formally: active muscle lengthening under load, occurring when the external load exceeds muscle force. Net negative mechanical work; produces the highest force per unit of neural drive and per unit of metabolic cost. Historically credited with unique tendon benefit — a claim not supported when [strain](#strain) magnitude is equated across contraction types.

## ee

*Energetics & Balance*

**EE (energy expenditure)** — The energy your body spends, counting everything. Formally: total energy output over a stated period, in kcal·day⁻¹; over 24 hours it is identical to [TDEE](#tdee). It is the "out" side of the energy-balance equation:

> ΔE_stored = [EI](#ei) − EE

**EE is not a fixed number you can subtract from.** It falls as body mass falls, as intake falls, and as [NEAT](#neat) is suppressed — see [metabolic adaptation](#metabolic-adaptation) and [energy compensation](#energy-compensation). This coupling between the two sides of the equation is why "calories in, calories out" is a correct accounting identity and a poor plan.

## effect-size

*Measurement & Research Terms*

**Effect size (Cohen's d, Hedges' g)** — A number expressing how big a difference is, stripped of the units it was measured in, so results from different studies can be compared. Formally:

> d = (mean₁ − mean₂) / pooled SD

Conventional interpretation: ~0.2 small, ~0.5 medium, ~0.8 large. **Hedges' g** applies a small-sample correction and is preferred in the typically small resistance-training trial. Effect size, not the p-value, indicates whether a difference is practically meaningful — a difference can be statistically real and far too small to notice.

## effective-reps

*Loading Variables & Prescription*

**Effective reps (stimulating reps) hypothesis** — The idea that only the last few hard reps of a set actually drive growth. Formally: the proposal that only the final repetitions of a set — those performed under near-maximal [motor-unit recruitment](#motor-unit-recruitment) and slowed contraction velocity, roughly the last ~5 before [failure](#momentary-failure) — contribute meaningfully to the hypertrophic stimulus. **Status: a plausible, useful heuristic that explains why 5–30 reps produce similar growth at matched effort (Schoenfeld et al., 2017b), but not a directly demonstrated mechanism.** No study has isolated the contribution of individual repetitions within a set, and the "~5" is not a measured quantity [UNVERIFIED — could not confirm a direct test]. It also sits awkwardly beside the finding that hypertrophy improves only *slightly* as sets approach failure (Robinson et al., 2024), which a strict version of the model would predict more strongly. Treat as a model, not a finding.

## effort-tolerance

*Effort, Fatigue & Recovery*

**Effort tolerance** — How much discomfort you are willing to push through at the end of a hard set. Formally: the psychological capacity to sustain effort into the highly uncomfortable final repetitions of a set. It is the practical limiter on very high-rep training (>30 reps), where sets typically terminate at the point of discomfort rather than at true [momentary failure](#momentary-failure) — producing a real but *sub-stimulus* set.

## ei

*Energetics & Balance*

**EI (energy intake)** — The calories you actually absorb from what you eat. Formally: total metabolizable energy consumed, in kcal·day⁻¹ or MJ·day⁻¹. Note that *metabolizable* energy is less than gross combustion energy, owing to incomplete digestion and absorption — a difference that is non-trivial for fiber, resistant starch, and whole nuts (where measured absorbed energy runs ~5–20% below label values). The "in" side of the balance equation; see [EE](#ee).

## elastin

*Anatomy & Composition*

**Elastin** — A stretchy matrix protein that helps tendon spring back to its resting shape. Formally: a highly extensible, cross-linked matrix protein (~1–2% of tendon dry mass) permitting large reversible deformation and assisting recovery of [crimp](#crimp) after unloading.

## emd

*Mechanics & Material Properties*

**EMD (electromechanical delay)** — The short lag between your nervous system switching a muscle on and force actually appearing at the tendon. Formally: the time interval between the onset of muscle electrical activity (EMG) and the onset of measurable force at the tendon. Units: ms (typically 20–100 ms). Shortened by higher tendon [stiffness](#stiffness), since less force is "spent" taking up series compliance — a slack rope must be pulled tight before it can pull anything.

## endotenon-epitenon-paratenon

*Anatomy & Composition*

**Endotenon / epitenon / paratenon** — Three connective-tissue wrappings: one between the internal bundles, one around the whole tendon, and one loose sleeve outside that. Formally: **Endotenon**: thin sheath separating and binding [fascicles](#fascicle); carries vessels and nerves; permits [fascicle sliding](#fascicle-sliding). **Epitenon**: the sheath surrounding the whole tendon, continuous with endotenon. **Paratenon**: loose areolar tissue external to the epitenon in tendons lacking a true synovial sheath (e.g. Achilles); highly vascular and the site of most measurable collagen turnover in adults. That last point matters: most measurable "tendon turnover" in an adult happens in the wrapping, not the core.

## energy-availability

*Effort, Fatigue & Recovery*

**Energy availability (EA)** — How much energy is left over for your body to run on after training has taken its share, scaled to your lean mass. Formally: dietary energy intake minus exercise energy expenditure, normalized to fat-free mass:

> EA = (intake − exercise expenditure) / FFM   (units: kcal·kg FFM⁻¹·day⁻¹)

Values below ~30 kcal·kg FFM⁻¹·day⁻¹ define **low energy availability**, the causal basis of **[RED-S](#red-s)**. Below that threshold, luteinising-hormone pulsatility is measurably disrupted within five days (Loucks & Thuma, 2003; n = 29 regularly menstruating sedentary women of normal body composition). **The number is an indicator, not a switch** — the 2023 IOC consensus cautions that energy availability is hard to measure in free-living people and that a single threshold oversimplifies (Mountjoy et al., 2023). Low EA suppresses [MPS](#mps-mpb), impairs recovery and connective-tissue remodeling, and raises injury risk — it lowers effective [MRV](#mrv).

## energy-compensation

*Energetics & Balance*

**Energy compensation** — The way your body quietly cancels part of the calories you burn exercising, by moving less the rest of the day or eating more. Formally: the physiological and behavioral reduction in non-exercise energy expenditure and/or increase in energy intake that partially offsets energy expended in exercise. Typical magnitude: compensation through reduced basal expenditure alone averages **~28%** across 1,754 DLW-measured adults, and is larger in people with more body fat (Careau et al., 2021); adding compensation through reduced [NEAT](#neat) and increased intake gives a working range of **~20–50% of the nominal exercise energy cost**, with very large inter-individual variance. The mechanistic basis of the [constrained TDEE model](#constrained-total-energy-expenditure-model), and the reason "exercise your way out of a bad diet" underperforms. **Note the corollary, which is often lost: roughly 70% of what you burn does still count.** Exercise is a mediocre deficit-*creation* tool and an excellent tissue-*protection* tool.

## energy-deficit

*Energetics & Balance*

**Energy deficit** — Taking in less energy than you spend, so the body has to draw on its own stores. Formally: a state in which [energy intake](#ei) is below [total daily energy expenditure](#tdee), producing net mobilization of stored substrate. Expressed absolutely (kcal·day⁻¹) or relatively (% below TDEE). **Relative expression is the more meaningful**, since a 500 kcal deficit is trivial for a 3500 kcal TDEE and severe for a 1600 kcal one.

## energy-density

*Diet Composition & Nutrition*

**Energy density** — How many calories are packed into a given weight of food. Formally: energy per unit mass of food, in kcal·g⁻¹. Ranges from ~0.1–0.5 (vegetables, fruit, broth) to ~5–9 (oils, nuts, confectionery). **A dominant determinant of ad libitum intake**, because humans regulate food intake substantially by volume and weight rather than by energy. Lowering dietary energy density permits equivalent food volume at lower energy intake — the single most robust practical lever for spontaneous intake reduction. Primary determinants: water content, then fiber, then fat.

## energy-storage-loading

*Training, Loading & Contraction*

**Energy-storage loading** — The middle rehab stage where you start bouncing gently — hops, low jumps — so the tendon has to store and release energy again. Formally: the rehabilitation/training stage in which loading transitions from slow, heavy, low-[SSC](#ssc) work toward faster stretch-shortening actions (submaximal bounding, low box jumps, hops) that require the tendon to store and release elastic energy. The bridge between [heavy slow resistance](#hsr) and full [plyometric](#plyometrics)/sport loading.

## energy-storing-tendon

*Anatomy & Composition*

**Energy-storing tendon** — A long, springy tendon like the Achilles that stretches and recoils to save energy when you run. Formally: a tendon functionally specialized to store and return elastic strain energy during cyclic locomotion (Achilles, patellar, equine superficial digital flexor). Characterized by relatively low stiffness for its size, high operating [strain](#strain) (often 4–8% in vivo), high [fascicle sliding](#fascicle-sliding) capacity, and a disproportionately high injury rate. Contrast [positional tendon](#positional-tendon).

## enthesis

*Anatomy & Composition*

**Enthesis** — The place where a tendon anchors into bone. Formally: the specialized attachment of tendon to bone. A *fibrocartilaginous* enthesis has four graded zones: (1) dense fibrous tendon, (2) uncalcified fibrocartilage, (3) the **tidemark** (a calcification front), (4) calcified fibrocartilage merging into bone. This gradient reduces stress concentration at the interface — a gradual change from soft to hard, rather than an abrupt joint that would tear. Entheses are the sites of [insertional tendinopathy](#insertional-tendinopathy) and [enthesitis](#enthesitis).

## enthesitis

*Pathology & Clinical*

**Enthesitis** — Genuine inflammation at a tendon's bone attachment, caused by a systemic disease rather than by training. Formally: inflammatory pathology of the [enthesis](#enthesis), characteristic of spondyloarthropathies (ankylosing spondylitis, psoriatic arthritis, reactive arthritis). Mechanistically distinct from mechanically driven [tendinopathy](#tendinopathy). Suspect when multiple entheses are symptomatic, when there is inflammatory back pain, [morning stiffness](#morning-stiffness) >30 min, or systemic features — that pattern calls for a physician, not a loading program.

## essential-body-fat

*Body Composition & Adipose Biology*

**Essential body fat** — The minimum fat a body needs to work at all. Formally: the adipose tissue required for physiological function — cell membranes, the central nervous system, bone marrow, and organ padding. ~3–5% in males, ~10–13% in females (the difference being sex-specific reproductive tissue) [consensus — no single source]. Below this threshold, endocrine, immune, thermoregulatory, and reproductive functions are compromised.

**⚠ Being above this number does not mean you are safe.** Essential fat is a floor for survival, not a threshold for endocrine health. Reproductive-axis suppression is driven by [energy availability](#energy-availability) — intake minus training expenditure, per kg of [fat-free mass](#ffm-lbm) — and routinely appears in women at 20–25% body fat, far above the essential-fat figure (Loucks & Thuma, 2003; Mountjoy et al., 2023). There is no body-fat percentage above which restriction is endocrinologically safe. If warning signs appear at the low end of the normal range, the correct response is to stop losing weight and reassess whether further loss is indicated — not to lose it more slowly.

## eswt

*Pharmacology, Nutrition & Medical*

**ESWT (extracorporeal shockwave therapy)** — A clinic treatment that fires pressure pulses into the tissue from outside the body. Formally: delivery of high-amplitude acoustic pressure pulses to tissue, in **focused** (deeper, higher energy) or **radial** (superficial, pressure-wave) form; dosed in energy flux density (mJ·mm⁻²). Proposed mechanisms include [neovascularization](#neovascularization), altered nociceptor signaling, and stimulated matrix turnover. Best supported as an **adjunct** to loading in insertional Achilles, [plantar fasciopathy](#plantar-fasciopathy), and calcific rotator cuff tendinopathy — but weaker than commonly claimed. A systematic review reported moderate effects while rating most included trials low quality (Mani-Babu et al., 2015), and a network meta-analysis found no clear advantage over other active treatments for Achilles tendinopathy (van der Vlist et al., 2021). **Evidence remains limited and inconsistent.**

## fascicle

*Anatomy & Composition*

**Fascicle** — A bundle of fibers inside a tendon; the biggest of the nested sub-units. Formally: the largest sub-tendon structural unit, a bundle of collagen fibers bounded by [endotenon](#endotenon-epitenon-paratenon). Fascicles are the units that slide relative to one another during elongation (see [fascicle sliding](#fascicle-sliding)). (Note: a *muscle* fascicle is a distinct structure — a bundle of muscle fibers — and muscle fascicle *length* is a separate architectural variable affecting shortening velocity; see [fascicle length adaptation](#fascicle-length-adaptation).)

## fascicle-length-adaptation

*Physiology & Adaptation*

**Fascicle length adaptation** — Muscle bundles getting longer by adding contractile units end-to-end, rather than getting thicker. Formally: change in the length (and hence sarcomere number in series) of muscle fascicles. Proposed to increase with training at [long muscle lengths](#lengthened) and with [eccentric](#eccentric-contraction) loading, and to raise maximum shortening velocity and shift the [length–tension relationship](#length-tension-relationship). **Weak and contested:** a systematic review of this exact question found the evidence suggestive but inconclusive, because almost every study estimated fascicle length by linear extrapolation from ultrasound — a method of questionable validity — and none has directly counted serial sarcomeres in humans (Wolf et al., 2025b). Distinct from [hypertrophy](#hypertrophy) in muscle [CSA](#csa), which reflects sarcomeres added in *parallel*.

## fascicle-sliding

*Anatomy & Composition*

**Fascicle sliding (interfascicular sliding)** — Bundles inside a tendon shearing past one another, which lets the whole tendon stretch further than its fibers alone could. Formally: relative shear displacement between adjacent [fascicles](#fascicle), permitted by the compliant interfascicular matrix ([endotenon](#endotenon-epitenon-paratenon)). It is a major contributor to whole-tendon extensibility in [energy-storing tendons](#energy-storing-tendon) and declines with age, shifting [strain](#strain) onto the fascicles themselves — an age-related injury mechanism.

## fat-burning-zone

*Measurement & Research Methods*

**"Fat-burning zone"** — The easy exercise intensity at which the largest *share* of the energy you burn comes from fat. Formally: the low-to-moderate exercise intensity (~60–65% HRmax) at which the *proportion* of energy derived from fat oxidation is maximal. **The reasoning error: maximizing the fat *fraction* while minimizing total energy expenditure does not maximize fat loss.** Higher intensities burn more total energy in less time, and 24-hour fat balance — a function of total energy balance — determines the outcome. The zone is real as a physiological observation and useless as a fat-loss strategy.

## fatigue

*Effort, Fatigue & Recovery*

**Fatigue** — A measurable drop in how much force you can produce, caused by the training you just did. Formally: an exercise-induced reduction in the capacity to produce force, comprising **peripheral fatigue** (contractile and excitation–contraction coupling impairment within the muscle) and **central fatigue** (reduced voluntary neural drive). Distinct from [DOMS](#doms) and from subjective tiredness. Fatigue is the currency spent to purchase stimulus — hence [SFR](#sfr).

## ffm-lbm

*Body Composition & Adipose Biology*

**FFM / LBM (fat-free mass / lean body mass)** — Everything in your body that is not fat: muscle, bone, organs, and water. Formally: **FFM** = total body mass minus all extractable lipid. **LBM** = FFM plus [essential fat](#essential-body-fat). Used near-interchangeably in practice; FFM is the more precisely defined. Comprises muscle, bone, organs, connective tissue, and body water. The principal predictor of [BMR](#bmr-rmr) and the tissue whose preservation is the actual objective of a well-run diet.

## fibril

*Anatomy & Composition*

**Fibril (collagen fibril)** — The smallest rope-like strand of collagen that carries load in a tendon. Formally: a quarter-staggered assembly of type I collagen molecules, typically 50–500 nm in diameter, exhibiting the 67 nm D-period banding. Fibril diameter distribution correlates with tensile strength. Fibrils bundle into fibers, fibers into [fascicles](#fascicle), fascicles into the tendon.

## fluoroquinolone

*Pharmacology, Nutrition & Medical*

**Fluoroquinolone** — A class of antibiotic carrying an official warning that it can damage or rupture tendons. Formally: a class of broad-spectrum antibiotics (ciprofloxacin, levofloxacin, moxifloxacin) carrying a regulatory **boxed warning** for tendinitis and tendon rupture, most commonly Achilles. Proposed mechanisms: chelation of divalent cations (Mg²⁺) disrupting integrin-matrix signaling, upregulated [MMP](#mmps) activity, oxidative stress, and [tenocyte](#tenocyte) apoptosis (Duman et al., 2025). Risk is elevated in adults over ~60, with concurrent [corticosteroids](#corticosteroid), and in renal impairment or transplant recipients; onset may be within days and risk persists for weeks to months after the course. **Moderate evidence** for the association; the magnitude of absolute risk is **limited and inconsistent** across studies. **What to do, safety-critical:** if tendon pain, swelling or inflammation develops during or after a course, stop the drug, contact the prescriber immediately, and unload that tendon completely until assessed — rupture can occur with little or no warning pain.

## force-plate

*Testing & Monitoring*

**Force plate** — A rigid platform that measures exactly how hard you push against the ground, moment by moment. Formally: a platform instrumented with force transducers measuring the ground reaction force vector over time. The reference tool for deriving jump height (impulse–momentum or flight-time methods), [RFD](#rfd), [ground contact time](#gct), [RSI](#rsi), and asymmetry.

## force-velocity-relationship

*Mechanics & Material Properties*

**Force–velocity relationship** — The rule that the faster a muscle shortens, the less force it can produce. Formally: the inverse relationship between a muscle's shortening velocity and its maximal force output; force is highest during [eccentric](#eccentric-contraction) (lengthening) actions, intermediate at zero velocity ([isometric](#isometric-contraction)), and falls progressively as [concentric](#concentric-contraction) shortening velocity rises. Relevant here because it explains part of the [SSC](#ssc) advantage: if the tendon does the lengthening and shortening, the muscle can stay near-isometric and therefore near its peak force.

## gct

*Testing & Monitoring*

**GCT (ground contact time)** — How long your foot stays on the ground during a step, jump, or landing. Formally: the interval during which the foot is in contact with the ground, in s or ms. Elite max-velocity sprinting: ~80–110 ms. Drop jump: ~150–250 ms. A key determinant of whether a task is a fast or slow [SSC](#ssc) action, and the denominator of [RSI](#rsi).

## ghrelin

*Metabolic Adaptation & Endocrine Regulation*

**Ghrelin** — The hormone that makes you feel hungry. Formally: the principal orexigenic (hunger-stimulating) hormone, secreted primarily by the stomach; the only known circulating hunger *initiator*. Rises pre-prandially and falls after eating. **Rises with weight loss and remains elevated for ≥1 year afterward**, in proportion to weight lost — a central mechanism of long-term regain pressure.

## glp-1

*Metabolic Adaptation & Endocrine Regulation*

**GLP-1 (glucagon-like peptide-1)** — A gut hormone released when you eat that slows the stomach and tells the brain you are full. Formally: an incretin hormone released from intestinal L-cells in response to nutrients. Effects: stimulates glucose-dependent insulin secretion, slows gastric emptying, and acts centrally to suppress appetite. Falls with weight loss (contributing to reduced [satiety](#satiety-vs-satiation)); the pharmacological target of [GLP-1 receptor agonists](#glp-1-receptor-agonist).

## glp-1-receptor-agonist

*Pharmacology & Clinical*

**GLP-1 receptor agonist** — A prescription drug that imitates the gut's own fullness hormone, so eating less stops feeling like a fight. Formally: a pharmacological agonist of the [GLP-1](#glp-1) receptor (liraglutide, semaglutide). Mechanism: delayed gastric emptying plus central appetite suppression, producing a large spontaneous reduction in energy intake. Efficacy is dose- and drug-specific: **liraglutide 3.0 mg daily → 8.4 kg vs 2.8 kg on placebo at 56 weeks (SCALE, n = 3,731; Pi-Sunyer et al., 2015)**; **semaglutide 2.4 mg weekly → ~14.9% mean body-weight loss at 68 weeks (STEP-1, n = 1,961; Wilding et al., 2021)**. Discontinuation: about **two-thirds of the lost weight was regained within one year** of stopping semaglutide plus lifestyle support (Wilding et al., 2022).

**Contraindications and cautions.** Contraindicated with a personal or family history of **medullary thyroid carcinoma or MEN2** (boxed warning). Caution with a history of **pancreatitis** and with **gallbladder disease**. Delayed gastric emptying creates a **pulmonary aspiration risk under anaesthesia or sedation** — tell any anaesthetist or endoscopist you are taking one. Doses of **insulin or sulfonylureas** must be reduced to avoid hypoglycaemia. GI adverse effects are common and are the main reason people stop. **Use in eating-disorder history, or for cosmetic leanness in people without a clinical indication, is outside what these trials studied and is a recognised clinical concern.** **Compounded or grey-market product bought online is not the studied drug** and has caused documented harm. A share of the weight lost is [lean mass](#lbm) unless [resistance training](#resistance-training) and high protein are maintained; the widely quoted 25–40% figure could not be traced to a primary body-composition source, so treat the direction as established and the number as unreliable. Prescription medicines with defined indications — a physician's decision, not a training one.

## gpp

*Training, Loading & Contraction*

**GPP (general physical preparation)** — The off-season base-building phase, before training becomes sport-specific. Formally: the foundational training phase emphasizing broad qualities (work capacity, maximal strength, structural tissue development) rather than sport-specific expression. The phase in which the bulk of tendon material adaptation should be pursued, because it is the only period with enough low-stakes time for an 8–12+ week adaptation.

## ground-substance

*Anatomy & Composition*

**Ground substance** — The gel that fills the spaces between collagen fibers. Formally: the non-fibrillar component of extracellular matrix — [proteoglycans](#proteoglycan), glycosaminoglycans, glycoproteins, and the water they bind — occupying the volume between collagen [fibrils](#fibril) and cells. It governs water content, fibril spacing, and [viscoelastic](#viscoelasticity) behavior. Clinically load-bearing because **increased ground substance** is one of the defining histological findings in [tendinopathy](#tendinopathy): the tendon holds more water and gel and less orderly collagen, which is what makes it thicker on imaging.

## gtn

*Pharmacology, Nutrition & Medical*

**GTN (glyceryl trinitrate / nitroglycerin) patch** — A stick-on patch, borrowed from heart medicine, applied over a painful tendon. Formally: a topical nitric-oxide donor applied over the affected tendon, on the rationale that NO stimulates collagen synthesis and modulates nociception. Trial results are mixed; headache is a common dose-limiting adverse effect.
## hard-set

*Loading Variables & Prescription*

**Hard set** — A set that was actually difficult — close enough to your limit that it counts. Formally: a set taken within roughly 0–3 [RIR](#rir), i.e. sufficiently close to [failure](#momentary-failure) to be counted toward [volume](#training-volume). Warm-up and sub-effort sets are excluded from volume counts. The concept exists because raw set counts are meaningless without an effort qualifier: twenty easy sets and twenty hard sets are not the same dose.

## hpa-axis

*Metabolic Adaptation & Endocrine Regulation*

**HPA axis (hypothalamic–pituitary–adrenal)** — The chain of command that runs your stress response, from brain to adrenal gland. Formally: the neuroendocrine stress axis — hypothalamic CRH → pituitary ACTH → adrenal [cortisol](#cortisol). Activated by energy restriction, which the body treats as a physiological stressor. Contrast the [HPG axis](#hpg-axis), which is suppressed by the same circumstances.

## hpg-axis

*Metabolic Adaptation & Endocrine Regulation*

**HPG axis (hypothalamic–pituitary–gonadal)** — The chain of command that runs reproduction and sex hormones, from brain to gonads. Formally: hypothalamic GnRH → pituitary LH/FSH → gonadal sex-steroid production. **The most energy-sensitive endocrine axis and therefore the earliest and most reliable warning signal of excessive restriction** — manifesting as menstrual irregularity or amenorrhea in females and reduced [testosterone](#testosterone), libido, and morning erections in males. Suppression is [leptin](#leptin)-mediated. See [RED-S](#red-s).

## hsr

*Training, Loading & Contraction*

**HSR (heavy slow resistance)** — Lifting heavy weights deliberately slowly — about three seconds up and three seconds down. Formally: a tendon-loading protocol using heavy external load with deliberately slow, controlled tempo through both phases — canonically **3 s [concentric](#concentric-contraction) / 3 s [eccentric](#eccentric-contraction)**, 3–4 sets, progressing from 15[RM](#rm) to 6RM over 12 weeks, 3×/week (Kongsgaard et al., 2009). Note the prescription is in **repetition maximum, not %[1RM](#one-rep-max)** — that is how the trials were run, and the conversion does not survive the tempo, since six seconds per repetition costs you reps at any given percentage. Rationale: high [strain](#strain) magnitude sustained for the ~3 s duration thought to maximize collagen synthesis signaling. **Equal to, not better than**, the [Alfredson protocol](#alfredson-protocol) for midportion Achilles — equally good and lasting outcomes, with greater patient satisfaction at 12 weeks that had gone by 52 weeks (Beyer et al., 2015). **Moderate evidence.** The better-adherence advantage is real and is why this document defaults to it. **Caveat:** claims that HSR produces superior *structural* normalization are **not supported** — findings are inconsistent between trials and sites.

## hydrolyzed-collagen-collagen-peptides-gelatin

*Pharmacology, Nutrition & Medical*

**Hydrolyzed collagen / collagen peptides / gelatin** — Collagen broken into small fragments and swallowed before training, on the theory that it supplies raw material for tendon repair. Formally: enzymatically fragmented collagen supplying a substrate profile rich in glycine, proline, and [hydroxyproline](#hydroxyproline). Proposed to act both as substrate and, via absorbed di/tripeptides (notably prolyl-hydroxyproline), as a signaling stimulus to fibroblasts. Protocol: **~15 g with ~50 mg [vitamin C](#ascorbate), 30–60 min before loading**. Evidence: raises circulating precursors and [PINP](#pinp), and increased collagen content in an *engineered ligament* construct rather than in a human tendon, in 8 participants (Shaw et al., 2017). **Countervailing evidence:** a stable-isotope tracer study measuring the outcome that matters found collagen protein ingestion during recovery from exercise **did not increase muscle connective tissue protein synthesis rates** (Aussieker et al., 2023). **Evidence remains limited and inconsistent** — a biomarker and bench finding with a direct tracer null against it, and no human tendon outcome trial in either direction. Low cost, low risk.

## hydroxyproline

*Pharmacology, Nutrition & Medical*

**Hydroxyproline (Hyp)** — An unusual amino acid found almost only in collagen, which makes it a useful fingerprint for collagen. Formally: a non-standard amino acid formed by post-translational hydroxylation of proline by [prolyl hydroxylase](#prolyl-lysyl-hydroxylase). Essential for triple-helix thermal stability; largely unique to collagen, hence used as a biochemical marker of collagen content and turnover.

## hyperpalatable-food

*Diet Composition & Nutrition*

**Hyperpalatable food** — Food formulated to be so rewarding that you keep eating past the point where you would normally stop. Formally: food engineered to combine fat, sugar, salt, and sodium in ratios that maximize reward while minimizing the sensory-specific satiety that normally terminates eating. Operationalized in the literature by defined threshold combinations (e.g. >25% energy from fat plus >0.30% sodium by weight). Drives intake beyond homeostatic need — a food-property explanation for overconsumption that requires no failure of willpower.

## hyperphagia

*Appetite, Behavior & Adherence*

**Hyperphagia** — Eating far more than usual, driven by a physiological hunger signal rather than by choice. Formally: sustained energy intake markedly above habitual or homeostatic requirement. **Post-restriction hyperphagia** — the surge in intake following a period of underfeeding — is a documented, reproducible consequence of energy restriction, established in the Minnesota Starvation Experiment and driven by elevated [ghrelin](#ghrelin), suppressed [leptin](#leptin), and reduced [satiety](#satiety-vs-satiation) signaling. Practical reading: post-diet overeating is a predictable output of the physiology, not a character failure — which is why the exit from a diet must be planned in advance.

## hyperplasia

*Physiology & Adaptation*

**Hyperplasia** — Growing *more* muscle fibers, as opposed to growing the ones you already have. Formally: an increase in the *number* of muscle fibers. Demonstrated in some animal models under extreme stretch-overload protocols (Antonio & Gonyea, 1993); **not established as a meaningful contributor in humans**. Human muscle growth is essentially entirely [hypertrophy](#hypertrophy). (For the fat-cell version of the same distinction, see [adipocyte hyperplasia vs. hypertrophy](#adipocyte-hyperplasia-vs-hypertrophy).)

## hypertrophy

*Physiology & Adaptation*

**Hypertrophy** — Muscle growth: existing fibers getting bigger. Formally: an increase in the size of existing muscle fibers, achieved by the addition of sarcomeres and other contractile and non-contractile material. Subtypes: **myofibrillar** (contractile protein accretion — the functionally meaningful form) and **sarcoplasmic** (expansion of non-contractile fluid and organelle volume; real but of modest magnitude and contested significance). Measured as fiber [CSA](#csa), whole-muscle CSA/volume (MRI, ultrasound), or lean mass (DXA — an indirect and noisy proxy). Contrast [hyperplasia](#hyperplasia).

## hysteresis

*Mechanics & Material Properties*

**Hysteresis** — The fraction of the energy stored in a stretched tendon that is lost as heat instead of being returned. Formally:

> hysteresis (%) = [(E_stored − E_returned) / E_stored] × 100

Healthy human tendon: ~7–10%, i.e. ~90–93% energy return. Hysteresis rises with degeneration, with age, and at slow loading rates. Practical meaning: a healthy Achilles is a very good spring, and a degenerated one is a worse one.

## igf-1

*Cell & Molecular Biology*

**IGF-1 (insulin-like growth factor 1)** — A growth signal that tendon cells release locally after loading. Formally: an anabolic peptide growth factor upregulated locally in tendon after mechanical loading. Stimulates [tenocyte](#tenocyte) proliferation and type I collagen synthesis; a principal mediator of load-induced tendon anabolism.

## iifym

*Diet Composition & Nutrition*

**IIFYM ("if it fits your macros")** — An approach that sets daily protein, fat, and carbohydrate targets and lets you fill them with any foods you like. Formally: a flexible dietary pattern prescribing macronutrient totals rather than permitted or forbidden foods. Its rationale is [adherence](#adherence) — flexible restraint outperforms rigid restraint (see [disinhibition](#disinhibition)) — not a metabolic advantage; like every other named diet, it works only through an [energy deficit](#energy-deficit). Its weakness is that macro targets alone say nothing about fiber, micronutrients, or [energy density](#energy-density).

## insertional-tendinopathy

*Pathology & Clinical*

**Insertional tendinopathy** — Tendon pain right at the bone attachment, rather than in the middle of the tendon. Formally: [tendinopathy](#tendinopathy) at the [enthesis](#enthesis). Distinguished from [midportion](#midportion-tendinopathy) by an additional **[compressive](#tendon-compression)** loading component as the tendon wraps the bone. Clinical consequence: positions of deep stretch (e.g. [dorsiflexion](#dorsiflexion-plantarflexion) below neutral for insertional Achilles; hip adduction for gluteal) are provocative and must be limited early in rehab. This is why stretching an insertional case makes it worse.

## insulin

*Metabolic Adaptation & Endocrine Regulation*

**Insulin** — The hormone released after eating that moves nutrients into storage and puts fat release on hold. Formally: the principal anabolic and storage hormone, secreted by pancreatic β-cells in response to (primarily) carbohydrate and (secondarily) protein. Promotes glucose uptake, glycogen synthesis, and lipogenesis; **inhibits [lipolysis](#lipolysis)** via HSL dephosphorylation. **Note on the carbohydrate–insulin model of obesity:** the hypothesis that carbohydrate-driven insulin secretion causes fat gain independently of energy balance has been **tested directly under metabolic-ward conditions and not supported** — at matched calories, fat restriction produced slightly *more* body-fat loss than carbohydrate restriction (Hall et al., 2015; n = 19), and an [isocaloric](#isocaloric) ketogenic diet produced only a small, transient rise in expenditure that did not accelerate fat loss (Hall et al., 2016; n = 17, 8 weeks inpatient). **Do not read this as a flat refutation of the whole model, which would overstate the evidence.** Proponents have published a weaker and more defensible formulation — that high-glycaemic-load diets shift partitioning and appetite in ways that promote positive energy balance *through intake* (Ludwig et al., 2021) — and the exchange is live in the peer-reviewed literature (Hall et al., 2018; Ludwig & Ebbeling, 2018). **Contested at the level of the weak model; refuted at the level of the strong one.** The narrow, defensible statement: insulin regulates substrate *partitioning*; energy balance regulates fat *mass*; carbohydrate quality still matters via appetite and food choice.

## integrin

*Cell & Molecular Biology*

**Integrin** — A protein that bolts a cell to the material around it, so when that material stretches, the cell feels it. Formally: a heterodimeric (α/β) transmembrane receptor linking extracellular matrix ligands to the intracellular actin cytoskeleton via focal adhesions. A primary mechanosensor: matrix strain deforms integrin-linked adhesion complexes, initiating [mechanotransduction](#mechanotransduction) signaling.

## intensity

*Loading Variables & Prescription*

**Intensity** — In training, "intensity" means two different things, and they are not interchangeable: how heavy the weight is, and how hard the set felt. Formally: **intensity of load** = %[1RM](#one-rep-max), a mechanical quantity; **intensity of effort** = [proximity to failure](#proximity-to-failure), quantified by [RIR](#rir)/[RPE](#rpe). These are independent: a 60% 1RM set can be maximal in effort, and a 90% 1RM single can be submaximal in effort. **Convention used in this document:** unqualified "intensity" in a programming context (deloads, tapers, periodization, retention of adaptation) means **intensity of load**; effort is always named explicitly as effort, [RIR](#rir), or [RPE](#rpe). A third informal usage — "high-intensity" describing plyometric or sprint work — refers to neither, and means high mechanical demand per contact; it is always written with a qualifier ("high-intensity plyometrics").

## intermittent-fasting

*Appetite, Behavior & Adherence*

**Intermittent fasting (IF)** — Eating only within set periods and not at all in between. Formally: any pattern alternating defined eating and fasting periods — alternate-day fasting, 5:2, or [time-restricted eating](#tre). **Evidence: no advantage over continuous restriction for weight or fat loss when energy and protein are equated** (Cioffi et al., 2018, meta-analysis of RCTs). Benefit for some individuals is entirely mediated by [adherence](#adherence) — a hard rule ("no food before noon") can be easier than a continuous one. Drawback: compressed windows make high protein intake harder, which matters for [LBM](#lbm) retention.

## isocaloric

*Diet Composition & Nutrition*

**Isocaloric (energy-matched)** — Comparing two diets that supply the same number of calories, so any difference must come from something other than calories. Formally: describing conditions matched for total energy intake, permitting the isolation of composition, timing, or food-form effects. **The essential check when reading any diet study**: most claims of a metabolic advantage for a particular diet dissolve once energy — and especially protein — are equated.

## isolation

*Exercise Mechanics*

**Isolation (single-joint) exercise** — A lift that moves one joint and targets one muscle. Formally: an exercise producing motion primarily at one joint, targeting one muscle group (biceps curl, leg extension, lateral raise, calf raise). Advantages: precise targeting, low systemic [fatigue](#fatigue), safe to take to [failure](#momentary-failure), useful for [regional hypertrophy](#regional-hypertrophy) and lagging muscles. Contrast [compound](#compound).

## isometric-contraction

*Training, Loading & Contraction*

**Isometric contraction** — Pushing hard against something that does not move, so the joint angle stays fixed. Formally: muscle activation without change in overall [MTU](#mtu) length. Note that the *muscle fascicles* may shorten while the *tendon* stretches, which is precisely why isometrics load tendon effectively despite nothing visibly moving. Used for tendon loading at high [MVC](#mvc) fractions with minimal [fatigue](#fatigue) and soreness cost. **The pain-relief claim is contested:** the influential result came from six volleyball players in a crossover study (Rio et al., 2015), and a meta-analysis of 10 randomised trials — 7 of them poor quality — found short-term pain reduction but no consistent advantage over other forms of exercise (Clifford et al., 2020). **Safety:** sustained near-maximal holds raise blood pressure sharply, especially if you hold your breath. Breathe throughout, and seek clearance first if you have uncontrolled hypertension or known heart disease.

## lbm

*Body Composition & Adipose Biology*

**LBM (lean body mass)** — Body mass that is not stored fat: muscle, bone, organs, connective tissue, and body water, plus the small amount of [essential fat](#essential-body-fat) inside them. Formally: LBM = [fat-free mass](#ffm-lbm) + essential fat; the two terms are used near-interchangeably in practice, with FFM the more precisely defined. In a poorly managed deficit, ~20–30% of total weight lost is LBM [consensus — no single source]; the true fraction varies strongly with starting fat mass, falling as fat mass rises (**Forbes' curve**; Forbes, 2000); with adequate protein, [resistance training](#resistance-training), a moderate deficit, and adequate sleep, this fraction can be reduced substantially. Note that measured LBM loss also includes glycogen and its bound water (~3 g water per g glycogen), so early "lean mass loss" readings overstate true tissue loss.

## length-tension-relationship

*Mechanics & Material Properties*

**Length–tension relationship** — The rule that a muscle produces its greatest force at one particular length, and less when it is bunched short or stretched long. Formally: the relationship between a muscle's length and the maximal active force it can generate, arising from the degree of overlap between actin and myosin filaments within each sarcomere; force peaks at an optimum length and declines on either side of it. It matters here for three reasons: it defines what "[lengthened](#lengthened)" and short-length training mean mechanically; [fascicle length adaptation](#fascicle-length-adaptation) shifts the curve; and [tendon elongation](#tendon-elongation) after rupture shifts the muscle onto an unfavorable part of it, which is why post-rupture torque deficits persist.

## lengthened

*Exercise Mechanics*

**Lengthened (stretched) position** — The part of a movement where the working muscle is at its longest — the bottom of a curl, the deep part of a squat. Formally: the portion of an exercise's [ROM](#rom) at which the target muscle is at its greatest length. Training with load in this position produces greater hypertrophy than short-length-biased training in most comparisons, plus greater [fascicle length](#fascicle-length-adaptation) adaptation. Exercise selection should consider the **resistance profile** — where in the range the exercise is hardest — and bias toward exercises loaded at long muscle lengths.

## lengthened-partials

*Exercise Mechanics*

**Lengthened partials** — Doing only the stretched half of each rep. Formally: repetitions performed through only the stretched portion of the [ROM](#rom) (e.g. the bottom half of a preacher curl). Recent trials show these match full-ROM training for hypertrophy at equal set counts in trained individuals (Wolf et al., 2025a), likely via greater time under load at long muscle lengths plus more [effective reps](#effective-reps) per set. This coexists with the finding that full ROM beats partial ROM *on average* (Pallarés et al., 2021), because that average pools stretched-position and shortened-position partials together. **Promising but under-replicated.** A legitimate progression tool, not a replacement for establishing full ROM first. Contrast **shortened partials**, which are clearly inferior; see [partial ROM](#partial-rom).

## leptin

*Metabolic Adaptation & Endocrine Regulation*

**Leptin** — A hormone released by fat tissue that tells the brain how much energy is in storage. Formally: an adipocyte-derived hormone signaling the size of energy stores to the hypothalamus; the master regulator of long-term energy homeostasis. Circulating leptin is proportional to fat mass **and** acutely responsive to energy intake — it falls rapidly with restriction, faster and further than fat mass itself. Falling leptin triggers the full defense program: hunger, reduced [T3](#thyroid-hormones), reduced [SNS](#sns) tone, suppressed [HPG axis](#hpg-axis), reduced [NEAT](#neat). **Causal evidence: administering leptin to weight-reduced humans reverses much of the adaptive response** (Rosenbaum & Leibel) — the strongest demonstration that leptin deficiency, not "damage," drives adaptation. Common obesity involves **leptin resistance** (high leptin, blunted central response), not leptin deficiency, which is why leptin therapy failed as an obesity treatment.

## linear-periodization

*Programming & Progression*

**Linear periodization (traditional/classic)** — A months-long plan in which sets and reps steadily fall while the weight steadily rises. Formally: a [periodization](#periodization) model in which [volume](#training-volume) decreases and [intensity of load](#intensity) increases progressively and monotonically across a [macrocycle](#macrocycle) (e.g. 4×12 → 4×8 → 4×5 → 3×3 over successive months). Distinct from [linear progression](#linear-progression), which is a load-increment rule, not a volume/intensity architecture — the two are frequently and unhelpfully conflated.

## linear-progression

*Programming & Progression*

**Linear progression (LP)** — Adding a fixed amount of weight every session or every week for as long as you can get away with it. Formally: a progression rule in which [load](#load) is increased by a fixed increment at a fixed interval for as long as the increment can be completed at the prescribed reps. Viable only while the [novice effect](#novice-effect) supports improvement at that interval: typically **8–16 weeks** for session-based LP in untrained trainees, and commonly **6–12 months** for weekly LP, which applies the same increments one-seventh as often. Terminates in a [stall](#stall), addressed by a [reset](#reset). *Both durations are coaching convention rather than measured outcomes* [UNVERIFIED — could not confirm]. Not to be confused with [linear periodization](#linear-periodization).

## lipolysis

*Body Composition & Adipose Biology*

**Lipolysis** — Releasing stored fat out of fat cells and into the bloodstream. Formally: enzymatic hydrolysis of stored triacylglycerol into free fatty acids and glycerol, catalyzed by [ATGL and HSL](#atgl-hsl). Stimulated by [catecholamines](#catecholamines) (via β-adrenergic receptors), growth hormone, and low [insulin](#insulin); inhibited by insulin and by α₂-adrenergic receptor activation. **Critically: lipolysis is not fat loss.** Released fatty acids are re-esterified and re-stored unless oxidized (see [β-oxidation](#beta-oxidation)). Only sustained negative energy balance produces net fat loss.

## load

*Loading Variables & Prescription*

**Load** — The weight on the bar. Formally: the external resistance applied, in kg or lb, or as %[1RM](#one-rep-max). **Do not confuse with [training load](#training-load)**, a cumulative dose measure covering everything you did over days or weeks. This document uses bare "load" for the weight itself; cumulative senses are always written as "training load" or named explicitly (e.g. "load spike", "weekly training-load change").

## load-cheating

*Exercise Mechanics*

**Load cheating (technical breakdown)** — Adding weight but paying for it by shortening the movement or swinging it up. Formally: increasing the external load while reducing [ROM](#rom), adding momentum, or recruiting non-target musculature. This is not [progressive overload](#progressive-overload): the stimulus to the target muscle may be unchanged or reduced while joint and connective-tissue stress rises. The reason progression rules must specify *"with acceptable technique"* as a completion criterion.

## load-management

*Training, Loading & Contraction*

**Load management** — Steering how much, how hard, and how fast you train so that demand never outruns what the tissue can currently take. Formally: systematic manipulation of the magnitude, frequency, intensity, and rate of change of mechanical loading to keep cumulative demand within the tissue's current capacity while progressively raising that capacity. Distinguishes **external load** (measurable work done: sets, tonnage, distance, foot contacts) from **internal load** (physiological/psychological response: [RPE](#rpe), heart rate, soreness). See [training load](#training-load) and [ACWR](#acwr).

## lop

*Pharmacology, Nutrition & Medical*

**LOP (limb occlusion pressure)** — The cuff pressure at which blood stops flowing into a limb, measured for that individual limb. Formally: the minimum cuff pressure at which arterial flow distal to the cuff ceases, measured individually with Doppler. [BFR](#bfr) protocols prescribe cuff pressure as a percentage of LOP (typically 40–80%) rather than as an absolute pressure, since LOP varies with limb circumference, blood pressure, and cuff width.

## lsi

*Testing & Monitoring*

**LSI (limb symmetry index)** — How the injured side performs as a percentage of the healthy side. Formally:

> LSI = (involved limb / uninvolved limb) × 100

Asymmetry >10–15% is a commonly used risk/return-to-play threshold. **Caveat:** LSI is inflated when the uninvolved limb also detrains — two equally weak legs score 100% — so it should be paired with absolute performance criteria and pre-injury baselines.

## lysyl-oxidase

*Cell & Molecular Biology*

**Lysyl oxidase (LOX)** — The enzyme that starts the process of chemically welding collagen strands to each other. Formally: a copper-dependent amine oxidase that oxidatively deaminates lysine and hydroxylysine residues in collagen telopeptides, initiating spontaneous formation of covalent enzymatic [cross-links](#collagen-cross-linking). Requires dietary copper. Upregulated by mechanical loading — the molecular link between training and stronger tendon material.
## macrocycle

*Programming & Progression*

**Macrocycle** — The biggest planning block: a whole training year, or one full run-up to a peak. Formally: the longest planning unit, typically a full training year or a complete cycle culminating in a peak (months to a year). Comprises multiple [mesocycles](#mesocycle), which in turn comprise [microcycles](#microcycle).

## mapk-erk-pathway

*Cell & Molecular Biology*

**MAPK / ERK pathway** — A relay of enzymes that carries a mechanical signal from the cell surface down to the genes. Formally: mitogen-activated protein kinase cascades (including extracellular signal-regulated kinase) transducing membrane-level mechanical and growth-factor signals to nuclear transcription factors; a core intracellular arm of tendon [mechanotransduction](#mechanotransduction).

## maximum-fat-oxidation-ceiling

*Energetics & Balance*

**Maximum fat oxidation ceiling (Alpert's model)** — There is a limit to how fast your body fat can supply energy, and it depends on how much fat you are carrying. Formally, a theoretical upper bound on the rate at which stored adipose tissue can supply energy:

> maximum ≈ **290 ± 25 kJ · (kg fat mass)⁻¹ · day⁻¹**
> ≈ **69 kcal · (kg fat mass)⁻¹ · day⁻¹** (range ~63–75)
> ≈ **31 kcal · (lb fat mass)⁻¹ · day⁻¹**

**⚠ The 290 figure is a *maximum*. The working number is lower.** The paper defines two quantities, and the popular literature only ever quotes the first:

| | kJ·kg fat⁻¹·d⁻¹ | kcal·kg fat⁻¹·d⁻¹ | kcal·lb fat⁻¹·d⁻¹ |
|---|---|---|---|
| **Maximum** transfer factor (s₀) | 290 ± 25 | **69.3** | **31.4** |
| **Realizable** transfer factor (s) | 240 ± 26 | **57.4** | **26.0** |

The realizable figure is the maximum minus an *activity coefficient* — the energy your movement is already claiming. For the semi-starvation subjects the paper models, that coefficient was 50.2 ± 7.5 kJ·kg⁻¹·d⁻¹, giving a realizable ceiling of 240 ± 26 **[strong — read from the source]**.

**What this means in practice.** The honest ceiling for someone who trains is roughly **57 kcal per kg of fat per day**, not 69 — about 17% lower. Reworking the earlier examples: a 100 kg person at 30% body fat can supply ~1,720 kcal/day from fat rather than ~2,080; a 70 kg person at 10% can supply ~400 rather than ~485. Every downstream source we checked, including earlier versions of this document, quotes the maximum and therefore overstates the limit. **The correction makes an aggressive deficit harder to justify, not easier** — which is the direction a ceiling of this kind should always be read.

**✔ Confirmed: the kilogram is fat mass.** Read directly from the paper. Its nomenclature defines `FM — fat mass, kg` and `s₀ — maximum energy transfer factor, kJ/kg d (= 290 ± 25)`, and the text states that *"maximum energy transfer factor times the FM represents the limit of the total energy rate that can be extracted from the FM."* So the ceiling is per kilogram of **fat**, and the per-pound conversion used everywhere in the fitness literature is correct **[strong — verified in the source]**.

**⚠ Unit warning.** The familiar "31 kcal" figure is **per pound**, not per kilogram. Stating it as 31 kcal per *kilogram* understates the published limit by a factor of 2.2, and that error is widespread. The source value is 290 ± 25 kJ·kg⁻¹·d⁻¹ (Alpert, 2005).

Energy demanded beyond this ceiling must be met from [lean body mass](#lbm) and glycogen.

**Status: limited.** Alpert derived the constant by fitting a model to the Minnesota Starvation Experiment (32 men) plus a few other underfeeding datasets. It has never been prospectively validated — no trial has assigned deficits above and below the ceiling and checked whether lean-mass loss behaves as predicted. Treat it as a physical upper bound and a useful intuition, **not** as a validated prescription and never as licence to diet harder. It is one constraint among several and rarely the binding one: at high body fat it is far above any sensible deficit, and for most women the binding limit is [energy availability](#energy-availability), not fat mobilisation. The empirically grounded version of the same idea is **Forbes' curve** — the proportion of weight lost as fat-free mass falls as starting fat mass rises (Forbes, 2000).

## mcid

*Measurement & Research Terms*

**MCID (minimal clinically important difference)** — The smallest change that the person actually notices or benefits from. Formally: the smallest change in an outcome that is meaningful to the individual, as distinct from a change that is merely statistically detectable. Relevant because many statistically significant training-study differences fall well below any threshold a lifter would notice. Pair it with [effect size](#effect-size) when judging whether a result matters.

## mechanical-tension

*Physiology & Adaptation*

**Mechanical tension** — The pulling force a working muscle fiber experiences; the main thing that makes muscle grow. Formally: the force experienced by an active muscle fiber, sensed by mechanosensors (including titin-based, costamere/[integrin](#integrin), and phospholipid-mediated pathways) and transduced into elevated [MPS](#mps-mpb) via [mTORC1](#mtor-mtorc1). "Active tension" — tension generated during muscle activation, as opposed to passive stretch alone — is the relevant quantity, which is why passive stretching is a weak hypertrophic stimulus.

## mechanotransduction

*Mechanics & Material Properties*

**Mechanotransduction** — How a cell turns a physical tug into a chemical instruction to build. Formally: the conversion of a mechanical stimulus into a biochemical/transcriptional cellular response. In tendon: matrix deformation → cell-membrane and cytoskeletal strain sensed by [integrins](#integrin), [Piezo](#piezo1-piezo2) channels and the [primary cilium](#primary-cilium) → intracellular signaling ([MAPK](#mapk-erk-pathway), [YAP/TAZ](#yap-taz), [TGF-β](#tgf-beta), [IGF-1](#igf-1)) → altered collagen and matrix gene expression. This is the mechanism that makes loading, rather than rest or nutrition alone, the required stimulus for connective-tissue adaptation.

## mesocycle

*Programming & Progression*

**Mesocycle** — A training block of a few weeks with one clear focus, usually ending in an easy week. Formally: an intermediate planning unit with a coherent training emphasis, typically **3–6 weeks**, conventionally ending in a [deload](#deload). The standard unit within which [volume progression](#volume-progression) is applied. Sits between the [microcycle](#microcycle) and the [macrocycle](#macrocycle).

## meta-analysis

*Measurement & Research Terms*

**Meta-analysis** — A study of studies: pooling many trials' results into one overall estimate. Formally: statistical pooling of [effect sizes](#effect-size) across studies to estimate a summary effect and quantify heterogeneity (I²). Strengths: greater precision, mitigation of small-study noise. Weaknesses in this field: heterogeneous volume definitions, dominance of short (6–12 week) trials in untrained participants, publication bias, and the classic **garbage-in–garbage-out** limitation. A **network meta-analysis** additionally permits indirect comparison of interventions never tested head-to-head.

## metabolic-adaptation

*Metabolic Adaptation & Endocrine Regulation*

**Metabolic adaptation (broad sense)** — Everything your body does during a diet to burn less and want to eat more. Formally: the full set of physiological and behavioral responses that reduce [TDEE](#tdee) and increase drive to eat during energy restriction. Four components: **(1)** reduced expenditure from reduced mass; **(2)** reduced [TEF](#tef) from reduced intake; **(3)** reduced [NEAT](#neat); **(4)** [adaptive thermogenesis](#adaptive-thermogenesis) proper. Only (4) is expenditure reduction *unexplained* by mass and intake, and it is the smallest term. Popular usage conflates all four and attributes the total to "metabolic damage." Note that in Parts I and II "adaptation" means a beneficial training response; here it means a defensive reduction in expenditure. The word is the same; the sign is opposite.

## metabolic-stress

*Physiology & Adaptation*

**Metabolic stress** — The burning, swollen "pump" feeling from metabolic by-products building up in a working muscle. Formally: accumulation of exercise metabolites (lactate, H⁺, inorganic phosphate) in working muscle, associated with cell swelling. Historically proposed as an independent hypertrophy driver. **Current position:** its contribution is largely *indirect* — metabolite accumulation accelerates fatigue of low-threshold [motor units](#motor-unit), driving recruitment of high-threshold units and thereby increasing the number of fibers exposed to [mechanical tension](#mechanical-tension).

## metabolic-ward-study

*Measurement & Research Methods*

**Metabolic ward study** — A study where participants live in a research facility so every calorie in and out can be measured rather than reported. Formally: a design in which participants live in a controlled facility with all food provided and weighed and all activity monitored. The only design that eliminates self-report error in intake. Expensive, small-sample, and short — but decisive for mechanistic questions. Metabolic ward studies are why the [carbohydrate–insulin model](#insulin) and "starvation mode" claims can be evaluated conclusively rather than argued.

## mev-mav-mrv

*Effort, Fatigue & Recovery*

**MEV / MAV / MRV (minimum effective, maximum adaptive, maximum recoverable volume)** — Three named landmarks on the "how many sets?" scale: the least that does anything, the range that works best, and the most you can recover from. Formally: **MEV** = the least weekly [volume](#training-volume) producing measurable adaptation; **MAV** = the range producing the greatest adaptation; **MRV** = the greatest volume from which the athlete can still recover (defined in full at [MRV](#mrv)). **Status: a practically useful conceptual model, not a set of empirically measured constants.** The landmarks are individual, muscle-specific, and vary with training state, diet, and sleep; they cannot be looked up in a table.

## micro-loading

*Loading Variables & Prescription*

**Micro-loading** — Using tiny fractional plates so you can add half a kilo instead of two and a half. Formally: use of increments smaller than the smallest standard plate (0.5–1.25 kg fractional plates) to sustain [load](#load) progression once standard 2.5–5 kg jumps exceed the athlete's weekly rate of strength gain. Necessary in practice because the minimum useful relative increment (~2%) becomes an absolute weight below standard plate resolution on small-muscle exercises.

## microcycle

*Programming & Progression*

**Microcycle** — The shortest repeating chunk of a plan — normally one week. Formally: the shortest repeating planning unit, conventionally one week (though it need not be 7 days). The unit over which [sets per muscle group](#sets-per-muscle-group-per-week) and [training frequency](#training-frequency) are counted.

## microdialysis

*Measurement & Research Methods*

**Microdialysis** — A technique for sampling the fluid around a tissue while the person is still alive and moving, using a fine tube with a semi-permeable wall. Formally: insertion of a thin probe with a dialysis membrane into tissue, perfused slowly with fluid so that small molecules diffuse in from the interstitial space and can be collected and assayed over time. Used here because it is how peritendinous collagen-synthesis markers were measured in the hours after loading — the source of the "synthesis rises 6–24 h, peaks ~24 h" kinetics that justify every-other-day tendon work.

## midportion-tendinopathy

*Pathology & Clinical*

**Midportion tendinopathy** — Tendon pain in the middle of the tendon, away from where it attaches to bone. Formally: [tendinopathy](#tendinopathy) of the tendon substance away from the [enthesis](#enthesis) (Achilles: 2–6 cm proximal to the calcaneal insertion). Purely tensile loading pattern, with no compressive component; the presentation with the strongest evidence base for [eccentric](#eccentric-contraction) and [HSR](#hsr) loading. Contrast [insertional tendinopathy](#insertional-tendinopathy), which must be managed differently.

## mifflin-st-jeor

*Measurement & Research Methods*

**Mifflin-St Jeor equation** — A formula that estimates your resting calorie burn from height, weight, age, and sex. Formally: a regression equation predicting [RMR](#bmr-rmr) from anthropometric variables, validated in the 1990s and generally the most accurate of the widely used prediction equations in non-athletic adults; typical individual error ±10–15%. Practical consequence: it is a starting guess only. Tracked intake against observed weight trend measures *your* [TDEE](#tdee) and beats every prediction equation, which is why this document sets maintenance by observation rather than by formula.

## mmps

*Cell & Molecular Biology*

**MMPs (matrix metalloproteinases)** — Enzymes that break down the tissue matrix, clearing out old material so new material can be laid down. Formally: a family of zinc-dependent endopeptidases that degrade extracellular matrix, including collagenases (MMP-1, -13) and gelatinases (MMP-2, -9). Counterbalanced by [TIMPs](#timps). MMP activity rises in the hours after loading, producing the transient **net-catabolic window** (~24–36 h) that precedes net collagen accretion — the mechanistic argument against loading a tendon hard every day. *MMP3* polymorphisms associate with tendinopathy risk.

## moment-arm

*Mechanics & Material Properties*

**Moment arm** — How far a tendon's line of pull sits from the joint it turns; the leverage it has. Formally: the perpendicular distance from a muscle–tendon's line of action to the joint's instantaneous axis of rotation. Units: m or cm. Joint torque τ = F × r, where F is tendon force and r the moment arm. A larger moment arm converts a given tendon force into greater joint torque but requires greater tendon excursion per unit joint rotation — hence the sprint-vs-endurance trade-off described in Part II §C.1.

## momentary-failure

*Effort, Fatigue & Recovery*

**Momentary failure** — The point in a set where you genuinely cannot complete another rep, however hard you try. Formally: set termination at the point where a further [concentric](#concentric-contraction) repetition cannot be completed through the full [ROM](#rom) despite maximal effort. Distinguish from **[technical failure](#technical-failure)** (technique degrades below an acceptable standard — this occurs earlier and is the more appropriate practical endpoint) and from **volitional termination** (stopping by choice, which is what most people actually do when they claim to reach failure). 0 [RIR](#rir) = momentary failure.

## morning-stiffness

*Testing & Monitoring*

**Morning stiffness** — A tendon that feels stiff, sore, and reluctant to move for the first minutes after you get out of bed. Formally: the duration and severity of stiffness and pain in the affected tendon on waking, reported serially and compared week to week rather than day to day. It is used in this document as a **monitoring variable, not a diagnosis**: within the [pain-monitoring model](#pain-monitoring-model), loading is acceptable provided morning stiffness does not progressively worsen across weeks, and worsening morning stiffness is the earliest reliable sign that loading has outrun tissue capacity. Note two other uses of the phrase: [enthesitis](#enthesitis) is suspected when morning stiffness exceeds 30 minutes with systemic features, and general "stiffness" elsewhere in this document means the mechanical property [stiffness](#stiffness), which is unrelated.

## motor-unit

*Physiology & Adaptation*

**Motor unit** — One nerve cell plus all the muscle fibers it controls; the smallest thing your nervous system can switch on. Formally: a single alpha motor neuron together with every muscle fiber it innervates; the smallest functional unit of voluntary force production. Units vary from small/low-threshold/fatigue-resistant (type I fibers) to large/high-threshold/fast-fatiguing (type II fibers).

## motor-unit-recruitment

*Physiology & Adaptation*

**Motor-unit recruitment** — Switching on more [motor units](#motor-unit) as the job gets harder. Formally: the progressive activation of motor units as force demand rises, governed by the [size principle](#size-principle). Full recruitment of high-threshold units — which innervate the type II fibers with the greatest hypertrophic potential — requires either high force (heavy load) or high fatigue (light load taken near [failure](#momentary-failure)). This is the mechanistic explanation for why 5–30 reps can produce equivalent hypertrophy at matched effort.

## mps-mpb

*Physiology & Adaptation*

**MPS / MPB (muscle protein synthesis / breakdown)** — The rate at which muscle protein is being built, and the rate at which it is being taken apart. Muscle grows only when the first outruns the second over time. Formally: the rates of protein incorporation into and removal from muscle tissue, typically expressed as fractional synthetic rate (%·h⁻¹) via stable-isotope tracer methods. Net protein balance = MPS − MPB; hypertrophy requires a chronically positive integral of this balance. Resistance exercise elevates MPS for **~24–48 h** in trained individuals (longer, up to ~72 h, in the untrained). **Interpretive caution:** this time course is a *weak* basis for setting training frequency. The large early MPS spike in untrained people is inflated by muscle damage and does not predict eventual growth; only once damage subsides does the MPS response correlate with hypertrophy (Damas et al., 2016). The case for a ~2×/week per-muscle floor rests on the frequency outcome literature (see [training frequency](#training-frequency)), not on this window.

## mrv

*Effort, Fatigue & Recovery*

**MRV (maximum recoverable volume)** — The most training you can do and still recover from it. Formally: the greatest [training volume](#training-volume) from which an individual can fully recover under prevailing conditions, beyond which performance degrades and adaptation reverses. Determined by genetics, training age, [energy availability](#energy-availability), sleep, and non-training stress. Exceeding MRV chronically produces [overreaching](#overreaching-overtraining). The upper landmark of the [MEV/MAV/MRV](#mev-mav-mrv) framework, and — like the others — an individual quantity that must be observed rather than looked up.

## mtor-mtorc1

*Physiology & Adaptation*

**mTOR / mTORC1 (mechanistic target of rapamycin complex 1)** — The cell's central switch for "conditions are right, start building protein." Formally: a serine/threonine kinase complex serving as the central integrator of mechanical, nutritional (leucine, insulin), and energetic (AMPK) signals regulating [MPS](#mps-mpb). Activated by mechanical loading independently of growth factors; its downstream effectors (p70S6K, 4E-BP1) control translation initiation. Evidence for its role, stated precisely: giving humans rapamycin (an mTORC1 inhibitor) before exercise blocked the acute ~40% rise in muscle protein synthesis over the following 1–2 h (Drummond et al., 2009). **Caveat:** that demonstrates an acute requirement for the synthesis response, not that mTORC1 is strictly necessary for long-term hypertrophy in humans — nobody has trained humans on rapamycin for months, and resistance exercise also activates rapamycin-*insensitive* pathways (Roberts et al., 2023). The older claim that rapamycin "abolishes load-induced hypertrophy, establishing necessity" overstated the evidence.

## mtu

*Anatomy & Composition*

**MTU (musculotendinous unit / muscle–tendon unit)** — Muscle and tendon treated as one system, because they act in series like a motor attached to a spring. Formally: the mechanically coupled series arrangement of muscle belly and its tendon(s), including [aponeurosis](#aponeurosis). Whole-MTU [stiffness](#stiffness) is the physiologically relevant quantity for [SSC](#ssc) function and is regulated both by tendon material properties and by neural modulation of muscle stiffness — meaning MTU stiffness can change within seconds, while tendon material stiffness takes months.

## muscle-confusion

*Programming & Progression*

**"Muscle confusion"** — The marketing claim that you must keep changing exercises or your muscles will "get used to it" and stop growing. Formally: the assertion that frequent, unsystematic exercise variation is required to prevent adaptation plateaus. **Not supported.** Some exercise variation has value (joint-stress distribution, [regional hypertrophy](#regional-hypertrophy), [adherence](#adherence)), but constant rotation destroys the session-to-session comparability that [progressive overload](#progressive-overload) depends on. Muscle tissue possesses no mechanism by which it could be "confused."

## muscle-damage

*Physiology & Adaptation*

**Muscle damage (exercise-induced)** — Microscopic tearing inside muscle fibers after hard or unfamiliar training. Formally: ultrastructural disruption of sarcomeres and membranes following unaccustomed, eccentric-biased, or long-muscle-length loading; indexed by force loss, [DOMS](#doms), and serum creatine kinase. **Once considered a hypertrophy driver; current position is that it is a cost, not a stimulus** — damage consumes remodeling resources that would otherwise support net accretion. The key evidence: across 10 weeks of training, damage peaked in week 1, and in that week the muscle-building signal was elevated but *unrelated* to eventual growth; only at weeks 3 and 10, once damage had subsided, did it correlate with hypertrophy (Damas et al., 2016). **Caveat:** that study had 10 participants, and carries much of the weight for this reversal. Damage co-occurs with growth because both follow high [mechanical tension](#mechanical-tension), not because damage causes growth.

## muscle-length

*Training, Loading & Contraction*

**Muscle length (long- vs. short-length training)** — Whether the muscle is stretched out or bunched up at the point where the exercise is hardest. Formally: the position on the [length–tension relationship](#length-tension-relationship) at which loading occurs. Training at long muscle lengths (stretched position) produces greater hypertrophic and architectural ([fascicle length](#fascicle-length-adaptation)) adaptation, and alters the tendon [strain](#strain) profile — which is why bent-knee and straight-knee calf work load different parts of the Achilles.

## muscle-memory

*Physiology & Adaptation*

**Muscle memory** — Muscle you built once and lost comes back much faster than it took to build the first time. Formally: accelerated re-acquisition of previously held muscle mass after detraining and retraining. Leading mechanism: **[myonuclear](#myonucleus) permanence** — myonuclei acquired during prior hypertrophy are retained (or at least their epigenetic legacy is) through atrophy, so re-growth does not require de-novo [satellite-cell](#satellite-cell)-mediated myonuclear accretion. Supported by epigenetic (DNA-methylation) evidence in humans: after loading, unloading and reloading, genes hypomethylated during growth stayed hypomethylated even once muscle mass had returned to baseline, and reloading produced greater growth (Seaborne et al., 2018). **Caveat:** that study had 8 participants. The myonuclear-retention claim itself remains **contested** — strong in animal models, limited and mixed in humans (Snijders et al., 2020).

## muscle-tendon-imbalance

*Training, Loading & Contraction*

**Muscle–tendon imbalance** — Muscle that has become strong faster than its tendon has become stiff, so every hard contraction over-stretches the tendon. Formally: a state in which muscular force-generating capacity has increased disproportionately relative to tendon [stiffness](#stiffness), so that a maximal contraction imposes tendon [strain](#strain) above the habitual (and safe) operating range. Quantifiable via simultaneous [MVC](#mvc) and ultrasound-derived stiffness measurement. In adolescent athletes followed longitudinally, high patellar tendon strain preceded tendinopathy (Mersmann et al., 2023) — **moderate evidence**, and the strongest prospective support for any tendon risk marker in this document. **Interpretive caution:** the frequently quoted "roughly 20% of elite athletes" figure (Mersmann et al., 2017) comes from small, sport-specific samples and is not a population rate.

## mvc

*Testing & Monitoring*

**MVC (maximal voluntary contraction)** — The hardest you can push or pull with a given muscle, measured with the joint held still. Formally: the greatest force or torque produced by a maximal voluntary effort, typically measured isometrically at a specified joint angle with a dynamometer. The reference denominator for tendon-loading intensity prescription (%MVC). Distinct from %[1RM](#one-rep-max), which is dynamic and exercise-specific — you cannot convert between them reliably.

## myonucleus

*Physiology & Adaptation*

**Myonucleus (pl. myonuclei)** — One of the many control centers inside a muscle fiber; muscle cells are unusual in having hundreds, spaced along their length. Formally: a nucleus residing within a multinucleated skeletal muscle fiber, each governing transcription for a surrounding cytoplasmic territory (the **myonuclear domain**). Because that domain has a size ceiling, a fiber growing substantially larger must acquire additional myonuclei, donated by [satellite cells](#satellite-cell). Retention of previously acquired myonuclei through atrophy is the leading proposed mechanism of [muscle memory](#muscle-memory).
## n

*Units, Abbreviations & Conventions*

**N (newton)** — The standard scientific unit of force. Formally: the force accelerating 1 kg at 1 m·s⁻². 1 kgf ≈ 9.81 N, so a 10 kg weight pulls with roughly 98 N. [Stiffness](#stiffness) is expressed in N·mm⁻¹; [RFD](#rfd) in N·s⁻¹.

## neat

*Energetics & Balance*

**NEAT (non-exercise activity thermogenesis)** — All the energy you burn moving around without calling it exercise: walking, standing, fidgeting, gesturing. Formally: energy expended in all physical activity that is not sleeping, eating, or deliberate exercise — occupational activity, walking, fidgeting, posture maintenance, spontaneous movement. Units: kcal·day⁻¹. **Often quoted as varying by up to ~2000 kcal·day⁻¹ between individuals of similar size** (Levine, 2004) — but that is a review estimate spanning occupational activity (a roofer versus a call-centre worker), not a controlled measurement, and should be treated as **limited**. The best-controlled figure comes from 8 weeks of 1000 kcal/day overfeeding in 16 adults, where the change in NEAT ranged from −98 to +692 kcal·day⁻¹ between individuals and predicted who gained fat (Levine et al., 1999). Either way it is by far the largest source of unexplained variance in [TDEE](#tdee). Highly suppressible: falls substantially and unconsciously during energy restriction, making it the dominant behavioral component of [metabolic adaptation](#metabolic-adaptation). Practical countermeasure: an explicit daily step target, since NEAT cannot be perceived reliably.

## neovascularization

*Pathology & Clinical*

**Neovascularization (neovessels)** — New blood vessels growing into a tendon that normally has very few. Formally: ingrowth of new vessels into normally hypovascular tendon, visualized on Doppler ultrasound. Accompanied by **neoinnervation** — sensory and sympathetic nerve fibers tracking the vessels — which is a proposed nociceptive source in [tendinopathy](#tendinopathy). Note: neovascularity correlates poorly with pain and with prognosis, so it is a finding to observe, not a target to treat.

## neural-adaptation

*Physiology & Adaptation*

**Neural adaptation** — Getting stronger because your nervous system learned to use the muscle you already have, not because the muscle got bigger. Formally: non-morphological improvements in force output arising from changes in the nervous system — increased [motor-unit](#motor-unit) recruitment and discharge rate, improved inter-muscular coordination, reduced antagonist co-contraction, and reduced inhibitory feedback. Dominates strength gains in the **first 2–4 weeks**: after 4 weeks of training, increased force was traced directly to changes in motor-unit recruitment and discharge rate (Del Vecchio et al., 2019). **Caveat:** that study used isometric ankle dorsiflexion in a small sample, so the boundary is indicative rather than exact. **The core mismatch problem:** neural gains are fast, muscle [CSA](#csa) is intermediate (6–8 weeks), and tendon adaptation (Part II §B.1) is slow (8–12+ weeks) — so a novice's force-producing capacity outruns their connective tissue's capacity to transmit it.

## novice-effect

*Physiology & Adaptation*

**Novice effect** — Beginners improve fast at almost anything, so early results say little about whether a program is good. Formally: the elevated rate and non-specificity of adaptation in untrained individuals, driven principally by rapid [neural adaptation](#neural-adaptation) and by a large gap between current and ceiling capacity. Consequence: nearly any reasonable program "works" in month one, and beginner results carry **no** evidence about a program's merit for trained lifters. See [training status](#training-status).

## nrs

*Testing & Monitoring*

**NRS (numeric rating scale)** — The "rate your pain from 0 to 10" scale. Formally: an 11-point self-report pain scale from 0 ("no pain") to 10 ("worst imaginable pain"). The scale referenced by the [pain-monitoring model](#pain-monitoring-model), where ≤5/10 during loading is the acceptability threshold.

## nsaid

*Pharmacology, Nutrition & Medical*

**NSAID (non-steroidal anti-inflammatory drug)** — Everyday anti-inflammatory painkillers such as ibuprofen. Formally: cyclooxygenase (COX-1/COX-2) inhibitors reducing prostaglandin synthesis. In tendon, they provide analgesia but blunt the prostaglandin-mediated component of load-induced collagen synthesis and [tenocyte](#tenocyte) proliferation. Since chronic [tendinopathy](#tendinopathy) is not primarily inflammatory, routine or prolonged use is inappropriate and may impair adaptation.

## nwcr

*Appetite, Behavior & Adherence*

**NWCR (National Weight Control Registry)** — A long-running database of people who lost a lot of weight and kept it off, used to study what they have in common. Formally: a prospective observational registry of >10,000 US adults who have maintained ≥13.6 kg (30 lb) of weight loss for ≥1 year. Members average 33 kg lost and >5 years maintained. Common reported behaviors among maintainers: high physical activity (~1 h/day, predominantly walking), regular self-weighing, consistent eating patterns across weekdays and weekends, breakfast consumption, and limited television viewing (Wing & Phelan, 2005). **Interpretive caution: self-selected and observational — these are correlates of successful maintenance, not demonstrated causes, and the sample is by construction composed only of successes.**

## one-rep-max

*Loading Variables & Prescription · Training, Loading & Contraction*

**1RM (one-repetition maximum)** — The heaviest weight you can lift once with good technique. Formally: the maximum load that can be moved through a full [ROM](#rom) exactly once with acceptable technique. The reference denominator for **intensity of load** (%1RM). Note that 1RM is exercise-specific, varies day-to-day by roughly ±5–10%, and can be estimated from submaximal [AMRAP](#amrap) sets via prediction equations (Epley, Brzycki) with error increasing beyond ~10 reps.

## orthobiologics

*Pharmacology, Nutrition & Medical*

**Orthobiologics** — Injections made from the patient's own blood, marrow, or cells, intended to accelerate healing. Formally: injected biologically derived preparations intended to modify healing — [PRP](#prp), bone-marrow aspirate concentrate, adipose-derived stromal vascular fraction, culture-expanded mesenchymal stromal cells. Highly heterogeneous in preparation and dose; current evidence for tendinopathy is insufficient to support routine use.

## overreaching-overtraining

*Effort, Fatigue & Recovery*

**Overreaching / overtraining** — Training more than you can recover from, on a scale from a temporary dip to a months-long collapse. Formally, a continuum of maladaptive fatigue accumulation: **functional overreaching** — short-term performance decrement with supercompensation on recovery (days-to-weeks), the intended outcome of an intensification block; **non-functional overreaching** — performance decrement persisting weeks-to-months without supercompensation; **overtraining syndrome** — prolonged (months+) performance decrement with systemic features (endocrine, immune, mood disturbance), rare in recreational trainees and frequently over-diagnosed. Practical early markers: multi-lift performance decline, disturbed sleep, elevated resting heart rate, motivational collapse.

## pa-mpa-gpa

*Units, Abbreviations & Conventions*

**Pa / MPa / GPa (pascal)** — The standard unit for pressure or [stress](#stress): force spread over an area. Formally: 1 Pa = 1 N·m⁻². 1 MPa = 10⁶ Pa; 1 GPa = 10⁹ Pa. Tendon [UTS](#uts) ≈ 50–100 MPa; tendon [Young's modulus](#youngs-modulus) ≈ 1–2 GPa.

## pain-monitoring-model

*Testing & Monitoring*

**Pain-monitoring model (Silbernagel)** — A set of three rules that tell you when training through some tendon pain is safe. Formally: a framework permitting continued loading and sport participation during tendon rehabilitation, provided (1) pain during activity ≤5/10 on the [NRS](#nrs); (2) pain returns to baseline **within 24 hours**; (3) [morning stiffness](#morning-stiffness) and pain do not progressively worsen across weeks. Its clinical significance is establishing that **loading within these limits produces outcomes at least as good as avoiding load**, which reframes rehab from avoidance to graded exposure. **Caveat:** it does **not** establish that tissue is undamaged — no study has shown that, and stating it that way overreads the evidence. **Moderate evidence:** one randomised trial of 38 patients with midportion Achilles tendinopathy (Silbernagel et al., 2007), now applied far more widely than it was tested. **Scope limit, safety-critical:** it presupposes a *confirmed diagnosis of tendinopathy*. It does not apply to undiagnosed pain, a suspected tendon tear or rupture, or a suspected [bone stress injury](#bone-stress-injury) — a complete Achilles rupture is frequently not severely painful, so this rule will wave a torn tendon through.

## partial-rom

*Exercise Mechanics*

**Partial ROM** — Reps done through only part of the available movement. Formally: repetitions performed through less than the full available [ROM](#rom). Must be subdivided: **[lengthened partials](#lengthened-partials)** (stretched half — effective) and **shortened partials** (contracted half — clearly inferior to full ROM). Aggregating them into a single "partials" category is the source of much confusion in the literature: the two halves of a movement are not equivalent.

## pcsa

*Testing & Monitoring*

**PCSA (physiological cross-sectional area)** — A thickness measurement taken across the muscle *fibers* rather than across the whole muscle, which is what actually predicts how much force it can make. Formally: muscle volume divided by fascicle length, corrected for pennation angle; the area perpendicular to the fibers rather than to the muscle's long axis. The correct architectural predictor of a muscle's maximum force capacity. Contrast anatomical [CSA](#csa).

## periodization

*Programming & Progression*

**Periodization** — Planning training in phases across months so that fatigue is managed and performance peaks when it needs to. Formally: the planned, systematic variation of training variables over time to manage [fatigue](#fatigue), direct adaptation, and time peak performance. Distinguished from mere *programming* (arranging a single block) by its multi-timescale hierarchy: [macrocycle](#macrocycle) → [mesocycle](#mesocycle) → [microcycle](#microcycle) → session. Evidence position: for **hypertrophy**, no model reliably outperforms another once [volume](#training-volume) and effort ([proximity to failure](#proximity-to-failure)) are equated — linear and daily undulating models produced likely-similar growth in meta-analysis (Grgic et al., 2017); for **peaked strength performance**, periodized models do outperform non-periodized ones, though **moderate evidence**, from trials that are mostly short and in relatively untrained participants.

## persistent-adaptive-thermogenesis

*Metabolic Adaptation & Endocrine Regulation*

**Persistent adaptive thermogenesis** — The metabolic slowdown from a diet failing to go away after the diet ends. Formally: [adaptive thermogenesis](#adaptive-thermogenesis) that fails to resolve after weight stabilization or partial regain. Principal evidence: the Biggest Loser 6-year follow-up, in which [RMR](#bmr-rmr) remained **499 ± 207 kcal·day⁻¹** below prediction despite substantial regain (Fothergill et al., 2016). **Interpretive cautions, which are substantial:** (1) n = 14 followed up, with no control group, and "predicted" RMR comes from a regression fitted at baseline, so part of the residual is model error; (2) the cohort underwent an extreme intervention (~40% BW loss in 30 weeks with [VLCD](#vlcd) plus several hours of daily exercise) and is not representative; (3) Hall subsequently reinterpreted the result — adaptation was largest in the contestants who sustained the biggest *increases in physical activity*, which fits the [constrained expenditure model](#constrained-total-energy-expenditure-model) rather than dieting-induced "damage" (Hall, 2022). Persistence appears to scale with the magnitude and speed of the original loss, and possibly with sustained activity rather than with restriction as such. **Contested.**

## phv

*Units, Abbreviations & Conventions*

**PHV (peak height velocity)** — The fastest point of the adolescent growth spurt. Formally: the point of maximum growth rate during the adolescent growth spurt (approximately ages 11–13 in girls, 13–15 in boys, with wide individual variation). Estimated from serial stature measurements or from maturity-offset equations. Clinically important because bone lengthening transiently outpaces [MTU](#mtu) adaptation, raising [apophysitis](#apophysitis) risk and warranting load modulation — moderating volume, not stopping.

## piezo1-piezo2

*Cell & Molecular Biology*

**Piezo1 / Piezo2** — Pores in the cell membrane that pop open when the membrane is stretched, letting charged particles in and starting a signal. Formally: mechanically activated non-selective cation channels that open in response to membrane tension, admitting Ca²⁺ and initiating downstream signaling. Piezo1 is implicated in tendon and bone mechanoadaptation; a gain-of-function *PIEZO1* variant is associated with enhanced athletic performance phenotypes.

## pinp

*Cell & Molecular Biology*

**PINP (procollagen type I N-terminal propeptide)** — An offcut released into the blood every time a new collagen molecule is finished, so measuring it tells you how fast collagen is being made. Formally: a cleavage fragment released stoichiometrically when procollagen type I is processed into mature collagen. Serum or peritendinous PINP is the standard biochemical marker of **type I collagen synthesis rate**. Its counterpart marker of degradation is ICTP/CTX-I.

## plantar-fasciopathy

*Pathology & Clinical*

**Plantar fasciopathy** — Pain under the heel and arch of the foot, worst on the first steps of the morning. Formally: a degenerative, overload-related condition of the plantar fascia at or near its calcaneal origin, sharing the non-inflammatory histology and load-responsive management of [tendinopathy](#tendinopathy); the older term "plantar fasciitis" implies an inflammatory process that is usually absent. Included here because it is one of the presentations with the best supporting evidence for [ESWT](#eswt) as an adjunct to progressive loading.

## plyometrics

*Training, Loading & Contraction*

**Plyometrics** — Jumping, bounding, and hopping done to spend as little time on the ground as possible. Formally: training using [SSC](#ssc) actions with the explicit intent of minimizing the amortization (ground-contact transition) phase and maximizing [RFD](#rfd) and elastic energy return. **Classification note:** plyometrics primarily train *neural* SSC function and [MTU](#mtu) stiffness *regulation*; they impose very high tendon [strain](#strain) but are inefficient at producing tendon *material* adaptation compared with heavy slow loading, because ballistic contractions spend too little time at high strain (Bohm et al., 2015). Hence: plyometrics **express** tendon capacity; heavy slow loading **builds** it. Inverting that order is the most common elite training error. **Moderate evidence** — the inference follows from the loading dose-response, not from a trial that sequenced the two.

## positional-tendon

*Anatomy & Composition*

**Positional tendon** — A short, stiff tendon built for precise control rather than for springiness. Formally: a tendon specialized for precise force transmission and joint positioning rather than energy storage (e.g. finger flexors, tibialis anterior, common digital extensor). Short, stiff, low operating [strain](#strain), low injury rate. Contrast [energy-storing tendon](#energy-storing-tendon).

## primary-cilium

*Cell & Molecular Biology*

**Primary cilium** — A single tiny antenna sticking out of a cell, used to sense its physical surroundings. Formally: a non-motile microtubule-based organelle projecting from the cell surface, functioning as a mechanosensory antenna. Present on [tenocytes](#tenocyte); cilium length is load-responsive.

## progressive-overload

*Programming & Progression*

**Progressive overload** — To keep adapting, training must keep getting harder than what your body has already got used to. Formally: the principle that adaptation requires the training stimulus to progressively exceed the level to which the tissue is currently adapted. Operationally, the *product* of stimulus magnitude and exposure must increase over time; any of the overload variables listed in Part I §1 may serve as the carrier — load, reps, sets, [proximity to failure](#proximity-to-failure), [ROM](#rom), [density](#training-density), or [frequency](#training-frequency). Related principles: **specificity** (adaptation is specific to the imposed demand), **[reversibility](#reversibility)**, **[individual variation](#responder-variability)**, and **diminishing returns**. It is the one non-negotiable in this document; see [resistance training](#resistance-training) for the practice it governs.

## prolotherapy

*Pharmacology, Nutrition & Medical*

**Prolotherapy** — Injecting an irritant into a painful area on the theory that provoking irritation triggers repair. Formally: injection of an irritant solution (commonly hypertonic dextrose) intended to provoke a localized healing response. Low-quality and inconsistent evidence.

## prolyl-lysyl-hydroxylase

*Pharmacology, Nutrition & Medical*

**Prolyl / lysyl hydroxylase** — The enzymes that chemically modify a new collagen strand so it can hold its shape and later be cross-linked. Formally: Fe²⁺- and 2-oxoglutarate-dependent dioxygenases that hydroxylate proline and lysine residues in nascent procollagen chains, requiring [ascorbate](#ascorbate) as a reducing cofactor. Prolyl hydroxylation stabilizes the triple helix; lysyl hydroxylation provides the sites for subsequent [cross-linking](#collagen-cross-linking). This dependency is why vitamin C deficiency wrecks collagen.

## protein-leverage-hypothesis

*Diet Composition & Nutrition*

**Protein leverage hypothesis** — The idea that people keep eating until they have had enough protein, so a low-protein diet makes them eat more of everything else. Formally: the proposal that humans regulate absolute protein intake more strongly than total energy intake, and will therefore over-consume total energy on a low-protein-density diet in order to reach a protein target. Offers a partial explanation for why increasing dietary protein reduces ad libitum energy intake, and for why dilution of protein by [ultra-processed foods](#upf) promotes overconsumption. **Status: well-supported for the protein-satiety effect; the strong version — that protein leverage explains population obesity — remains contested.**

## proteoglycan

*Anatomy & Composition*

**Proteoglycan** — A protein with long sugar chains attached, which holds water and organizes the surrounding tissue. Formally: a glycosylated protein bearing one or more covalently attached glycosaminoglycan chains. In tendon, proteoglycans regulate fibril assembly, retain water, and mediate interfibrillar load transfer; they are the main constituent of [ground substance](#ground-substance). See [decorin](#decorin), [aggrecan](#aggrecan).

## proximity-to-failure

*Effort, Fatigue & Recovery*

**Proximity to failure** — How close you stopped to the point where another rep would have been impossible. Formally: the distance, in repetitions, between set termination and [momentary failure](#momentary-failure). Quantified by [RIR](#rir) (0 RIR = failure, 3 RIR = three reps left). Alongside [volume](#training-volume), one of the two variables that must be equated before comparing training methods; most contradictory findings in the hypertrophy literature trace to a failure to equate it. Sets taken to failure hold only a trivial hypertrophy advantage over sets stopped short (Refalo et al., 2023), but the relationship is not flat: growth improves slightly as sets approach failure (Robinson et al., 2024). **For strength that same meta-regression found no detectable relationship** — the intervals contained the null and the competing models disagreed on sign, so proximity to failure is a hypertrophy variable, not a strength one.

## prp

*Pharmacology, Nutrition & Medical*

**PRP (platelet-rich plasma)** — An injection of the patient's own blood, spun down to concentrate the clotting cells and their growth factors. Formally: an autologous blood fraction centrifuged to concentrate platelets and their growth factors (PDGF, [TGF-β](#tgf-beta), VEGF, [IGF-1](#igf-1)). Subclassified as leukocyte-rich (LR-PRP) or leukocyte-poor (LP-PRP). Despite mechanistic plausibility and wide use, well-conducted placebo-controlled trials have shown **no benefit over a placebo injection**: PRP versus saline, double-blind, n = 54 (de Vos et al., 2010), and PRP versus sham, n = 240 (Kearney et al., 2021), both in midportion Achilles tendinopathy. **Not supported.**
## pyy

*Pharmacology & Clinical*

**PYY (peptide YY)** — A gut hormone released after a meal that damps down appetite for hours afterwards. Formally: a hormone released from intestinal L-cells post-prandially in proportion to energy consumed, acting centrally to suppress appetite. Falls with weight loss (reducing [satiety](#satiety-vs-satiation)) and rises markedly after [bariatric surgery](#bariatric-surgery), contributing to that procedure's appetite-suppressing effect.

## radiocarbon-bomb-pulse-dating

*Cell & Molecular Biology*

**Radiocarbon bomb-pulse dating** — A way of finding out how old a tissue is, using the radioactive carbon that nuclear weapons testing put into the atmosphere in the mid-20th century. Formally: a tissue-age method exploiting the sharp atmospheric ¹⁴C spike from above-ground nuclear testing (~1955–1963) and its subsequent exponential decline; tissue ¹⁴C content is matched against the known atmospheric curve to date when a protein's carbon was fixed. Applied to 28 forensic human Achilles samples, it indicates that core collagen carbon is largely incorporated during height growth — hence "before ~age 17" — with minimal subsequent replacement (Heinemeier et al., 2013). This is the single finding behind this document's claim that adult tendon is modified rather than rebuilt. **Interpretive caution:** the study reports *very limited* turnover inferred from dating and does **not** publish a measured half-life, so any "half-life of decades" figure is extrapolation and is not used in this document. The same method applied to diseased tendon found the opposite — years of abnormally high collagen turnover preceding symptoms (Heinemeier et al., 2018) — so the low-turnover picture describes healthy tendon only. **Moderate evidence:** one cross-sectional cohort, one tendon, one laboratory, not independently replicated.

## rct

*Units, Abbreviations & Conventions*

**RCT (randomized controlled trial)** — A study that decides at random who gets the treatment, so the groups differ only by the treatment. Formally: a study design in which participants are randomly allocated to intervention or control, minimizing selection bias and confounding. **Placebo-controlled** RCTs are the relevant standard for injection therapies, where expectation effects are large — which is precisely why several positively regarded injectables ([PRP](#prp)) failed once properly blinded.

## red-s

*Effort, Fatigue & Recovery*

**RED-S (relative energy deficiency in sport)** — What happens across the whole body when an athlete under-eats for their training load for long enough. Formally: a syndrome arising from sustained low [energy availability](#energy-availability), with impairments spanning endocrine function, bone mineral density, immunity, menstrual function, protein synthesis, and performance. Supersedes the earlier, narrower "female athlete triad" concept and applies to all sexes. Menstrual disturbance is its earliest reliable signal; see [HPG axis](#hpg-axis).

## refeed

*Appetite, Behavior & Adherence*

**Refeed** — A planned day or two of eating at maintenance, usually with extra carbohydrate, in the middle of a diet. Formally: a short (typically 1–2 day) planned increase to maintenance energy, usually carbohydrate-led, within a deficit. Physiological effects: glycogen restoration, restored training performance, transient [leptin](#leptin) rise. **Effect on fat-loss outcomes is small and inconsistent across trials**; the defensible rationales are training performance and psychological relief, not metabolic restoration. Shorter than a [diet break](#diet-break).

## regional-hypertrophy

*Physiology & Adaptation*

**Regional hypertrophy (non-uniform hypertrophy)** — Different parts of the same muscle grow by different amounts depending on the exercise. Formally: growth that differs between proximal, middle, and distal regions of a muscle, and between heads of a multi-head muscle, depending on exercise selection and joint angle. Establishes that "training a muscle" is not a single undifferentiated stimulus, and is the rationale for including multiple exercises per muscle group.

## rep-range

*Loading Variables & Prescription*

**Rep range** — A prescribed window of reps, like 8–12, rather than a fixed number. Formally: a prescribed interval of permissible repetitions per set, within which [load](#load) is held constant and repetitions serve as the progression variable. See [double progression](#double-progression). Its function is to permit progression despite day-to-day performance variance: on a bad day you make the bottom of the range and still progress.

## repetition

*Loading Variables & Prescription*

**Repetition (rep)** — One complete performance of the movement — down and back up. Formally: one complete execution of an exercise's movement cycle, conventionally comprising an [eccentric](#eccentric-contraction) phase, a transition, and a [concentric](#concentric-contraction) phase, through the prescribed [ROM](#rom).

## rer-rq

*Measurement & Research Methods*

**RER / RQ (respiratory exchange ratio / respiratory quotient)** — A number derived from your breathing that indicates whether you are burning mostly fat or mostly carbohydrate right now. Formally:

> RER = V̇CO₂ / V̇O₂

Values: ~0.70 = pure fat oxidation; ~1.00 = pure carbohydrate oxidation; ~0.85 = mixed. Used to infer substrate utilization. **Critical interpretive point: RER during a single exercise bout does not determine fat loss.** Twenty-four-hour substrate balance governs, and it is dominated by total energy balance and total carbohydrate intake — which is why the "[fat-burning zone](#fat-burning-zone)" is a measurement artifact rather than a strategy.

## reset

*Programming & Progression*

**Reset** — Dropping the weight back about 10% after you get stuck, then climbing again. Formally: a deliberate reduction in [load](#load) (conventionally ~10%) following a [stall](#stall), from which the previous progression rule is re-applied, allowing the athlete to re-approach and pass the prior sticking point with accumulated adaptation. Two consecutive failed resets is the standard criterion for abandoning [linear progression](#linear-progression). Distinct from a [deload](#deload), which is scheduled and reduces volume rather than being triggered and reducing load.

## residual-training-effect

*Programming & Progression*

**Residual training effect** — How long a given quality sticks around after you stop training it. Formally: the duration for which an adaptation persists after its specific training stimulus is withdrawn. Ordering (approximate): aerobic endurance and maximal strength are long-lasting (~30 ± 5 days); anaerobic power and maximal speed are short (~5–15 days). The basis of [block periodization](#block-periodization) sequencing — you train the durable qualities first and the perishable ones last.

## resistance-training

*Training, Loading & Contraction*

**Resistance training** — Training against a resisting force — weights, machines, bands, or your own body — with the intent of increasing strength or muscle size. Formally: repeated voluntary muscle actions performed against an external [load](#load), organized into [sets](#set) and [repetitions](#repetition) and governed by [progressive overload](#progressive-overload). It is the practice; progressive overload is the principle it must obey. Why it matters here: it is the single most effective intervention for retaining [lean body mass](#lbm) in an [energy deficit](#energy-deficit), the required stimulus for [hypertrophy](#hypertrophy), and — in the heavy, slow forms described in Part II — the only reliable way to build tendon capacity.

## responder-variability

*Physiology & Adaptation*

**Responder variability** — The same program produces very different results in different people. Formally: the large inter-individual variance in adaptive response to an identical training stimulus, spanning from high responders to genuine non-responders in some measures. Attributable to genetics, [satellite cell](#satellite-cell) pool size, baseline training status, nutrition, and sleep. Consequence: group-mean results from trials describe a *distribution*, and an individual's own tracked response outranks the population mean for programming decisions.

## rest-interval

*Loading Variables & Prescription*

**Rest interval (inter-set rest)** — How long you rest between sets. Formally: the recovery period between sets. Evidence: rest **≥2 minutes** produces greater hypertrophy than ≤1 minute for [compound](#compound) exercises, because short rest degrades subsequent-set performance and thus total [volume load](#volume-load). **Moderate evidence** — the headline result comes from a single 8-week trial in 21 resistance-trained men comparing 3-minute against 1-minute rests (Schoenfeld et al., 2016). Practical: 2–3 min for compounds, 1–2 min for [isolation](#isolation), where systemic recovery demand is lower. Rest reduction is a conditioning stimulus, not a hypertrophy stimulus; see [training density](#training-density).

## reverse-dieting

*Appetite, Behavior & Adherence*

**Reverse dieting** — Adding calories back very slowly after a diet, on the claim that this "rebuilds the metabolism." Formally: the practice of raising calories in small increments (e.g. 50–100 kcal/week) after a diet, on the stated rationale of restoring metabolic rate while minimizing fat regain. **No controlled trial supports the metabolic-rebuilding claim** [UNVERIFIED — no trial could be located testing it either way]. What the practice plausibly does provide is a structured, gradual return to maintenance with continued self-monitoring, which supports [adherence](#adherence) and limits overshoot. Value it as a behavioral protocol; discount the stated mechanism.

## reversibility

*Programming & Progression*

**Reversibility (detraining)** — Use it or lose it: adaptations fade when the training that produced them stops. Formally: the principle that adaptations regress when the stimulus is withdrawn. Rates differ markedly by tissue: [neural adaptations](#neural-adaptation) and muscle [CSA](#csa) decline over weeks-to-months and are rapidly recoverable via [muscle memory](#muscle-memory); [tendon stiffness](#stiffness) declines within ~2–8 weeks and is *slow* to rebuild — an asymmetry that makes return-from-layoff the highest-risk phase. See [detraining](#detraining).

## rfd

*Mechanics & Material Properties*

**RFD (rate of force development)** — How fast you can produce force, as opposed to how much force you can eventually produce. Formally: the time derivative of force, dF/dt, typically taken over defined windows (0–50, 0–100, 0–200 ms) from contraction onset. Units: N·s⁻¹. Determined by neural drive, muscle contractile properties, and series [stiffness](#stiffness). The key determinant of performance in movements with [ground contact times](#gct) too short to reach peak force — which is most of sprinting and jumping.

## rir

*Effort, Fatigue & Recovery · Training, Loading & Contraction*

**RIR (repetitions in reserve)** — How many more reps you could have done if you had kept going. Formally: the number of additional repetitions that could have been completed to [momentary failure](#momentary-failure) at the point a set was terminated. 0 RIR = failure. The prescription variable for [proximity to failure](#proximity-to-failure). **Validity caveat:** accuracy is poor in general, and the error runs toward stopping earlier than believed. Across 12 studies and 414 participants, accuracy improved as the set approached failure and as load rose, but resistance-training *experience* did not measurably improve it (Halperin et al., 2022) — so the common claim that estimates are poor in beginners and reliable in trained lifters is **not supported**. Everyone benefits from periodic calibration against actual failure on machine-based exercises.

## rm

*Training, Loading & Contraction*

**RM (repetition maximum)** — The heaviest weight that allows exactly a given number of reps. Formally: the maximum load that permits exactly *n* repetitions. "6RM" = the heaviest load allowing 6 and only 6 repetitions. Not to be confused with %[1RM](#one-rep-max), though the two map to each other approximately (e.g. 6RM ≈ 85% 1RM, with considerable exercise- and individual-dependent variance).

## rom

*Exercise Mechanics · Training, Loading & Contraction*

**ROM (range of motion)** — How far the joint actually travels during a rep. Formally: the angular excursion through which the joint(s) travel during a repetition. **Full ROM** = the complete actively controllable range with acceptable technique, which is individual (determined by anthropometry and mobility) and not a fixed standard. Establishing full ROM comes first; loading it comes second; shortening it to add weight is [load cheating](#load-cheating), not progression. Contrast [partial ROM](#partial-rom).

## rpe

*Effort, Fatigue & Recovery*

**RPE (rating of perceived exertion)** — A self-scored number for how hard something felt. Formally: a subjective effort scale. Two distinct scales share the abbreviation: the original **Borg 6–20** scale (designed to track heart rate), and the resistance-training **[RIR](#rir)-based RPE scale (1–10)**, in which RPE 10 = 0 RIR, RPE 9 = 1 RIR, RPE 8 = 2 RIR, and so on. Unqualified "RPE" in strength contexts means the latter, and that is the sense used in this document. **Session-RPE** (a single whole-session rating × duration) is a separate construct used to quantify internal [training load](#training-load).

## rsi

*Testing & Monitoring*

**RSI (reactive strength index)** — A single number for how bouncy an athlete is: jump height divided by time spent on the ground. Formally:

> RSI = jump height (m) / [ground contact time](#gct) (s)

Units: m·s⁻¹. Typically assessed via [drop jump](#drop-jump-vs-depth-jump) from a standardized box height. A modified form, **RSImod**, uses jump height / time-to-takeoff from a [CMJ](#cmj). **Monitoring use:** a decline in RSI at stable body mass and [training load](#training-load) is an early indicator of neuromuscular [fatigue](#fatigue). **Moderate evidence** for that use. The stronger claim — that RSI decline specifically precedes *tendon* symptoms — has not been demonstrated prospectively for tendinopathy and should be treated as a hypothesis. **Validity caveat:** RSI is a ratio of two small, variable numbers and moves with instruction, footwear, surface, warm-up and motivation as much as with fatigue. Establish your own week-to-week variation across several stable weeks, then act only on declines that persist over two or three sessions and exceed it. A single-session dip is noise.

## running-economy

*Testing & Monitoring*

**Running economy** — How much energy it costs you to run at a given pace; lower is better, like fuel consumption. Formally: the steady-state oxygen (or energy) cost of running at a given submaximal velocity, expressed as mL O₂·kg⁻¹·km⁻¹ or J·kg⁻¹·m⁻¹. Improved by higher tendon [stiffness](#stiffness) via reduced muscular work per stride; one of the three principal determinants of distance-running performance alongside V̇O₂max and lactate threshold.

## satellite-cell

*Physiology & Adaptation*

**Satellite cell** — A dormant stem cell sitting on the surface of a muscle fiber, which wakes up after training and donates new nuclei to the fiber. Formally: a quiescent muscle stem cell residing between the sarcolemma and basal lamina. On mechanical or damage stimulus it proliferates and donates nuclei to existing fibers, raising [myonuclear](#myonucleus) number and supporting the transcriptional demand of a larger fiber. Long assumed necessary for hypertrophy beyond a certain magnitude (the myonuclear-domain ceiling), but that necessity is **contested**: mice depleted of over 90% of their satellite cells still roughly doubled muscle mass under two weeks of overload (McCarthy et al., 2011). Better described as facilitating and sustaining growth than as strictly gating it.

## satiety-vs-satiation

*Diet Composition & Nutrition*

**Satiety vs. satiation** — Two different kinds of fullness: the one that makes you put your fork down, and the one that keeps you from wanting food later. Formally: **satiation** is the process terminating a given eating episode (how much you eat now); **satiety** is the post-ingestive inhibition of further eating (how long until you eat again). Both are increased by protein, fiber, food volume, low [energy density](#energy-density), and solid over liquid form. Hunger management in a deficit is fundamentally a satiation/satiety-engineering problem, not a willpower problem.

## set

*Loading Variables & Prescription*

**Set** — A run of reps done back-to-back before you rest. Formally: a group of consecutive repetitions performed without rest. The standard unit for counting [training volume](#training-volume) in hypertrophy research — but only when the set was hard enough to count; see [hard set](#hard-set) and [sets per muscle group](#sets-per-muscle-group-per-week).

## set-point-theory

*Metabolic Adaptation & Endocrine Regulation*

**Set point theory** — The model that your body has a target weight it actively defends, pushing back when you move away from it. Formally: the model that body weight is regulated around a biologically determined target, defended by compensatory changes in intake and expenditure. Supported by the vigorous, asymmetric defense of weight loss documented in Part III §2.3 — falling [leptin](#leptin), rising [ghrelin](#ghrelin), suppressed [NEAT](#neat). Its weakness: it cannot explain population-level weight gain over recent decades without invoking a "moving" set point, at which point the model loses predictive value. See [settling point](#settling-point-theory).

## sets-per-muscle-group-per-week

*Loading Variables & Prescription*

**Sets per muscle group per week** — The standard way of counting training volume: how many hard sets each muscle got in a week. Formally: the count of [hard sets](#hard-set) directly targeting a given muscle within a [microcycle](#microcycle) — the dominant volume metric in contemporary hypertrophy literature. Conventions vary on whether indirect involvement counts as a full set, a half set, or nothing — a substantial source of between-study inconsistency, and the largest meta-regression to date found that crediting indirect work *fractionally* predicts outcomes best (Pelland et al., 2026). Dose–response is approximately monotonic from ~4 to ~20+ sets/week with clearly diminishing returns beyond ~10–20; no group-level downturn at high volumes has been observed.

## settling-point-theory

*Metabolic Adaptation & Endocrine Regulation*

**Settling point theory** — The model that your weight simply comes to rest wherever your biology, habits, and food environment balance out, with no defended target required. Formally: the model that body weight settles at an equilibrium determined by the interaction of physiology, environment, food availability, and habit. Better accommodates environmental effects on population weight than [set point theory](#set-point-theory). **Current position:** the two models are complementary — the defense of weight loss is real and asymmetric (strong against loss, weak against gain), while the equilibrium level itself is strongly environment-dependent. Practical reading: your body defends downward movement far more vigorously than upward.

## sfr

*Effort, Fatigue & Recovery*

**SFR (stimulus-to-fatigue ratio)** — How much growth stimulus you get for how much tiredness you pay. Formally: a conceptual ratio of hypertrophic stimulus generated to systemic and local [fatigue](#fatigue) incurred by a given set, exercise, or session. Not directly measurable, but a useful decision heuristic: it explains why the last rep before failure has a poor SFR, why heavy deadlifts have a poorer SFR than leg presses for quadriceps hypertrophy, and why machine work is often preferable late in a session.
## shoe-drop

*Training, Loading & Contraction*

**Shoe drop (heel-to-toe offset)** — How much higher the heel of a shoe sits than its forefoot. Formally: the difference in stack height between the heel and forefoot of a shoe, in mm. Lower drop increases required ankle [dorsiflexion](#dorsiflexion-plantarflexion) and Achilles/plantarflexor load; higher drop offloads the Achilles and increases knee load. Abrupt drop reductions are a recognized Achilles tendinopathy trigger — the change matters more than the value.

## si-units

*Units, Abbreviations & Conventions*

**SI units** — The standard international measurement system (metres, kilograms, seconds, newtons, pascals). Formally: the International System of Units. Quantities in this document use SI unless a field convention dictates otherwise (e.g. tendon [stiffness](#stiffness) in N·mm⁻¹ rather than N·m⁻¹; [GCT](#gct) in ms). Energy is reported in kcal throughout, as is conventional in the nutrition literature.

## silbernagel-combined-graded-protocol

*Testing & Monitoring*

**Silbernagel combined/graded protocol** — A four-stage Achilles rehab program that lets you keep running while you rehabilitate, guided by pain rules rather than by rest. Formally: a four-phase, pain-guided Achilles rehabilitation program progressing from basic [concentric](#concentric-contraction)–[eccentric](#eccentric-contraction) calf work through heavy loading to [plyometric](#plyometrics) and sport-specific loading, explicitly permitting continued running under the [pain-monitoring model](#pain-monitoring-model). Notable for demonstrating that activity cessation is unnecessary: continued running and jumping under the pain rule did not worsen outcomes versus stopping (Silbernagel et al., 2007). **Moderate evidence** — one randomised trial of 38 patients.

## size-principle

*Physiology & Adaptation*

**Size principle (Henneman)** — Your body always calls on its small, fatigue-resistant [motor units](#motor-unit) first and its big, powerful ones last. Formally: motor units are recruited in ascending order of motor-neuron size, hence of force threshold: small, fatigue-resistant units first, large, fast-fatiguing units last (Henneman et al., 1965). The foundational reason that either heavy load **or** proximity to [failure](#momentary-failure) is required for full recruitment, and thus why both heavy-low-rep and light-high-rep training can build muscle.

## sns

*Metabolic Adaptation & Endocrine Regulation*

**SNS (sympathetic nervous system) tone** — How switched-on your "fight-or-flight" nervous system is, moment to moment. Formally: the level of sympathetic outflow, assessable via [catecholamine](#catecholamines) turnover and heart-rate variability. Falls with energy restriction under [leptin](#leptin) signaling, reducing [BMR](#bmr-rmr), [NEAT](#neat), and thermogenesis, and producing the characteristic cold intolerance and low resting heart rate of dieting.

## spot-reduction

*Body Composition & Adipose Biology*

**Spot reduction** — The belief that training a body part burns the fat sitting on top of it. It does not. Formally: the disproven claim that exercising a specific muscle preferentially reduces adipose tissue overlying it. Fat mobilization is systemic and hormonally mediated; regional fat-loss *order* is genetically determined, largely by regional α₂- vs. β-adrenergic receptor density and blood flow. Controlled trials consistently show no localized fat reduction — 12 weeks of localized single-leg endurance resistance training produced fat loss in the *upper body*, not the trained leg (Ramírez-Campillo et al., 2013; n = 11).

## ssc

*Mechanics & Material Properties*

**SSC (stretch-shortening cycle)** — Stretching a muscle–tendon unit immediately before shortening it, so it acts like a spring being loaded and released — the reason a countermovement jump beats a jump from a standstill. Formally: a movement pattern in which an active muscle–tendon unit is stretched (eccentric phase) immediately before shortening (concentric phase), separated by a brief transition (**amortization phase**). Performance enhancement arises from elastic energy storage and return in tendon, stretch-reflex potentiation, and the muscle operating near-isometrically at favorable [force–velocity](#force-velocity-relationship) conditions. **Fast SSC**: [ground contact](#gct) <250 ms (sprint, depth jump). **Slow SSC**: >250 ms (countermovement jump, layup).

## stall

*Programming & Progression*

**Stall (plateau)** — Getting stuck: you cannot make the prescribed reps at the prescribed weight, session after session. Formally: failure to complete the prescribed repetitions at the prescribed [load](#load) across consecutive attempts, in the absence of an identifiable acute cause (illness, sleep loss, under-eating). The trigger for a [reset](#reset) or a change of progression model. Distinguish a true stall from a single bad session.

## stiffness

*Mechanics & Material Properties*

**Stiffness (k)** — How much force it takes to stretch something by a given amount; a stiff tendon lengthens little under a big pull. Formally, a *structural* property: the slope of the force–elongation relationship,

> k = ΔF / ΔL   (units: N·mm⁻¹)

Depends on the tendon's material properties **and** its geometry (length and [CSA](#csa)) — so a tendon can become stiffer simply by becoming thicker. Not interchangeable with [Young's modulus](#youngs-modulus), which removes the geometry. Tendon stiffness is typically reported over a defined force range (e.g. 50–100% [MVC](#mvc)) because the relationship is non-linear at low loads. **Note:** in this document "stiffness" always means this mechanical property; the clinical symptom of a stiff, sore tendon on waking is called [morning stiffness](#morning-stiffness) and is unrelated.

## strain

*Mechanics & Material Properties*

**Strain (ε)** — How far something has stretched, expressed as a fraction of its original length; 5% strain means 5% longer than at rest. Formally:

> ε = ΔL / L₀   (expressed as a fraction or %)

The variable that [tenocytes](#tenocyte) actually sense. Functional in-vivo Achilles strain during locomotion is ~4–9%, and the **~4.5–6.5% window** is the target zone for adaptive loading. The often-quoted "microdamage above ~4–5%, rupture at ~8–10%" figures are **ex-vivo cadaveric failure limits and are not on the same measurement basis** — living tendon operates above the ex-vivo "microfailure" threshold routinely and without injury. Do not compare the two sets of numbers directly. **Note:** "strain" in this mechanical sense is not the injury called a muscle strain (a tear); where the injury is meant, this document writes "muscle-strain injury."

## stress

*Mechanics & Material Properties*

**Stress (σ)** — Force divided by the area carrying it — the same pull is more punishing on a thinner tendon. Formally:

> σ = F / A   (units: Pa = N·m⁻²; tendon values conventionally reported in [MPa](#pa-mpa-gpa))

Plotted against [strain](#strain), it produces the stress–strain curve whose regions ([toe](#toe-region), linear, microfailure, rupture) define what loading a tendon can tolerate. Not to be confused with psychological or systemic stress.

## stress-relaxation

*Mechanics & Material Properties*

**Stress relaxation** — Hold a tissue at a fixed stretch and the force it pushes back with slowly fades. Formally: progressive decrease in [stress](#stress) over time under a constant applied [strain](#strain); the complement of [creep](#creep) (constant load, increasing strain) and a defining feature of [viscoelasticity](#viscoelasticity).

## sub-tendon

*Anatomy & Composition*

**Sub-tendon** — One of the separate strands inside a tendon that is shared by more than one muscle. Formally: an anatomically distinct fascicle bundle within a compound tendon arising from a specific muscle head. The Achilles comprises three sub-tendons (soleus, medial gastrocnemius, lateral gastrocnemius) arranged with variable helical twist; non-uniform [strain](#strain) distribution between them is implicated in tendinopathy — one strand can be overloaded while the tendon as a whole looks fine.

## taper

*Programming & Progression · Training, Loading & Contraction*

**Taper** — Cutting training volume in the final weeks before a competition so you arrive fresh without going stale. Formally: a pre-competition phase of progressively reduced [volume](#training-volume) (typically 40–60%) with maintained or slightly raised [intensity of load](#intensity), intended to dissipate [fatigue](#fatigue) while preserving fitness. Not applicable to open-ended hypertrophy training. Shares its shape with a [deload](#deload) but not its purpose: a taper is aimed at a date, a deload at recovery within an ongoing block.

## tdee

*Energetics & Balance*

**TDEE (total daily energy expenditure)** — Everything you burn in a day, added up. Formally: the sum of all energy expended in 24 h:

> TDEE = [BMR](#bmr-rmr) + [TEF](#tef) + [EAT](#eat) + [NEAT](#neat)

Units: kcal·day⁻¹. Measured accurately only by [doubly labeled water](#dlw) or whole-room [calorimetry](#calorimetry-direct-and-indirect); estimated in practice from tracked intake against observed weight trend, which outperforms all prediction equations (see [Mifflin-St Jeor](#mifflin-st-jeor)). **TDEE is not a constant** — it falls with mass loss, with restriction, and with adaptation, which is why any fixed calorie target eventually becomes maintenance.

## technical-failure

*Effort, Fatigue & Recovery*

**Technical failure** — The point in a set where you could still grind out another rep, but not with acceptable technique. Formally: set termination at the point at which movement quality — [ROM](#rom), bar path, control, or trunk position — degrades below a pre-defined standard, irrespective of whether further repetitions are mechanically possible. It occurs earlier than [momentary failure](#momentary-failure) and is the more appropriate practical endpoint for [compound](#compound) exercises. Load-bearing in this document because every progression rule that says "with clean technique" is specifying technical failure, not momentary failure, as the boundary — and because adding reps or weight past this point is [load cheating](#load-cheating), not progress.

## tef

*Energetics & Balance*

**TEF (thermic effect of food) / DIT (diet-induced thermogenesis)** — The energy your body spends digesting and processing what you eat. Formally: the energy cost of digesting, absorbing, and assimilating ingested nutrients, expressed as a percentage of the energy of the food consumed. Values: **protein 20–30%, carbohydrate 5–10%, fat 0–3%, alcohol ~10–30%**. Whole-diet TEF is ~8–15% of intake. Higher for minimally processed foods than for equivalent-macronutrient processed foods — one mechanism by which food processing affects energy balance beyond intake volume. One of the four components of [TDEE](#tdee).

## tempo

*Loading Variables & Prescription*

**Tempo** — How fast you move through each part of a rep, written as a string of numbers. Formally: the prescribed duration of each phase of a repetition, conventionally written as a 3- or 4-digit code — **[eccentric](#eccentric-contraction)–bottom pause–[concentric](#concentric-contraction)–top pause**, in seconds (e.g. **3-0-3** = 3 s down, no pause, 3 s up). Evidence for hypertrophy: repetition durations from ~0.5 s to ~8 s produce similar growth, and only very slow (>10 s) tempos impair it, by limiting load (Schoenfeld et al., 2015). **Moderate evidence** — the pooled trials were short and largely in untrained participants. Tempo matters far more for tendon work — see [HSR](#hsr) — where ~3 s per phase is the effective dose.

## tendinitis

*Pathology & Clinical*

**Tendinitis** — An outdated name for tendon pain, based on the assumption that it is caused by inflammation. Formally: a term implying primary inflammatory-cell-mediated tendon pathology, retained only for genuinely acute inflammatory presentations and for **paratenonitis** (inflammation of the [paratenon](#endotenon-epitenon-paratenon), which *is* inflammatory). For chronic overuse presentations the correct term is [tendinopathy](#tendinopathy). The distinction is not pedantic: it is why anti-inflammatory treatment underperforms loading.

## tendinopathy

*Pathology & Clinical*

**Tendinopathy** — Persistent tendon pain and loss of function from overload, with the tendon often thickened. Formally: the clinical syndrome of localized tendon pain, loss of function, and often thickening, associated with mechanical overload — deliberately descriptive rather than histological. Related terms: **tendinosis** (the histological finding of non-inflammatory degeneration — disorganized collagen, increased [ground substance](#ground-substance), altered cellularity, [neovascularization](#neovascularization)); **paratenonitis** (inflammation of the surrounding paratenon). See [continuum model](#continuum-model-of-tendon-pathology) for staging. **Caveat on the inflammation question:** the slogan that tendinopathy involves *no* inflammation was an overcorrection to the obsolete term "[tendinitis](#tendinitis)". Classic acute inflammatory cells are largely absent in chronic disease, but inflammatory signalling and resident immune cells do participate, including chronically (Millar et al., 2021). The defensible statement is the narrow one: this is not an acute inflammatory condition, and treating it as one has failed.

## tendinopathy-associated-genes

*Cell & Molecular Biology*

**Tendinopathy-associated genes** — Inherited variants that modestly raise the risk of tendon problems. Formally: polymorphisms with replicated (though modest and population-variable) associations with tendinopathy or rupture risk — ***COL5A1*** (type V collagen α1, regulates fibril diameter — the most consistently replicated), ***COL1A1*** (type I collagen α1), ***TNC*** (tenascin-C, a matrix glycoprotein), ***MMP3*** ([MMP](#mmps) regulation), ***GDF5***. Effect sizes are small; family history remains the more useful clinical signal.

## tendon-compression

*Pathology & Clinical*

**Tendon compression** — A tendon being squashed sideways against bone, on top of being pulled lengthwise. Formally: transverse compressive load applied to a tendon where it wraps a bony prominence or pulley, superimposed on tensile load. Induces fibrocartilaginous change ([aggrecan](#aggrecan) expression). A principal aggravating mechanism in [insertional tendinopathies](#insertional-tendinopathy); the reason static stretching is contraindicated in these presentations, since stretching increases the compression rather than relieving it.

## tendon-elongation

*Pathology & Clinical*

**Tendon elongation (post-rupture)** — A repaired tendon healing longer than it was, which permanently weakens the muscle it serves. Formally: permanent increase in resting tendon length after rupture or repair, typically from [creep](#creep) under load before healing consolidates. Mechanically it shifts the muscle onto an unfavorable region of the [length–tension relationship](#length-tension-relationship) and reduces plantarflexion torque and [RFD](#rfd) — the primary reason for persistent long-term deficits after Achilles rupture, and the rationale for protecting repair length early.

## tendon-xanthoma

*Pathology & Clinical*

**Tendon xanthoma** — A lumpy cholesterol deposit inside a tendon, visible and palpable as a nodule. Formally: nodular lipid (cholesterol-laden macrophage) deposition within tendon, classically in the Achilles and extensor tendons of the hand. A physical sign of familial hypercholesterolemia; warrants lipid screening rather than loading management.

## tenocyte

*Anatomy & Composition*

**Tenocyte** — The resident cell of tendon: it senses load and both builds and removes the surrounding material. Formally: an elongated fibroblast-lineage cell arranged in longitudinal rows between [fibrils](#fibril). Functions: matrix synthesis (collagen, [proteoglycans](#proteoglycan)), matrix degradation ([MMPs](#mmps)), and [mechanotransduction](#mechanotransduction). *Tenoblast* denotes the more rounded, metabolically active immature form; a shift back toward rounded morphology is a histological feature of [tendinopathy](#tendinopathy).

## testosterone

*Metabolic Adaptation & Endocrine Regulation*

**Testosterone** — The main male sex hormone, present and functionally important in both sexes. Formally: the principal androgen; supports [MPS](#mps-mpb), libido, mood, and bone density. Falls with aggressive restriction, very low dietary fat (<~15–20% of intake), low body fat, and sleep restriction — though in dieting athletes the dominant driver is low [energy availability](#energy-availability) rather than the dietary fat percentage as such (Mountjoy et al., 2023), so eating more fat at the same low intake does not protect it. Its decline is a marker of excessive restriction rather than an independent problem to treat — the correct response is to fix the deficit, not the hormone.

## tgf-beta

*Cell & Molecular Biology*

**TGF-β (transforming growth factor beta)** — A signaling molecule that tells cells to lay down connective tissue. Formally: a cytokine superfamily member central to fibrogenesis. In tendon, load-induced TGF-β signaling (via SMAD2/3) drives type I collagen transcription. Dysregulated chronic TGF-β signaling contributes to fibrotic and degenerative matrix change — the same signal builds tendon and, unregulated, degrades it.

## thyroid-hormones

*Metabolic Adaptation & Endocrine Regulation*

**Thyroid hormones (T4, T3, rT3)** — The hormones that set your cells' overall metabolic speed. Formally: thyroxine (T4) is the prohormone; **triiodothyronine (T3)** is the active form, generated by peripheral deiodination and the principal determinant of cellular metabolic rate. In energy restriction, T4 typically remains normal while **T3 falls and reverse-T3 rises** — a state termed *low-T3 syndrome* or *euthyroid sick syndrome*. **This is a normal adaptive response to restriction, not thyroid disease**, and it resolves on refeeding; it should not be treated pharmacologically in an otherwise healthy dieter.

## timps

*Cell & Molecular Biology*

**TIMPs (tissue inhibitors of metalloproteinases)** — The brakes on the enzymes that break tissue down. Formally: endogenous proteins that bind and inhibit [MMPs](#mmps). The MMP:TIMP ratio determines net matrix degradation; its disturbance is a proposed mechanism in tendinopathy — matrix turnover is a balance, and pathology is that balance tipping.

## tirzepatide

*Pharmacology & Clinical*

**Tirzepatide (dual GIP/GLP-1 receptor agonist)** — A prescription drug that imitates two gut fullness hormones at once, currently the most effective weight-loss medicine available. Formally: a dual incretin agonist acting at both the [GLP-1](#glp-1) receptor and the GIP (glucose-dependent insulinotropic polypeptide) receptor, producing dose-dependent mean body-weight loss of **~15% (5 mg), ~19.5% (10 mg) and ~21% (15 mg) at 72 weeks** — up to 22.5% on the efficacy estimand — in SURMOUNT-1 (n = 2,539; Jastreboff et al., 2022), the largest effect achieved pharmacologically to date. **All the caveats of [GLP-1 agonists](#glp-1-receptor-agonist) apply in full**: the MEN2/medullary thyroid carcinoma contraindication, pancreatitis and gallbladder cautions, the anaesthesia aspiration risk from delayed gastric emptying, hypoglycaemia risk alongside insulin or sulfonylureas, lean-mass loss without training and protein, rapid regain on discontinuation, unsuitability for cosmetic use or for people with an eating-disorder history, and the danger of compounded grey-market product.
## toe-region

*Mechanics & Material Properties*

**Toe region** — The first, easy part of stretching a tendon, where the wavy fibers are just pulling straight and very little force is needed. Formally: the initial low-[stiffness](#stiffness), upwardly concave portion of the tendon [stress](#stress)–[strain](#strain) curve (0–2% strain), corresponding to progressive straightening of [crimp](#crimp) rather than to stretching of the collagen molecules themselves.

## training-density

*Loading Variables & Prescription*

**Training density** — How much work you cram into the time available. Formally: work performed per unit of time, i.e. [volume load](#volume-load) divided by session duration. Increased by shortening [rest intervals](#rest-interval) or using supersets (alternating exercises with little or no rest between them). A legitimate progression variable for work capacity and time efficiency; a poor one for hypertrophy, since it typically forces load or rep reductions.

## training-frequency

*Loading Variables & Prescription*

**Training frequency** — How many times a week you train a given muscle. Formally: the number of sessions per [microcycle](#microcycle) in which a given muscle group is trained. Evidence: training a muscle at least twice weekly beat once weekly in meta-analysis, but that advantage largely reflects the higher-frequency groups doing more total work — once weekly [volume](#training-volume) is equated, frequencies across the practical range produce similar hypertrophy, and whether 3×/week beats 2× is undetermined (Schoenfeld et al., 2019). The most recent meta-regression likewise finds frequency operating mainly through volume accumulation (Pelland et al., 2026). Frequency's practical value is therefore as a **volume-distribution tool** — higher frequency permits more weekly sets at acceptable per-session quality — rather than as an independent stimulus.

## training-load

*Loading Variables & Prescription*

**Training load** — The total amount of training you have done over a period — not the weight on the bar. Formally: the cumulative dose of training. **External load** = objectively measured work (tonnage, [volume load](#volume-load), sets, distance, foot contacts). **Internal load** = the individual's physiological/psychological response (session-[RPE](#rpe) × duration, heart-rate-based measures, soreness). Both are needed: identical external loads produce different internal loads across individuals and states. Where this document says "load spike", "weekly training-load change", or "[ACWR](#acwr)", it means training load; where it says "[load](#load)", it means the weight lifted.

## training-status

*Measurement & Research Terms*

**Training status (training age)** — How long, and how well, someone has trained before now. Formally: the duration and quality of an individual's prior resistance-training exposure. **The dominant moderator of nearly every finding in this field.** Results obtained in untrained participants over 8–12 weeks — which describes the majority of the literature — generalize poorly to trained lifters, in whom [novice-effect](#novice-effect) noise no longer masks true between-condition differences.

## training-volume

*Loading Variables & Prescription*

**Training volume** — How much work you did, however you choose to count it. Formally: the total quantity of work performed, operationalized three ways which are **not interchangeable**: (1) **[sets per muscle group](#sets-per-muscle-group-per-week)** — the current standard for hypertrophy; (2) **[volume load](#volume-load)** — sets × reps × load, in kg; (3) **total repetitions**. Volume load is misleading across exercises and rep ranges, since a high-rep light set can accumulate more tonnage than a hard heavy set. **Scope note:** in Part I and Part III, volume is a primary driver of hypertrophy; in Part II it explicitly is *not* the driver of tendon adaptation, where [strain](#strain) magnitude governs. The word is the same; the role differs by tissue.

## tre

*Appetite, Behavior & Adherence*

**TRE (time-restricted eating)** — Eating only within the same set number of hours each day, without necessarily counting calories. Formally: confining intake to a consistent daily window (commonly 8–10 h) without deliberate energy restriction. Weight loss, where it occurs, is generally attributable to the incidental energy reduction that window restriction produces. Independent circadian benefits (particularly for *early* TRE, with the window shifted earlier in the day) are plausible and under active investigation but not established as clinically decisive. A subtype of [intermittent fasting](#intermittent-fasting).

## ucp1

*Body Composition & Adipose Biology*

**UCP1 (uncoupling protein 1, thermogenin)** — A protein that lets a cell burn fuel purely to make heat, deliberately wasting the energy instead of storing it. Formally: an inner-mitochondrial-membrane protein of [brown](#bat) and [beige](#beige) adipocytes that permits proton re-entry without ATP synthesis, uncoupling substrate oxidation from energy capture and releasing the energy as heat. The molecular basis of non-shivering thermogenesis.

## under-reporting

*Measurement & Research Methods*

**Under-reporting (of dietary intake)** — People consistently record eating less than they actually eat — not by lying, but by forgetting, mis-estimating, and skipping unusual days. Formally: the systematic, well-replicated tendency to under-record energy intake in self-report, quantified against [DLW](#dlw). Typical magnitude: **~20% in lean individuals, 30–50% in individuals with obesity**, with parallel over-reporting of physical activity. The best-known demonstration measured 10 self-described "diet-resistant" subjects against [DLW](#dlw) and found ~47% under-reporting of intake and ~51% over-reporting of exercise (Lichtman et al., 1992) — note n = 10, deliberately selected for treatment failure, so that is the extreme case rather than the average. Mechanisms: forgotten items, portion underestimation, unrecorded cooking oils and drinks, and non-recording of atypical days. **Practical consequence: usually the correct explanation for an "unexplained" plateau in someone with substantial fat to lose. Audit intake before adjusting calories.** This is a measurement phenomenon, not a moral one — it occurs in dietitians measuring themselves.

**⚠ The clinical exception.** None of this applies to a lean person, an athlete, or someone who has already been restricting for months. In that person a reported intake of 1200 kcal is more likely accurate than not, and the correct response is to **stop dieting and eat more** — not to audit harder and cut further. Chronically low intake in an already-lean person is a clinical finding, not a tracking error.

## undulating

*Programming & Progression*

**Undulating (non-linear) periodization** — Mixing heavy, medium, and light work continuously instead of shifting gradually from one to the other. Formally: a [periodization](#periodization) model in which [intensity of load](#intensity) and [volume](#training-volume) fluctuate frequently rather than trending monotonically. Subtypes: **[DUP](#dup)** (daily undulating — variation within the week) and **WUP** (weekly undulating — variation from week to week). Rationale: repeated exposure to multiple adaptive stimuli and distribution of joint/tissue stress.

## upf

*Diet Composition & Nutrition*

**UPF (ultra-processed food)** — Industrially formulated food built from extracted ingredients and additives rather than from recognizable whole foods. Formally: category 4 of the **NOVA classification** — industrial formulations made largely or wholly from substances extracted from foods, plus additives, containing little or no intact whole food. **Key evidence: Hall et al. (2019) metabolic-ward randomised crossover RCT — 20 adults, 4 weeks as inpatients, ad libitum ultra-processed vs. unprocessed diets matched for presented calories, energy density, macronutrients, sugar, sodium and fibre. Participants spontaneously ate ~500 kcal·day⁻¹ more on the UPF arm, gaining weight on it while losing weight on the other.** Strong internal validity; **limited generalisability** — n = 20, 4 weeks, single facility. This establishes a causal effect of food processing on intake independent of nutrient composition. **Caveat:** NOVA is criticized for grouping heterogeneous foods (protein powder and confectionery share category 4), so the classification is a useful heuristic rather than a precise causal category.

## uts

*Mechanics & Material Properties*

**UTS (ultimate tensile strength)** — The most pull a material can take before it breaks. Formally: the maximum [stress](#stress) a material sustains before failure. Human tendon: ~50–100 [MPa](#pa-mpa-gpa).

## vbt

*Loading Variables & Prescription*

**VBT (velocity-based training)** — Using a sensor to measure how fast the bar moves, and letting that decide the weight and when to stop the set. Formally: prescription and [autoregulation](#autoregulation) driven by the measured mean concentric velocity of the bar (m·s⁻¹), captured by a linear position transducer, accelerometer, or camera. Two uses: **(1) load prescription** — because the load–velocity relationship is close to linear and individual-specific, a target velocity selects the appropriate %[1RM](#one-rep-max) for that day's actual readiness; **(2) set termination** — see [velocity loss threshold](#velocity-loss-threshold). Well validated for strength; unnecessary for beginners, whose technical variability degrades velocity signal quality.

## velocity-loss-threshold

*Loading Variables & Prescription*

**Velocity loss threshold** — Stopping the set once your reps have slowed by a set percentage compared with your fastest one. Formally, a set-termination criterion in [VBT](#vbt):

> velocity loss (%) = [(v_best − v_current) / v_best] × 100

The set ends when concentric velocity falls the prescribed percentage below the fastest (usually first) repetition of that set. Serves as an objective proxy for [proximity to failure](#proximity-to-failure), since velocity decays approximately linearly with accumulating [fatigue](#fatigue). Typical prescriptions: **10–20%** loss for strength and power (low fatigue), **20–40%** for hypertrophy. Its advantage over [RIR](#rir) is that it does not depend on subjective self-assessment, which is unreliable in the untrained.

## viscoelasticity

*Mechanics & Material Properties*

**Viscoelasticity** — Behaving partly like a spring and partly like thick syrup, so how a tissue responds depends on how fast and how long you load it. Formally: the property of exhibiting both elastic (energy-storing, rate-independent) and viscous (energy-dissipating, rate-dependent) behavior. Manifestations in tendon: [creep](#creep), [stress relaxation](#stress-relaxation), [hysteresis](#hysteresis), and strain-rate-dependent stiffness (tendon is stiffer at higher loading rates).

## vlcd

*Diet Composition & Nutrition*

**VLCD (very-low-calorie diet)** — A medically supervised diet of under 800 calories a day, usually taken as formulated shakes. Formally: a diet providing <800 kcal·day⁻¹, typically as meal replacements formulated for micronutrient completeness. Produces rapid loss but with elevated [LBM](#lbm) loss, larger [adaptive thermogenesis](#adaptive-thermogenesis), and clinical risks including cholelithiasis (gallstones), electrolyte disturbance, and cardiac arrhythmia. The most dangerous moment is **coming off it**: reintroducing food after prolonged severe restriction can trigger **refeeding syndrome** — a rapid fall in blood phosphate and potassium plus thiamine depletion, which can cause heart failure and death. Electrolytes must be monitored medically during refeeding. **Requires medical supervision**; used clinically for pre-surgical weight loss and severe obesity, and inappropriate as a self-directed strategy.

**⚠ Refeeding syndrome.** The most dangerous moment of a VLCD is coming *off* it. Reintroducing food — particularly carbohydrate — drives phosphate, potassium, magnesium and thiamine into cells fast enough to cause severe hypophosphataemia, hypokalaemia and thiamine depletion, and can precipitate cardiac failure, arrhythmia, seizures and death. It is recognised, preventable, and occasionally fatal (Mehanna et al., 2008). Anyone ending a VLCD or any prolonged severe restriction requires **medical electrolyte monitoring and graded reintroduction of food**, not a self-managed return to normal eating.

## volume-equated-effort-equated

*Measurement & Research Terms*

**"Volume-equated" / "effort-equated"** — A study design in which both groups do the same amount of work, or work equally hard, so that only the thing being tested differs. Formally: designs in which conditions are matched for [training volume](#training-volume) and/or [proximity to failure](#proximity-to-failure), isolating the variable actually under test. **The single most important thing to check when reading a training study**: an unequated comparison (e.g. "high frequency beats low frequency" where the high-frequency group also did more sets) tests volume, not the named variable.

## volume-load

*Loading Variables & Prescription*

**Volume load (tonnage)** — Total kilograms lifted: sets times reps times weight. Formally:

> volume load = sets × repetitions × load   (units: kg)

Useful for tracking progression *within a single exercise and rep range*; unreliable for comparing across exercises, rep ranges, or individuals, because it treats 20 easy reps and 5 hard ones as interchangeable if the tonnage matches. See [training volume](#training-volume).

## volume-progression

*Programming & Progression*

**Volume progression** — Progressing by adding sets over a block rather than by adding weight. Formally: a progression scheme in which added [sets](#set) — rather than added [load](#load) — carry the overload across a [mesocycle](#mesocycle), typically escalating from a [MEV](#mev-mav-mrv)-level starting point toward the athlete's [MRV](#mrv), then [deloading](#deload). Should not be combined with simultaneous load progression in the same [microcycle](#microcycle): two overload variables at once makes the cause of any problem unidentifiable.

## water-retention

*Body Composition & Adipose Biology*

**Water retention (masking fat loss)** — Extra body water hiding real fat loss on the scale, sometimes for weeks. Formally: transient increases in total body water that conceal ongoing fat loss in scale weight. Causes: elevated [cortisol](#cortisol) (from dieting stress, sleep loss, or training load), sodium and carbohydrate intake changes (glycogen binds ~3 g water per g), menstrual cycle phase (luteal-phase retention of 0.5–2 kg is normal), post-training inflammation, and travel. **Practical consequence:** fat loss is continuous while scale weight is not. Multi-week "whooshes" — sudden drops after a static period — are water dynamics, not sudden fat loss. Act only on 7-day rolling averages.

## weight-cycling

*Appetite, Behavior & Adherence*

**Weight cycling ("yo-yo dieting")** — Losing weight and regaining it, repeatedly. Formally: repeated cycles of intentional loss followed by regain. **Evidence that cycling independently damages metabolism or worsens subsequent weight-loss capacity is weak and contested** (Mackie et al., 2017, systematic review). Better-supported concerns: cumulative [LBM](#lbm) loss if [resistance training](#resistance-training) is absent during cycles, and the psychological cost of repeated perceived failure. Not a reason to avoid attempting weight loss.

## yap-taz

*Cell & Molecular Biology*

**YAP / TAZ** — Two proteins that move into the cell nucleus when the cell is under mechanical tension, switching on building programs. Formally: mechanoresponsive transcriptional co-activators of the Hippo signaling pathway. Under mechanical tension and stiff-substrate conditions they translocate to the nucleus and drive proliferative and matrix-synthetic gene programs; under low tension they are cytoplasmically sequestered and degraded. Part of the [mechanotransduction](#mechanotransduction) chain in tendon.

## youngs-modulus

*Mechanics & Material Properties*

**Young's modulus (E, elastic modulus)** — A measure of how stiff a *material* is, independent of how much of it there is — steel has a high modulus whether the bar is thick or thin. Formally, the slope of the [stress](#stress)–[strain](#strain) relationship in the linear region:

> E = σ / ε   (units: Pa; tendon ≈ 1–2 GPa)

The correct variable for asking "did the tissue itself change quality?", as opposed to [stiffness](#stiffness), which also changes when the tendon merely gets thicker.

---

# Part V Bibliography

Every source cited here: **105 papers**, each with a DOI you can paste into a search box or a library request form. Alphabetical by first author, so an in-text citation like *(Kharazi et al., 2021)* is found by scanning for **Kharazi**.

**58 are open access** — free to read now. **47 are paywalled**; any university or public library can obtain those through interlibrary loan at no cost, usually in a few days, and authors may legally share their own accepted manuscripts if you email them.

**Two sources predate DOIs.** Keys A, Brožek J, Henschel A, Mickelsen O, Taylor HL. *The Biology of Human Starvation.* University of Minnesota Press; 1950 — the Minnesota Starvation Experiment. Elia M. Organ and tissue contribution to metabolic rate. In: Kinney JM, Tucker HN, eds. *Energy Metabolism: Tissue Determinants and Cellular Corollaries.* Raven Press; 1992 — the origin of the ~13 kcal/kg/day figure for resting muscle.

**How to read a citation here.** A reference is a pointer, not a guarantee. Where a claim rests on a small sample, a short trial, or untrained participants, the text says so at the claim itself — that context matters more than the presence of a reference. *[consensus — no single source]* marks textbook material with no single origin paper. *[UNVERIFIED]* marks claims we could not trace to a source we could read; they are flagged rather than quietly dropped.

---

Alfredson H, Pietilä T, Jonsson P, Lorentzon R. Heavy-Load Eccentric Calf Muscle Training For the Treatment of                     Chronic Achilles Tendinosis. The American Journal of Sports Medicine. 1998;26(3):360-366. doi:10.1177/03635465980260030301 · **open access**

Alpert SS. A limit on the energy transfer rate from the human fat store in hypophagia. Journal of Theoretical Biology. 2005;233(1):1-13. doi:10.1016/j.jtbi.2004.08.029 · *paywalled*

ANTONIO J, GONYEA WJ. Skeletal muscle fiber hyperplasia. Medicine &amp; Science in Sports &amp; Exercise. 1993;25(12):1333???1345. doi:10.1249/00005768-199312000-00004 · *paywalled*

Arampatzis A, Karamanidis K, Albracht K. Adaptational responses of the human Achilles tendon by modulation of the applied cyclic strain magnitude. Journal of Experimental Biology. 2007;210(15):2743-2753. doi:10.1242/jeb.003814 · *paywalled*

Arampatzis A, Peper A, Bierbaum S, Albracht K. Plasticity of human Achilles tendon mechanical and morphological properties in response to cyclic strain. Journal of Biomechanics. 2010;43(16):3073-3079. doi:10.1016/j.jbiomech.2010.08.014 · *paywalled*

AUSSIEKER T, HILKENS L, HOLWERDA AM, FUCHS CJ, HOUBEN LHP, SENDEN JM, et al. Collagen Protein Ingestion during Recovery from Exercise Does Not Increase Muscle Connective Protein Synthesis Rates. Medicine &amp; Science in Sports &amp; Exercise. 2023;55(10):1792-1802. doi:10.1249/MSS.0000000000003214 · **open access**

Bajunaid R, Niu C, Hambly C, Liu Z, Yamada Y, Aleman-Mateo H, et al. Predictive equation derived from 6,497 doubly labelled water measurements enables the detection of erroneous self-reported energy intake. Nature Food. 2025;6(1):58-71. doi:10.1038/s43016-024-01089-5 · **open access**

Beyer R, Kongsgaard M, Hougs Kjær B, Øhlenschlæger T, Kjær M, Magnusson SP. Heavy Slow Resistance Versus Eccentric Training as Treatment for Achilles Tendinopathy. The American Journal of Sports Medicine. 2015;43(7):1704-1711. doi:10.1177/0363546515584760 · *paywalled*

BICKEL CS, CROSS JM, BAMMAN MM. Exercise Dosing to Retain Resistance Training Adaptations in Young and Older Adults. Medicine &amp; Science in Sports &amp; Exercise. 2011;43(7):1177-1187. doi:10.1249/MSS.0b013e318207c15d · *paywalled*

Bohm S, Mersmann F, Tettke M, Kraft M, Arampatzis A. Human Achilles tendon plasticity in response to cyclic strain: effect of rate and duration. Journal of Experimental Biology. 2014;217(22):4010-4017. doi:10.1242/jeb.112268 · *paywalled*

Bohm S, Mersmann F, Arampatzis A. Human tendon adaptation in response to mechanical loading: a systematic review and meta-analysis of exercise intervention studies on healthy adults. Sports Medicine - Open. 2015;1(1). doi:10.1186/s40798-015-0009-9 · **open access**

Byrne NM, Sainsbury A, King NA, Hills AP, Wood RE. Intermittent energy restriction improves weight loss efficiency in obese men: the MATADOR study. International Journal of Obesity. 2017;42(2):129-138. doi:10.1038/ijo.2017.206 · **open access**

Careau V, Halsey LG, Pontzer H, Ainslie PN, Andersen LF, Anderson LJ, et al. Energy compensation and adiposity in humans. Current Biology. 2021;31(20):4659-4666.e2. doi:10.1016/j.cub.2021.08.016 · **open access**

Catenacci VA, Ogden LG, Stuht J, Phelan S, Wing RR, Hill JO, et al. Physical Activity Patterns in the National Weight Control Registry. Obesity. 2008;16(1):153-161. doi:10.1038/oby.2007.6 · **open access**

Chimenti RL, Neville C, Houck J, Cuddeford T, Carreira D, Martin RL. Achilles Pain, Stiffness, and Muscle Power Deficits: Midportion Achilles Tendinopathy Revision – 2024. Journal of Orthopaedic &amp; Sports Physical Therapy. 2024:1-77. doi:10.2519/jospt.2024.13079 · *paywalled*

Clifford C, Challoumas D, Paul L, Syme G, Millar NL. Effectiveness of isometric exercise in the management of tendinopathy: a systematic review and meta-analysis of randomised trials. BMJ Open Sport &amp; Exercise Medicine. 2020;6(1):e000760. doi:10.1136/bmjsem-2020-000760 · **open access**

Coleman M, Burke R, Augustin F, Piñero A, Maldonado J, Fisher JP, et al. Gaining more from doing less? The effects of a one-week deload period during supervised resistance training on muscular adaptations. PeerJ. 2024;12:e16777. doi:10.7717/peerj.16777 · **open access**

Cook JL, Purdam CR. Is tendon pathology a continuum? A pathology model to explain the clinical presentation of load-induced tendinopathy. British Journal of Sports Medicine. 2008;43(6):409-416. doi:10.1136/bjsm.2008.051193 · **open access**

Coombes BK, Bisset L, Brooks P, Khan A, Vicenzino B. Effect of Corticosteroid Injection, Physiotherapy, or Both on Clinical Outcomes in Patients With Unilateral Lateral Epicondylalgia. JAMA. 2013;309(5):461. doi:10.1001/jama.2013.129 · *paywalled*

Damas F, Phillips SM, Libardi CA, Vechin FC, Lixandrão ME, Jannig PR, et al. Resistance training‐induced changes in integrated myofibrillar protein synthesis are related to hypertrophy only after attenuation of muscle damage. The Journal of Physiology. 2016;594(18):5209-5222. doi:10.1113/JP272472 · **open access**

De Boer MD, Maganaris CN, Seynnes OR, Rennie MJ, Narici MV. Time course of muscular, neural and tendinous adaptations to 23 day unilateral lower‐limb suspension in young men. The Journal of Physiology. 2007;583(3):1079-1091. doi:10.1113/jphysiol.2007.135392 · **open access**

de Vos RJ, Weir A, van Schie HTM, Bierma-Zeinstra SMA, Verhaar JAN, Weinans H, et al. Platelet-Rich Plasma Injection for Chronic Achilles Tendinopathy. JAMA. 2010;303(2):144. doi:10.1001/jama.2009.1986 · *paywalled*

Del Vecchio A, Casolo A, Negro F, Scorcelletti M, Bazzucchi I, Enoka R, et al. The increase in muscle force after 4 weeks of strength training is mediated by adaptations in motor unit recruitment and rate coding. The Journal of Physiology. 2019;597(7):1873-1887. doi:10.1113/JP277250 · **open access**

Docking SI, Ooi CC, Connell D. Tendinopathy: Is Imaging Telling Us the Entire Story?. Journal of Orthopaedic &amp; Sports Physical Therapy. 2015;45(11):842-852. doi:10.2519/jospt.2015.5880 · *paywalled*

Drummond MJ, Fry CS, Glynn EL, Dreyer HC, Dhanani S, Timmerman KL, et al. Rapamycin administration in humans blocks the contraction‐induced increase in skeletal muscle protein synthesis. The Journal of Physiology. 2009;587(7):1535-1546. doi:10.1113/jphysiol.2008.163816 · **open access**

Dulloo AG, Jacquet J. Adaptive reduction in basal metabolic rate in response to food deprivation in humans: a role for feedback signals from fat stores. The American Journal of Clinical Nutrition. 1998;68(3):599-606. doi:10.1093/ajcn/68.3.599 · **open access**

Duman E, Müller-Deubert S, Pattappa G, Stratos I, Sieber SA, Clausen-Schaumann H, et al. Fluoroquinolone-Mediated Tendinopathy and Tendon Rupture. Pharmaceuticals. 2025;18(2):184. doi:10.3390/ph18020184 · **open access**

FORBES GB. Body Fat Content Influences the Body Composition Response to Nutrition and Exercise. Annals of the New York Academy of Sciences. 2000;904(1):359-365. doi:10.1111/j.1749-6632.2000.tb06482.x · *paywalled*

Fothergill E, Guo J, Howard L, Kerns JC, Knuth ND, Brychta R, et al. Persistent metabolic adaptation 6 years after “The Biggest Loser” competition. Obesity. 2016;24(8):1612-1619. doi:10.1002/oby.21538 · *paywalled*

Fukashiro S, Komi PV, J�rvinen M, Miyashita M. In vivo achilles tendon loading' during jumping in humans. European Journal of Applied Physiology and Occupational Physiology. 1995;71(5):453-458. doi:10.1007/BF00635880 · *paywalled*

Garthe I, Raastad T, Refsnes PE, Koivisto A, Sundgot-Borgen J. Effect of Two Different Weight-Loss Rates on Body Composition and Strength and Power-Related Performance in Elite Athletes. International Journal of Sport Nutrition and Exercise Metabolism. 2011;21(2):97-104. doi:10.1123/ijsnem.21.2.97 · *paywalled*

Goris AH, Westerterp-Plantenga MS, Westerterp KR. Undereating and underrecording of habitual food intake in obese men: selective underreporting of fat intake. The American Journal of Clinical Nutrition. 2000;71(1):130-134. doi:10.1093/ajcn/71.1.130 · **open access**

Goris AH, Meijer EP, Kester A, Westerterp KR. Use of a triaxial accelerometer to validate reported food intakes. The American Journal of Clinical Nutrition. 2001;73(3):549-553. doi:10.1093/ajcn/73.3.549 · **open access**

Grgic J, Mikulic P, Podnar H, Pedisic Z. Effects of linear and daily undulating periodized resistance training programs on measures of muscle hypertrophy: a systematic review and meta-analysis. PeerJ. 2017;5:e3695. doi:10.7717/peerj.3695 · **open access**

Hall KD, Sacks G, Chandramohan D, Chow CC, Wang YC, Gortmaker SL, et al. Quantification of the effect of energy imbalance on bodyweight. The Lancet. 2011;378(9793):826-837. doi:10.1016/S0140-6736(11)60812-X · **open access**

Hall KD, Ayuketah A, Brychta R, Cai H, Cassimatis T, Chen KY, et al. Ultra-Processed Diets Cause Excess Calorie Intake and Weight Gain: An Inpatient Randomized Controlled Trial of Ad Libitum Food Intake. Cell Metabolism. 2019;30(1):67-77.e3. doi:10.1016/j.cmet.2019.05.008 · **open access**

Halperin I, Malleron T, Har-Nir I, Androulakis-Korakakis P, Wolf M, Fisher J, et al. Accuracy in Predicting Repetitions to Task Failure in Resistance Exercise: A Scoping Review and Exploratory Meta-analysis. Sports Medicine. 2021;52(2):377-390. doi:10.1007/s40279-021-01559-x · **open access**

Heinemeier KM, Schjerling P, Heinemeier J, Magnusson SP, Kjaer M. Lack of tissue renewal in human adult Achilles tendon is revealed by nuclear bomb
                    <sup>14</sup>
                    C. The FASEB Journal. 2013;27(5):2074-2079. doi:10.1096/fj.12-225599 · **open access**

Heinemeier KM, Schjerling P, Øhlenschlæger TF, Eismark C, Olsen J, Kjær M. Carbon‐14 bomb pulse dating shows that tendinopathy is preceded by years of abnormally high collagen turnover. The FASEB Journal. 2018;32(9):4763-4775. doi:10.1096/fj.201701569R · *paywalled*

Henneman E, Somjen G, Carpenter DO. FUNCTIONAL SIGNIFICANCE OF CELL SIZE IN SPINAL MOTONEURONS. Journal of Neurophysiology. 1965;28(3):560-580. doi:10.1152/jn.1965.28.3.560 · *paywalled*

Impellizzeri FM, Tenan MS, Kempton T, Novak A, Coutts AJ. Acute:Chronic Workload Ratio: Conceptual Issues and Fundamental Pitfalls. International Journal of Sports Physiology and Performance. 2020;15(6):907-913. doi:10.1123/ijspp.2019-0864 · *paywalled*

Kalm LM, Semba RD. They Starved So That Others Be Better Fed: Remembering Ancel Keys and the Minnesota Experiment. The Journal of Nutrition. 2005;135(6):1347-1352. doi:10.1093/jn/135.6.1347 · **open access**

Kearney RS, Ji C, Warwick J, Parsons N, Brown J, Harrison P, et al. Effect of Platelet-Rich Plasma Injection vs Sham Injection on Tendon Dysfunction in Patients With Chronic Midportion Achilles Tendinopathy. JAMA. 2021;326(2):137. doi:10.1001/jama.2021.6986 · **open access**

Kharazi M, Bohm S, Theodorakis C, Mersmann F, Arampatzis A. Quantifying mechanical loading and elastic strain energy of the human Achilles tendon during walking and running. Scientific Reports. 2021;11(1). doi:10.1038/s41598-021-84847-w · **open access**

Kongsgaard M, Kovanen V, Aagaard P, Doessing S, Hansen P, Laursen AH, et al. Corticosteroid injections, eccentric decline squat training and heavy slow resistance training in patellar tendinopathy. Scandinavian Journal of Medicine &amp; Science in Sports. 2009;19(6):790-802. doi:10.1111/j.1600-0838.2009.00949.x · **open access**

Kubo K, Akima H, Ushiyama J, Tabata I, Fukuoka H, Kanehisa H, et al. Effects of resistance training during bed rest on the viscoelastic properties of tendon structures in the lower limb. Scandinavian Journal of Medicine &amp; Science in Sports. 2004;14(5):296-302. doi:10.1046/j.1600-0838.2003.00368.x · *paywalled*

Kubo K, Ikebukuro T, Maki A, Yata H, Tsunoda N. Time course of changes in the human Achilles tendon properties and metabolism during training and detraining in vivo. European Journal of Applied Physiology. 2011;112(7):2679-2691. doi:10.1007/s00421-011-2248-x · *paywalled*

Kumagai K, Abe T, Brechue WF, Ryushi T, Takano S, Mizuno M. Sprint performance is related to muscle fascicle  length in male 100-m sprinters. Journal of Applied Physiology. 2000;88(3):811-816. doi:10.1152/jappl.2000.88.3.811 · *paywalled*

Lee SSM, Piazza SJ. Built for speed: musculoskeletal structure and sprinting ability. Journal of Experimental Biology. 2009;212(22):3700-3707. doi:10.1242/jeb.031096 · *paywalled*

Levine JA, Eberhardt NL, Jensen MD. Role of Nonexercise Activity Thermogenesis in Resistance to Fat Gain in Humans. Science. 1999;283(5399):212-214. doi:10.1126/science.283.5399.212 · *paywalled*

Levine JA. Nonexercise activity thermogenesis (NEAT): environment and biology. American Journal of Physiology-Endocrinology and Metabolism. 2004;286(5):E675-E685. doi:10.1152/ajpendo.00562.2003 · *paywalled*

Levine JA, Lanningham-Foster LM, McCrady SK, Krizan AC, Olson LR, Kane PH, et al. Interindividual Variation in Posture Allocation: Possible Role in Human Obesity. Science. 2005;307(5709):584-586. doi:10.1126/science.1106561 · *paywalled*

Levine JA. Nonexercise activity thermogenesis – liberating the life‐force. Journal of Internal Medicine. 2007;262(3):273-287. doi:10.1111/j.1365-2796.2007.01842.x · **open access**

Lichtman SW, Pisarska K, Berman ER, Pestone M, Dowling H, Offenbacher E, et al. Discrepancy between Self-Reported and Actual Caloric Intake and Exercise in Obese Subjects. New England Journal of Medicine. 1992;327(27):1893-1898. doi:10.1056/NEJM199212313272701 · *paywalled*

Lichtwark GA, Wilson AM. <i>In vivo</i> mechanical properties of the human Achilles tendon during one-legged hopping. Journal of Experimental Biology. 2005;208(24):4715-4725. doi:10.1242/jeb.01950 · *paywalled*

Lis DM, Baar K. Effects of Different Vitamin C–Enriched Collagen Derivatives on Collagen Synthesis. International Journal of Sport Nutrition and Exercise Metabolism. 2019;29(5):526-531. doi:10.1123/ijsnem.2018-0385 · *paywalled*

Loucks AB, Thuma JR. Luteinizing Hormone Pulsatility Is Disrupted at a Threshold of Energy Availability in Regularly Menstruating Women. The Journal of Clinical Endocrinology &amp; Metabolism. 2003;88(1):297-311. doi:10.1210/jc.2002-020369 · *paywalled*

Mani-Babu S, Morrissey D, Waugh C, Screen H, Barton C. The Effectiveness of Extracorporeal Shock Wave Therapy in Lower Limb Tendinopathy. The American Journal of Sports Medicine. 2014;43(3):752-761. doi:10.1177/0363546514531911 · *paywalled*

Martin RL, Chimenti R, Cuddeford T, Houck J, Matheson J, McDonough CM, et al. Achilles Pain, Stiffness, and Muscle Power Deficits: Midportion Achilles Tendinopathy Revision 2018. Journal of Orthopaedic &amp; Sports Physical Therapy. 2018;48(5):A1-A38. doi:10.2519/jospt.2018.0302 · **open access**

McCarthy JJ, Mula J, Miyazaki M, Erfani R, Garrison K, Farooqui AB, et al. Effective fiber hypertrophy in satellite cell-depleted skeletal muscle. Development. 2011;138(17):3657-3666. doi:10.1242/dev.068858 · **open access**

Meerman R, Brown AJ. When somebody loses weight, where does the fat go?. BMJ. 2014;349(dec16 13):g7257-g7257. doi:10.1136/bmj.g7257 · **open access**

Mehanna HM, Moledina J, Travis J. Refeeding syndrome: what it is, and how to prevent and treat it. BMJ. 2008;336(7659):1495-1498. doi:10.1136/bmj.a301 · *paywalled*

Mellor R, Bennell K, Grimaldi A, Nicolson P, Kasza J, Hodges P, et al. Education plus exercise versus corticosteroid injection use versus a wait and see approach on global outcome and pain from gluteal tendinopathy: prospective, single blinded, randomised clinical trial. BMJ. 2018:k1662. doi:10.1136/bmj.k1662 · **open access**

Mersmann F, Bohm S, Arampatzis A. Imbalances in the Development of Muscle and Tendon as Risk Factor for Tendinopathies in Youth Athletes: A Review of Current Evidence and Concepts of Prevention. Frontiers in Physiology. 2017;8. doi:10.3389/fphys.2017.00987 · **open access**

Mersmann F, Domroes T, Tsai M, Pentidis N, Schroll A, Bohm S, et al. Longitudinal Evidence for High-Level Patellar Tendon Strain as a Risk Factor for Tendinopathy in Adolescent Athletes. Sports Medicine - Open. 2023;9(1). doi:10.1186/s40798-023-00627-y · **open access**

Millar NL, Silbernagel KG, Thorborg K, Kirwan PD, Galatz LM, Abrams GD, et al. Tendinopathy. Nature Reviews Disease Primers. 2021;7(1). doi:10.1038/s41572-020-00234-1 · **open access**

Miller BF, Olesen JL, Hansen M, Døssing S, Crameri RM, Welling RJ, et al. Coordinated collagen and muscle protein synthesis in human patella tendon and quadriceps muscle after exercise. The Journal of Physiology. 2005;567(3):1021-1033. doi:10.1113/jphysiol.2005.093690 · **open access**

Morton RW, Murphy KT, McKellar SR, Schoenfeld BJ, Henselmans M, Helms E, et al. A systematic review, meta-analysis and meta-regression of the effect of protein supplementation on resistance training-induced gains in muscle mass and strength in healthy adults. British Journal of Sports Medicine. 2017;52(6):376-384. doi:10.1136/bjsports-2017-097608 · **open access**

Mountjoy M, Ackerman KE, Bailey DM, Burke LM, Constantini N, Hackney AC, et al. 2023 International Olympic Committee’s (IOC) consensus statement on Relative Energy Deficiency in Sport (REDs). British Journal of Sports Medicine. 2023;57(17):1073-1098. doi:10.1136/bjsports-2023-106994 · **open access**

Murphy C, Koehler K. Energy deficiency impairs resistance training gains in lean mass but not strength: A meta‐analysis and meta‐regression. Scandinavian Journal of Medicine &amp; Science in Sports. 2021;32(1):125-137. doi:10.1111/sms.14075 · **open access**

Myhrvold SB, Brouwer EF, Andresen TKM, Rydevik K, Amundsen M, Grün W, et al. Nonoperative or Surgical Treatment of Acute Achilles’ Tendon Rupture. New England Journal of Medicine. 2022;386(15):1409-1420. doi:10.1056/NEJMoa2108447 · **open access**

Nedeltcheva AV, Kilkus JM, Imperial J, Schoeller DA, Penev PD. Insufficient Sleep Undermines Dietary Efforts to Reduce Adiposity. Annals of Internal Medicine. 2010;153(7):435-441. doi:10.7326/0003-4819-153-7-201010050-00006 · **open access**

Ochen Y, Beks RB, van Heijl M, Hietbrink F, Leenen LPH, van der Velde D, et al. Operative treatment versus nonoperative treatment of Achilles tendon ruptures: systematic review and meta-analysis. BMJ. 2019:k5120. doi:10.1136/bmj.k5120 · **open access**

Pallarés JG, Hernández‐Belmonte A, Martínez‐Cava A, Vetrovsky T, Steffl M, Courel‐Ibáñez J. Effects of range of motion on resistance training adaptations: A systematic review and meta‐analysis. Scandinavian Journal of Medicine &amp; Science in Sports. 2021;31(10):1866-1881. doi:10.1111/sms.14006 · **open access**

Pareja‐Blanco F, Rodríguez‐Rosell D, Sánchez‐Medina L, Sanchis‐Moysi J, Dorado C, Mora‐Custodio R, et al. Effects of velocity loss during resistance training on athletic performance, strength gains and muscle adaptations. Scandinavian Journal of Medicine &amp; Science in Sports. 2016;27(7):724-735. doi:10.1111/sms.12678 · **open access**

Pelland JC, Remmert JF, Robinson ZP, Hinson SR, Zourdos MC. The Resistance Training Dose Response: Meta-Regressions Exploring the Effects of Weekly Volume and Frequency on Muscle Hypertrophy and Strength Gains. Sports Medicine. 2026;56(2):481-505. doi:10.1007/s40279-025-02344-w · *paywalled*

Ravussin E, Redman LM, Rochon J, Das SK, Fontana L, Kraus WE, et al. A 2-Year Randomized Controlled Trial of Human Caloric Restriction: Feasibility and Effects on Predictors of Health Span and Longevity. The Journals of Gerontology Series A: Biological Sciences and Medical Sciences. 2015;70(9):1097-1104. doi:10.1093/gerona/glv057 · **open access**

Refalo MC, Helms ER, Trexler ET, Hamilton DL, Fyfe JJ. Influence of Resistance Training Proximity-to-Failure on Skeletal Muscle Hypertrophy: A Systematic Review with Meta-analysis. Sports Medicine. 2022;53(3):649-665. doi:10.1007/s40279-022-01784-y · **open access**

Rio E, Kidgell D, Purdam C, Gaida J, Moseley GL, Pearce AJ, et al. Isometric exercise induces analgesia and reduces inhibition in patellar tendinopathy. British Journal of Sports Medicine. 2015;49(19):1277-1283. doi:10.1136/bjsports-2014-094386 · **open access**

Roberts BM, Nuckols G, Krieger JW. Sex Differences in Resistance Training: A Systematic Review and Meta-Analysis. Journal of Strength and Conditioning Research. 2020;34(5):1448-1460. doi:10.1519/JSC.0000000000003521 · *paywalled*

Roberts MD, McCarthy JJ, Hornberger TA, Phillips SM, Mackey AL, Nader GA, et al. Mechanisms of mechanical overload-induced skeletal muscle hypertrophy: current understanding and future directions. Physiological Reviews. 2023;103(4):2679-2757. doi:10.1152/physrev.00039.2022 · **open access**

Robinson ZP, Pelland JC, Remmert JF, Refalo MC, Jukic I, Steele J, et al. Exploring the Dose–Response Relationship Between Estimated Resistance Training Proximity to Failure, Strength Gain, and Muscle Hypertrophy: A Series of Meta-Regressions. Sports Medicine. 2024;54(9):2209-2231. doi:10.1007/s40279-024-02069-2 · *paywalled*

Schoeller DA, Ravussin E, Schutz Y, Acheson KJ, Baertschi P, Jequier E. Energy expenditure by doubly labeled water: validation in humans and proposed calculation. American Journal of Physiology-Regulatory, Integrative and Comparative Physiology. 1986;250(5):R823-R830. doi:10.1152/ajpregu.1986.250.5.R823 · *paywalled*

Schoeller DA. Measurement of Energy Expenditure in Free-Living Humans by Using Doubly Labeled Water. The Journal of Nutrition. 1988;118(11):1278-1289. doi:10.1093/jn/118.11.1278 · *paywalled*

Schoenfeld BJ, Ogborn DI, Krieger JW. Effect of Repetition Duration During Resistance Training on Muscle Hypertrophy: A Systematic Review and Meta-Analysis. Sports Medicine. 2015;45(4):577-585. doi:10.1007/s40279-015-0304-0 · *paywalled*

Schoenfeld BJ, Pope ZK, Benik FM, Hester GM, Sellers J, Nooner JL, et al. Longer Interset Rest Periods Enhance Muscle Strength and Hypertrophy in Resistance-Trained Men. Journal of Strength and Conditioning Research. 2016;30(7):1805-1812. doi:10.1519/JSC.0000000000001272 · *paywalled*

Schoenfeld BJ, Grgic J, Ogborn D, Krieger JW. Strength and Hypertrophy Adaptations Between Low- vs. High-Load Resistance Training: A Systematic Review and Meta-analysis. Journal of Strength and Conditioning Research. 2017;31(12):3508-3523. doi:10.1519/JSC.0000000000002200 · *paywalled*

Schoenfeld BJ, Grgic J, Krieger J. How many times per week should a muscle be trained to maximize muscle hypertrophy? A systematic review and meta-analysis of studies examining the effects of resistance training frequency. Journal of Sports Sciences. 2018;37(11):1286-1295. doi:10.1080/02640414.2018.1555906 · *paywalled*

Seaborne RA, Strauss J, Cocks M, Shepherd S, O’Brien TD, van Someren KA, et al. Human Skeletal Muscle Possesses an Epigenetic Memory of Hypertrophy. Scientific Reports. 2018;8(1). doi:10.1038/s41598-018-20287-3 · **open access**

Seynnes OR, de Boer M, Narici MV. Early skeletal muscle hypertrophy and architectural changes in response to high-intensity resistance training. Journal of Applied Physiology. 2007;102(1):368-373. doi:10.1152/japplphysiol.00789.2006 · *paywalled*

Shaw G, Lee-Barthel A, Ross ML, Wang B, Baar K. Vitamin C–enriched gelatin supplementation before intermittent activity augments collagen synthesis. The American Journal of Clinical Nutrition. 2017;105(1):136-143. doi:10.3945/ajcn.116.138594 · **open access**

Silbernagel KG, Thomeé R, Eriksson BI, Karlsson J. Continued Sports Activity, Using a Pain-Monitoring Model, during Rehabilitation in Patients with Achilles Tendinopathy. The American Journal of Sports Medicine. 2007;35(6):897-906. doi:10.1177/0363546506298279 · *paywalled*

Snijders T, Aussieker T, Holwerda A, Parise G, van Loon LJC, Verdijk LB. The concept of skeletal muscle memory: Evidence from animal and human studies. Acta Physiologica. 2020;229(3). doi:10.1111/apha.13465 · **open access**

Sumithran P, Prendergast LA, Delbridge E, Purcell K, Shulkes A, Kriketos A, et al. Long-Term Persistence of Hormonal Adaptations to Weight Loss. New England Journal of Medicine. 2011;365(17):1597-1604. doi:10.1056/NEJMoa1105816 · *paywalled*

van der Vlist AC, Winters M, Weir A, Ardern CL, Welton NJ, Caldwell DM, et al. Which treatment is most effective for patients with Achilles tendinopathy? A living systematic review with network meta-analysis of 29 randomised controlled trials. British Journal of Sports Medicine. 2020;55(5):249-256. doi:10.1136/bjsports-2019-101872 · **open access**

Wackerhage H, Schoenfeld BJ, Hamilton DL, Lehti M, Hulmi JJ. Stimuli and sensors that initiate skeletal muscle hypertrophy following resistance exercise. Journal of Applied Physiology. 2019;126(1):30-43. doi:10.1152/japplphysiol.00685.2018 · **open access**

Wang Z, Ying Z, Bosy-Westphal A, Zhang J, Schautz B, Later W, et al. Specific metabolic rates of major organs and tissues across adulthood: evaluation by mechanistic model of resting energy expenditure. The American Journal of Clinical Nutrition. 2010;92(6):1369-1377. doi:10.3945/ajcn.2010.29885 · **open access**

Westerterp KR. Diet induced thermogenesis. Nutrition &amp; Metabolism. 2004;1(1). doi:10.1186/1743-7075-1-5 · **open access**

WIESINGER H, KÖSTERS A, MÜLLER E, SEYNNES OR. Effects of Increased Loading on In Vivo Tendon Properties. Medicine &amp; Science in Sports &amp; Exercise. 2015;47(9):1885-1895. doi:10.1249/MSS.0000000000000603 · **open access**

Wing RR, Hill JO. S<scp>UCCESSFUL</scp> W<scp>EIGHT</scp> L<scp>OSS</scp> M<scp>AINTENANCE</scp>. Annual Review of Nutrition. 2001;21(1):323-341. doi:10.1146/annurev.nutr.21.1.323 · *paywalled*

WISHNOFSKY M. Caloric Equivalents of Gained or Lost Weight. The American Journal of Clinical Nutrition. 1958;6(5):542-546. doi:10.1093/ajcn/6.5.542 · *paywalled*

Wolf M, Androulakis Korakakis P, Piñero A, Mohan AE, Hermann T, Augustin F, et al. Lengthened partial repetitions elicit similar muscular adaptations as full range of motion repetitions during resistance training in trained individuals. PeerJ. 2025;13:e18904. doi:10.7717/peerj.18904 · **open access**

Wolf M, Korakakis PA, Roberts MD, Plotkin DL, Franchi MV, Contreras B, et al. Does longer-muscle length resistance training cause greater longitudinal growth in humans? A systematic review. Sports Medicine and Health Science. 2026;8(1):34-42. doi:10.1016/j.smhs.2025.03.001 · **open access**

Wren TA, Yerby SA, Beaupré GS, Carter DR. Mechanical properties of the human achilles tendon. Clinical Biomechanics. 2001;16(3):245-251. doi:10.1016/S0268-0033(00)00089-9 · *paywalled*

[author unlisted]. Dietary Reference Intakes for Energy. ?. 2023. doi:10.17226/26818 · *paywalled*
