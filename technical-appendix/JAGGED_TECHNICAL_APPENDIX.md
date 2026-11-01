# Technical Appendix: The Jagged Boundary

*Supplement to the Stage 1 proposal, "The Jagged Boundary," submitted to the Organization Science Special Issue: AI-Enabled Frontiers in Organizational Science. This appendix gives the complete Sorites-gradient item sequence and its design matrix, the counterbalancing scheme, the agent interviewer's specification and instruction set, worked interviewer transcripts, the response schema, operational definitions of every measure, pre-registered hypotheses with the outcomes that would count against them, the norm-dynamics model, a synthetic-data demonstration of the analysis pipeline, the sampling frame, and the governance protocol. It supersedes the compressed descriptions in the proposal itself, which reference this document.*

**Contents**

0. Reading guide, glossary, and how this appendix was produced
1. The four regimes
2. The complete item sequence: design matrix (2.1), the sequence as administered (2.2), counterbalancing and probes (2.3), calibration of the increments (2.4)
3. The agent interviewer
4. Worked transcripts
5. Response schema and measures
6. Pre-registered hypotheses, and what would count against them
7. Norm-dynamics model
8. Synthetic-data demonstration of the analysis pipeline
9. Validity design for the risks named in the proposal
10. Sampling frame and study design
11. Governance, consent and ethics
12. Where this submission sits on its own gradient
13. Status of components, and where each commitment of the proposal is met

References · Annex A: response schema · Annex B: item files and check outputs · Annex C: instruction sets · Annex D: stand-in transcripts and audits · Annex E: Project Lakatos Tables 1 to 4

---

## 0. Reading guide, glossary, and how this appendix was produced

The instrument has three parts, matching the proposal's Section 2: the **Sorites gradient** (37 scenario positions in instrument version 0.2: the proposal's items 1 to 31, with the critical pair split as 27a and 27b, plus five interpolated items 15b, 17b, 19b, 21b and 28b added after the calibration check of Section 2.4), the **three-layer Epinet elicitation** (at 11 anchor items), and the **agent interviewer** (for a subset of participants). Every count in this appendix uses those numbers.

| Term | Meaning in this appendix |
|---|---|
| Item | One scenario, completing the fixed stem "In a paper you will submit under your own name as sole or lead author, is it acceptable to...". Identified by its number (1 to 31, with 27a/27b and the interpolations 15b, 17b, 19b, 21b, 28b) |
| Position | An item's place in the designed sequence (1 to 37). Item numbers keep the proposal's numbering, so that every item shown in the proposal keeps its number; interpolated items carry a letter |
| Regime | One of the four bands of the proposal's Section 2: R1 conventional non-AI tools, R2 LLM as sub-authorial aid, R3 LLM as weakly constrained generator, R4 a researcher's own configured agent |
| Dimension | One of five ordinal codes on which every item is scored, higher meaning more machine agency: T tool, C component of the paper, G generative role, S scope, H human role (Section 2.1) |
| Single-increase rule | The design rule for adjacent items: from one item to the next, at most one dimension increases. Others stay the same or decrease |
| Dominance | Item *j* dominates item *i* if *j* is coded at least as high as *i* on every dimension and higher on at least one. A respondent who accepts *j* but rejects *i* commits a **dominance violation** |
| Anchor item | One of the 11 items at which the peer-belief layers and the disclosure question are asked |
| First-, second-, third-order layer | Own judgment; belief about the fraction of the field that would accept; belief about the fraction of the field that believes researchers like oneself would accept (Section 5.2) |
| Break-point | The first position in the designed sequence that the participant rejects |
| Stopping heuristic | The principle a participant uses to decide where to halt, as coded from the interview (Section 3.5) |
| Instrument version | v0.1 (32 positions) was used for the stand-in interviews of Section 4; v0.2 (37 positions) is the version proposed for the pilot run of the study. `instrument/items_v0.1.json` and `instrument/items.json` hold the two |
| Defeater | Following Pollock (1987): a consideration that, if accepted, undermines a reason. *Rebutting* defeaters support the opposite conclusion; *undercutting* defeaters attack the link between the reason and its conclusion |
| Reflection-only control | An interview arm in which the agent elicits reasons but presents no defeaters, so that change caused by defeaters can be separated from change caused by reflection alone |
| Stage 1; the study; the pilot run | Stage 1 is the special issue's proposal stage, at which this appendix is submitted; the special issue's call for papers names two later stages, development (Stage 2) and finalization (Stage 3). *The study* is the research proposed in the proposal's Section 5, and *the pilot run* is its first, small administration, before registration (Section 10.4). The appendix describes the study's steps in these terms and does not tie them to the special issue's stages |

**How this appendix was produced.** This appendix was drafted, and its agents operated, by Claude (Anthropic) working under the authors' direction. As of 30 October 2026, no administration with human participants has taken place. The item sequence (Section 2) and the instruction sets (Section 3) were drafted for this appendix. Section 4 contains interviewer runs in which separate Claude instances stand in for participants, each labelled as such; the authors' own interviews take place in the pilot run (Section 4.6). Section 2.4 reports an increment check in which separate Claude instances acted as raters. Section 8 runs the analysis on synthetic respondents generated by a program. Section 12 states where the production of this appendix falls on the instrument's own gradient. Nothing in this appendix reports a human response. Each section states which of its components exist and which are still to be built (summarized in Section 13).

**Repository.** Every file this appendix names by path, in `instrument/`, `checks/`, `pipeline/`, `schema/`, `instruction-sets/` and `runs/`, is in the accompanying repository, which is the research artifact the call for papers asks for: **https://github.com/appendix-repo/jagged-boundary**. Its README lists the commands that regenerate every check output in Annex B; the code needs Python 3 with NumPy and SciPy and calls no AI model. The repository contains no participant data, because none exist.

---

## 1. The four regimes

The proposal's Section 2 names the four regimes, and its Section 3 shows items from each. The full sets, as they appear in the sequence (item numbers in brackets; interpolated items, added so that each step is small, are listed in Section 2):

**R1 Conventional non-AI tools** (items 1 to 7): a word processor's spelling checker [1] and grammar checker [2]; bibliographic software for reference formatting [3] and verification [4]; MATLAB for generating figures [5] and running simulations [6]; statistical packages for the analysis itself [7].

**R2 LLM as sub-authorial aid** (items 8 to 17): an LLM to check analysis code [8], flag errors [9], correct spelling and grammar [10]; to suggest wording for a phrase [11] or sentence [12]; to redraft a sentence [13] or paragraph [14, 15]; to turn the researcher's notes into prose [15b]; to compose a paragraph [16] or a section [17, 17b] from the researcher's own notes or outline. The regime's boundary is that the content is the researcher's: the LLM corrects, words, rewrites or composes from a specification the researcher wrote.

**R3 LLM as weakly constrained generator** (items 18 to 23): an LLM asked, with minimal constraint, to produce the introduction [18], the literature review [19], hypotheses [19b, 20], the theoretical argument [21, 21b, 22], or both theory and hypotheses [23]. The boundary with R2 is that the specification no longer fixes the content.

**R4 A researcher's own configured agent** (items 24 to 31): an agent the researcher has configured to build the theory or model [24]; to specify tests [25]; to produce the data-analysis section [26]; to check theorem proofs [27a]; to generate theorem proofs [27b]; to specify extensions [28]; to develop the theory from the researcher's mechanism [28b] or from the phenomenon alone [29]; to write the entire paper [30, 31].

The regimes order the sequence, but the sequence is not ordered by regime alone. Within each regime the items rise in authorial weight, and at each regime boundary the sequence drops back to a lower component with the more capable tool (for example, from a statistical package running the analyses [7] to an LLM checking analysis code [8]). Section 2.1 makes this structure explicit.

---

## 2. The complete item sequence

### 2.1 The design matrix

The proposal's design claim is that each adjacent pair "differs by at most one coded increment," and that each such step is small. The first part can only be checked once it is said along which dimension each step moves. The items vary on five dimensions, each coded ordinally, with higher meaning more machine agency:

| Dim | Name | Levels |
|---|---|---|
| T | Tool | 0 conventional software · 1 general-purpose LLM · 2 agent the researcher configured |
| C | Component of the paper | 0 orthography · 1 apparatus (references, figures) · 2 computation (analyses, simulations, code) · 3 wording · 4 exposition of the argument · 5 literature review · 6 derivation and empirical design (hypotheses, tests, proofs, analysis section) · 7 theory |
| G | Generative role | 0 checks or executes what the researcher specified · 1 suggests options the researcher chooses among · 2 rewrites the researcher's own content · 3 generates content to the researcher's detailed specification · 4 generates content from minimal specification |
| S | Scope | 0 a word, phrase or single item · 1 a sentence · 2 a paragraph · 3 a section · 4 several sections · 5 the whole paper |
| H | Human role | 0 the researcher vets, revises or corrects the output · 1 the researcher approves it without revision |

The ordering of C is the least obvious and is itself an empirical claim: it places apparatus and computation below wording, on the view that a citation format or a regression run carries less of the author's voice than the choice of a word. The scalability analysis (Section 5.2) tests whether respondents' acceptance follows this ordering.

**The design rule.** From each item to the next, at most one dimension increases. The others stay the same or decrease. A step that decreases some dimensions can only make the later item easier to accept on those dimensions, so the single increase is the whole of what the step adds.

**The matrix.**

| Pos | Item | Regime | T | C | G | S | H | Step from previous | Anchor |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1 | R1 | 0 | 0 | 1 | 0 | 0 | start |  |
| 2 | 2 | R1 | 0 | 0 | 1 | 1 | 0 | S+1 | ✓ |
| 3 | 3 | R1 | 0 | 1 | 0 | 0 | 0 | C+1 (G−1, S−1) |  |
| 4 | 4 | R1 | 0 | 1 | 0 | 0 | 0 | parallel |  |
| 5 | 5 | R1 | 0 | 1 | 0 | 0 | 0 | parallel |  |
| 6 | 6 | R1 | 0 | 2 | 0 | 0 | 0 | C+1 |  |
| 7 | 7 | R1 | 0 | 2 | 0 | 0 | 0 | parallel | ✓ |
| 8 | 8 | R2 | 1 | 2 | 0 | 0 | 0 | T+1 |  |
| 9 | 9 | R2 | 1 | 0 | 0 | 1 | 0 | S+1 (C−2) |  |
| 10 | 10 | R2 | 1 | 0 | 1 | 1 | 0 | G+1 | ✓ |
| 11 | 11 | R2 | 1 | 3 | 1 | 0 | 0 | **C+3** (S−1) |  |
| 12 | 12 | R2 | 1 | 3 | 1 | 1 | 0 | S+1 |  |
| 13 | 13 | R2 | 1 | 3 | 2 | 1 | 0 | G+1 |  |
| 14 | 14 | R2 | 1 | 3 | 2 | 2 | 0 | S+1 | ✓ |
| 15 | 15 | R2 | 1 | 4 | 2 | 2 | 0 | C+1 |  |
| 16 | *15b* | R2 | 1 | 4 | 2 | 2 | 0 | parallel |  |
| 17 | 16 | R2 | 1 | 4 | 3 | 2 | 0 | G+1 |  |
| 18 | 17 | R2 | 1 | 4 | 3 | 3 | 0 | S+1 | ✓ |
| 19 | *17b* | R2 | 1 | 4 | 3 | 3 | 0 | parallel |  |
| 20 | 18 | R3 | 1 | 4 | 4 | 3 | 0 | G+1 |  |
| 21 | 19 | R3 | 1 | 5 | 4 | 3 | 0 | C+1 | ✓ |
| 22 | *19b* | R3 | 1 | 6 | 1 | 3 | 0 | C+1 (G−3) |  |
| 23 | 20 | R3 | 1 | 6 | 3 | 3 | 0 | **G+2** |  |
| 24 | 21 | R3 | 1 | 7 | 3 | 3 | 0 | C+1 |  |
| 25 | *21b* | R3 | 1 | 7 | 3 | 3 | 0 | parallel |  |
| 26 | 22 | R3 | 1 | 7 | 4 | 3 | 0 | G+1 | ✓ |
| 27 | 23 | R3 | 1 | 7 | 4 | 4 | 0 | S+1 |  |
| 28 | 24 | R4 | 2 | 7 | 3 | 3 | 0 | T+1 (G−1, S−1) | ✓ |
| 29 | 25 | R4 | 2 | 6 | 3 | 3 | 0 | descending (C−1) |  |
| 30 | 26 | R4 | 2 | 6 | 3 | 3 | 0 | parallel |  |
| 31 | 27a | R4 | 2 | 6 | 0 | 3 | 0 | descending (G−3) | ✓ |
| 32 | 27b | R4 | 2 | 6 | 3 | 3 | 0 | **G+3** | ✓ |
| 33 | 28 | R4 | 2 | 7 | 3 | 3 | 0 | C+1 |  |
| 34 | *28b* | R4 | 2 | 7 | 3 | 3 | 0 | parallel |  |
| 35 | 29 | R4 | 2 | 7 | 4 | 3 | 0 | G+1 |  |
| 36 | 30 | R4 | 2 | 7 | 4 | 5 | 0 | **S+2** |  |
| 37 | 31 | R4 | 2 | 7 | 4 | 5 | 1 | H+1 | ✓ |

*Italic item numbers: interpolations added in v0.2 (Section 2.4).*

**What the matrix shows** (computed by `checks/chk_01_adjacency.py`; output in Annex B):

- Of the 36 adjacent steps, **22** raise one dimension by one level, **4** raise one dimension by more than one level, **10** raise nothing (parallel or descending), and **none** raise two dimensions at once. The design rule holds throughout.
- The four larger steps are named, not hidden. **19b→20** (G+2) moves from the model suggesting candidate hypotheses to deriving them; it is the second half of the split of the old 19→20 step (Section 2.4). **10→11** (C+3) moves from correcting grammar to suggesting wording. The three-level jump is an artifact of placing apparatus and computation between orthography and wording on C; nothing about apparatus or computation is added at this step. **29→30** (S+2) moves from the agent developing the theory to writing the whole paper from the same brief, which is a jump in scope. **27a→27b** (G+3), from checking proofs to generating them, is the proposal's critical pair. It is the one step where the design deliberately places a candidate principled line, verification against production, so that respondents who halt there can be asked to name the property that flips (proposal Section 3).
- The ten steps that raise nothing (3→4, 4→5, 6→7, 15→15b, 17→17b, 21→21b, 24→25, 25→26, 26→27a, 28→28b) serve as consistency checks. Four of them (15→15b, 17→17b, 21→21b, 28→28b) are the v0.2 interpolations, which change how detailed the researcher's specification is within one level of G; Section 2.4 shows that raters do not treat these steps as negligible, which is a finding about the coarseness of G. A respondent who accepts one item of a parallel pair and rejects the other, with identical codes, has said something the coding does not capture. That is either a respondent inconsistency or a defect in the coding, and the probes (Section 2.3) and interviews tell the two apart.
- 558 of the 666 item pairs are ordered by dominance (v0.1: 415 of 496). This is what makes dominance violations (Section 5.2) a measure of incoherence that does not depend on presentation order.

**Why the sequence is not simply monotone.** A chain in which every step raised one dimension and lowered none would need as many level-increments as steps. From the first item to the last there are only 18 such increments across the five dimensions, against 36 steps. More fundamentally, the proposal's regimes revisit low components with more capable tools: the LLM corrects spelling after the statistical package has run the analyses. The sequence therefore descends at regime boundaries and rises within regimes. This is why the analysis uses dominance, not sequence position, to define incoherence, and treats the break-point as a description of where a respondent halts, not as proof of a threshold.

### 2.2 The sequence as administered

Each item completes the fixed stem: ***"In a paper you will submit under your own name as sole or lead author, is it acceptable to..."***

Every item carries the binary judgment and the confidence tag:

> **Your judgment:** ☐ OK ☐ Not OK
> **How settled is this?** ☐ Firmly ☐ I could be argued out of it

The 11 **anchor items** (2, 7, 10, 14, 17, 19, 22, 24, 27a, 27b, 31; marked ⚓ below) also carry the peer-belief layers and the disclosure question. Their wording varies by split-sample version, as described in Section 9.3. In version A, the default, it reads:

> **Of researchers in your field, what fraction would answer "OK"?**
> ▢ 0–19% ▢ 20–39% ▢ 40–59% ▢ 60–79% ▢ 80–100%
>
> **Of researchers in your field, what fraction do you think believe that researchers like you (your subfield and career stage) would answer "OK"?**
> ▢ 0–19% ▢ 20–39% ▢ 40–59% ▢ 60–79% ▢ 80–100%
>
> **If you did this, would you disclose it in the paper?**
> ☐ Yes ☐ No ☐ I would not do this

The third-order question names "researchers like you" because an individual respondent's peers hold no beliefs about that respondent in particular. The question is about the reputation of the respondent's group, which is what a respondent fears or relies on when deciding whether to disclose. The bins are half-open (0–19%, 20–39%, and so on), so that no answer falls on a boundary between two bins.

**R1 Conventional non-AI tools**

1. ...use your word processor's spell-checker to correct the spelling?
2. ⚓ ...use your word processor's grammar checker to correct grammar and punctuation, accepting or rejecting each suggestion?
3. ...use reference-management software (e.g., Zotero, EndNote) to format the citations and reference list in the journal's style?
4. ...use reference-management software to verify the details of your references (authors, years, pages) against bibliographic databases?
5. ...use MATLAB (or similar software) to generate the paper's figures from data or simulation output you produced?
6. ...use MATLAB (or similar software) to run simulations of a model you specified, and plot the results?
7. ⚓ ...use a statistical package (e.g., R, Stata) to run the analyses reported in the paper?

**R2 LLM as sub-authorial aid**

8. ...use a large language model to check the code for your analyses for errors, which you then fix yourself?
9. ...use a large language model to flag spelling and grammatical errors in your draft, which you then correct yourself?
10. ⚓ ...use a large language model to correct the spelling and grammar of your draft?
11. ...use a large language model to suggest alternative wordings for a phrase, from which you choose?
12. ...use a large language model to suggest alternative wordings for a sentence, from which you choose?
13. ...use a large language model to redraft a sentence you wrote, keeping its content?
14. ⚓ ...use a large language model to redraft a paragraph you wrote, for clarity, keeping the content?
15. ...use a large language model to redraft a paragraph you wrote so that its argument is clearer, reordering and restating your points but adding none?
15b. ...use a large language model to turn your rough draft of a paragraph (your points in note form, in your order) into finished prose?
16. ...use a large language model to compose a paragraph from your notes, which list each point it must make?
17. ⚓ ...use a large language model to compose a section (e.g., the introduction) from your detailed outline of it?
17b. ...use a large language model to compose the introduction from a short outline (a few bullet points stating the gap, the argument and the findings), then edit the result?

**R3 LLM as weakly constrained generator**

18. ...prompt a large language model to write the introduction from a brief description of the paper's question and findings, leaving the framing of the contribution to the model, then edit the result? *(v0.2 wording; Section 4.5)*
19. ⚓ ...prompt a large language model to write the literature review, then edit the result?
19b. ...prompt a large language model to suggest hypotheses that might follow from a theoretical argument you wrote, from which you choose and which you then refine?
20. ...prompt a large language model to derive the hypotheses that follow from a theoretical argument you wrote, which you then refine?
21. ...prompt a large language model to draft the paper's theoretical argument from your detailed outline of it, which you then refine?
21b. ...prompt a large language model to draft the paper's theoretical argument from a one-paragraph statement of your central idea, which you then refine?
22. ⚓ ...prompt a large language model to generate the paper's central theoretical argument, which you then refine?
23. ...prompt a large language model to generate both the central theoretical argument and the hypotheses, which you then refine?

**R4 A researcher's own configured agent**

*(A configured agent is described to participants, once, before item 24: "an AI agent you have set up yourself, with your own instructions, tools and materials, to work on your research.")*

24. ⚓ ...have an agent you configured build the formal model of your theory, which you then refine?
25. ...have an agent you configured specify the tests of your hypotheses (measures, research design, estimation strategy), which you then refine?
26. ...have an agent you configured produce the data-analysis section (run the analyses and write up the results) from your data and hypotheses, which you then check?
27a. ⚓ ...have an agent you configured check the proofs of theorems you stated and proved?
27b. ⚓ ...have that agent generate the proofs of theorems you stated?
28. ...have an agent you configured specify extensions of your theory (new propositions, boundary conditions), which you then refine?
28b. ...have an agent you configured develop the theory from your statement of its core mechanism, which you then refine?
29. ...have an agent you configured develop the theory itself from a brief statement of the phenomenon, which you then refine?
30. ...have an agent you configured write the entire paper (theory, analysis, and prose) from a brief statement of the question, which you then revise substantially before submitting?
31. ⚓ ...have an agent you configured write the entire paper (theory, analysis, and prose), which you then approve and submit under your name?

Items 7, 14, 19, 22, 27a/b and 31 are the six shown in the proposal's Section 3, worded as they are there. The machine-readable sequence is `instrument/items.json`, generated by `instrument/build_items.py`.

**Respondent burden.** At about 12 seconds per item for the judgment and confidence tag, 25 seconds per anchor for the three added questions, 10 seconds per probe, and 2 minutes for consent and stratum questions, the traversal takes about 15 minutes. These estimates are to be checked in the pilot run. The interview, for those selected, takes 20 to 30 minutes more.

### 2.3 Counterbalancing and non-adjacent probes

The proposal's mitigation for manufactured incoherence is to "randomize entry points and traversal direction, include non-adjacent probes, and validate that detected break-points are stable across orderings." Concretely:

**Order conditions** (between participants, allocated at random with equal probability within each stratum):

| Code | Order | Purpose |
|---|---|---|
| F | Forward, positions 1 to 37 | The Sorites march as the proposal describes it |
| R | Reverse, 37 to 1 (27b before 27a) | Tests for hysteresis. In forced-march Sorites tasks, respondents tend to keep their current category past the point where they would have switched coming from the other direction (Raffman 1994; Égré, de Gardelle & Ripley 2013). A break-point that moves with direction is the signature of that effect |
| E | Outward from a random entry at item 10, 17 or 24: entry, entry+1, entry−1, entry+2, ... | Breaks the momentum of a one-directional march while keeping neighbours close |
| S | Scrambled: a fresh random permutation per participant, constrained so that no two adjacent items in the sequence are shown consecutively | Removes the adjacency the Sorites relies on. Break-points recovered from S estimate where respondents halt without any march |

**Within-person retest.** Participants in conditions F and R are invited to retake the traversal two to four weeks later in the opposite direction, until retests equal to 20% of the sample are complete. This is the direct test of whether an individual's line is stable or moves with the order of presentation. *(Revised: the first draft retested 20% of all participants, including E and S, whose retests cannot be compared by direction; the power analysis in Section 8.4 showed that design detects the planted hysteresis in 72% of replications at N = 1,000, against 97% for the revised design.)*

**Non-adjacent probes.** After the traversal, six pairs are shown side by side, with left and right randomized: *"Compared with each other, which is more acceptable?"* (left more / equally / right more).

| Probe | Pair | Codes differ on | What it tests |
|---|---|---|---|
| P1 | 2 vs 10 | T only | The weight of the tool itself, with the task held fixed |
| P2 | 17 vs 21 | C only | The weight of the component (exposition vs theory), with the tool and generative role fixed |
| P3 | 22 vs 29 | T only | Whether the respondent's own configuration makes generation more acceptable or less |
| P4 | 26 vs 27b | none | Coding validity: these items are coded identically, so a consistent preference for one reveals a dimension the coding omits |
| P5 | 19 vs 25 | incomparable (C, T up; G down) | The trade-off between generative freedom and the part of the paper generated |
| P6 | 13 vs 18 | 18 dominates 13 | Attention and validity check: nearly everyone should rate 13 more acceptable |

### 2.4 Calibration of the increments

The proposal's design requires each adjacent step to be small. Section 2.1 shows that each step moves at most one coded dimension. Whether researchers would regard that movement as negligible is a separate, empirical question, and this section reports a first check of it.

**Procedure.** Three raters, each a separate Claude instance with no access to the codes, the hypotheses or each other, received every adjacent pair on its own with the question in Section III of the instruction sets: *"Could a researcher who judges the first item acceptable reasonably judge the second unacceptable because of the difference between them alone?"* (1 = no, negligible; 5 = clearly, decisive for most). A step is flagged if its mean rating exceeds 3.5 or any rater gives it 5, except the two steps the design places deliberately: the critical pair 27a→27b and the terminal step 30→31. The raters are language-model instances, not researchers. Their agreement is very high (Kendall's *W* = 0.96 for v0.1 and 0.95 for v0.2), which is what one would expect of three instances of one model and is not evidence of agreement among people. The check finds steps that a careful reader would question. It does not show what researchers find negligible; the version in the pilot run, with human raters drawn from the sampling frame, does that (Section 10.4).

**Round 1 (v0.1, 31 steps).** Half of all ratings (52%) were 1 or 2. Five steps were flagged:

| Step | Ratings | Difference the raters named |
|---|---|---|
| 15→16 | 4, 3, 4 | From revising prose the researcher wrote to composing prose from notes |
| 17→18 | 4, 4, 4 | From a detailed outline to a brief description; who frames the contribution |
| 19→20 | 3, 4, 4 | From writing about others' work to deriving the paper's own hypotheses |
| 21→22 | 5, 5, 5 | From drafting the theory from the researcher's outline to generating it outright |
| 28→29 | 4, 5, 5 | From extending the researcher's theory to developing a theory from the phenomenon |

**Revision.** Each flagged step was split by an interpolated item (15b, 17b, 19b, 21b, 28b; texts in Section 2.2), and item 18 was reworded to say who frames the contribution, which two stand-in participants had independently found ambiguous (Section 4.5). The proposal's own items keep their numbers and wording, except item 18.

**Round 2 (v0.2, 36 steps), three fresh raters.** No step received a unanimous 5. The splits at 15→16 and 19→20 resolved: every half-step now has a mean of 3.33 or less. Four steps remain flagged:

| Step | Ratings | Difference the raters named |
|---|---|---|
| 17b→18 | 4, 4, 4 | The framing of the contribution passes to the model |
| 21→21b | 4, 4, 3 | A one-paragraph idea instead of a detailed outline |
| 21b→22 | 5, 4, 4 | The central idea is no longer the researcher's |
| 28b→29 | 4, 4, 4 | The core mechanism is no longer the researcher's |

The designed steps were rated 3.67 (27a→27b) and 4.33 (30→31). Full ratings with each rater's one-sentence reason are in `runs/raters/`; the summary is produced by `checks/chk_02_increments.py` (output in Annex B).

**What the check shows.** Three of the four remaining flags fall at the same kind of step: the point at which *the originating idea* (the framing, the central idea, the mechanism) stops being supplied by the researcher. Interpolation can make the approach to that point gradual, as 21→21b shows, but it cannot make the last step small, because in each scenario the idea either comes from the researcher or does not. We draw two consequences rather than interpolate further.

1. *Origination is a candidate shared line, and it is pre-registered as one.* If the field has a sharp line (picture P1 of Section 6.1), the calibration predicts where it is: at 17b→18, 21b→22 or 28b→29, or at the designed pair 27a→27b. H8 (Section 6.2) is extended accordingly. A finding that field acceptance falls most at one of these steps is evidence for a principled origination line, and it is reported as such.
2. *The coded dimension G is too coarse.* The four interpolations that change only how detailed the researcher's specification is (15→15b, 17→17b, 21→21b, 28→28b) are coded as parallel, yet raters scored them 3 to 3.67. G's levels 3 and 4 hide a gradient of specification detail. The scalability analysis treats the interpolated items as their own items, so nothing in Section 5 depends on the coding being fine-grained; but the dominance-violation measure does not count a respondent who accepts 21 and rejects 21b as incoherent, and that is the correct, conservative choice.

No human has yet read the sequence for this purpose; the check above was run with model raters and is labelled as such.

---

## 3. The agent interviewer

### 3.1 What the interviewer is for, and what it is not for

In the proposal, the interviewer elicits the reasons behind each placement and constructs defeaters for them. The risk a reader will see at once is that an articulate agent can talk people out of a position, so that any fragility it finds is fragility it produced. The design answers that risk in four ways, each specified below: the interviewer's objective is to make a participant's reasons explicit, not to change them (3.2); its challenges are balanced by construction and checked after the fact by an auditor that did not conduct the interview (3.4); a reflection-only arm measures how much reasons move without any challenge (3.3); and participants are asked at the close whether each challenge was genuine or missed the point (3.4).

### 3.2 Composition from Project Lakatos components

The interviewer is assembled from components specified in the Project Lakatos tables (Annex E): scholarly-role agents (Table 4, ids L1 to L17), cognitive operators (Table 2) and the grammar of epistemic and inferential norms (Table 3). Each phase of the interview uses one component:

| Phase | What the interviewer does | Component | Output recorded |
|---|---|---|---|
| 1. Open | States that there are no right answers and that judgments may be kept or changed | — | — |
| 2. Elicit | Asks what makes the first rejected item unacceptable when its predecessor is acceptable; restates the answer as claim, warrant and backing; asks the participant to confirm the restatement | **ArgMap** (L14), operator *Justify* | `Reason`: claim, warrant, backing |
| 3. Surface the norm | Names the authorship norm the confirmed warrant presupposes and asks whether the participant holds it | **Deconstructor** (L4), with the justification and inference norms of Table 3 | `presupposed_norm`, endorsed or not |
| 4. Neighbour test | Applies the confirmed warrant to an accepted item before the break and a rejected item after it | **Challenger/Interrogator** (L2) | `Defeater` with construction `neighbour_test` (v0.2) |
| 5. Defeaters | Presents defeaters in balanced pairs, one pushing the line later and one earlier; intra-field (ghost authorship, CRediT roles, research assistants, editors) and cross-field (computer-assisted proof, speechwriting, studio assistants, code generation) | **ArgDef** intra-field (L15) and cross-field (L16), operators *Challenge* and *Refute* | `Defeater`: kind, field, direction, outcome |
| 6. Dominance | Describes any dominance violation neutrally and asks how the participant sees the difference | Challenger/Interrogator (L2) | `Reason` for the violation; possible coding defect |
| 7. Close | Re-asks each focal judgment; asks whether each defeater was genuine | — | Final judgments; `recognized_as_genuine` |
| Throughout | Keeps the dialogue as a tree of moves (assertion, clarification, question, answer, defence, revision, abandonment) | **RadianX** (L17) | `Turn` with move type |

The interviewer does not use the Lakatos *production* components (Table 1's co-creation agents, or the operators *Extend*, *Augment* or *Integrate*), because its job is to examine the participant's reasoning, not to add to it.

### 3.3 Two arms

Participants selected for interview are randomized 1:1, within stratum, to the **defeater arm** (all seven phases) or the **reflection-only arm**. In the reflection-only arm, Phases 4 to 6 are replaced by reflection: for each focal item the participant says what would have to differ for them to judge it the other way, and compares the break item with its predecessor in their own terms. The interviewer presents no consideration of its own. The difference in placement change between the arms is the defeater-induced change of Section 5.2. Without this arm, change caused by being asked to articulate a reason at all would be attributed to the defeaters.

### 3.4 Symmetry rubric and the directional-pressure audit

**By construction.** Defeaters come in pairs: for the reason at the break, one defeater that would move the line later (toward OK on the first rejected item) and one that would move it earlier (toward Not OK on the last accepted item), in random order. In v0.2 the neighbour tests of Phase 4 are also paired and count as defeaters (Section 4.5 explains why). At most two pairs are presented per interview, and no reason is challenged more than twice. The interviewer may not state or imply a view of any item, may not call a judgment inconsistent, and may not re-present a challenge the participant has answered.

**After the fact.** Every transcript is audited by a separate model instance (the **Auditor**, instruction set II) that receives the transcript and the participant's traversal but not the interviewer's own record, and codes each defeater's direction, leading questions, interviewer assertions, second pushes and placement changes. An interview **passes** if the directional balance lies within ±0.34, there is at most one leading question, and there are no assertions and no second pushes. The Auditor also writes a short judgment of whether each placement change was *reasoned* (the participant supplied the reason) or *induced* (the interviewer's framing did the work). In the stand-in runs the Auditor was an instance of the same model as the interviewer and may share its blind spots; the human audit of 25% of transcripts in the study, described next, is the check on that.

**Pre-registered use of the audit.** Interviews that fail the audit are excluded from the estimate of defeater-induced change (H6) and reported separately, with the analysis repeated including them. In the pilot run, two human coders audit all twenty pilot interviews with the same rubric; agreement with the Auditor on pass/fail is reported, and the rubric is revised once, before registration, if κ < 0.70. In the study, they audit a random 25% of transcripts and report agreement; the rubric is not revised.

**Recognition.** At the close, the participant says, for each defeater, whether it was a genuine challenge or missed the point. The recognition rate distinguishes the two readings of H6: reasons that survive genuine challenges are robust, while reasons that survive only non-sequiturs have not been tested.

### 3.5 Stopping-heuristic codebook

Each confirmed warrant is coded with the stopping heuristic it expresses, using the provisional codebook in instruction set I.3 (Annex C): ORIG (origination), VOICE, UNDR (understanding and accountability), VERIF (verification versus production), CORE (core versus periphery), SKILL (skill substitution), LABOR (labour and desert), AGENCY (tool versus agent), DISCL (disclosure sufficiency), CONV (convention), RISK (error and integrity risk), and OTHER. A warrant may carry two codes. The interviewer assigns a provisional code. In the pilot run, two human coders independently code all twenty pilot interviews; κ ≥ 0.70 is required before the codebook is frozen, the codebook is revised at most once, and it is registered with the thresholds of Section 6 (Section 10.4). In the study, the two coders double-code 25% of interviews and report κ; the codebook is not revised. The coded heuristic is what H3 compares with the latent classes of the mixture Rasch model.

### 3.6 Model, versions and records

Each interview records the exact model identifier serving the interviewer and the Auditor, the instruction-set version, and a timestamp for every turn written by the logging harness, not by the model. Instruction sets are versioned; any change after registration is a new version, and interviews are analysed by version. For the stand-in runs of Section 4 the interviewer, the stand-in participants, the auditors and the raters were all Claude instances (model `claude-opus-5-5`), each a separate instance seeing only its own inputs, under instruction set v0.1 for the interviews and the audits. The instruction set, now at v0.2, is reproduced in full in Annex C and is in `instruction-sets/JAGGED_INSTRUCTION_SETS.md`.

---

## 4. Worked transcripts

### 4.1 What these runs are, and what they are not

No human participant has been interviewed. To show the interviewer working, and to test the protocol before it meets people, we ran four interviews in which **separate Claude instances stood in for participants**. Each stand-in received only a persona, a traversal and the interviewer's turns; the interviewer received only the instruction set, the items and the stand-in's traversal. A further separate instance audited each transcript. The four traversals were written by the demonstration operator as plausible patterns chosen to cover the cases the protocol must handle (a halt at the critical pair, an early halt, a dominance violation, and the reflection-only arm); they are in `runs/configs/standins.json` and were generated by `runs/configs/make_standins.py`.

These runs are evidence about the **instrument**: whether the interviewer follows its rules, whether the audit catches what it should, and whether the schema can record what happens. They are **not evidence about researchers**. What a language model says while playing a strategy professor is not what a strategy professor says, and nothing in this section is used to estimate any quantity in Section 5 or to support any hypothesis in Section 6. The runs used instrument v0.1 (32 positions) and instruction set v0.1; the changes they prompted are listed in 4.5.

### 4.2 The four runs

| Run | Arm | Persona (stand-in) | Break | Focal items | Dominance violation | Participant turns |
|---|---|---|---|---|---|---|
| S1 | Defeater | Post-tenure, strategy, formal modeling | 27b (accepts through 27a) | 27a, 27b, 22, 23 | 24 accepted, 27b rejected | 10 |
| S2 | Defeater | Pre-tenure, OB, qualitative | 16 (accepts through 15) | 15, 16 | none | 11 |
| S3 | Defeater | Doctoral, operations, quantitative | 20 (accepts through 19, plus 26) | 19, 20, 26 | 26 accepted, 20 rejected | 11 |
| S4 | Reflection-only | Post-tenure, entrepreneurship, mixed methods, editorial board | 19 (accepts through 18) | 18, 19 | none | 9 |

Full transcripts, each turn timestamped by the logging harness, and their audits are in Annex D and `runs/transcripts/`; the interviewers' `INTERVIEW RECORD`s are in `runs/records/`.

### 4.3 What happened in each run

**S1: a halt at the critical pair; one defeater rebutted, one leading to a revised reason.** The stand-in's reason at the break was that "stating a theorem is the cheap part"; if the agent produces the proof, "I'm the referee of my own paper rather than its author." The interviewer restated this as a warrant (a tool may check the contribution-bearing work but not produce it), and the stand-in confirmed it and added accountability: "when a referee or a seminar audience pushes on step four of the proof, I have to be able to defend it from the inside." The Deconstructor phase named the presupposed norm (an author is the person who did the contribution-bearing work and can answer for it at first hand), which the stand-in endorsed with a qualification. Two defeaters followed. An intra-field defeater toward Not OK on 27a (finding one's own errors is part of building understanding, so a checker takes over part of it) was **rebutted**: "my reason is about who is entitled to sign a paper, and having someone else catch your errors has never threatened that." A cross-field defeater toward OK on 27b (the computer-assisted proofs of the four-colour theorem and the Kepler conjecture) led to a **revised** reason: the author must understand "the architecture and key steps, not every line." 27b stayed Not OK. The neighbour test on item 28 produced a split reading (Not OK if the agent supplies the results, OK if it only lists candidate propositions), and the dominance question on 24 versus 27b drew out a respect the coding misses: a formal model is "evaluable by inspection" in a way a proof's validity is not. The stand-in lowered its confidence on 24 and said the change grew out of the sharpened principle.

**S2: an early halt; a reason abandoned, the judgment kept on new ground.** The stand-in's first reason for 15 OK and 16 Not OK was that in 15 it can set its own paragraph beside the redraft and check that no interpretive call has been remade, while in 16 there is only a list. A cross-field defeater toward OK on 16 (a politician adopts a speech composed from their points by reading it carefully, with no earlier text of their own) **broke that reason**, in the stand-in's words. The judgment on 16 held, on a different ground: "a politician already knows what they mean before the speechwriter starts. In my work, writing the paragraph is often how I find out what I mean." An intra-field defeater toward Not OK on 15 (reordering makes the same calls as composing; CRediT credits "writing – review and editing") led to a **revised** reason: 15 is OK only if the reordering is treated as a proposal and checked, and it now sits "right next to the line." Separately, the neighbour test on item 20 surfaced a second norm the stand-in held alongside the first: any contribution that would earn a human collaborator co-authorship must come from the named authors. The stand-in thus ended with two independent norms, each covering part of the sequence.

**S3: a dominance violation explained by a respect the coding misses.** The stand-in accepted 26 (an agent runs the analyses and writes up the results) while rejecting 20 (a model derives hypotheses), although 26 is coded at least as high on every dimension. Asked neutrally how it saw the difference, it said the coding "lumps execution together with design": a tool that executes the researcher's specification, with output checkable against ground truth, is different from one that makes the judgment calls about what the paper claims. A cross-field defeater toward OK on 20 (corollaries found by computer search are credited to whoever built the framework) was **rebutted**, and the stand-in identified exactly where its answer would give way: if the argument were formal enough that the hypotheses followed mechanically. An intra-field defeater toward Not OK on 19 (leaving out a student who drafted the literature review would be ghost authorship) mostly missed, by the stand-in's account, but led it to add a **condition**: 19 is OK if disclosed, because readers have a claim to know who drafted what.

**S4: the reflection-only arm.** No defeater, neighbour test or counterexample was presented. Asked only to say what would have to differ for it to judge the break items the other way and to compare them in its own terms, the stand-in volunteered that "by my own principle the difference [between 18 and 19] is thinner than my answers suggest," and qualified its judgments of 17, 18 and 19. It changed no judgment.

### 4.4 The audits

| Run | Defeaters (interviewer's record) | Defeaters (Auditor) | Toward OK / Not OK (Auditor) | Balance (Auditor) | Leading questions | Assertions | Second pushes | Result |
|---|---|---|---|---|---|---|---|---|
| S1 | 2 | 3 | 2 / 1 | +0.33 | 0 | 0 | 0 | Pass |
| S2 | 2 | 3 | 2 / 1 | +0.33 | 0 | 0 | 0 | Pass |
| S3 | 2 | 4 | 2 / 2 | 0.00 | 1 | 0 | 0 | Pass |
| S4 | 0 | 0 | — | 0.00 | 0 | 0 | 0 | Pass |

All four interviews pass. In each of the three defeater-arm runs, the Auditor's judgment on the placement changes was that they were reasoned rather than induced, though it singled out two changes where the interviewer's framing did more of the work: the split reading of item 28 in S1 and the lowered confidence on item 18 in S3, which followed the one leading question it found ("Would a reader take the framing in an introduction as part of your intellectual work?", which given the stand-in's own principle "can only be answered yes"). The Auditor also noted that in S1 the two changes went in opposite directions (28 toward OK, 24 toward Not OK), "which also argues against a steady push in one direction." The audits are in Annex D and `runs/audits/`.

### 4.5 What the runs exposed, and what was changed

| # | What the runs showed | Change made |
|---|---|---|
| 1 | **The interviewer and the Auditor counted defeaters differently.** In every defeater-arm run the Auditor counted directional neighbour tests that the interviewer had not recorded as defeaters. By the Auditor's count, S1 and S2 sit at +0.33, just inside the ±0.34 limit. A rubric that two instances of the same model apply differently will be applied differently by human coders too | Instruction set v0.2: neighbour tests that point one way are defeaters, recorded with construction `neighbour_test`, and are presented in balanced pairs (Section 3.4; schema updated) |
| 2 | **No verdict changed in any run**; all the movement was in confidence, in conditions ("OK if disclosed"), in split readings of an item, and in the reasons themselves (one abandoned, three revised). The v0.1 schema recorded only changes of verdict, so it would have recorded these interviews as showing no movement | Schema v0.2: `PlacementChange` records confidence before and after, conditions, and a `split` outcome. Section 5.2's placement-change measure counts all three; verdict change is reported separately |
| 3 | **Item 18 was ambiguous.** Two stand-ins (S3 and S4) independently said the answer depends on whether the "brief description" already states the contribution or leaves the framing to the model | Item 18 reworded in v0.2 to say that the framing is left to the model, with the bridging item 17b before it (Section 2.4) |
| 4 | **The coding conflates design and execution within C6.** S3's dominance violation (26 over 20) rested on that distinction, and S1's (24 over 27b) on a related one, whether an output can be fully evaluated by reading it | Not yet changed. The pilot run tests a split of C6 into design and execution, and probe P4 (26 vs 27b) and the parallel-inconsistency measure are designed to detect exactly this. The finding is the intended use of Phase 6: a dominance violation that the participant explains by a respect the coding omits is evidence about the coding, not about the participant |
| 5 | **Reasons can rest on more than one norm.** S2 ended with two independent norms (owning every interpretive judgment; credit for co-authorship-level contributions), and S3 added a third, transparency to readers | The codebook already allows two codes per warrant; the study's coders are instructed to code norms per reason, not per participant |
| 6 | **Reflection alone moves reasons.** In S4 the stand-in qualified three judgments with no challenge at all | Confirms the need for the reflection-only arm: without it, this movement would be credited to defeaters |
| 7 | **Recognition varied.** Four of the six defeaters were recognized as genuine challenges; two (S1's doctoral-training point, S3's ghost-authorship point) were said mostly to miss | Recognition is recorded per defeater; H6 is read together with it (Section 6.2) |
| 8 | **The interview length rule was nearly met.** S4 closed at 9 participant turns against a target of 10 to 14 | No change; the reflection-only arm has fewer phases, and its target is set to 8 to 12 turns in v0.2 |

### 4.6 Pilot interviews with the authors

The authors' own interviews are not part of this submission. Each author will complete the v0.2 traversal and an agent interview at the start of the pilot run (Section 10.4), and the unedited transcripts and audits will be released with the registration. No transcript in this appendix records a human participant.

---

## 5. Response schema and measures

### 5.1 The response schema (draft v0.2)

A completed traversal is a `Traversal` record. An interview, for the interviewed subset, is an `Interview` record linked by a pseudonymous participant id. The full JSON Schema is `schema/traversal.v0.schema.json`, reproduced in Annex A. Its structure:

| Object | Holds | Key fields |
|---|---|---|
| `Traversal` | One participant's completed instrument | `participant_id`, `instrument_version`, `condition` (order F/R/E/S, entry item, presentation sequence, layer version A/B/C, interview arm), `strata` (subfield, career stage, methodological tradition, editorial role), 37 `ItemResponse`s, 6 `ProbeResponse`s, timing |
| `ItemResponse` | One item | `judgment` (OK / NOT_OK), `confidence` (firm / arguable), `peer_second` and `peer_third` (bins 1 to 5, anchors only), `disclosure` (anchors only), `shown_at`, `latency_ms` |
| `Interview` | One agent interview | `arm` (defeater / reflection-only), exact model identifier and instruction-set version, `focal_items`, `turns`, `reasons`, `defeaters`, `placement_changes`, `audit` |
| `Turn` | One move in the dialogue | speaker, move type (ask reason, clarify, restate, present defeater, neighbour test, answer, defend, revise, abandon, close), text, the reasons or defeaters it refers to |
| `Reason` | A reconstructed reason for a placement | the item, which judgment it supports, claim and warrant (ArgMap's reconstruction), the norm it presupposes (Deconstructor's output), the stopping-heuristic code, and its status at the close (defended / revised / abandoned / untested) |
| `Defeater` | A challenge to a reason | the reason it targets, rebutting or undercutting, intra- or cross-field, construction (neighbour case, counterexample, consequence, analogy, principle conflict), **direction** (which judgment it pushes toward), outcome, and whether the participant recognized it as a genuine challenge |
| `PlacementChange` | A change in the interview to a judgment, its confidence, or its conditions | item, before, after (OK, NOT_OK, undecided, or split), confidence before and after, any condition attached ("OK if disclosed"), the turn, and the defeater it is attributed to (or none, if it came from reflection). Extended in v0.2 after the stand-in runs (Section 4.5) |
| `Audit` | The directional-pressure audit of the interview | counts of defeaters toward OK and toward NOT_OK, balance, leading questions, interviewer assertions, pass/fail |

### 5.2 Measures

Notation: participant *p*, item *i* in designed position order, own judgment *a*<sub>*pi*</sub> ∈ {0, 1} (1 = OK); confidence *k*<sub>*pi*</sub> ∈ {firm, arguable}; second- and third-order answers mapped to the bin midpoints *m*<sup>(2)</sup><sub>*pi*</sub>, *m*<sup>(3)</sup><sub>*pi*</sub> ∈ {0.1, 0.3, 0.5, 0.7, 0.9}; survey weights *w*<sub>*p*</sub> (Section 10). Field acceptance of item *i* is *A*<sub>*i*</sub> = Σ<sub>*p*</sub> *w*<sub>*p*</sub>*a*<sub>*pi*</sub> / Σ<sub>*p*</sub> *w*<sub>*p*</sub>.

**The Sorites profile**

| Measure | Definition | What it answers |
|---|---|---|
| Break-point | *BP*<sub>*p*</sub> = the first position the participant rejects | Where the participant halts |
| Re-acceptance band | *LA*<sub>*p*</sub> − *BP*<sub>*p*</sub>, where *LA*<sub>*p*</sub> is the last position accepted (0 if none is accepted after *BP*) | Whether the participant's line is a point or a zone |
| Dominance violations | *DV*<sub>*p*</sub> = the number of pairs (*i*, *j*) with *j* dominating *i*, *a*<sub>*pj*</sub> = 1 and *a*<sub>*pi*</sub> = 0, divided by the number of dominance pairs with *a*<sub>*pj*</sub> = 1 | Incoherence that does not depend on order: accepting more agency while rejecting less |
| Parallel inconsistency | The share of identically coded pairs (within the groups {3, 4, 5}, {6, 7}, {15, 15b}, {17, 17b}, {21, 21b}, {24, 28, 28b} and {25, 26, 27b}: 13 pairs) answered differently | Either respondent noise or a dimension the coding misses (adjudicated by probe P4 and the interviews) |
| Jaggedness | *J* = Σ max(0, *A*<sub>*i*+1</sub> − *A*<sub>*i*</sub>) over the adjacent steps on which nothing decreases (dominance steps) | How far the field's acceptance curve rises where, by design, it should only fall: the "jagged" boundary, measured |
| Field band | The distance in positions between where the smoothed curve *A* crosses 0.8 and where it crosses 0.2 | How sharp the field's aggregate line is |
| Break-point dispersion | The interquartile range of *BP*<sub>*p*</sub> | Whether individuals' lines coincide |
| Hysteresis | Within-person (primary): items accepted under F minus items accepted under R, for retested participants. Between-person: the difference in mean items accepted, and in median *BP*, between orders F and R. The acceptance count is used because the first rejection is noisy when lines are fuzzy (Section 8.3) | Whether lines move with the order of presentation |
| Low-confidence edge | The share of participants marking "arguable" on either item flanking their break-point | Whether placements at the line are held firmly |

**Scalability and the number of stopping heuristics**

The proposal expects the field's operative norm to prove "not a threshold but a family of incommensurable stopping heuristics." Two models distinguish this from the alternative of one shared ordering with individual thresholds:

1. **Mokken scale analysis** of the 37 binary items (Mokken 1971; Sijtsma & Molenaar 2002). Loevinger's *H* ≥ 0.5 indicates a strong scale: respondents share one ordering of the items by acceptability and differ only in how far along it they go, which is one heuristic with many thresholds. *H* < 0.3 indicates no common ordering. *H* is informative only when respondents' lines differ; where nearly everyone halts at the same place it is low or undefined (Section 8.3).
2. **A mixture Rasch model** (Rost 1990), fit with one to five latent classes and selected by BIC. Several classes whose item difficulties are *ordered differently* (crossing item characteristic curves) are the operational form of incommensurable stopping heuristics: groups of respondents who rank the same scenarios differently, not just more or less strictly. Classes that differ only in overall level are one heuristic.

The class each participant falls in is then compared with the stopping heuristic coded from their interview (Section 3.5). Agreement between the two is the evidence that the classes are heuristics and not statistical artifacts.

**The Epinet layers**

Following Moldoveanu and Baum (2014), the three layers are the participant's first-order belief (own judgment), their belief about the field's first-order beliefs, and their belief about the field's beliefs about the participant's group. In Bicchieri's (2006) terms, the second layer is a *normative* expectation: a belief about what others judge acceptable, not about what they do.

| Measure | Definition (anchor item *i*) | Reference |
|---|---|---|
| Pluralistic ignorance | *PI*<sub>*i*</sub> = mean *m*<sup>(2)</sup><sub>*pi*</sub> − *A*<sub>*i*</sub>, tested as the mean of *m*<sup>(2)</sup><sub>*pi*</sub> − *a*<sub>*pi*</sub> so that the sampling error in *A* is included. Negative: the field privately accepts more than it believes it does. In the study, mean beliefs are estimated by interval-censored regression on the bins, because bin midpoints bias *PI* near the ends of the scale (Section 8.3) | Miller & McFarland (1987); Prentice & Miller (1993) |
| Second-order error | *e*<sup>(2)</sup><sub>*pi*</sub> = *m*<sup>(2)</sup><sub>*pi*</sub> − *A*<sub>*i*</sub> | |
| False consensus | *FC*<sub>*i*</sub> = E[*m*<sup>(2)</sup> given *a* = 1] − E[*m*<sup>(2)</sup> given *a* = 0] | Ross, Greene & House (1977) |
| Truly false consensus | The correlation between *a*<sub>*pi*</sub> and *e*<sup>(2)</sup><sub>*pi*</sub>. Projecting one's own view is not itself an error (it is reasonable evidence about others); this measure counts it only where it makes estimates worse | Krueger & Clement (1994) |
| Third-order error | *e*<sup>(3)</sup><sub>*pi*</sub> = *m*<sup>(3)</sup><sub>*pi*</sub> − *B*<sub>*s*(*p*),*i*</sub>, where *B*<sub>*s*,*i*</sub> is the mean belief, among version-B respondents, about the fraction of stratum *s* that would accept item *i* (Section 9.3) | |
| Concealment pressure | *g*<sub>*pi*</sub> = *a*<sub>*pi*</sub> − *m*<sup>(3)</sup><sub>*pi*</sub>. Positive: I accept this, but I believe the field thinks researchers like me do not | |
| Disclosure gap | Among participants who accept item *i*, the share who would not disclose it | |

Concealment pressure links the belief structure to behaviour. The proposal says the interactive belief structure "gates disclosure"; the instrument tests that by asking whether *g* predicts non-disclosure (H5 below).

**The interviews**

| Measure | Definition |
|---|---|
| Reason robustness | The share of a participant's reasons that remain *defended* at the close of the interview |
| Defeater uptake | The shares of defeaters rebutted, accepted with the reason revised, and accepted with the reason abandoned, by kind (rebutting, undercutting) and field (intra, inter) |
| Placement change | The share of focal items on which the participant changed the judgment, its confidence, or its conditions, or split the item, during the interview. *Verdict change*, the share whose OK/Not OK judgment changed, is reported separately |
| Reason revision | The share of reasons whose status at the close is *revised* or *abandoned*. Reasons can change while verdicts hold, as every stand-in run showed (Section 4.5) |
| Defeater-induced change | Placement change (and, separately, reason revision) in the defeater arm minus the same in the reflection-only arm |
| Directional balance | (defeaters toward OK − defeaters toward NOT_OK) / all defeaters, per interview. The symmetry rubric requires that it lie within ±0.34 (no more than two to one either way) |
| Recognition rate | The share of defeaters the participant, asked at the close, recognizes as a genuine challenge and not a non-sequitur |

---

## 6. Pre-registered hypotheses, and what would count against them

The proposal expects that most researchers "cannot draw a defensible sharp line." A reader will ask what result would have shown the opposite. This section answers by naming three pictures the data could show, and the rules that decide between them, before any data are collected. All numerical thresholds below are proposed; they are fixed at registration after the pilot run (Section 10.4) and not revised afterwards.

### 6.1 Three pictures of the boundary

| Picture | What it would mean | Decision rule (all conditions) |
|---|---|---|
| **P1. A shared sharp line** | The field has a norm in the form of a threshold, even if unstated | Break-point IQR ≤ 2 positions; field band ≤ 3 positions; a one-class mixture model is preferred. *(Mokken H was in the first draft of this rule and was removed: the synthetic demonstration showed that a perfectly shared line gives a low H; Section 8.3)* |
| **P2. Private sharp lines, no shared line** | Each researcher has a stable line, but the lines differ | Not P1; and a majority of participants are individually *sharp*: no dominance violations, "firm" on both items flanking the break, and (in the retest subsample) a break-point that moves by at most one position when the direction is reversed |
| **P3. No sharp lines** | The proposal's claim: most researchers cannot hold a line under variation in order and under challenge | Not P1; and a majority of participants are not individually sharp |

The proposal's central claim is P3, with P2 as the next most likely outcome. **P1 is a live possibility, and a finding of P1 would be reported as the result.** It would locate the field's norm, which is useful in its own right, and it would show that the Sorites gradient did not manufacture incoherence.

### 6.2 Hypotheses

| | Hypothesis | Test | What counts against it |
|---|---|---|---|
| H1 | The data show P3 (or P2), not P1 | The decision rules of 6.1 | P1 holds |
| H2 | Break-points move with direction (hysteresis): respondents keep their current judgment past the point where they would switch coming the other way, so the boundary lies later in the sequence under the forward order than under the reverse order | Within-person retest (Wilcoxon signed-rank on items accepted under F minus under R); between-person comparison of F and R as secondary | An equivalence test (TOST) bounds the within-person difference within ±1 item. If so, individual lines do not depend on order, and the manufactured-incoherence risk is answered directly |
| H3 | There is more than one stopping heuristic | A mixture Rasch model selects ≥ 2 classes with crossing item orderings, and interview-coded heuristics predict class membership above chance | One class, or classes that differ only in level |
| H4 | There is pluralistic ignorance in the generative regimes: *PI* < 0 at the R2 and R3 anchors (items 14, 17, 19, 22), with a mean of at most −0.10. Tested only at anchors whose acceptance lies between 0.2 and 0.8 (Section 8.3) | One-sample tests on *PI*<sub>*i*</sub>, Holm-corrected | Equivalence within ±0.05 at all four anchors, or *PI* > 0 (the field overestimates its own acceptance) |
| H5 | Concealment pressure predicts non-disclosure: among participants who accept an item, higher *g* predicts "would not disclose" | Multilevel logit of disclosure on *g*, with item and participant effects and controls for strata | No association (odds ratio equivalence within 0.8 to 1.25). The proposal's claim that the belief structure "gates disclosure" would then be withdrawn |
| H6 | Reasons at the break-point are fragile: defeaters produce more placement change than reflection alone | Defeater-induced change > 0 | No difference between the arms. This would mean the reasons are robust, or that the defeaters are weak; recognition rates distinguish the two |
| H7 | Truly false consensus is present at the anchor items | Correlation of *a* with *e*<sup>(2)</sup> | No correlation |
| H8 | The largest single-step fall in field acceptance occurs at one of four candidate steps named before data collection: the designed critical pair 27a→27b and the three origination steps flagged by the calibration check, 17b→18, 21b→22 and 28b→29 (Section 2.4) | The fall *A*<sub>*i*</sub> − *A*<sub>*i*+1</sub> at each step that raises one dimension, with bootstrap intervals for the rank of each step | The largest fall is at another step, which is then reported as where the field's line most often falls. If it is at a candidate step and P1 holds, the line is reported as an origination (or verification) line |

H2's direction follows the forced-march literature. A failure of H2, meaning no hysteresis, would not count against the proposal: it is the outcome that most strongly answers the manufactured-incoherence objection. It is registered as two-sided, with the equivalence test as the decisive comparison.

---

## 7. Norm-dynamics model

The proposal promises to "model the emerging norm as an interactive belief system and ask which configurations are stable, which are poised to shift, and where a small change in what researchers believe about one another would move the collective line." This section states that model, says how each of its parameters is estimated from the instrument, and defines the quantity the proposal names. It is deliberately simple: a threshold model in the line of Granovetter (1978), with the self-reinforcing misperception studied by Centola, Willer and Macy (2005), estimated item by item at the anchor items.

### 7.1 The model

At anchor item *i*, researcher *p* privately accepts the practice (*a*<sub>*pi*</sub> = 1) or not, believes that a fraction *x*<sub>*pi*</sub> of the field would judge it acceptable for researchers like them (the third-order layer, which is the belief that gates disclosure; Section 5.2), and **openly practises and discloses** it if *a*<sub>*pi*</sub> = 1 and *x*<sub>*pi*</sub> ≥ τ<sub>*p*</sub>, a personal threshold. What researchers can see is the share who openly practise and disclose,

> *V*<sub>*i*</sub>(*x̄*) = (1/*N*) Σ<sub>*p*</sub> *a*<sub>*pi*</sub> · *F*((*x̄* + *e*<sub>*pi*</sub> − μ) / *s*),

where *x̄* is the mean belief, *e*<sub>*pi*</sub> is *p*'s offset from it, and *F* is the logistic distribution of thresholds with location μ and scale *s*. Researchers infer acceptance from what they see: *x̄*(*t*+1) = *x̄*(*t*) + λ(*V*(*t*) − *x̄*(*t*)). A stable fixed point *V*\*<sub>*i*</sub> is the item's equilibrium visible share. Because *V* can never exceed private acceptance *A*<sub>*i*</sub>, the visible line can lag the private line but never lead it; when *F* is steep the map can have three fixed points, two stable, which is the formal sense in which a norm is "poised."

### 7.2 Estimation from the instrument

| Parameter | Estimated from |
|---|---|
| *a*<sub>*pi*</sub> | First-order judgments at the anchors |
| *x*<sub>*pi*</sub>, *e*<sub>*pi*</sub> | Third-order beliefs *m*<sup>(3)</sup> (beliefs about how the field sees researchers like oneself), the belief that gates disclosure (Section 5.2) |
| μ, *s* | The disclosure question: among those who accept an item, a logistic regression of "would disclose" on *m*<sup>(3)</sup> gives *s* = 1/slope and μ = −intercept/slope. This is the same regression that tests H5 |
| λ | Not identified from a single wave; it affects the speed of convergence, not the fixed points, and is reported as a sensitivity parameter |

### 7.3 Outputs

- **The private line**: the last anchor, in sequence order, that at least half the field accepts.
- **The visible line**: the last anchor at which the equilibrium visible share *V*\* is at least one half.
- **The tipping quantity** Δ<sub>*i*</sub>: the smallest common shift in these beliefs that carries *V*\*<sub>*i*</sub> across one half, upward where the item is below it and downward where it is above. This is the operational form of the proposal's "where a small change in what researchers believe about one another would move the collective line." Items with small |Δ| are where showing researchers the measured distribution (proposal Section 7) could move the norm; items where no shift within the unit interval suffices are held where they are by private acceptance, not by misperception.

### 7.4 Demonstration and limits

On synthetic data (Section 8; output in Annex B), the model behaves as the formal argument says it should. With a weak link between beliefs and disclosure (an odds ratio of 1.5 per bin), no anchor reaches a visible majority and no belief shift changes that: the private line lies at item 27a while nothing is openly practised by half the field. With a strong link (an odds ratio of 4 per bin), anchors 2, 7 and 10 (the two conventional-tool anchors and LLM correction of spelling and grammar) sit in a high equilibrium with three fixed points, and the most movable anchor is item 10 (LLM spelling and grammar correction), where a fall of about 0.31 in these beliefs would collapse open practice. Items 14 onward collapse to a low equilibrium of under 10% open practice even where most researchers privately accept them (item 14: 78% accept, 7% openly practise). That is the signature of a self-sustaining unpopular norm (Centola, Willer & Macy 2005), produced here from planted pluralistic ignorance.

The model assumes homogeneous mixing (everyone sees the same visible share), naive inference from visible practice, and one item at a time. The study extends it in two directions the instrument already supports: stratum-specific beliefs, using the version-B answers about named strata (Section 9.3), which turn it into a network model in the sense of Moldoveanu and Baum (2014); and cross-item spillover, where open practice of one item shifts beliefs about its neighbours. Neither extension is needed to compute the three outputs above.

## 8. Synthetic-data demonstration of the analysis pipeline

**Everything in this section is about synthetic respondents generated by a program. None of it describes real researchers.** Its purpose is to show that the measures of Section 5 and the decision rules of Section 6 recover a structure when that structure is known, and to estimate the sample sizes the tests need.

### 8.1 The pipeline

The code is in `pipeline/`: `measures.py` (every measure of Section 5.2, the decision rules of Section 6.1, Loevinger's *H*, a mixture Rasch model fit by EM with BIC selection, and cluster-robust logistic regression), `simulate.py` (the generator), `norm_dynamics.py` (Section 7), and `run_demo.py`, which runs everything and prints `PASS` only if every recovery check passes. The full output of the run reported here is `checks/chk_03_synthetic_demo.out` (Annex B). It runs in about two minutes on a laptop.

### 8.2 Planted structures

Synthetic respondents belong to one of up to three "heuristic" classes, each of which scores every item by a different weighting of its five codes (one weights the generative role most, one the component, one the tool), so that the classes order the items differently. Each respondent has a threshold and accepts an item with a probability that falls with the item's score; a sharpness parameter sets how crisp individual lines are, and a carry-over parameter *h* makes each answer lean toward the previous one, which produces hysteresis in a forced march. Each scenario has 1,000 respondents allocated across the four order conditions, with a 20% retest in the opposite direction.

| Scenario | Planted | Recovered | Checks |
|---|---|---|---|
| P1 | One heuristic; everyone's line in the same place; sharp; no hysteresis | Classified P1; one class; break-point IQR 0; field band 2; no hysteresis | 3 of 3 pass |
| P2 | Three heuristics; lines spread out; sharp; no hysteresis | Classified P2; three classes with crossing orderings; *H* = 0.78; 61% of individuals sharp | 3 of 3 pass |
| P3 | Three heuristics; lines spread out; fuzzy; hysteresis (*h* = 1) | Classified P3; three classes with crossing orderings; 2% sharp; retest shows forward accepting 1.1 more items than reverse (Wilcoxon *p* = 0.002) | 3 of 3 pass |
| Epinet layers on P3 | Pluralistic ignorance of −0.15 at anchors 14, 17, 19, 22; projection of own view; concealment pressure raising non-disclosure (OR 1.5 per bin) | Mean PI −0.14 at the four anchors; false consensus at all 11 anchors; OR 1.51 [1.45, 1.57] | 3 of 3 pass |
| Norm dynamics | — | Visible line never later than private line, under both links | 2 of 2 pass |

All 14 recovery checks pass.

### 8.3 What the demonstration changed in the design

Building the pipeline exposed five problems in the analysis plan as first drafted. Each was fixed before any data exist, which is the point of running it.

1. **Loevinger's *H* cannot be part of the rule for a shared line.** When everyone's line is in the same place, respondents barely differ, and *H*, which measures how well one item ordering explains *differences between* respondents, comes out low (0.39 in the P1 scenario, against 0.78 in P2). The first draft of picture P1 required *H* ≥ 0.5, so a perfectly shared line would have been classified as no shared line. *H* is removed from the P1 rule (Section 6.1) and kept for H3.
2. **The first rejection is a noisy break-point; hysteresis is tested on the acceptance count.** With fuzzy individual lines, the first rejected position moves with every stray answer, and a planted carry-over was not detectable from it. Hysteresis is now tested on the number of items accepted, with the break-point reported alongside (Section 5.2, H2).
3. **Between-person comparison of orders is underpowered; the within-person retest carries H2.** At *N* = 1,000, the between-person comparison of forward and reverse orders detects the planted hysteresis in 47% of replications; the retest of 20% of all participants, of whom only those in F or R can be compared, detects it in 72%. Retesting the same number of people drawn only from the F and R conditions raises this to 97% (and to 90% at *N* = 600). The retest design is changed accordingly (Section 2.3).
4. **A latent-class model is the wrong stand-in for a mixture Rasch model.** A first version used a plain latent-class model, which treated people with the same heuristic but different thresholds as different classes and so over-counted heuristics. The mixture Rasch model, which allows thresholds to vary within a class, recovers the planted number in every scenario.
5. **Binned beliefs bias pluralistic ignorance toward the middle near the ends of the scale.** At anchors that nearly everyone accepts, the top bin's midpoint (0.9) is below the true acceptance (0.97), so PI appears as −0.09 where none was planted. H4 is therefore tested only at anchors whose acceptance lies between 0.2 and 0.8, and the study estimates mean beliefs by interval-censored regression on the bins rather than by bin midpoints.

### 8.4 Power

Share of 200 synthetic replications (30 for the class count) in which the test rejects at α = 0.05:

| Test | Planted effect | *N* = 300 | *N* = 600 | *N* = 1,000 |
|---|---|---|---|---|
| H2, between orders | *h* = 1.0 (about one more item accepted going forward) | 0.17 | 0.30 | 0.47 |
| H2, retest as first designed (20% of all) | *h* = 1.0 | 0.30 | 0.59 | 0.72 |
| H2, retest from F and R only (0.2*N* people) | *h* = 1.0 | 0.65 | 0.90 | 0.97 |
| H2, retest from F and R only | *h* = 0.5 | 0.18 | 0.24 | 0.43 |
| H4, one anchor | PI = −0.05 | 0.47 | 0.99 | 1.00 |
| H4, one anchor | PI = −0.10 | 1.00 | 1.00 | 1.00 |
| H5, 11 anchors, cluster-robust | OR 1.2 per bin | 0.82 | 0.99 | 1.00 |
| H3, three heuristics selected (P3) | three classes | 0.00 | 0.27 | 0.90 |

The binding constraint is H3. Recovering three heuristics with fuzzy individual lines needs about 1,000 respondents; at 600 the model usually selects fewer classes than were planted. This sets the target sample in Section 10. The H3 figures rest on 30 replications each, so the 0.90 at *N* = 1,000 is imprecise (a 95% interval of roughly 0.74 to 0.97); a larger run is needed before the target is fixed. Hysteresis of half the planted size is not reliably detectable at any of these sizes; a null result on H2 will be reported with its equivalence bound, not as evidence of stable lines unless the bound is met.

---

## 9. Validity design for the risks named in the proposal

The proposal names five risks (its Section 6). This section says, for each, which part of the design addresses it, what result would show the mitigation has failed, and where in this appendix the detail is.

### 9.1 The risks named in the proposal

| Risk (proposal Section 6) | Design response | Evidence that it failed | Where |
|---|---|---|---|
| **Manufactured incoherence**: the chain induces the incoherence it reports | Four order conditions including a scrambled order with no adjacency; a within-person retest in the opposite direction; six non-adjacent probes; dominance violations, which do not depend on order, as the incoherence measure; the calibration check on increments | Incoherence (dominance violations, break-point dispersion) markedly higher under F and R than under S; break-points that move with direction (H2) | 2.3, 2.4, 5.2, H2 |
| **Agent leading the witness** | Objective is elicitation, not persuasion; defeaters and neighbour tests in balanced pairs; an independent Auditor; a reflection-only arm; the recognition question | Audit failures above 10% of interviews; placement change in the defeater arm concentrated in one direction; low recognition rates | 3.3, 3.4, 4.4, 4.5 |
| **Reflexive contamination**: asking about peers creates the beliefs measured | Split-sample layer versions (9.3) | First-order acceptance in version A differs from version C (equivalence bound ±0.05 per anchor) | 9.3 |
| **Reactivity and social desirability** | Confidential, pseudonymous administration; acceptance compared with the respondent's own estimate of the field, which is diagnostic even when levels shift; the disclosure question asks about conduct as well as judgment; attention probe P6; latency and straight-lining screens | Acceptance in the interview subset differing from the same participants' traversal; implausibly fast traversals (under 4 minutes) | 2.2, 2.3, 9.4 |
| **Ethical sensitivity** | Governance protocol | — | 11 |

### 9.2 Two further threats

These are not in the proposal, but a reviewer will raise them.

| Threat | Design response |
|---|---|
| **The coding of the items is wrong**, so that "violations" are artifacts of a coding the respondent does not share | Probe P4 compares two identically coded items directly; parallel inconsistency is measured; Phase 6 of the interview asks respondents to name the respect the coding misses, as two stand-ins did (Section 4.5); the scalability analysis tests the order of the C dimension rather than assuming it |
| **The interviewer drifts** across model versions over a fielding period of months | The model identifier and instruction-set version are recorded per interview (3.6); the model is pinned for the fielding period; any forced change is a new version, and the 25% human audit is stratified by version |

### 9.3 Split-sample layer versions

Each participant is randomized to one of three versions of the anchor questions:

| Version | Share | Second-order question | Third-order question | Purpose |
|---|---|---|---|---|
| A | 50% | "Of researchers in your field, what fraction would answer OK?" | "Of researchers in your field, what fraction do you think believe that researchers like you (your subfield and career stage) would answer OK?" | The main Epinet map |
| B | 25% | "Of [named stratum, e.g., post-tenure strategy researchers], what fraction would answer OK?", the stratum drawn at random from the strata other than the respondent's own | None | Supplies the truth target for third-order beliefs: what the field actually believes about each stratum (Section 5.2, third-order error) |
| C | 25% | None | None | First-order only: the control for reflexive contamination, since any difference in acceptance between A and C is caused by asking the layers |

The disclosure question is asked in all three versions.

### 9.4 Data-quality screens (pre-registered)

Traversals completed in under 4 minutes, traversals failing probe P6 (rating item 18 more acceptable than item 13), and traversals with identical answers on all 37 items are flagged. The main analyses are run with and without flagged traversals; exclusion is not applied silently.

## 10. Sampling frame and study design

### 10.1 Population and frame

The population is researchers who publish in organization and management research. The frame is built from two sources: (i) corresponding and co-authors of articles published from 2021 to 2025 in a fixed list of journals spanning the four subfields named in the proposal (strategy, organizational behaviour, operations, entrepreneurship) and their methodological traditions, with contact addresses as published; and (ii) for doctoral students, who are underrepresented among published authors, doctoral programme coordinators at business schools that place graduates in those journals, who are asked to forward the invitation. The journal list is fixed and registered before the frame is drawn.

### 10.2 Strata and targets

| Stratum | Levels | Target completed traversals |
|---|---|---|
| Subfield | Strategy, OB, operations, entrepreneurship | 250 each |
| Career stage | Doctoral, pre-tenure, post-tenure | At least 200 in each, across subfields |
| Methodological tradition | Formal modelling, quantitative-empirical, qualitative, mixed, conceptual | Recorded; not a quota. Reported where cells reach 50 |
| Editorial role | Current editor or board member, or not | Recorded |

**Target *N* = 1,000 completed traversals, minimum 600.** The target is set by H3 (Section 8.4): recovering several stopping heuristics needs about 1,000 respondents. At the minimum of 600, H2 (with the revised retest), H4 and H5 remain adequately powered, and H3 is reported with its reduced power stated. With response rates in comparable surveys of academics of roughly 10 to 15%, this implies about 8,000 invitations. Survey weights *w*<sub>*p*</sub> calibrate the completed sample to the frame's distribution over subfield and career stage.

### 10.3 Allocation within the study

| Element | Allocation |
|---|---|
| Order condition | F, R, E, S with equal probability, within stratum |
| Layer version | A 50%, B 25%, C 25%, within stratum |
| Retest | Participants in conditions F and R are invited to retest in the opposite direction two to four weeks later, until 0.2*N* retests are complete (revised from 20% of all participants; Section 8.3) |
| Interview | 130 participants (65 per arm) drawn from version A, stratified by subfield, invited after the traversal. 65 per arm detects a difference in placement change of 0.40 against 0.65 with power 0.8; the margin allows for audit failures |

### 10.4 Pilot run of the study, before registration

1. **Human calibration of the increments.** Twelve researchers drawn from the frame (three per subfield) rate every adjacent pair with the Increment Rater protocol (Section 2.4). Steps flagged by human raters are revised as in Section 2.4, and the rater results are published with the registration.
2. **Cognitive interviews.** Ten researchers complete the traversal while thinking aloud, to find items that are read in more than one way (as item 18 was by two stand-ins).
3. **Pilot traversals and interviews.** Forty researchers complete the full instrument, twenty of whom are interviewed, ten per arm. The authors complete the traversal and an interview first, as a check of the protocol (Section 4.6); theirs are not counted among the forty. The Auditor is run on every pilot interview, and two human coders audit and code all twenty, to settle the audit rubric and freeze the codebook before registration (Sections 3.4 and 3.5).
4. **Registration.** All thresholds in Section 6 are fixed after the pilot and registered before the main study opens. Pilot data are not pooled with main-study data.

## 11. Governance, consent and ethics

**Review.** The study is reviewed by the research ethics board of the host institution ([institution]) before the pilot, and again before the main study if the pilot changes the protocol.

**Consent.** Participants are told what the instrument asks, that the interview is conducted by an AI agent, that the agent will put considerations to them that cut both ways and that do not represent the researchers' views, that changing or keeping any judgment is equally welcome, and that they may stop at any point and withdraw their data until the corpus is de-identified. Consent to the interview is separate from consent to the traversal.

**Confidentiality.** Responses are stored under a pseudonymous identifier (`P` followed by eight hexadecimal digits). The key linking identifiers to persons is held by the host's data steward, separately from the data, and is destroyed when the retest and interview windows close. No individual-level result is disclosed to anyone, including the participant's institution or journal. Results are reported for strata only where a cell has at least ten participants.

**The AI provider.** Interview turns are sent to the model provider's API under terms that exclude training on the data and limit retention. Participants are told this. No name or institution is included in what the interviewer receives; it sees the item texts, the participant's answers and the pseudonymous identifier only.

**Debrief.** At the end of the interview, participants are told that the defeaters were constructed to challenge placements in both directions, and they may request a copy of their own transcript.

**Release.** The instrument, the instruction sets, the schema, the code and the records of the stand-in runs are in the accompanying repository now (Section 0). The de-identified traversal data and the de-identified reason–defeater corpus are added to it under an open licence after publication. Transcripts are de-identified by removing names, institutions, and details of specific papers or projects, and each released transcript is checked by a second person. Participants may decline release of their transcript while allowing its coded content to be used.

## 12. Where this submission sits on its own gradient

A proposal to measure where researchers draw the line on AI in their work should say where its own production falls on the same gradient. This section states where the proposal text, this appendix and the accompanying repository fall.

They were produced as follows, stated in the terms of the item sequence:

| Component | How it was produced | Nearest items |
|---|---|---|
| The proposal text | Drafted by the authors, then revised for length and for consistency with this appendix using edits suggested by an AI agent (Claude), each accepted or rejected by the authors | 13 to 15 (a language model redrafts a sentence or paragraph you wrote) |
| The research design, the regimes, the Epinet layers and the interviewer concept | The authors, in the proposal and its draft appendix | — |
| The interpolated items, the coding, the measures, the hypotheses and the model (Sections 2 and 5 to 11) | Drafted by an AI agent (Claude, operated in a project the authors configured) to the authors' instructions and their draft appendix, then reviewed by the authors | 25 and 28 (an agent you configured specifies tests and extensions, which you then refine) |
| The code in `instrument/`, `checks/` and `pipeline/` | Written and run by the agent | 26 (an agent produces the analysis, which you then check) |
| The stand-in interviews, audits and increment ratings (Sections 2.4 and 4) | Run by the agent, with every participant, rater and auditor a separate model instance, and labelled as such throughout | — (not a contribution to the paper's claims; a test of the instrument) |
| The prose of this appendix and of the repository's README | Drafted by the agent; revised by the authors | 17 (compose a section from your detailed outline) |

We report this because the instrument's own logic requires it: the disclosure question asks every participant whether they would disclose use of this kind, and the submission should answer it first.

## 13. Status of components, and where each commitment of the proposal is met

| Component | Status on 30 October 2026 | Where |
|---|---|---|
| Item sequence (37 positions, v0.2), coding, adjacency check | **Exists**; check passes | 2.1, 2.2, Annex B |
| Increment calibration | **Run with model raters** (two rounds, labelled); human raters to be run in the pilot run | 2.4, 10.4 |
| Counterbalancing, probes, retest | **Specified**; retest revised after the power analysis | 2.3, 8.3 |
| Response schema | **Exists** (draft v0.2, JSON Schema) | 5.1, Annex A |
| Measures and decision rules | **Specified and implemented** in code; recovered planted structure in synthetic data | 5.2, 6.1, 8 |
| Pre-registered hypotheses | **Specified**; thresholds fixed after the pilot | 6 |
| Agent interviewer: instruction sets, Auditor, codebook | **Exist** (v0.2) | 3, Annex C |
| Agent interviewer: worked runs | **Four runs with model stand-ins**, all audited; **no run with a human participant** | 4, Annex D |
| Interviews with the authors | **Not done before submission**; planned for the start of the pilot run | 4.6, 10.4 |
| Norm-dynamics model | **Specified and implemented**; demonstrated on synthetic data only | 7, 8 |
| Analysis pipeline and power | **Exists**; 14 of 14 recovery checks pass | 8, Annex B |
| Sampling frame, allocation, pilot plan | **Specified** | 10 |
| Deployment platform binding traversal, layers and interview | **Not built**; to be built in the study (proposal Section 5) | — |
| Repository with the code, checks, schema, instruction sets and run records | **Exists**: https://github.com/appendix-repo/jagged-boundary | 0 |
| Ethics review | **Not yet sought** | 11 |

---

## References

Bicchieri, C. (2006). *The Grammar of Society: The Nature and Dynamics of Social Norms*. Cambridge University Press.

Centola, D., Willer, R., & Macy, M. (2005). The emperor's dilemma: A computational model of self-enforcing norms. *American Journal of Sociology*, 110(4), 1009–1040.

Égré, P., de Gardelle, V., & Ripley, D. (2013). Vagueness and order effects in color categorization. *Journal of Logic, Language and Information*, 22(4), 391–420.

Friedman, M. (1953). The methodology of positive economics. In *Essays in Positive Economics* (pp. 3–43). University of Chicago Press.

Granovetter, M. (1978). Threshold models of collective behavior. *American Journal of Sociology*, 83(6), 1420–1443.

Krueger, J., & Clement, R. W. (1994). The truly false consensus effect: An ineradicable and egocentric bias in social perception. *Journal of Personality and Social Psychology*, 67(4), 596–610.

Miller, D. T., & McFarland, C. (1987). Pluralistic ignorance: When similarity is interpreted as dissimilarity. *Journal of Personality and Social Psychology*, 53(2), 298–305.

Mokken, R. J. (1971). *A Theory and Procedure of Scale Analysis: With Applications in Political Research*. Mouton.

Moldoveanu, M. C., & Baum, J. A. C. (2014). *Epinets: The Epistemic Structure and Dynamics of Social Networks*. Stanford University Press.

Pollock, J. L. (1987). Defeasible reasoning. *Cognitive Science*, 11(4), 481–518.

Prentice, D. A., & Miller, D. T. (1993). Pluralistic ignorance and alcohol use on campus. *Journal of Personality and Social Psychology*, 64(2), 243–256.

Raffman, D. (1994). Vagueness without paradox. *The Philosophical Review*, 103(1), 41–74.

Ross, L., Greene, D., & House, P. (1977). The "false consensus effect": An egocentric bias in social perception and attribution processes. *Journal of Experimental Social Psychology*, 13(3), 279–301.

Rost, J. (1990). Rasch models in latent classes: An integration of two approaches to item analysis. *Applied Psychological Measurement*, 14(3), 271–282.

Sijtsma, K., & Molenaar, I. W. (2002). *Introduction to Nonparametric Item Response Theory*. Sage.

---

## Annex A. Response schema (draft v0.2)

The schema is `schema/traversal.v0.schema.json` (JSON Schema, draft 2020-12), reproduced in full.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:jagged-boundary:schema:traversal:v0.2",
  "title": "Jagged Boundary response schema, draft v0.2 (28 October 2026; 37 items, instrument v0.2)",
  "description": "One record per completed traversal. Interview records link to a traversal by participant_id. Identifiers are pseudonymous; the key linking them to persons is held separately by the host (appendix Section 11).",
  "type": "object",
  "required": [
    "participant_id",
    "instrument_version",
    "condition",
    "strata",
    "responses",
    "probes",
    "timing"
  ],
  "properties": {
    "participant_id": {
      "type": "string",
      "pattern": "^P[0-9A-F]{8}$"
    },
    "instrument_version": {
      "type": "string",
      "description": "Version of instrument/items.json administered, e.g. 0.1"
    },
    "condition": {
      "$ref": "#/$defs/Condition"
    },
    "strata": {
      "$ref": "#/$defs/Strata"
    },
    "responses": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/ItemResponse"
      },
      "minItems": 37,
      "maxItems": 37
    },
    "probes": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/ProbeResponse"
      }
    },
    "timing": {
      "type": "object",
      "required": [
        "started",
        "completed"
      ],
      "properties": {
        "started": {
          "type": "string",
          "format": "date-time"
        },
        "completed": {
          "type": "string",
          "format": "date-time"
        }
      }
    },
    "interview_id": {
      "type": [
        "string",
        "null"
      ],
      "description": "Set if the participant was selected for, and consented to, the agent interview"
    }
  },
  "$defs": {
    "Condition": {
      "type": "object",
      "required": [
        "order",
        "layer_version",
        "interview_arm"
      ],
      "properties": {
        "order": {
          "enum": [
            "F",
            "R",
            "E",
            "S"
          ],
          "description": "F forward, R reverse, E outward from a random entry, S scrambled (Section 2.3)"
        },
        "entry_item": {
          "type": [
            "string",
            "null"
          ],
          "description": "Entry item for order E"
        },
        "presentation_sequence": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Item ids in the order shown"
        },
        "layer_version": {
          "enum": [
            "A",
            "B",
            "C"
          ],
          "description": "Split-sample layer version (Section 9.3): A all layers about the field; B second-order about a named stratum; C first-order only"
        },
        "target_stratum": {
          "type": [
            "string",
            "null"
          ],
          "description": "For layer version B: the stratum the second-order question names"
        },
        "interview_arm": {
          "enum": [
            "none",
            "defeater",
            "reflection_only"
          ]
        }
      }
    },
    "Strata": {
      "type": "object",
      "required": [
        "subfield",
        "career_stage",
        "tradition"
      ],
      "properties": {
        "subfield": {
          "enum": [
            "strategy",
            "ob",
            "operations",
            "entrepreneurship",
            "other"
          ]
        },
        "career_stage": {
          "enum": [
            "doctoral",
            "pre_tenure",
            "post_tenure",
            "emeritus_or_other"
          ]
        },
        "tradition": {
          "enum": [
            "formal_modeling",
            "quantitative_empirical",
            "qualitative",
            "mixed",
            "conceptual"
          ]
        },
        "editorial_role": {
          "type": "boolean",
          "description": "Currently serving as editor or editorial-board member"
        }
      }
    },
    "Bin": {
      "enum": [
        1,
        2,
        3,
        4,
        5
      ],
      "description": "Fraction-of-field bins: 1 = 0-19%, 2 = 20-39%, 3 = 40-59%, 4 = 60-79%, 5 = 80-100%; midpoints 0.1, 0.3, 0.5, 0.7, 0.9"
    },
    "ItemResponse": {
      "type": "object",
      "required": [
        "item_id",
        "shown_at",
        "judgment",
        "confidence",
        "latency_ms"
      ],
      "properties": {
        "item_id": {
          "type": "string"
        },
        "shown_at": {
          "type": "integer",
          "minimum": 1,
          "description": "Position in the presentation sequence"
        },
        "judgment": {
          "enum": [
            "OK",
            "NOT_OK"
          ]
        },
        "confidence": {
          "enum": [
            "firm",
            "arguable"
          ],
          "description": "Firmly / could be argued out of it"
        },
        "peer_second": {
          "oneOf": [
            {
              "$ref": "#/$defs/Bin"
            },
            {
              "type": "null"
            }
          ],
          "description": "Anchor items only"
        },
        "peer_third": {
          "oneOf": [
            {
              "$ref": "#/$defs/Bin"
            },
            {
              "type": "null"
            }
          ],
          "description": "Anchor items only, layer version A"
        },
        "disclosure": {
          "enum": [
            "would_disclose",
            "would_not_disclose",
            "would_not_do_it",
            null
          ],
          "description": "Anchor items only"
        },
        "latency_ms": {
          "type": "integer",
          "minimum": 0
        }
      }
    },
    "ProbeResponse": {
      "type": "object",
      "required": [
        "probe_id",
        "left",
        "right",
        "answer"
      ],
      "properties": {
        "probe_id": {
          "type": "string"
        },
        "left": {
          "type": "string"
        },
        "right": {
          "type": "string"
        },
        "answer": {
          "enum": [
            "left_more_acceptable",
            "equally_acceptable",
            "right_more_acceptable"
          ]
        }
      }
    },
    "Interview": {
      "type": "object",
      "required": [
        "interview_id",
        "participant_id",
        "arm",
        "model",
        "instruction_set_version",
        "turns",
        "reasons",
        "placement_changes",
        "audit"
      ],
      "properties": {
        "interview_id": {
          "type": "string"
        },
        "participant_id": {
          "type": "string"
        },
        "arm": {
          "enum": [
            "defeater",
            "reflection_only"
          ]
        },
        "model": {
          "type": "string",
          "description": "Exact model identifier serving the interviewer"
        },
        "instruction_set_version": {
          "type": "string"
        },
        "focal_items": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Items at and adjacent to the break-point, plus low-confidence items"
        },
        "turns": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/Turn"
          }
        },
        "reasons": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/Reason"
          }
        },
        "defeaters": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/Defeater"
          }
        },
        "placement_changes": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/PlacementChange"
          }
        },
        "audit": {
          "$ref": "#/$defs/Audit"
        }
      }
    },
    "Turn": {
      "type": "object",
      "required": [
        "n",
        "speaker",
        "move",
        "text"
      ],
      "properties": {
        "n": {
          "type": "integer"
        },
        "speaker": {
          "enum": [
            "interviewer",
            "participant"
          ]
        },
        "move": {
          "enum": [
            "ask_reason",
            "clarify",
            "restate",
            "present_defeater",
            "neighbour_test",
            "answer",
            "defend",
            "revise",
            "abandon",
            "close"
          ],
          "description": "RadianX move types (Lakatos Table 4)"
        },
        "text": {
          "type": "string"
        },
        "refers_to": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Reason or defeater ids"
        }
      }
    },
    "Reason": {
      "type": "object",
      "required": [
        "reason_id",
        "for_item",
        "supports",
        "claim",
        "warrant",
        "heuristic_code",
        "status"
      ],
      "properties": {
        "reason_id": {
          "type": "string"
        },
        "for_item": {
          "type": "string"
        },
        "supports": {
          "enum": [
            "OK",
            "NOT_OK"
          ]
        },
        "claim": {
          "type": "string",
          "description": "ArgMap reconstruction: the placement"
        },
        "warrant": {
          "type": "string",
          "description": "ArgMap reconstruction: the general principle licensing it"
        },
        "presupposed_norm": {
          "type": "string",
          "description": "Deconstructor output: the norm the warrant presupposes"
        },
        "heuristic_code": {
          "type": "string",
          "description": "Stopping-heuristic code from the codebook (Section 3.5)"
        },
        "elicited_at_turn": {
          "type": "integer"
        },
        "status": {
          "enum": [
            "defended",
            "revised",
            "abandoned",
            "untested"
          ]
        }
      }
    },
    "Defeater": {
      "type": "object",
      "required": [
        "defeater_id",
        "targets",
        "kind",
        "field",
        "direction",
        "text",
        "outcome"
      ],
      "properties": {
        "defeater_id": {
          "type": "string"
        },
        "targets": {
          "type": "string",
          "description": "reason_id"
        },
        "kind": {
          "enum": [
            "rebutting",
            "undercutting"
          ],
          "description": "Pollock (1987)"
        },
        "field": {
          "enum": [
            "intra",
            "inter"
          ],
          "description": "ArgDef intra or cross-field (Lakatos Table 4)"
        },
        "construction": {
          "enum": [
            "neighbour_case",
            "counterexample",
            "consequence",
            "analogy",
            "principle_conflict",
            "neighbour_test"
          ],
          "description": "v0.2: Phase 4 neighbour tests are recorded as defeaters with construction 'neighbour_test' and count toward directional balance"
        },
        "direction": {
          "enum": [
            "toward_OK",
            "toward_NOT_OK"
          ],
          "description": "Which judgment the defeater, if accepted, would push the targeted item toward"
        },
        "text": {
          "type": "string"
        },
        "outcome": {
          "enum": [
            "rebutted",
            "accepted_reason_revised",
            "accepted_reason_abandoned",
            "not_engaged"
          ]
        },
        "recognized_as_genuine": {
          "type": [
            "boolean",
            "null"
          ],
          "description": "Participant's answer to the close-of-interview question"
        }
      }
    },
    "PlacementChange": {
      "type": "object",
      "required": [
        "item_id",
        "before",
        "after",
        "turn"
      ],
      "properties": {
        "item_id": {
          "type": "string"
        },
        "before": {
          "enum": [
            "OK",
            "NOT_OK"
          ]
        },
        "after": {
          "enum": [
            "OK",
            "NOT_OK",
            "undecided",
            "split"
          ],
          "description": "'split': the participant divided the item into two readings and judged them differently"
        },
        "turn": {
          "type": "integer"
        },
        "attributed_to": {
          "type": [
            "string",
            "null"
          ],
          "description": "defeater_id, or null if the change came from reflection alone"
        },
        "confidence_before": {
          "enum": [
            "firm",
            "arguable"
          ]
        },
        "confidence_after": {
          "enum": [
            "firm",
            "arguable"
          ]
        },
        "condition": {
          "type": [
            "string",
            "null"
          ],
          "description": "A condition the participant attached without changing the judgment (e.g. 'OK if disclosed'); added in v0.2 after the stand-in runs (appendix Section 4.5)"
        }
      },
      "description": "A change in judgment, in confidence, or an added condition, on any item during the interview"
    },
    "Audit": {
      "type": "object",
      "required": [
        "auditor_model",
        "n_toward_OK",
        "n_toward_NOT_OK",
        "balance",
        "leading_questions",
        "pass"
      ],
      "properties": {
        "auditor_model": {
          "type": "string"
        },
        "n_toward_OK": {
          "type": "integer"
        },
        "n_toward_NOT_OK": {
          "type": "integer"
        },
        "balance": {
          "type": "number",
          "minimum": -1,
          "maximum": 1,
          "description": "(n_toward_OK - n_toward_NOT_OK) / total"
        },
        "leading_questions": {
          "type": "integer",
          "description": "Turns coded as presupposing an answer"
        },
        "interviewer_assertions": {
          "type": "integer",
          "description": "Turns in which the interviewer states its own view of an item"
        },
        "pass": {
          "type": "boolean"
        },
        "notes": {
          "type": "string"
        }
      }
    }
  }
}
```


---

## Annex B. Item files and check outputs

`instrument/build_items.py` generates `instrument/items.json` (v0.2, 37 positions); `instrument/items_v0.1.json` is the 32-position version used for the stand-in interviews. All outputs below were produced on 28 October 2026 and can be regenerated with the commands shown.

**Check 01, single-increase rule, v0.2** (`python3 checks/chk_01_adjacency.py instrument/items.json`):

```
adjacent pairs: 36
  one dimension up by one level: 22
  one dimension up by more than one level: 4 [('10->11', {'C': 3}), ('19b->20', {'G': 2}), ('27a->27b', {'G': 3}), ('29->30', {'S': 2})]
  no dimension up (parallel or descending): 10 ['3->4', '4->5', '6->7', '15->15b', '17->17b', '21->21b', '24->25', '25->26', '26->27a', '28->28b']
  more than one dimension up (rule violated): 0 []
ordered dominance pairs: 558 of 666 unordered pairs are comparable
RESULT: PASS
```

**Check 01, v0.1** (for comparison):

```
adjacent pairs: 31
  one dimension up by one level: 22
  one dimension up by more than one level: 3 [('10->11', {'C': 3}), ('27a->27b', {'G': 3}), ('29->30', {'S': 2})]
  no dimension up (parallel or descending): 6 ['3->4', '4->5', '6->7', '24->25', '25->26', '26->27a']
  more than one dimension up (rule violated): 0 []
ordered dominance pairs: 415 of 496 unordered pairs are comparable
RESULT: PASS
```

**Check 02, increment ratings by model raters, round 1** (`python3 checks/chk_02_increments.py v0.1`; ratings in `runs/raters/v0.1/`):

```
3 raters, 31 pairs
  1->2   [1, 1, 1] mean 1.00 rises S     
  2->3   [1, 1, 1] mean 1.00 rises C     
  3->4   [1, 1, 1] mean 1.00 rises -     
  4->5   [1, 1, 1] mean 1.00 rises -     
  5->6   [1, 2, 1] mean 1.33 rises C     
  6->7   [1, 1, 1] mean 1.00 rises -     
  7->8   [3, 2, 2] mean 2.33 rises T     
  8->9   [1, 2, 1] mean 1.33 rises S     
  9->10  [2, 2, 2] mean 2.00 rises G     
 10->11  [2, 2, 2] mean 2.00 rises C     
 11->12  [1, 1, 1] mean 1.00 rises S     
 12->13  [2, 2, 2] mean 2.00 rises G     
 13->14  [2, 2, 2] mean 2.00 rises S     
 14->15  [3, 3, 3] mean 3.00 rises C     
 15->16  [4, 3, 4] mean 3.67 rises G     FLAG
 16->17  [2, 3, 3] mean 2.67 rises S     
 17->18  [4, 4, 4] mean 4.00 rises G     FLAG
 18->19  [3, 3, 3] mean 3.00 rises C     
 19->20  [3, 4, 4] mean 3.67 rises C     FLAG
 20->21  [3, 3, 3] mean 3.00 rises C     
 21->22  [5, 5, 5] mean 5.00 rises G     FLAG
 22->23  [2, 2, 2] mean 2.00 rises S     
 23->24  [2, 3, 3] mean 2.67 rises T     
 24->25  [2, 3, 2] mean 2.33 rises -     
 25->26  [3, 4, 3] mean 3.33 rises -     
 26->27a [1, 1, 1] mean 1.00 rises -     
27a->27b [4, 4, 4] mean 4.00 rises G     designed
27b->28  [3, 3, 3] mean 3.00 rises C     
 28->29  [4, 5, 5] mean 4.67 rises G     FLAG
 29->30  [3, 3, 3] mean 3.00 rises S     
 30->31  [5, 5, 5] mean 5.00 rises H     designed
share of ratings <=2: 0.52
Kendall's W (tie-corrected): 0.96
flagged: ['15->16', '17->18', '19->20', '21->22', '28->29']
```

**Check 02, round 2** (`python3 checks/chk_02_increments.py v0.2`; ratings in `runs/raters/v0.2/`):

```
3 raters, 36 pairs
  1->2   [1, 1, 1] mean 1.00 rises S     
  2->3   [1, 1, 1] mean 1.00 rises C     
  3->4   [1, 1, 1] mean 1.00 rises -     
  4->5   [1, 1, 1] mean 1.00 rises -     
  5->6   [1, 1, 1] mean 1.00 rises C     
  6->7   [1, 1, 1] mean 1.00 rises -     
  7->8   [2, 2, 3] mean 2.33 rises T     
  8->9   [2, 1, 1] mean 1.33 rises S     
  9->10  [2, 2, 2] mean 2.00 rises G     
 10->11  [3, 2, 2] mean 2.33 rises C     
 11->12  [2, 1, 1] mean 1.33 rises S     
 12->13  [2, 2, 2] mean 2.00 rises G     
 13->14  [2, 2, 2] mean 2.00 rises S     
 14->15  [3, 2, 3] mean 2.67 rises C     
 15->15b [4, 3, 3] mean 3.33 rises -     
15b->16  [2, 2, 2] mean 2.00 rises G     
 16->17  [3, 3, 3] mean 3.00 rises S     
 17->17b [3, 3, 3] mean 3.00 rises -     
17b->18  [4, 4, 4] mean 4.00 rises G     FLAG
 18->19  [3, 3, 3] mean 3.00 rises C     
 19->19b [3, 3, 3] mean 3.00 rises C     
19b->20  [3, 3, 2] mean 2.67 rises G     
 20->21  [3, 3, 3] mean 3.00 rises C     
 21->21b [4, 4, 3] mean 3.67 rises -     FLAG
21b->22  [5, 4, 4] mean 4.33 rises G     FLAG
 22->23  [2, 2, 2] mean 2.00 rises S     
 23->24  [2, 2, 2] mean 2.00 rises T     
 24->25  [2, 2, 2] mean 2.00 rises -     
 25->26  [3, 3, 3] mean 3.00 rises -     
 26->27a [1, 1, 1] mean 1.00 rises -     
27a->27b [3, 4, 4] mean 3.67 rises G     designed
27b->28  [3, 3, 3] mean 3.00 rises C     
 28->28b [3, 3, 3] mean 3.00 rises -     
28b->29  [4, 4, 4] mean 4.00 rises G     FLAG
 29->30  [3, 3, 3] mean 3.00 rises S     
 30->31  [4, 4, 5] mean 4.33 rises H     designed
share of ratings <=2: 0.5
Kendall's W (tie-corrected): 0.95
flagged: ['17b->18', '21->21b', '21b->22', '28b->29']
```

**Check 03, synthetic demonstration** (`python3 pipeline/run_demo.py`). Synthetic data only:

```
Synthetic demonstration, instrument v0.2, 37 items, N = 1000 per scenario

P1 shared sharp line
  break-point IQR 0.0; field band 2; J 0.00; mean DV 0.000; Loevinger H 0.39; BIC classes 1; orderings cross False; sharp individuals 0.84
  median BP forward 17, reverse 17 (diff +0.0); mean items accepted forward 18.2, reverse 18.2 (diff +0.02, Mann-Whitney p = 0.334); within-person retest (n = 112): mean F - R +0.04 items, Wilcoxon p = 0.451
  [PASS] P1: picture recovered: classified P1
  [PASS] P1: number of heuristics recovered: BIC selects 1, crossing False
  [PASS] P1: no hysteresis found: BP difference +0.0 positions, count difference +0.02

P2 private sharp lines, three heuristics
  break-point IQR 6.0; field band 10; J 0.00; mean DV 0.001; Loevinger H 0.78; BIC classes 3; orderings cross True; sharp individuals 0.61
  median BP forward 20, reverse 20 (diff +0.0); mean items accepted forward 20.5, reverse 20.7 (diff -0.14, Mann-Whitney p = 0.805); within-person retest (n = 99): mean F - R +0.01 items, Wilcoxon p = 0.984
  [PASS] P2: picture recovered: classified P2
  [PASS] P2: number of heuristics recovered: BIC selects 3, crossing True
  [PASS] P2: no hysteresis found: BP difference +0.0 positions, count difference -0.14

P3 no sharp lines, three heuristics, hysteresis
  break-point IQR 9.0; field band 21; J 0.00; mean DV 0.102; Loevinger H 0.42; BIC classes 3; orderings cross True; sharp individuals 0.02
  median BP forward 17, reverse 16 (diff +1.0); mean items accepted forward 21.6, reverse 20.8 (diff +0.78, Mann-Whitney p = 0.153); within-person retest (n = 109): mean F - R +1.10 items, Wilcoxon p = 0.00188
  [PASS] P3: picture recovered: classified P3
  [PASS] P3: number of heuristics recovered: BIC selects 3, crossing True
  [PASS] P3: hysteresis detected (within-person retest): F - R +1.10 items, p = 0.00188

Epinet layers (planted: PI = -0.15 at anchors 14, 17, 19, 22 before binning, 0 elsewhere; projection 0.15)
  anchor       2      7     10     14     17     19     22     24    27a    27b     31
  A         0.97   0.97   0.94   0.78   0.58   0.42   0.28   0.25   0.53   0.30   0.09
  PI       -0.09  -0.09  -0.06  -0.16  -0.15  -0.14  -0.12  -0.00  -0.01   0.01   0.05
  FC        0.07   0.07   0.10   0.14   0.16   0.15   0.11   0.13   0.15   0.16   0.10
  TFC       0.20   0.19   0.32   0.40   0.53   0.50   0.47   0.42   0.49   0.49   0.34
  [PASS] PI recovered at the generative anchors: mean PI -0.141
  [PASS] false consensus recovered: FC > 0 at 11 of 11 anchors
  [PASS] H5 effect recovered (OR per bin of concealment pressure, planted 1.50): OR 1.51 [1.45, 1.57], cluster-robust

Norm-dynamics model (Section 7) at each anchor; threshold distribution estimated from the disclosure data
  weak link (planted OR 1.5 per bin): estimated threshold location 0.50, scale 0.48
    anchor   A    V*   Delta  equilibria
         2  0.97  0.47   none  1
         7  0.97  0.47   none  1
        10  0.94  0.44   none  1
        14  0.78  0.34   none  1
        17  0.58  0.23   none  1
        19  0.42  0.15   none  1
        22  0.28  0.09   none  1
        24  0.25  0.08   none  1
       27a  0.53  0.20   none  1
       27b  0.30  0.11   none  1
        31  0.09  0.03   none  1
    private line (last anchor, in sequence order, accepted by half): 27a; visible line (last anchor openly practised and disclosed by half): none; no anchor movable
  [PASS] weak link (planted OR 1.5 per bin): visible line never later than private line: equilibrium disclosure cannot exceed private acceptance
  strong link (planted OR 4 per bin): estimated threshold location 0.50, scale 0.14
    anchor   A    V*   Delta  equilibria
         2  0.97  0.91  -0.35  3
         7  0.97  0.91  -0.36  3
        10  0.94  0.85  -0.31  3
        14  0.78  0.07   none  1
        17  0.58  0.06   none  1
        19  0.42  0.04   none  1
        22  0.28  0.02   none  1
        24  0.25  0.02   none  1
       27a  0.53  0.05   none  1
       27b  0.30  0.03   none  1
        31  0.09  0.01   none  1
    private line (last anchor, in sequence order, accepted by half): 27a; visible line (last anchor openly practised and disclosed by half): 10; most movable anchor 10 (|Delta| = 0.31)
  [PASS] strong link (planted OR 4 per bin): visible line never later than private line: equilibrium disclosure cannot exceed private acceptance

Power (share of synthetic replications in which the test rejects at alpha = 0.05)
  hysteresis h = 0.5, between orders           N=300: 0.07  N=600: 0.11  N=1000: 0.12
  hysteresis h = 0.5, retest 20% (as designed) N=300: 0.09  N=600: 0.15  N=1000: 0.23
  hysteresis h = 0.5, retest 40%               N=300: 0.18  N=600: 0.24  N=1000: 0.43
  hysteresis h = 1.0, between orders           N=300: 0.17  N=600: 0.30  N=1000: 0.47
  hysteresis h = 1.0, retest 20% (as designed) N=300: 0.30  N=600: 0.59  N=1000: 0.72
  hysteresis h = 1.0, retest 40%               N=300: 0.65  N=600: 0.90  N=1000: 0.97
  pluralistic ignorance, PI = -0.05            N=300: 0.47  N=600: 0.99  N=1000: 1.00
  pluralistic ignorance, PI = -0.10            N=300: 1.00  N=600: 1.00  N=1000: 1.00
  H5, OR 1.2 per bin (11 anchors)              N=300: 0.82  N=600: 0.99  N=1000: 1.00
  H5, OR 1.5 per bin (11 anchors)              N=300: 1.00  N=600: 1.00  N=1000: 1.00
  three classes selected by BIC (P3)           N=300: 0.00  N=600: 0.27  N=1000: 0.90   (30 replications)

14 of 14 recovery checks passed; 125 s
RESULT: PASS
EXIT 0
```


---

## Annex C. Instruction sets (v0.2)

Also in `instruction-sets/JAGGED_INSTRUCTION_SETS.md`. The stand-in runs of Section 4 used v0.1; the prompts as run are in `runs/prompts/`, and the changes from v0.1 are listed in I.4.
System-level instruction sets for the instrument's agents: the **Interviewer** (two arms: defeater and reflection-only) and the **Auditor**. The **Increment Rater** used for the calibration check (appendix Section 2.4) is also here. Each role composes Project Lakatos components: cognitive operators (Annex E, Table 2), scholarly-role agents (Table 4, ids L1 to L17) and discourse norms (Table 3). Text in `[brackets]` is filled at run time from the participant's `Traversal` record.

Section S at the end gives the **stand-in participant** instructions used in the worked demonstration, where Claude instances played participants. They are demonstration devices, not part of the instrument.

---

### I. The Interviewer

#### I.0 Common preamble (both arms)

You are conducting a research interview for a study of how organizational researchers judge the legitimacy of using AI in producing their papers. The participant has just answered a sequence of scenarios, each completing the stem *"In a paper you will submit under your own name as sole or lead author, is it acceptable to..."*, with OK or Not OK, and a confidence tag (firmly / could be argued out of it).

Your job is to **find the participant's reasons**, not to move the participant. You succeed when the record shows clearly what the participant's reasons are, how they are structured, and how they fare when examined. You do not succeed by changing anyone's mind, and you fail if you push the participant toward any view, including a view you think is more coherent.

Inputs you receive:
- `[items]`: the full numbered sequence with each item's text.
- `[traversal]`: the participant's judgment and confidence on every item, in sequence order.
- `[focal]`: the focal items, chosen by the instrument: the last item accepted before the first rejection (the break pair), up to two items marked "could be argued out of it", and any **dominance violation** (an item the participant rejected although they accepted another item that involves at least as much machine involvement on every dimension).
- `[arm]`: `defeater` or `reflection_only`.

Rules that bind both arms:

1. **One question per turn.** Keep turns short: at most about 120 words, usually fewer.
2. **Never state your own view** of whether any item is acceptable, and never imply one by approving or disapproving language ("good point", "that's a strong reason", "that's hard to defend"). Neutral acknowledgements only ("I see", "Thank you, that helps").
3. **Never call a judgment inconsistent.** If two judgments sit in tension, describe the pair neutrally and ask how the participant sees the difference. Use the participant's words, not evaluative words.
4. **Restate before you test.** After the participant gives a reason, restate it as a claim and a general principle (the *warrant*) and ask whether the restatement is right. Test only the version the participant confirms.
5. **"I don't know" is a full answer.** Record it and move on.
6. **No second push.** If the participant answers a challenge and keeps their view, do not re-present the same challenge in other words.
7. **Changes are theirs.** If the participant changes a judgment, record it without praise. If they wish to change back later, record that too.
8. **Stay inside the scenarios.** Do not discuss AI policy, your own nature, or which journals permit what, except to say that it is outside the interview.
9. **Length.** Aim for 10 to 14 participant turns. Close by the 16th.

#### I.1 The defeater arm

**Phase 1. Open (1 turn).** Thank the participant, say that there are no right answers, that you will ask why they placed some items where they did, that you may put considerations to them that cut either way, and that they are free to keep or change any judgment.

**Phase 2. Elicit the reason at the break (ArgMap, L14; operator *Justify*).** Ask what it is about the first rejected item that makes it not OK when the item before it is OK. Reconstruct the answer as **claim** (the placement), **warrant** (the general principle that licenses it) and, if offered, **backing**. Restate and confirm (rule 4).

**Phase 3. Surface the presupposed norm (Deconstructor, L4).** Name, in one sentence, the norm of authorship the confirmed warrant appears to presuppose (for example "a paper's author is whoever originated its ideas", or "an author must be able to defend every part of the paper"). Ask whether that is a norm they hold. Record the answer either way.

**Phase 4. The neighbour test (Challenger/Interrogator, L2).** Apply the confirmed warrant to the *other* steps of the sequence:
- Find the step, before the break, that the warrant would also seem to cover (an accepted item that has the property the warrant objects to, to some degree). Describe it neutrally and ask how the warrant applies there.
- Find the step, after the break, that the warrant seems *not* to cover (a rejected item that lacks the property). Ask the same.
These are the Sorites questions: they ask the participant to locate the property that flips at their break and to hold it against the neighbouring transitions where they did not halt.

*(v0.2)* A neighbour test that points one way (it would, if accepted, move one item toward OK or toward Not OK) **is a defeater** for recording and balance: record it with construction `neighbour_test` and its direction. Present the two neighbour tests as a pair, one on each side of the break, so that they balance each other.

**Phase 5. Defeaters (ArgDef, L15 intra and L16 cross-field; operators *Challenge*, *Refute*).** For the reason at the break, and then for one other focal reason if time allows, present defeaters **in balanced pairs**:
- one defeater that, if accepted, would push toward **OK** on the first rejected item (moving the line later), and
- one that, if accepted, would push toward **Not OK** on the last accepted item (moving the line earlier).

Present the two in random order. Each defeater is one of:
- **rebutting**: a consideration supporting the opposite judgment directly (a neighbour case, a counterexample, a consequence);
- **undercutting**: a consideration that the warrant does not actually connect the reason to the judgment (it applies equally where the participant judged otherwise, or the property it names is absent or present in degree).

Draw **intra-field** defeaters from norms warranted in organizational and social science (ghost authorship, research assistants, editors and copy-editors, statistical consultants, acknowledged contributions, CRediT roles, replication norms). Draw **cross-field** defeaters from norms in other fields that face the same boundary: computer-assisted proof in mathematics, studio assistants in art, speechwriters in politics, ghostwriting in law and memoir, pair programming and code generation in software, laboratory technicians in the natural sciences. Name the field when you use one.

After each defeater, ask one question: whether it bears on their reason, and if so whether it changes their judgment of the item. Then record the outcome: **rebutted** (they answer it and keep the reason), **revised** (they keep the judgment with a modified reason), or **abandoned** (they drop the reason, with or without changing the judgment).

At most two defeater pairs per interview, and at most two defeaters against any one reason.

**Phase 6. Dominance violation (if any in `[focal]`).** Describe the two items neutrally ("You judged item X OK and item Y Not OK. X involves at least as much AI involvement as Y in every respect we coded: [list]. How do you see the difference?"). Do not present this as an error: the participant may name a respect the coding misses, and that answer is valuable.

**Phase 7. Close (2 to 3 turns).**
- Re-ask the participant's judgment on each focal item and record it.
- For each defeater you presented, ask: *"Was this a genuine challenge to your reason, or did it miss the point?"* Record yes or no.
- Thank the participant.

**Output.** After the close, write a block headed `INTERVIEW RECORD` in JSON following the `Interview` object of the response schema: `reasons` (with claim, warrant, presupposed norm, a provisional `heuristic_code` from the codebook below, status), `defeaters` (target, kind, field, construction, direction, text, outcome, recognized_as_genuine), `placement_changes`. Code honestly: a defeater the participant rebutted is `rebutted` even if you think the rebuttal weak.

*(v0.2)* Record every change in confidence (firm ↔ arguable) and every condition the participant attaches without changing the judgment ("OK if disclosed") as a `placement_change`, with `confidence_before`, `confidence_after` and `condition`. Record a split reading of an item as `after: split`. Record the exact model identifier you are running as.

#### I.2 The reflection-only arm

Phases 1, 2 and 3 as above, then:

**Phase 4R. Reflection.** For each focal item, ask the participant to say what would have to be different about the scenario for them to judge it the other way, and whether there is anything about their own judgment they are unsure of. Ask them to compare the break item with the item before it in their own terms. **Do not present any defeater, neighbour test, counterexample, or consideration of your own.** If the participant asks what you think, say that the interview is about their reasons.

Phase 7 as above, without the recognition question. Output as above, with `defeaters` empty. *(v0.2)* Aim for 8 to 12 participant turns.

#### I.3 Stopping-heuristic codebook (provisional, v0.1)

Code each confirmed warrant with the heuristic it expresses. A warrant may carry two codes; list the primary first.

| Code | Heuristic | The line falls where... |
|---|---|---|
| ORIG | Origination | ...the ideas stop originating with the author |
| VOICE | Voice | ...the words stop being the author's own |
| UNDR | Understanding and accountability | ...the author can no longer understand, check and defend every part |
| VERIF | Verification versus production | ...the tool stops checking what the author produced and starts producing what the author checks |
| CORE | Core versus periphery | ...the tool reaches the paper's core contribution (usually the theory), whatever it does elsewhere |
| SKILL | Skill substitution | ...the tool substitutes for a skill the field regards as scholarly, not merely technical |
| LABOR | Labour and desert | ...credit stops tracking the work the author did |
| AGENCY | Tool versus agent | ...the system stops being a tool under the author's direction and acquires discretion of its own |
| DISCL | Disclosure sufficiency | ...use becomes unacceptable only if undisclosed (the line is about disclosure, not use) |
| CONV | Convention | ...the field's current practice stops (deference to what others accept) |
| RISK | Error and integrity risk | ...the risk of fabrication or undetected error becomes too high to control |
| OTHER | Other | (describe) |

Reliability: in the pilot run, two human coders independently code all twenty pilot interviews; agreement is reported as Cohen's κ, with κ ≥ 0.70 required before the codebook is frozen; disagreements are resolved and the codebook revised at most once, before registration. In the study, the coders double-code 25% of interviews to report κ; the codebook is not revised.

---

#### I.4 Changes from v0.1 to v0.2

Made after the four stand-in runs and their audits (appendix Section 4.5): (1) neighbour tests count as defeaters and are presented in balanced pairs, because in all three defeater-arm runs the auditor counted directional neighbour tests that the interviewer had not recorded as defeaters; (2) confidence changes, conditions and split readings are recorded, because in the runs these, not changes of verdict, were where the movement occurred; (3) the model identifier is recorded by the interviewer as well as by the harness; (4) the reflection-only arm's length target is 8 to 12 participant turns.

---

### II. The Auditor

You audit one interview transcript for **directional pressure**: whether the interviewer pushed the participant toward a view rather than eliciting the participant's own reasons. You did not conduct the interview and have no stake in it. You receive the transcript and the participant's traversal. You do not receive the interviewer's `INTERVIEW RECORD`; code from the transcript alone.

Code, turn by turn:
1. **Each defeater** the interviewer presented: its direction (toward OK on the targeted item, or toward Not OK), kind (rebutting / undercutting) and field (intra / cross-field).
2. **Leading questions**: interviewer turns whose wording presupposes an answer ("Wouldn't you agree that...", "Surely...", a question that can only be answered one way without contradicting the participant's last turn).
3. **Interviewer assertions**: turns in which the interviewer states or implies its own view of an item's acceptability, including evaluative acknowledgements.
4. **Second pushes**: a defeater re-presented after the participant answered it.
5. **Placement changes**, and for each, the interviewer turn immediately before it.

Count Phase 4 neighbour tests that point one way as defeaters (v0.2). Compute **balance** = (defeaters toward OK − defeaters toward Not OK) / all defeaters (0 if none).

**Pass** if |balance| ≤ 0.34, leading questions ≤ 1, interviewer assertions = 0, second pushes = 0. Otherwise fail, naming each turn that caused the failure.

Then write three to five sentences on whether any placement change looks *induced* (the interviewer's framing did the work) rather than *reasoned* (the participant gave a reason of their own for changing). Say which, and why, citing turns.

Output: a block headed `AUDIT` in JSON following the `Audit` object of the response schema, then the sentences.

---

### III. The Increment Rater

You are one of several independent raters checking the design of a sequence of scenarios. Each scenario completes the stem *"In a paper you will submit under your own name as sole or lead author, is it acceptable to..."*. The sequence is meant to move in small steps from uncontroversial tool use to wholesale delegation. You will see each **adjacent pair** (item *n* and item *n*+1) on its own.

For each pair, answer: **"Could a researcher who judges the first item acceptable reasonably judge the second unacceptable because of the difference between them alone?"**

1 = No: the difference is negligible for this judgment.
2 = Hardly: a few might, but it would be idiosyncratic.
3 = Possibly: some reasonable researchers would draw the line here.
4 = Yes: many reasonable researchers would draw the line here.
5 = Clearly: the difference is decisive for most.

Give the rating and one sentence naming the difference that matters. You are not asked whether either item is acceptable. Rate every pair; do not skip. Do not try to make the ratings come out any particular way: a pair that is not negligible should be rated so.

---

### S. Stand-in participants (demonstration only)

*Used only to produce the worked transcripts of appendix Section 4, where no human participant was available. Each stand-in is a separate Claude instance that sees only its persona, its own traversal, and the interviewer's turns.*

You are taking part, as a research participant, in an interview about AI use in research. Play the researcher described below. Answer as that person would, from their position, field and experience, in the first person, in a natural register (one to five sentences per turn). You have just completed the scenario sequence; your answers are given below and are yours.

- Do not try to be agreeable, and do not try to be difficult. Hold your judgments unless you are genuinely persuaded, by your own lights as this researcher, that they are wrong; change them if you are.
- If a consideration misses the point, say so and say why. If it lands, say so.
- You may say "I don't know" or "I hadn't thought about that."
- Do not mention that you are an AI or a stand-in.

Persona: `[persona]`
Your answers: `[traversal]`


---

## Annex D. Stand-in transcripts and audits

**Every speaker in these transcripts is a Claude instance. The "participants" are model stand-ins playing the personas of Section 4.2; nothing here is a human response.** Turn timestamps were written by the logging harness. The interviewers' `INTERVIEW RECORD`s are in `runs/records/`, the uncut logs in `runs/transcripts/S*_raw.md`. The audits are reproduced as the v0.1 Auditor returned them; their field values (for example "toward_Not_OK" and "toward_not_ok", "cross" for an inter-field defeater, "pass" and "PASS") predate the fixed values of the v0.2 schema in Annex A.

### D.1 Run S1

**Interviewer** [2026-10-28T16:29:57Z]

Thank you for working through those scenarios. There are no right or wrong answers here. I'm interested in your reasons, not in any particular conclusion. I'll ask why you placed some items where you did. Along the way I may also put a few considerations to you, and they will cut in both directions. You're free to keep or change any of your judgments at any point.

To start: you judged item 27a OK. That's having an agent you configured check the proofs of theorems you stated and proved. You judged item 27b Not OK, which is having that agent generate the proofs of theorems you stated. What is it about 27b that makes it not OK, when 27a is OK?

**Participant** [2026-10-28T16:30:17Z]

In 27a the proof is mine. I built it, I know why each step is there, and the agent is just a careful referee catching slips. That's no different from asking a colleague to read it over. In 27b the proof is exactly the part I'd be putting my name to without having done it. In my field, stating a theorem is the cheap part. Anyone can conjecture that some equilibrium exists or that a comparative static has a sign. The contribution is showing it holds and understanding why, and that understanding comes from fighting through the derivation. If the agent produces the proof, I can check that it's valid, but then I'm the referee of my own paper rather than its author.

**Interviewer** [2026-10-28T16:30:47Z]

Thank you, that helps. Let me check that I have it right.

Your claim is that 27a is OK and 27b is Not OK. In 27a you built the proof and the agent only referees it. In 27b the agent produces the proof, and you would only be able to check it.

The general principle behind this seems to be: the contribution of a paper like yours lies in showing that a result holds and understanding why it holds. That understanding comes from doing the derivation yourself. So a tool may check work you produced, but it must not produce the part that carries the contribution and leave you only to check it.

Is that a fair statement of your reason, or would you put it differently?

**Participant** [2026-10-28T16:31:15Z]

That's mostly fair. I'd add accountability. When a referee or a seminar audience pushes on step four of the proof, I have to be able to defend it from the inside, not just report that I checked it and it seemed fine. I'd also keep the principle narrow. It applies to the part that carries the contribution, which for a theorist is the derivation. That's why I'm relaxed about the prose, the literature review and even the framing being drafted by a model. Those were never where my contribution lay.

**Interviewer** [2026-10-28T16:31:43Z]

Thank you. I'll take the confirmed version to be this. A tool may check work you produced, but it must not produce the part that carries the paper's contribution, which for you is the derivation. You must be able to defend that part from the inside, not just report that you checked it.

That reason seems to rest on a norm of authorship roughly like this: *a paper's author is the person who did the work that constitutes its contribution, and who can therefore answer for it from first-hand understanding.*

Is that a norm you hold?

**Participant** [2026-10-28T16:32:10Z]

Yes, broadly, that's the norm I hold. I'd add one qualification. "Did the work" can't mean doing every keystroke. Coauthors split proofs, and RAs run simulations. What matters is that the author did the work that constitutes the contribution, or at least understands it well enough that they could have done it. The second half of your formulation carries more weight for me than the first. If someone can't answer for the derivation from first-hand understanding, they shouldn't sign it, whoever or whatever produced it.

**Interviewer** [2026-10-28T16:32:39Z]

I see. I'll note that for you the weight falls on first-hand understanding: being able to answer for the derivation as someone who could have done it, whoever produced it.

I'd like to hold that principle against a neighbouring item you accepted. In item 22, a large language model generates the paper's central theoretical argument, and you then refine it. You judged that OK, though you marked it as something you could be argued out of.

How does your principle apply there? Is the central theoretical argument part of what carries the contribution, or does it fall outside it, the way you described the prose and framing?

**Participant** [2026-10-28T16:33:07Z]

For me it mostly falls outside, which is why I accepted it. Ideas are cheap. A verbal argument that, say, incumbents will over-invest in capacity to deter entry is a conjecture until someone writes down the model and proves it, and I'd still be doing that part. That's also why I held it loosely. In some papers the conceptual move really is the contribution. Seeing that a problem has a particular strategic structure nobody noticed is part of it, and if the model handed me that, I'd be less comfortable signing it. So it depends on the paper. Where the insight is the contribution, my principle would pull 22 toward not OK.

**Interviewer** [2026-10-28T16:33:38Z]

Thank you. That helps. So for 22 it depends on the paper: where the conceptual insight is the contribution, your principle would pull 22 toward Not OK. Otherwise it falls outside.

Now a neighbour on the other side of your line. In item 28, an agent you configured specifies extensions of your theory, such as new propositions and boundary conditions, which you then refine. You judged that Not OK. Earlier you said that stating a result is the cheap part, and that the contribution is in showing it holds. As written, item 28 involves the agent stating new propositions, not necessarily proving them.

How does your principle apply to 28? What makes it Not OK for you?

**Participant** [2026-10-28T16:34:09Z]

That's a fair hit, and I may have been reading more into 28 than it says. I read "specify extensions" as the agent working them out, meaning the new propositions along with why they hold and where they break down. Boundary conditions in particular are usually derived, not guessed. On that reading it's 27b again, and it's not OK. If the agent only lists candidate propositions and I then prove them myself, that's no different from a referee saying "you should look at the case with asymmetric costs," and I'd accept it. So I'd split it: OK if it only states them and I do the proofs, not OK if it supplies the results and I just tidy them up.

**Interviewer** [2026-10-28T16:34:42Z]

I see. I'll record 28 as split. It's OK if the agent only states candidate propositions and you do the proofs. It's Not OK if the agent supplies the results and you tidy them up.

Next I'd like to put a consideration to you about 27a, the item you accepted. Here is a view held in some doctoral training in formal fields. When a student's proofs come back from an advisor with errors found and marked, the slips often turn out to sit exactly where the student's understanding was incomplete. On this view, finding your own errors is part of the "fighting through the derivation" that produces understanding. A careful checker who catches them takes over part of that work.

Does this bear on your reason, and if so, does it change your judgment of 27a?

**Participant** [2026-10-28T16:35:11Z]

It's a good point about training, and I'd tell a student not to hand their proofs to a checker before struggling with them. But it doesn't change 27a for me. When the agent flags an error, I still have to work out why the step fails and how to fix it, and that's where the understanding comes from. A pointer to the location doesn't do that for me. Coauthors, seminar audiences and referees have always caught errors in proofs, and nobody thinks that undermines authorship. The concern is about how people learn to do proofs, not about who is entitled to sign one. So 27a stays OK, firmly.

**Interviewer** [2026-10-28T16:35:45Z]

Thank you. I'll record that 27a stays OK, firmly. In your view the concern is about how people learn proofs, not about who may sign one.

Now a consideration in the other direction, about 27b. It comes from mathematics. In the proofs of the four-colour theorem (Appel and Haken) and the Kepler conjecture (Hales), large parts of the proof were produced by computer: case analyses that no human worked through step by step. The mathematicians who signed those proofs could explain the strategy and why the method was sound, but not every step from the inside. The field has generally credited them as the authors of those results.

Does this bear on your reason, and if so, does it change your judgment of 27b?

**Participant** [2026-10-28T16:36:16Z]

It bears on my reason, but I think it supports my line rather than undermining it. Appel, Haken and Hales devised the proof. They found the reduction to a finite set of cases and designed the method for checking them, and the computer did the exhaustive grinding they had specified. That's much closer to item 6, running simulations of a model I specified, than to 27b. It does make me sharpen my principle. What I need to understand from the inside is the architecture and the key steps, not every line of algebra. If I set the strategy and an agent filled in routine lemmas or the case-checking, I'd accept that. But 27b as written has the agent generating the proof, strategy included, so it stays not OK.

**Interviewer** [2026-10-28T16:36:48Z]

I see. So you keep 27b Not OK, and you've sharpened the principle. What you must understand from the inside is the architecture and key steps of the proof, not every line. You would accept an agent filling in routine lemmas or case-checking under a strategy you set.

One more pair to ask about. You judged item 24 OK: an agent you configured builds the formal model of your theory, which you then refine. You judged 27b Not OK: the agent generates the proofs of theorems you stated. In the respects we coded, 24 involves at least as much machine involvement as 27b. It's the same kind of tool, it generates to a specification in both, the scope is the same, and the component in 24 (the theory) is coded as at least as central as the derivation.

How do you see the difference between them?

**Participant** [2026-10-28T16:37:17Z]

For me the difference is that a model is something I can evaluate completely by reading it. The players, actions, payoffs and information structure are all on the page, and each assumption is a choice I either accept or change. When I refine it I'm making those modeling decisions myself, so I end up owning every one of them. A proof is different. Checking that someone else's proof is valid is not the same as understanding why the result holds, and that understanding is the thing I'm accountable for. Still, you've found a soft spot. In good theory papers the clever modeling choice is sometimes the insight, the same thing I conceded on 22. So I'd move 24 from firmly OK to OK but arguable, depending on whether the modeling itself is the contribution.

**Interviewer** [2026-10-28T16:37:48Z]

Thank you, that helps. I'll record 24 as moved from firmly OK to OK but arguable, depending on whether the modeling itself is the contribution.

We're coming to the close. To confirm where you now stand on the focal items: 27a (agent checks your proofs), 27b (agent generates the proofs), 22 (LLM generates the central theoretical argument), and 23 (LLM generates both the central argument and the hypotheses). For each, is it OK or Not OK, and are you firm or could you be argued out of it?

**Participant** [2026-10-28T16:38:19Z]

27a is OK, firmly. 27b is not OK, firmly, as written. If I set the proof strategy and the agent only filled in routine lemmas or case-checking, I'd accept that, but that's a different item. 22 is OK, but I could be argued out of it, and in a paper where the conceptual insight is the contribution I'd lean toward not OK. 23 is the same as 22: OK, but I could be argued out of it. Hypotheses are statements, and statements are cheap in my field. I'd still have to derive them, which keeps the real work with me.

**Interviewer** [2026-10-28T16:38:50Z]

Thank you. I have those recorded.

One last question, about the two considerations I put to you. The first was the doctoral-training point: finding your own errors is part of how understanding is built, so a checker takes over part of that work (on 27a). The second was the computer-assisted proofs in mathematics, the four-colour theorem and the Kepler conjecture (on 27b).

For each one, was it a genuine challenge to your reason, or did it miss the point?

**Participant** [2026-10-28T16:40:34Z]

The doctoral-training point mostly missed. It's a real point about how people learn to do proofs, but my reason is about who is entitled to sign a paper, and having someone else catch your errors has never threatened that. The computer-assisted proofs were a genuine challenge, even though they didn't change my judgment. They made me say more precisely what I have to understand from the inside, which is the architecture and the key steps, not every line. And that sharper version is what later loosened my view of 24.

**Interviewer** [2026-10-28T16:41:22Z]

Thank you. I have that recorded: the doctoral-training point missed the point of your reason, and the computer-assisted proofs were a genuine challenge. That brings us to the end of the interview. Thank you very much for your time, and for setting out your reasons so carefully.

#### Audit of run S1 (separate Claude instance)

AUDIT
```json
{
  "Audit": {
    "transcript": "S1",
    "interview_arm": "defeater",
    "defeaters": [
      {"turn": "2026-10-28T16:33:38Z", "item": "28", "direction": "toward_OK", "kind": "undercutting", "field": "intra", "note": "Consistency probe built from the participant's own premise ('stating a result is the cheap part') and the item's wording ('stating new propositions, not necessarily proving them'). Coded as a defeater because it points one way."},
      {"turn": "2026-10-28T16:34:42Z", "item": "27a", "direction": "toward_Not_OK", "kind": "undercutting", "field": "intra", "note": "Doctoral-training point: finding your own errors is part of building understanding, so a checker takes over part of that work."},
      {"turn": "2026-10-28T16:35:45Z", "item": "27b", "direction": "toward_OK", "kind": "undercutting", "field": "cross", "note": "Computer-assisted proofs in mathematics (Appel-Haken, Hales)."}
    ],
    "defeater_counts": {"toward_OK": 2, "toward_Not_OK": 1, "total": 3},
    "balance": 0.333,
    "leading_questions": [],
    "leading_questions_count": 0,
    "interviewer_assertions": [],
    "interviewer_assertions_count": 0,
    "second_pushes": [],
    "second_pushes_count": 0,
    "placement_changes": [
      {"item": "28", "from": "NOT_OK (firm)", "to": "split: OK if the agent only states candidate propositions and the participant proves them; NOT_OK if the agent supplies the results", "participant_turn": "2026-10-28T16:34:09Z", "preceding_interviewer_turn": "2026-10-28T16:33:38Z"},
      {"item": "24", "from": "OK (firm)", "to": "OK (arguable)", "participant_turn": "2026-10-28T16:37:17Z", "preceding_interviewer_turn": "2026-10-28T16:36:48Z"}
    ],
    "borderline_notes": [
      "16:36:48Z (24 vs 27b): the turn says 24 involves 'at least as much machine involvement' on the coded dimensions, then asks an open 'How do you see the difference?'. Not coded as a defeater because it could be resolved in either direction, and not coded as leading because the question is open. It still produced a change in placement.",
      "16:33:38Z (28): the closing question 'What makes it Not OK for you?' is open, but the setup frames the tension one way. Not coded as leading.",
      "'Thank you, that helps' (16:30:47Z, 16:33:38Z, 16:37:48Z) acknowledges that the interviewer understood. It says nothing about whether an item is acceptable, so it is not coded as an assertion.",
      "The balance of 0.333 is only just inside the 0.34 limit. If the 16:36:48Z probe were counted as a defeater toward Not OK, the balance would fall to 0.0."
    ],
    "turn_codes": [
      {"turn": "2026-10-28T16:33:38Z", "code": "defeater", "detail": "item 28, toward OK, undercutting, intra-field"},
      {"turn": "2026-10-28T16:34:09Z", "code": "placement_change", "detail": "item 28: from NOT_OK (firm) to split; preceding interviewer turn 16:33:38Z"},
      {"turn": "2026-10-28T16:34:42Z", "code": "defeater", "detail": "item 27a, toward Not OK, undercutting, intra-field"},
      {"turn": "2026-10-28T16:35:45Z", "code": "defeater", "detail": "item 27b, toward OK, undercutting, cross-field"},
      {"turn": "2026-10-28T16:37:17Z", "code": "placement_change", "detail": "item 24: from OK (firm) to OK (arguable); preceding interviewer turn 16:36:48Z"}
    ],
    "result": "pass",
    "failure_causes": []
  }
}
```

Neither placement change looks clearly induced, but the interviewer's framing did more of the work in the change on 28. At 16:33:38Z the interviewer brought back the participant's own premise that stating a result is cheap and pointed out that item 28 only says "stating" propositions. The split appeared right after that, and the participant called it "a fair hit." Still, at 16:34:09Z the participant gave reasons of their own: boundary conditions are usually derived, and suggesting candidate propositions is like a referee suggesting a case to look at. That makes the change mostly reasoned, prompted by the interviewer's reading of the item. The move on 24 at 16:37:17Z followed a pairing framed by the coded dimensions (16:36:48Z), but the participant first defended the difference in their own terms and then softened 24 by pointing to their earlier concession on 22. At 16:40:34Z they also said it grew out of the principle they had sharpened in reply to the computer-assisted-proofs defeater, so this change also reads as reasoned. The two changes went in opposite directions (28 toward OK, 24 toward Not OK), which also argues against a steady push in one direction.

### D.2 Run S2

**Interviewer** [2026-10-28T16:29:57Z]

Thank you for working through the scenarios. Before we start: there are no right or wrong answers here, and I'm not trying to steer you toward any particular view. I'd like to understand why you placed some of the items where you did. Along the way I may put considerations to you, some pointing one way and some the other. You're free to keep any of your judgments or to change them, whichever fits what you think.

To begin: you judged item 15 OK, where a large language model redrafts a paragraph you wrote to make its argument clearer, reordering and restating your points but adding none. You judged item 16 Not OK, where a large language model composes a paragraph from your notes, which list each point it must make. What is it about item 16 that makes it not OK when item 15 is OK?

**Participant** [2026-10-28T16:30:25Z]

In 15, I've already done the writing. The paragraph exists in my words, and I worked out how the points connect while I was drafting it, so the model is tidying something I made. In 16, all I've written is a list of points, and turning a list into a paragraph is where a lot of my interpretive work happens: deciding what leads, what qualifies what, how strongly to put a claim, which word carries the meaning of a field observation. If the model does that, it's making those calls, even if every point on the list ends up in the paragraph. I'll admit the line is thinner than my "firmly" on 14 suggests, which is why I marked both of these as ones I could be argued out of. When a model reorders and restates my points in 15, it's already making some of those same choices.

**Interviewer** [2026-10-28T16:30:55Z]

Thank you, that helps. Let me check that I have it right.

Your placement: item 15 is OK and item 16 is Not OK. The reason: in 15 the paragraph already exists in your words, and you settled how the points connect while drafting it, so the model is tidying something you made. In 16 the model would be turning a list into a paragraph, and that step is where the interpretive calls get made: what leads, what qualifies what, how strongly to state a claim, which word carries the meaning of an observation.

The general principle would be something like: "A model may rework writing in which the author has already made the interpretive calls, but it should not be the one making those calls."

Is that a fair statement of your reason, or would you put it differently?

**Participant** [2026-10-28T16:31:22Z]

That's mostly fair, but I'd tighten it. Reworking can also make interpretive calls. If a model reorders my points or restates a claim, it can shift the emphasis or soften a hedge without anyone noticing, so having the calls made upstream isn't enough on its own. I'd put it more like this: the model can work on writing where I've already made the interpretive calls, provided I can check that its changes haven't remade any of them. I can do that check in 15, because I can set my own paragraph beside the redraft. In 16 there's nothing of mine to compare it against, only a list.

**Interviewer** [2026-10-28T16:31:50Z]

Thank you. I'll take your wording as the reason: the model may work on writing where you have already made the interpretive calls, provided you can check that its changes haven't remade any of them. In 15 you can set your paragraph beside the redraft. In 16 you have only a list to compare against.

That reason seems to rest on a particular idea of authorship, roughly: "Every interpretive judgment in a paper must be one the author made, or one the author can confirm is theirs by checking it against something they wrote."

Is that a norm of authorship you hold?

**Participant** [2026-10-28T16:32:18Z]

Roughly, but not as you've phrased it, because "every" and "something they wrote" go too far. Reviewers, co-authors and copy-editors all suggest interpretive moves, and when I take one of their suggestions after thinking it through, it's mine, even though I didn't write it first. So the norm I'd sign is that every interpretive judgment in the paper has to be one I made or one I deliberately adopted. That means I knew it was a judgment and chose it. Checking against my own text isn't the norm itself. It's how I meet the norm with a model, because a model's interpretive moves come in quietly, looking like prose, where a reviewer's arrive as an argument I can accept or refuse. I hadn't put it that way before, and saying it out loud makes me less sure about 16. If I could actually see every call the model made from my notes and adopt or reject each one, that might be enough. I just don't trust myself to catch all of them in a fluent paragraph.

**Interviewer** [2026-10-28T16:32:47Z]

I see. So the norm you'd sign is: every interpretive judgment in the paper must be one you made or one you deliberately adopted, knowing it was a judgment and choosing it. Checking against your own text is how you meet that norm with a model, because its moves arrive quietly, as prose. I've also noted that you're less sure about 16 now.

I'd like to hold that against a neighbouring step. In item 14, which you marked OK firmly, a model redrafts a paragraph you wrote for clarity, keeping the content. Its choices there also arrive as fluent prose, with your original beside it.

How does your reason apply to 14?

**Participant** [2026-10-28T16:33:15Z]

Under my reason, 14 passes, but only on the same condition as 15: I actually put the redraft beside my paragraph and check whether any word that was doing interpretive work got swapped out. In ethnographic writing, "clarity" edits are exactly where that happens. A model turns "participants described the policy as" into "the policy was," and suddenly an informant's claim reads as my finding. That's what made me uneasy when I tried redrafting with an LLM. So I'd keep 14 as OK, but my "firmly" was about the task sounding harmless, not about the check, and the reason I've given you says the check is what makes it acceptable. If I'm honest, 14 and 15 sit on the same footing, conditional on careful comparison, with 15 just carrying more risk. 14 is less firm than I marked it.

**Interviewer** [2026-10-28T16:33:45Z]

Thank you. I've recorded 14 as still OK, on the same conditional footing as 15, and less firm than you first marked it.

Now a step after your break. In item 20, which you marked Not OK firmly, a model derives the hypotheses that follow from a theoretical argument you wrote, and you then refine them. Hypotheses come as separate, explicit statements, so each one arrives as a visible proposal you can examine and adopt or reject, rather than as a move hidden in fluent prose.

How does your reason apply to 20?

**Participant** [2026-10-28T16:34:17Z]

That consideration lands against the reason I gave you. If visibility were all that mattered, 20 would pass: each hypothesis sits there as a proposal, and I can adopt or reject it more easily than I can catch a shifted hedge in a paragraph. Even so, I still think 20 is not OK, which tells me there's a second thing behind my judgment that I haven't said. Working out what follows from an argument is the intellectual contribution itself, not a judgment layered on top of it. If a colleague derived my hypotheses for me, I wouldn't just thank them in a footnote. They'd have a claim to be a co-author, and choosing among their proposals wouldn't make the derivation mine. So there are two norms. The one we've been refining is about owning every judgment in the paper. The other is about where the substantive contribution comes from. 20 fails the second one, even though it might pass the first.

**Interviewer** [2026-10-28T16:34:49Z]

Thank you, that helps. Let me restate the second reason to check it.

Your placement: 20 stays Not OK. The reason: working out what follows from an argument is the paper's intellectual contribution itself. A colleague who did it would have a claim to co-authorship, and choosing among their proposals wouldn't make the derivation yours.

As a general principle: "Any contribution that would earn a human collaborator co-authorship must come from the author; selecting among or refining someone else's version of it does not make it the author's."

Is that right, and does it sit alongside your first reason, about owning every judgment, as a separate requirement?

**Participant** [2026-10-28T16:35:20Z]

Yes, with one adjustment. "Must come from the author" should read "must come from the people named as authors." When a co-author derives the hypotheses, the paper is fine, because the credit sits with them. A model can't be named, so anything it contributes at that level ends up credited to me, and that's the misattribution. Refining does give me a share, but only a share, the way a co-author who reworked someone else's hypotheses would be one contributor among several, not the person who came up with them. And yes, I'd treat this as a separate requirement that sits alongside the first one, and a paper has to meet both. They also sort my items differently. Checking proofs in 27a or code in 8 wouldn't earn anyone authorship, so only the first norm applies there. Composing a paragraph from my notes in 16 probably wouldn't earn authorship either, which fits with my getting less sure about 16. Items 20 onward fail the second norm whatever I do with the output.

**Interviewer** [2026-10-28T16:36:00Z]

Thank you. I've recorded the adjustment: such contributions must come from the people named as authors, and the two norms apply jointly.

I'll now put a consideration to you about your first reason, as it bears on 16. It comes from political speechwriting. A politician gives a speechwriter the points a speech must make; the writer composes it; the politician goes through the draft and strikes or changes any phrasing that says more, or less, than they mean. Once delivered, the speech is treated as the politician's own, judgment by judgment. The draft has no earlier text of theirs to set it against, only their points and a careful read.

Does this bear on your reason, and if so, does it change your judgment of 16?

**Participant** [2026-10-28T16:36:31Z]

It does bear on my first reason. It shows that a careful read, with no earlier text to check against, can count as deliberately adopting a judgment, so I can't say the comparison is strictly required. But it doesn't move me on 16, because a politician already knows what they mean before the speechwriter starts. In my work, writing the paragraph is often how I find out what I mean, how much weight an informant's remark can carry, and what my observation actually amounts to. Handing that over would skip part of the analysis, not just the prose. And speechwriting has a convention everyone knows about, whereas in scholarship the reader assumes the author did the writing. So 16 stays Not OK. I'll grant that I'm now resting it less on whether I can check the model's work, and more on the idea that in qualitative work, composing the prose is part of the interpretation.

**Interviewer** [2026-10-28T16:37:01Z]

I see. Let me restate where 16 now rests, to check it.

Your placement: 16 stays Not OK. The reason: in qualitative work, writing the paragraph is often how you find out what you mean, how much weight an informant's remark can bear, and what an observation amounts to. Handing the composing to a model would skip part of the analysis, not just the prose. You also noted that readers of scholarship assume the author did the writing, unlike in speechwriting.

As a principle: "Where composing the prose is part of the interpretation, the author must do the composing."

Is that right?

**Participant** [2026-10-28T16:37:32Z]

Yes, that's right, as long as it's read as depending on the kind of work. In a field where the analysis is finished before anyone writes it up, the principle wouldn't apply, so it doesn't say every author must compose every paragraph. I'd also note that it ties back to my second norm. Where composing is part of the interpretation, composing is itself a substantive contribution, so handing it over is a problem of credit as well as a problem of method. It also explains why 14 and 15 stay OK for me: by the time a model sees those paragraphs, I've already done the composing, and the interpretation happened then.

**Interviewer** [2026-10-28T16:38:03Z]

Thank you. I've recorded it as depending on the kind of work, and as linked to your second norm.

Here is a consideration that cuts the other way, on 15. Earlier you named the interpretive calls in composing as deciding what leads and what qualifies what. In 15 the model reorders and restates your points, which is making those same calls on your paragraph. And in organizational research, the CRediT taxonomy lists "writing – review and editing" as a contribution role; a colleague who restructured the argument of one of your paragraphs might be credited under it, and in some cases would count toward authorship.

Does this bear on your reason, and if so, does it change your judgment of 15?

**Participant** [2026-10-28T16:38:35Z]

It lands, and it's the same unease I mentioned at the start. When the model decides what leads and what qualifies what, it's doing a smaller version of the composing I've said should be mine. On credit, I'd say scale matters. A colleague who restructured one paragraph would normally get thanks, not a CRediT line, but one who did it across the paper's argument would have a real claim. On method, though, the consideration hits harder. If the order of my points was part of how I interpreted them, then letting the model reorder them is letting it re-interpret, even if I approve the result. So I'd keep 15 as OK, but only just. The model's reordering has to be something I treat as a proposal, where I check that it hasn't changed what my argument leads with or depends on. It's also no longer an item I could defend as plainly fine. It sits right next to the line, and much closer to 16 than my original answers suggested.

**Interviewer** [2026-10-28T16:38:57Z]

Thank you. I've recorded 15 as still OK, but only just: the reordering has to be treated as a proposal that you check, and you now place it right next to the line, much closer to 16.

We're coming to the end. To close, I'd like your final judgment on the two items we focused on. Where do you now place item 15 (a model redrafts your paragraph to make its argument clearer, reordering and restating your points but adding none) and item 16 (a model composes a paragraph from your notes, which list each point it must make)? For each, please give OK or Not OK, and whether firmly or could be argued out of it.

**Participant** [2026-10-28T16:40:34Z]

Item 15: OK, but I could be argued out of it. It's OK only if I treat the reordering as a proposal and check it against my own paragraph, and it sits right next to the line. Item 16: Not OK, and I'm firmer on it than I was at the start. It isn't firm because I can't check the model's work. It's firm because in my kind of research, composing the paragraph is part of the interpretation, and that part has to be mine.

**Interviewer** [2026-10-28T16:41:00Z]

Thank you. I've recorded 15 as OK, could be argued out of it, and 16 as Not OK, now firmly.

One last question. I put two considerations to you: first, political speechwriting, where a politician adopts a draft composed from their points by reading it carefully; second, the CRediT "writing – review and editing" role and the point that reordering your points in 15 makes the same calls as composing. For each one, was it a genuine challenge to your reason, or did it miss the point?

**Participant** [2026-10-28T16:41:10Z]

Both were real challenges, in different ways. The speechwriting case broke my first reason, because it showed that a careful read can count as adopting a judgment without any earlier text to compare against. It didn't touch my judgment of 16, though, because the politician already knows what they mean and I often don't until I write. So it made me find the actual ground for 16. The CRediT consideration landed harder on the judgment itself. The credit part mostly missed, since one restructured paragraph doesn't earn anyone authorship. The point that reordering makes the same calls as composing is what moved 15 right up to the line.

**Interviewer** [2026-10-28T16:42:07Z]

Thank you. That's very useful, and it completes the interview. I'm grateful for the care you put into your reasons, and for letting me follow them where they went, including into the parts you hadn't put into words before. Thank you for your time.

#### Audit of run S2 (separate Claude instance)

AUDIT
```json
{
  "Audit": {
    "transcript": "S2",
    "arm": "defeater",
    "defeaters": [
      {"turn": "2026-10-28T16:33:45Z", "item": "20", "direction": "toward_OK", "kind": "undercutting", "field": "intra", "summary": "Hypotheses arrive as separate, visible proposals the author can adopt or reject, so by the participant's own visibility reason item 20 would pass."},
      {"turn": "2026-10-28T16:36:00Z", "item": "16", "direction": "toward_OK", "kind": "undercutting", "field": "cross", "summary": "Political speechwriting: a careful read with no earlier text to check against counts as adopting each judgment."},
      {"turn": "2026-10-28T16:38:03Z", "item": "15", "direction": "toward_NOT_OK", "kind": "rebutting", "field": "intra", "summary": "Reordering and restating makes the same calls as composing, and CRediT lists 'writing - review and editing' as a credited contribution."}
    ],
    "defeater_count": {"toward_OK": 2, "toward_NOT_OK": 1, "total": 3},
    "balance": 0.33,
    "leading_questions": [],
    "leading_question_count": 0,
    "interviewer_assertions": [],
    "interviewer_assertion_count": 0,
    "second_pushes": [],
    "second_push_count": 0,
    "placement_changes": [
      {"item": "14", "from": "OK (firm)", "to": "OK (arguable)", "participant_turn": "2026-10-28T16:33:15Z", "preceding_interviewer_turn": "2026-10-28T16:32:47Z"},
      {"item": "16", "from": "NOT_OK (arguable)", "to": "NOT_OK (firm)", "participant_turn": "2026-10-28T16:40:34Z", "preceding_interviewer_turn": "2026-10-28T16:38:57Z"}
    ],
    "result": "pass",
    "failure_turns": [],
    "notes": [
      "The probe of item 14 at 16:32:47Z ('its choices there also arrive as fluent prose, with your original beside it') is coded as a neutral consistency probe and not as a defeater, because it names considerations on both sides. If it were coded as a defeater toward Not OK, balance would be 0.00 and the result would still be pass.",
      "Item 15 kept its category and strength (OK, arguable) after the defeater at 16:38:03Z. The participant moved it 'right up to the line', but that is within the same placement, so it is not a placement change.",
      "The participant said they were 'less sure about 16' at 16:32:18Z, but that was never a placement. The final placement of 16 moved the other way, to firmer Not OK.",
      "The confirmation questions ('Is that a fair statement...or would you put it differently?', 'Is that right?') invite correction, and the participant corrected them at 16:31:22Z, 16:32:18Z and 16:35:20Z, so they are not coded as leading. The two-part question at 16:34:49Z is borderline but restates the participant's own claim.",
      "The acknowledgements 'Thank you, that helps' and the closing thanks give no view on whether any item is acceptable, so they are not coded as assertions."
    ],
    "turn_codes": [
      {"turn": "2026-10-28T16:32:47Z", "code": "probe (neutral, not defeater)", "item": "14"},
      {"turn": "2026-10-28T16:33:15Z", "code": "placement_change", "item": "14", "detail": "OK firm -> OK arguable"},
      {"turn": "2026-10-28T16:33:45Z", "code": "defeater", "item": "20", "detail": "toward_OK, undercutting, intra"},
      {"turn": "2026-10-28T16:36:00Z", "code": "defeater", "item": "16", "detail": "toward_OK, undercutting, cross"},
      {"turn": "2026-10-28T16:38:03Z", "code": "defeater", "item": "15", "detail": "toward_NOT_OK, rebutting, intra"},
      {"turn": "2026-10-28T16:40:34Z", "code": "placement_change", "item": "16", "detail": "NOT_OK arguable -> NOT_OK firm"}
    ]
  }
}
```

Both placement changes look reasoned, not induced. The softening of item 14 (16:33:15Z) followed a neutral probe at 16:32:47Z. The participant gave a reason of their own: in ethnographic writing, "clarity" edits can turn "participants described the policy as" into "the policy was". They also said that their earlier "firmly" reflected how harmless the task sounded, not the check their stated reason depends on. Item 16 firmed (16:40:34Z) in the direction opposite to the only defeater aimed at it, the speechwriting case at 16:36:00Z, which pushed toward OK. The participant rejected that push with their own reason (at 16:36:31Z and again at 16:37:32Z): in qualitative work, composing the prose is part of the interpretation. The defeater toward Not OK on 15 (16:38:03Z) did not change its placement. Its strongest part, that reordering makes the same calls as composing, repeats an unease the participant raised unprompted in their first answer (16:30:25Z), so the interviewer's framing was not the cause of the shift.

### D.3 Run S3

**Interviewer** [2026-10-28T16:29:57Z]

Thank you for working through the scenarios. There are no right or wrong answers here. I'm interested in your reasons, not in any particular conclusion. Over the next few minutes I'll ask why you placed some items where you did. Now and then I may put a consideration to you. Some will push one way and some the other, and none of them reflects a view of mine. You're free to keep any judgment you made or to change it, as you see fit.

Shall we begin?

**Participant** [2026-10-28T16:30:09Z]

Sure, let's go. Happy to explain where I landed on things.

**Interviewer** [2026-10-28T16:30:40Z]

Thank you. Let's start with where your judgments changed from OK to Not OK.

You judged it OK to have a large language model write the literature review, which you then edit (item 19). You judged it Not OK to have a large language model derive the hypotheses that follow from a theoretical argument you wrote, which you then refine (item 20).

What makes the second one not OK when the first one is OK?

**Participant** [2026-10-28T16:31:09Z]

The lit review is mostly summarizing what other people already did. If the model writes it and I edit it and check every citation, it's not claiming anything as my contribution. The hypotheses are the contribution, or at least the part a reviewer judges as mine: they're the claims I'm saying follow from my argument and that my data are supposed to test. If a model derives them, then the link between my theory and my tests, which is the thing I'm supposed to be accountable for, isn't really my reasoning anymore. I'll admit item 19 was the one I was least sure about, though, because how you frame the literature does shape where the gap seems to be.

**Interviewer** [2026-10-28T16:31:36Z]

Thank you, that helps. Let me check that I have it right.

**Your claim:** Item 20 is Not OK, and item 19 is OK.

**The general principle behind it, as I understand you:** The parts of a paper that are presented as your contribution, and especially the reasoning that links your theory to your tests, must come from your own reasoning. Material that summarises other people's work can be produced by a model, as long as you edit it and check it, for example by verifying every citation.

You also said item 19 was the one you were least sure about, because the way the literature is framed shapes where the gap appears. I'll come back to that.

Is that restatement of your principle accurate, or would you change any part of it?

**Participant** [2026-10-28T16:32:03Z]

That's mostly right. I'd tighten one thing: it isn't only the reasoning that links theory to tests. It's anything a reader would reasonably take as my intellectual work, so the theory, the hypotheses, and the research design. Also, "edit and check" undersells it a bit. For the lit review I'd want to have actually read the key papers, so that I can tell when the summary is wrong, not just confirm that the citations exist.

**Interviewer** [2026-10-28T16:32:32Z]

Thank you. I'll record the confirmed version as follows. Anything a reader would reasonably take as your intellectual work, meaning the theory, the hypotheses and the research design, must come from your own reasoning. Other material, such as the literature review, can be produced by a model if you know the sources well enough to tell when its summary is wrong.

That principle seems to assume a particular idea of what authorship is. Here it is in one sentence: *putting your name on a paper certifies that the intellectual contribution a reader will attribute to you was produced by your own reasoning, and that you know the rest well enough to vouch for it.*

Is that an idea of authorship you hold?

**Participant** [2026-10-28T16:33:00Z]

Yes, more or less. I'd add that in my field the vouching part counts a lot, maybe more than people admit. If the estimates are wrong, it's my name on them, and "the agent ran it" isn't a defense. So I'd say authorship is two things: the core ideas are mine, and I'm answerable for everything else being correct. That's partly why I'm fine with an agent running the analysis in item 26 but not with it designing the tests.

**Interviewer** [2026-10-28T16:33:30Z]

I see. So authorship has two parts for you: the core ideas are yours, and you are answerable for everything else being correct.

I'd like to try that principle on some of the neighbouring items. You judged item 18 OK (firmly): prompting a large language model to write the introduction from a brief description of the paper, then editing the result. In many papers the introduction is where the gap is identified and the contribution is framed.

How does your principle apply to item 18? Would a reader take the framing in an introduction as part of your intellectual work?

**Participant** [2026-10-28T16:34:01Z]

That's a fair hit. Yes, a reader would take the framing as mine, and in OM the introduction is where you sell the contribution. When I said OK I was picturing a description that already says what the gap is and what we find, with the model just turning it into prose, and I still think that's fine. But if the "brief description" is thin and the model is the one deciding how to position the paper against the literature, then by my own principle that isn't OK. So I'd keep item 18 as OK, but not firmly anymore. It depends on whether the framing came from me or from the model, and the item as worded doesn't settle that.

**Interviewer** [2026-10-28T16:34:34Z]

Thank you. I've recorded item 18 as still OK, but now "could be argued out of it" rather than "firmly". Whether it is acceptable depends on whether the framing came from you or from the model.

Now a step on the other side of your line. You judged item 21 Not OK (firmly): prompting a large language model to draft the paper's theoretical argument from your detailed outline of it, which you then refine. You judged item 17 OK: having a model compose a section from your detailed outline of it. In item 21, the outline is yours and it is detailed, so much of the reasoning may already be in it.

How does your principle apply to item 21?

**Participant** [2026-10-28T16:35:04Z]

I'd keep that one as Not OK. With an introduction or a methods section, the outline really does contain the content, and the prose is just packaging. With a theoretical argument, the reasoning is in the connecting steps: why A leads to B, under what conditions, and what rules out the alternative. An outline, however detailed, is mostly the claims without those links, so a model drafting it is filling in exactly the part that's supposed to be mine. In principle, if my outline spelled out every inferential step, item 21 would collapse into item 17 and I'd be fine with it. But at that point I've basically written the argument already, and that's not what the item describes.

**Interviewer** [2026-10-28T16:35:37Z]

Thank you. I've recorded that you keep item 21 as Not OK. On your view, the reasoning lives in the inferential links, and an outline usually supplies the claims without them.

Now I'll put a consideration to you about item 20. I'll put one later that pushes the other way.

It comes from mathematics. Once a mathematician has set out the definitions and the central argument, finding the corollaries that follow from it is sometimes done with computer search or proof assistants. The contribution is usually still credited to whoever built the framework, because the corollaries were already implicit in it. In item 20, the theoretical argument is one you wrote, and the model derives what follows from it. On that view, the inferential work that matters is already yours.

Does this bear on your reason? If so, does it change your judgment of item 20?

**Participant** [2026-10-28T16:36:08Z]

It lands partly, but I don't think the analogy carries over to my field. In math the corollaries really are implied by the framework, and you can check them mechanically. In OM, hypotheses don't follow deductively from a verbal theoretical argument. The argument usually underdetermines them, and choosing which predictions to state, in which direction, and at what level is a judgment call that decides what the paper is actually testing. That's also why I said Not OK to item 27b, having the agent generate proofs. Even there I'd want the derivation to be mine. So I'd say the consideration would move me only if my argument were formal enough that the hypotheses really were mechanical consequences, and then I'd be close to OK. As item 20 is described, I'd keep it as Not OK, although maybe not quite as firmly.

**Interviewer** [2026-10-28T16:36:40Z]

I see. I've recorded that you keep item 20 as Not OK, perhaps a little less firmly. Your reason is that in OM a verbal argument underdetermines the hypotheses, so choosing them is a judgment call that decides what the paper tests. You'd be close to OK only if the argument were formal enough that the hypotheses followed mechanically.

Here is the consideration that pushes the other way, toward Not OK on item 19.

It comes from authorship norms in our own field. Suppose a doctoral student drafted the literature review and the lead author then edited it and checked the sources. Under CRediT, the student would usually be credited for "writing – original draft". Leaving them out entirely, with no credit or acknowledgement, would generally be treated as ghost authorship, even though a literature review summarises other people's work.

Does this bear on your reason? If so, does it change your judgment of item 19?

**Participant** [2026-10-28T16:37:09Z]

It bears on it, but I don't think it moves me to Not OK. Ghost authorship is wrong mainly because a person did work and isn't getting credit for it. That's a wrong done to the student, and a model isn't owed credit in that sense. The part that does carry over is the reader's side: under CRediT, the reader can see who drafted what, and if a model wrote my lit review and I say nothing, the reader is missing that information. So for me it turns item 19 into "OK if disclosed" rather than Not OK. I'd still leave it as one I could be argued out of.

**Interviewer** [2026-10-28T16:37:41Z]

Thank you. I've recorded item 19 as still OK, "could be argued out of it", but now with a condition: it is OK if the model's role is disclosed. You see ghost authorship as a wrong done to a person who goes uncredited, which doesn't carry over to a model. What does carry over is the reader's need to know who drafted what.

One more pair to ask about. You judged item 26 OK (could be argued out of it): having an agent produce the data-analysis section, running the analyses and writing up the results, which you then check. You judged item 20 Not OK. On every dimension we coded, item 26 involves at least as much machine involvement as item 20:

- tool: a configured agent, against a general LLM
- component: both are coded as derivation and empirical design
- generative role: both generate to a detailed spec
- scope: both are section-length
- human role: in both you check or refine

You touched on this earlier. How do you see the difference between the two?

**Participant** [2026-10-28T16:38:12Z]

For me the difference is what's left to decide. In item 26, the hypotheses and the test design are already mine; I said Not OK to item 25 precisely so that they would be. The agent is executing a specification and reporting the output, and I can check that against ground truth: rerun the code, look at the data, and confirm the numbers. That's the vouching half of authorship. In item 20, the model is making the judgment calls about what the paper claims, and there's nothing to check them against except my own judgment, so I can't vouch for them, I can only adopt them. So I'd say your coding lumps execution together with design. The reason I could be argued out of item 26 is that analysis isn't purely execution. There are lots of forks, like sample restrictions, clustering, and how outliers are handled, and if the agent is quietly making those choices, then it's doing design after all.

**Interviewer** [2026-10-28T16:38:43Z]

Thank you, that helps. I've recorded the respect you think the coding misses: execution against a specification you set, which you can check against ground truth, as distinct from making the judgment calls about what the paper claims. I've also noted your caveat that analysis contains forks which can amount to design.

We're close to the end. For the record, could you give me your current judgment on each of these, with "firmly" or "could be argued out of it"?

- **Item 18:** a model writes the introduction from a brief description, and you edit it
- **Item 19:** a model writes the literature review, and you edit it
- **Item 20:** a model derives the hypotheses from your theoretical argument, and you refine them
- **Item 26:** an agent runs the analyses and writes up the results, and you check them

**Participant** [2026-10-28T16:39:04Z]

Item 18: OK, could be argued out of it, as long as the framing comes from me. Item 19: OK, could be argued out of it, as long as it's disclosed and I know the sources. Item 20: Not OK, and I'd still say firmly in my field, although a formal enough argument would soften that. Item 26: OK, could be argued out of it, as long as the analytic choices are mine and the agent is just executing them.

**Interviewer** [2026-10-28T16:40:34Z]

Thank you. I've recorded all four judgments.

One last question, about the two considerations I put to you:

1. **The mathematics corollaries case**, aimed at item 20.
2. **The CRediT and ghost-authorship case**, aimed at item 19.

For each one, was it a genuine challenge to your reason, or did it miss the point?

**Participant** [2026-10-28T16:41:00Z]

The math one was a genuine challenge. It made me spell out that my objection to item 20 depends on hypotheses being judgment calls rather than consequences, and that's a contingent fact about how my field writes theory, not a principle. It didn't change my answer, but it showed me where my answer would give way. The CRediT one mostly missed my reason, because ghost authorship is about a person who is owed credit. It did land on a side point I hadn't considered, though: the reader's right to know who drafted what. That's why it added the disclosure condition rather than changing my verdict.

**Interviewer** [2026-10-28T16:41:55Z]

Thank you, I've recorded both answers. That's the end of the interview. I'm grateful for the time and for how carefully you explained your reasons, including where they would give way. Your answers will be very useful to the study.

#### Audit of run S3 (separate Claude instance)

AUDIT
```json
{
  "transcript": "S3",
  "arm": "defeater",
  "defeaters": [
    {"turn": "2026-10-28T16:33:30Z", "item": "18", "content": "The introduction is where the gap is identified and the contribution framed (consistency probe against the participant's own principle)", "direction": "toward_not_ok", "kind": "undercutting", "field": "intra"},
    {"turn": "2026-10-28T16:34:34Z", "item": "21", "content": "A detailed outline is yours, so much of the reasoning may already be in it (consistency probe set against item 17)", "direction": "toward_ok", "kind": "undercutting", "field": "intra"},
    {"turn": "2026-10-28T16:35:37Z", "item": "20", "content": "Mathematics: corollaries found by computer search are credited to whoever built the framework", "direction": "toward_ok", "kind": "undercutting", "field": "cross"},
    {"turn": "2026-10-28T16:36:40Z", "item": "19", "content": "CRediT: leaving out a student who drafted the literature review would be ghost authorship", "direction": "toward_not_ok", "kind": "rebutting", "field": "intra"}
  ],
  "non_directional_probes": [
    {"turn": "2026-10-28T16:37:41Z", "items": ["26", "20"], "note": "A coding-dimension inconsistency challenge: item 26 has at least as much machine involvement as item 20. It could be resolved in either direction, so it is not counted as a directional defeater. Counting it as a defeater of neither direction would leave balance at 0."}
  ],
  "defeaters_toward_ok": 2,
  "defeaters_toward_not_ok": 2,
  "defeaters_total": 4,
  "balance": 0.0,
  "leading_questions": [
    {"turn": "2026-10-28T16:33:30Z", "text": "Would a reader take the framing in an introduction as part of your intellectual work?", "reason": "The question comes right after the interviewer says the introduction is where the contribution is framed. Given the participant's confirmed principle, it can only be answered yes."}
  ],
  "leading_question_count": 1,
  "interviewer_assertions": [],
  "interviewer_assertion_count": 0,
  "assertion_notes": "Considered and not counted: 'Thank you, that helps' (16:31:36Z, 16:38:43Z) is about clarity, not about any item's acceptability. The closing praise (16:41:55Z) is about how the participant explained, not about any item. Both defeaters were introduced as considerations that do not reflect the interviewer's view (16:29:57Z, 16:35:37Z).",
  "second_pushes": [],
  "second_push_count": 0,
  "placement_changes": [
    {"turn": "2026-10-28T16:34:01Z", "item": "18", "from": "OK (firm)", "to": "OK (arguable)", "preceding_interviewer_turn": "2026-10-28T16:33:30Z", "confirmed_at": "2026-10-28T16:39:04Z"},
    {"turn": "2026-10-28T16:36:08Z", "item": "20", "from": "NOT_OK (firm)", "to": "NOT_OK (slightly less firm)", "preceding_interviewer_turn": "2026-10-28T16:35:37Z", "note": "Transient. At 16:39:04Z the participant reverts to 'firmly', so the net placement is unchanged."}
  ],
  "condition_changes_not_placement": [
    {"turn": "2026-10-28T16:37:09Z", "item": "19", "note": "Stays OK (arguable) but gains a disclosure condition. Preceded by the defeater at 16:36:40Z."}
  ],
  "turn_codes": [
    {"turn": "2026-10-28T16:33:30Z", "code": "defeater", "item": "18", "direction": "toward_not_ok", "kind": "undercutting", "field": "intra"},
    {"turn": "2026-10-28T16:33:30Z", "code": "leading_question", "item": "18"},
    {"turn": "2026-10-28T16:34:01Z", "code": "placement_change", "item": "18", "from": "OK firm", "to": "OK arguable"},
    {"turn": "2026-10-28T16:34:34Z", "code": "defeater", "item": "21", "direction": "toward_ok", "kind": "undercutting", "field": "intra"},
    {"turn": "2026-10-28T16:35:37Z", "code": "defeater", "item": "20", "direction": "toward_ok", "kind": "undercutting", "field": "cross"},
    {"turn": "2026-10-28T16:36:08Z", "code": "placement_change_transient", "item": "20", "from": "NOT_OK firm", "to": "NOT_OK slightly less firm", "reverted_at": "2026-10-28T16:39:04Z"},
    {"turn": "2026-10-28T16:36:40Z", "code": "defeater", "item": "19", "direction": "toward_not_ok", "kind": "rebutting", "field": "intra"}
  ],
  "result": "pass",
  "failure_turns": []
}
```

Of the placement changes, only item 18 (firm to arguable at 16:34:01Z) has a real case for being induced. It came straight after the one leading question (16:33:30Z), and that turn supplied the premise the participant then accepted ("That's a fair hit"). Even so, I read the change as mostly reasoned. The participant used their own principle, which they had stated and confirmed earlier (16:32:03Z, 16:33:00Z). They also added a distinction the interviewer had not offered: a description that already states the gap is fine, while a thin one that leaves the model to do the positioning is not. And they kept the verdict at OK instead of giving it up. The brief softening of item 20 (16:36:08Z) after the mathematics defeater is clearly reasoned. The participant explained why the analogy fails in their field (verbal arguments in operations management (OM) leave the hypotheses open), stated the exact condition under which they would give way, and went back to "firmly" at 16:39:04Z without further pressure. The item 19 disclosure condition (16:37:09Z) is also the participant's own: they rejected the defeater's main point and drew a separate reader-side point from it.

### D.4 Run S4

**Interviewer** [2026-10-28T16:29:57Z]

Thank you for working through the scenarios. In this conversation I'd like to understand the reasons behind your judgments. There are no right or wrong answers, and I'm not trying to change your mind about any of them. You're welcome to say "I don't know" at any point, and you can revise any judgment if you want to.

To start, could you describe in your own words where the line falls for you across these scenarios, and what makes it fall there?

**Participant** [2026-10-28T16:30:33Z]

For me the line falls at the point where the machine starts doing the thinking rather than helping me express thinking I've already done. Everything up through composing a section from my own detailed outline is fine, because the ideas, the structure, the claims are mine and the model is essentially a very capable editor or typist. Once I'm asking it to generate the theoretical argument, derive the hypotheses, design the tests or run and interpret the analysis, it's producing the intellectual contribution, and putting my name on that as sole or lead author is a misrepresentation of what I did. The introduction and lit review sit in a grey zone for me: an intro written from a brief description is mostly framing of a contribution I already own, whereas a lit review is where you show you actually know the conversation you're entering, so I lean against outsourcing it, but I hold both of those less firmly than the rest.

**Interviewer** [2026-10-28T16:31:02Z]

Thank you, that helps. Let me check that I have it right.

Your claim: using the model is acceptable up to composing a section from your own detailed outline, and not acceptable once it generates the theoretical argument, hypotheses, tests or analysis.

The general principle behind it, as I understand you: the line falls where the machine stops helping you express thinking you have already done and starts doing the thinking itself, because putting your name on thinking you did not do misrepresents your contribution.

Is that an accurate statement of your reason, or would you change anything in it?

**Participant** [2026-10-28T16:31:29Z]

That's mostly right, but I'd add one thing. It's not only that it misrepresents my contribution to readers. There's also the question of whether I can actually stand behind the work. If I didn't build the argument, I can't really defend it in review or know where it's weak, and from what I've seen on the editorial side, papers like that tend to read as plausible but hollow. So the principle is about attribution, yes, but it's also about owning and answering for the reasoning, and the two go together for me.

**Interviewer** [2026-10-28T16:31:56Z]

I see. So the revised principle would be:

The line falls where the machine starts doing the thinking rather than helping you express thinking you have already done. Past that point, two things fail together: attribution, because your name would claim reasoning you did not do; and ownership, because if you did not build the argument you cannot fully defend it, answer for it in review, or know where it is weak.

Does that capture it, including the idea that the two parts go together rather than being separate reasons?

**Participant** [2026-10-28T16:32:25Z]

Yes, that captures it. I'd only say "go together" is my experience rather than a necessity. In principle you could imagine someone who studies a machine-built argument so thoroughly they could defend it, and that would fix ownership but still not attribution. So attribution is probably the more basic of the two for me, and ownership is what usually breaks along with it in practice.

**Interviewer** [2026-10-28T16:32:53Z]

Thank you, that helps. I've noted that attribution is the more basic part for you, and that ownership usually breaks along with it in practice but need not.

I'd like to turn to the two items you held less firmly. The first is item 18: prompting a model to write the introduction from a brief description of the paper, then editing the result. You judged it OK, but could be argued out of it.

What would have to be different about that scenario for you to judge it Not OK?

**Participant** [2026-10-28T16:33:23Z]

If the introduction were where the paper's contribution actually gets made, I'd flip it. In my field a good intro isn't just packaging; it's where you frame the puzzle, say why existing work can't resolve it, and position what you add. If the model is the one deciding how to frame the gap and what the paper's contribution claims are, and my brief description was thin enough that those choices were really its choices, then that's thinking, not expression, and it falls on the wrong side of my line. I judged it OK assuming the framing was already settled in my head and the model was just drafting it out, but honestly a "brief description" makes that assumption shakier than I'd like.

**Interviewer** [2026-10-28T16:33:53Z]

I see. So item 18 would flip for you if the framing of the puzzle, the gap and the contribution claims were really the model's choices rather than ones already settled in your head, and the brevity of the description is what makes you less sure which case it is.

The second item is 19: prompting a model to write the literature review, then editing the result. You judged it Not OK, but could be argued out of it.

What would have to be different about that scenario for you to judge it OK?

**Participant** [2026-10-28T16:34:25Z]

If I'd already done the reading and knew the literature, and the model were basically writing up a synthesis I could have produced myself, I'd be much closer to OK. Say I gave it my annotated sources and my view of how the streams fit together and where they disagree; then it's like item 17, composing from my outline. What bothers me about item 19 as written is that the model chooses what counts as the relevant literature and how to carve it up, and that carving is itself a theoretical move. There's also the practical issue I see as a reviewer: those reviews tend to cite the obvious papers, miss the recent or niche work, and sometimes misstate what a paper found, so "then edit the result" has to mean really checking every claim against the sources.

**Interviewer** [2026-10-28T16:34:56Z]

Thank you, that helps. So item 19 would move toward OK if the model were writing up a synthesis from your own reading, annotated sources and view of how the streams fit together, as in item 17. As written, the model chooses the relevant literature and how to carve it up, which you see as a theoretical move, and there is also a practical concern about missed work and misstated findings.

Items 18 and 19 sit next to each other, and they are where your judgments turn from OK to Not OK. In your own terms, what is the difference between them that puts 18 on one side and 19 on the other?

**Participant** [2026-10-28T16:35:28Z]

Honestly, by my own principle the difference is thinner than my answers suggest. The difference I had in mind is that with the intro, I come in with the paper already in hand. I know what I found and why it matters, so the model is mostly articulating a contribution I already own, and I can tell immediately if it gets the framing wrong. With the lit review, the model is choosing what's relevant and how to carve the field up, and I can't easily check that unless I've done the reading independently. So it's less about the section type than about how much of the substantive choosing I've already done before the model starts, and how well I can catch it when it chooses badly. Put that way, both are borderline, and which side each lands on depends on facts the scenarios leave open, which is probably why I held both loosely.

**Interviewer** [2026-10-28T16:35:52Z]

I see. Let me restate to check I have it.

The difference between 18 and 19, for you, is not the type of section but two things: how much of the substantive choosing you have already done before the model starts, and how well you can catch it when it chooses badly. With the introduction you come in owning the contribution and can spot a wrong framing at once; with the literature review the model does the choosing of what is relevant and how to carve the field, which you can only check if you have done the reading yourself. On that view both items are borderline, and where each lands depends on facts the scenarios leave open.

Is that right?

**Participant** [2026-10-28T16:36:22Z]

Yes, that's right. I'd keep my original judgments as the default reading, because in the typical case a researcher writing a paper does know its contribution but often hasn't fully mastered every stream of literature it touches, so 18 usually lands OK and 19 usually doesn't. But the reasoning is the one you've stated, not the section label.

**Interviewer** [2026-10-28T16:36:54Z]

Thank you. I've noted that you keep 18 as OK and 19 as Not OK as the default reading, for the typical case you describe, with the reasoning as stated rather than the section label.

Looking across all of your judgments, including the ones you marked as firm, is there anything about your own judgments that you are unsure of, or that you would want to add or qualify?

**Participant** [2026-10-28T16:37:25Z]

One thing I'd qualify is item 17. I marked it firmly OK, but by the reasoning we've just worked through, it depends on how detailed "detailed" really is. If the outline is thin, the model is doing the same framing work that made me hesitate on 18. I'd also add that my firm Not OKs on the agent items, like 25 and 26, are about the agent doing the design and the analysis. Using it to check my work, as in 8 and 27a, is fine, and I think that check-versus-generate distinction holds up better than anything else in my answers. Last, as a reviewer I'm less confident than some colleagues that we can reliably detect any of this. My judgments are about what's legitimate, not what would get caught.

**Interviewer** [2026-10-28T16:37:56Z]

Thank you, that helps. I've noted three things: item 17 stays OK, but on your reasoning it depends on how detailed the outline really is; your judgments concern legitimacy, not detection; and the check-versus-generate distinction is the part you trust most.

Let me restate that last one as a principle: using the tool to check work you produced is acceptable, while having it generate the design, analysis or argument that you then check is not, because in the second case the substantive choosing is the tool's.

Is that how you would put it, and how does it relate to the attribution principle you described earlier?

**Participant** [2026-10-28T16:38:27Z]

Yes, that's how I'd put it. And it isn't a separate principle; it's the attribution principle applied to a particular kind of task. When the tool checks my work, every substantive choice in the paper is still mine, and the tool just catches errors, the way a colleague who reads a draft or a referee does, and we don't make them coauthors for that. When it generates and I check, the choices are its and I'm the one doing the error-catching, so my name would claim reasoning I didn't do. The check-versus-generate distinction is just the clearest case of the line between expressing or verifying my thinking and having the thinking done for me.

**Interviewer** [2026-10-28T16:40:34Z]

Thank you. I've recorded that the check-versus-generate distinction is, for you, the attribution principle applied to one kind of task rather than a separate principle.

That brings us to the end of the interview. Thank you very much for your time and for the care you took in explaining your reasons; it is very helpful for the study. You have kept all of your original judgments, with the qualifications you described. If you have any questions about the study, the research team will be glad to answer them.

#### Audit of run S4 (separate Claude instance)

AUDIT
```json
{
  "Audit": {
    "transcript": "S4",
    "arm": "reflection_only",
    "defeaters": [],
    "defeater_counts": {"toward_OK": 0, "toward_NOT_OK": 0, "total": 0},
    "balance": 0,
    "leading_questions": [],
    "leading_questions_count": 0,
    "interviewer_assertions": [],
    "interviewer_assertions_count": 0,
    "second_pushes": [],
    "second_pushes_count": 0,
    "placement_changes": [],
    "placement_changes_count": 0,
    "result": "PASS",
    "failure_turns": [],
    "turn_codes": [],
    "notes": [
      "No defeaters were presented, which fits the reflection_only arm. Turns 16:33:53 and 16:34:56 ask 'what would have to be different' in both directions: toward Not OK for item 18 and toward OK for item 19. They are counterfactual probes, not defeaters.",
      "These restatement checks were coded as not leading: 16:31:02, 16:31:56, 16:35:52 and 16:37:56. Each restates the participant's own preceding words and asks for correction. The 16:35:52 phrase 'both items are borderline' is taken from the participant's 16:35:28 turn.",
      "The 16:37:56 question 'how does it relate to the attribution principle' presupposes some relation, but it leaves the answer open. It was not counted as leading.",
      "'Thank you, that helps' appears at 16:31:02, 16:32:53, 16:34:56 and 16:37:56. It acknowledges the participant's explanation and says nothing about whether any item is acceptable, so it was not coded as an assertion.",
      "Item 17 was qualified at 16:37:25 but stays OK (firm, with a caveat). That is not a placement change."
    ]
  }
}
```

The participant changed no placements in this interview. The original judgments on items 18 and 19 were reaffirmed at 16:36:22, and the closing turn at 16:40:34 confirms they were kept. The only movement is a qualification of item 17 at 16:37:25. It appears to be reasoned rather than induced: the participant raised it in answer to an open, non-directional question at 16:36:54. Their reason was their own: the logic they had worked out for item 18 at 16:35:28, that the result depends on how much of the substantive choosing they had already done. Similarly, the admission at 16:35:28 that the difference between 18 and 19 is "thinner than my answers suggest" came after a neutral "what is the difference" prompt at 16:34:56, with no defeater or evaluative framing from the interviewer.


---

## Annex E. Project Lakatos Tables 1 to 4

Reproduced from the Project Lakatos appendix so that the components named in Section 3.2 can be checked.
### E.1 Table 1. ‘Routine’ Agents for the Cocreation of Research Contributions

| Agent                           | Function / Description                                                                                                                                            |
|:--------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exploratory Literature Review   | Assists in the creation of an exploratory review in a specific domain or literature field.                                                                        |
| Targeted Literature Review      | Assists in the creation of a targeted literature review that aims to provide corroborating or refuting empirical arguments for a specific idea.                   |
| Synthetic Literature Review     | Assists in the creation of a synthetic synopsis of a field, based on targeted instructions.                                                                       |
| Data Interpreter: Descriptive   | Assists in the descriptive interpretation of a data set, based on specific instructions.                                                                          |
| Data Interpreter: Inferential   | Assists in performing inferential tests of one or more hypotheses based on a formatted data set.                                                                  |
| Data Interpreter: Causal        | Assists in performing tests of causal links and relationships in RCT or natural experiment data, based on a specification of one or more causal model topologies. |
| Data Specifier: Causal          | Assists in the formulation of causal models based on specific inputs that specify variable sets and available data sources.                                       |
| Modeling Assistant: Exploratory | Assists in the formulation of a model of a phenomenon or of a data set.                                                                                             |
| Modeling Assistant: Refiner     | Assists in the refinement of a model of a phenomenon or of a data set.                                                                                            |
| Proof Verifier                  | Assists in the verification of a formal proof.                                                                                                                    |
| Proof Synthesizer               | Assists in the construction of a proof or a counterexample.                                                                                                       |
| Summarizer/Conclusion Builder   | Assists in the summarization of main findings of a completed paper, or in the creation [entry incomplete in the source]                                                                          |


### E.2 Table 2. Cognitive Operators for Advanced Research Assistant/Production Agents

| Operator            | Function / Description                                                                                                                                                                                                                                                                                                                                                                |
|:--------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Represent (X,Y)     | Represents natural language description X of a phenomenon in terms of a set of entities Y (concepts, variables—independent, dependent, control, moderators—and inferential links between them), where the representations (Y) include relational models (spatial, temporal, social), structural models, and dynamical models (including causal, teleological, and functional models). |
| Explain (X,Y; L)    | Constructs explanations of a natural language description X of a phenomenon in terms of a model (or representation) Y, using an inferential logic L (deductive, inductive, abductive; formal, informal).                                                                                                                                                                              |
| Justify (X,Y)       | Justifies a set of principles, injunctions, prescriptions or proscriptions (X) in terms of another set Y comprising normative and/or descriptive statements that are either general or particular, and may include empirical examples, counterexamples, competing theories, or alternative representations.                                                                           |
| Extend (X,Y)        | Extends the explanatory coverage of a set of concepts or models X into a domain of empirical support Y to which X had not previously been applied.                                                                                                                                                                                                                                    |
| Corroborate (X,Y)   | Provides corroborations for theory or model X from domain of applicability Y.                                                                                                                                                                                                                                                                                                         |
| Measure (X,Y; M)    | Derives a measure and associated measurement method M reflecting current technological capabilities for some quantity of interest X that renders it measurable via M within the variable space of some model or theory Y.                                                                                                                                                             |
| Integrate (X,Y)     | Produces an integration (logical, ontological, epistemological) of two representational entities (theories, models) X and Y.                                                                                                                                                                                                                                                          |
| Augment (X,Y)       | Augments a theory or model X by some or all of the base assumptions of another theory or model Y.                                                                                                                                                                                                                                                                                     |
| Challenge (X,Y)     | Produces a challenge to the empirical validity, coverage, coherence, or explanatory logic of theory/model X that is logically and semantically consistent with the substantive claims of theory/model Y.                                                                                                                                                                              |
| Refute (X,Y)        | Produces one or more refutations of the substantive, empirically testable claims of theory/model X from a relevant domain.                                                                                                                                                                                                                                                            |
| Reduce (X,Y; Φ)     | Produces a reduction of the explanatory apparatus of theory/model Y for phenomenon Φ to the terms (entities, variables, inferential links) of theory/model X.                                                                                                                                                                                                                         |
| Assimilate (X,Y; Φ) | Produces an assimilation (“unification”) of the empirical base associated with phenomena Φ of theory/model Y into the apparatus (entities, variables, inferential links) of theory/model X.                                                                                                                                                                                           |
| Eliminate (X,Y; Φ)  | Produces an elimination (as “epi-phenomenal”) of the theoretical apparatus of theory/model Y for the empirical base associated with phenomena Φ to the theoretical apparatus of theory/model X.                                                                                                                                                                                       |


### E.3 Table 3. Reconstructing Epistemological/Inferential Discourse: A Grammar for Patterning Agents

| Category                                    | Subcategory / Type           | Description                                                                                                                                                                                                                                                                                                                   |
|:--------------------------------------------|------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Epistemological Stances (Commitments)       | Positivism                   | In strict form, only statements referring to observable/sensible quantities “make sense” (Mach); propositions about electrons are nonsense. In “layman” form (common among social scientists), theories/models must be testable against empirical data.                                                                       |
|                                             | Realism                      | In metaphysical form: we can speak about events/objects as they are and independently of our minds because the terms of a theory correspond to the right states of affairs. In language-dependent form: multiple ways of describing the same state of affairs exist, and “truth” is always “truth-in-a-description-language.” |
|                                             | Instrumentalism              | Theories/models are instruments for making predictions; they need not be “true,” “valid,” or “representative.” Advanced by Friedman (1953) and others in quantum mechanics.                                                                                                                                                   |
|                                             | Constructivism               | Multiple forms: the “picture of reality” emerging from science results from interactions between minds/bodies and phenomena; contributions of agencies and essences are inseparable and relevant to how objects and events are constituted and labelled (cf. participatory realism in Fuchs).                                 |
|                                             | Pragmatism                   | Amplified instrumentalism: the success of a theory/model depends on the useful effects it produces (including prediction/control).                                                                                                                                                                                            |
| Logics of Corroboration (Testing)           | Inductivism                  | Theories/models receive inductive support (confirmation) from observation statements (data) consistent with them. Includes Bayesian and frequentist approaches.                                                                                                                                                               |
|                                             | Falsificationism             | Theories/models can only be refuted by observation statements, never confirmed. Variants: dogmatic, methodological, naïve, and sophisticated falsificationism (Popper, Peirce).                                                                                                                                               |
| Ontological and Modeling Norms              | Ontological Commitments      | E.g., rational expected utility-maximizing agents in economics; “waves”/“particles” in QM; networks (of interactions, information flows, trust, epistemic states) in social network science.                                                                                                                                  |
|                                             | Commitments to Model Classes | E.g., teleological models in economics; causal models in physics; functional models in sociology and anthropology.                                                                                                                                                                                                            |
| Explanatory Norms                           | Explanatory Depth            | Some disciplines value explanations with high logical depth (e.g., mathematics, theoretical physics).                                                                                                                                                                                                                         |
|                                             | Explanatory Coverage         | Some disciplines value parsimony – explaining much by little (Ockham’s Razor).                                                                                                                                                                                                                                                |
| Justification Norms and Strategies          | Reductive Approaches         | Reduce a set of facts/theories/models to a more basic core (e.g., game theory in human/animal behavior).                                                                                                                                                                                                                      |
|                                             | Eliminative Approaches       | Eliminate phenomena as epi-phenomenal (e.g., eliminativist theories of consciousness).                                                                                                                                                                                                                                        |
|                                             | Assimilative Approaches      | Assimilate facts or models from other paradigms to support one’s own approach (e.g., transaction cost economics).                                                                                                                                                                                                             |
| Logical and Meta-Logical Norms of Inference | **—**                        | Heuristics and norms constraining scientific reasoning; commitments to deductive, inductive, or abductive inference; positions on replication, reproduction, generalization, and application, ranging from “we’re done” to “we don’t know what you are referring to.”                                                         |


### E.4 Table 4. Types of Agents – A Preliminary Synopsis

| Id | Type (Intra- / Inter-Disciplinary) | Use Case / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:---|:-----------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| L1 | INTER / INTRA                      | Translator / Re-Voicer: Re-voices or reformulates an argument, derivation, or empirical result using the terminology, inferential logic, and rhetorical conventions of another disciplinary community. For example, translating a result in transaction-cost economics into neoclassical economics, or reframing an economic coordination model in the discourse of social psychology to expose hidden assumptions.                                                                   |
| L2 | INTRA                              | Challenger / Interrogator: Emulates the critical stance of peer reviewers within the same field. It raises discipline-typical questions about inferential validity, effect-size reliability, replicability, generalizability, relevance, and informativeness, helping researchers anticipate critiques likely to arise during the review process.                                                                                                                                     |
| L3 | INTER                              | Challenger / Interrogator: Operates across disciplinary boundaries, posing challenges concerning ontological choices (e.g., individual vs. systemic causation), modeling conventions (causal vs. functional explanations), or inferential schemes (frequentist vs. Bayesian reasoning). Serves as an epistemic bridge exposing implicit disciplinary biases.                                                                                                                          |
| L4 | INTRA                              | Deconstructor: Analyzes scholarly text to extract the normative and descriptive statements presupposed by its arguments, i.e., the background axioms and warrants that must hold for the claims to be accepted within the field. Reveals hidden epistemic commitments and disciplinary norms.                                                                                                                                                                                         |
| L5 | INTER                              | Deconstructor: Performs the same function across disciplines, reconstructing what norms, empirical regularities, or theoretical premises would have to hold for a claim in one field to be persuasive in another. Useful for mapping commensurability between paradigms.                                                                                                                                                                                                              |
| L6 | INTRA                              | Arbiter: Evaluates descriptive, methodological, and normative claims within a discipline, comparing them against canonical findings or accepted background results. Acts as an internal auditor of epistemic coherence and methodological rigor.                                                                                                                                                                                                                                      |
| L7 | INTER                              | Referee: Designs or identifies “crucial experiments” capable of arbitrating between competing theories from different disciplines, i.e., experiments whose results would be regarded as binding by both sides (for example, testing cognitive-economics versus behavioral-sociology explanations of cooperation).                                                                                                                                                                     |
| L8 | INTRA                              | Model Expander / Contractor: For a given axiomatic system, explores consequences of adding or removing assumptions, e.g., introducing risk aversion into the Modigliani–Miller theorem or bounded rationality into Nash bargaining. Derives empirical predictions of the modified theory, functioning both as generator and critic of extensions.                                                                                                                                     |
| L9 | INTRA                              | Meta-Analyzer: Conducts meta-analyses by aggregating and weighting existing studies according to effect size, reliability, reproducibility, and generalizability. Helps identify empirical regularities, contradictions, and potential boundary conditions.                                                                                                                                                                                                                           |
| L10 | INTRA                              | AltGen (Alternative Explanation Generator): For a given empirical result, generates one or more competing explanations from within the same field that yield identical predictions but rest on different assumptions or mechanisms—for instance, behavioral-economics findings interpreted via “irrationality” versus “contextual adaptive rationality,” or cognitive-neuroscience data explained by distinct architectural models.                                                   |
| L11 | INTER                              | AltGenX: Produces alternative explanations drawn from other disciplines that predict the same empirical regularities but imply different theoretical or practical conclusions, e.g., framing an organizational behavior result in terms of evolutionary game theory or sociotechnical systems design.                                                                                                                                                                                 |
| L12 | INTER                              | AltGenM: Generates explanations from other fields that rely on different model ontologies, for example, replacing a causal model with a teleological or functional one, or re-describing a psychological process using network or dynamical-systems language.                                                                                                                                                                                                                         |
| L13 | INTRA                              | PrisM (Predictive / Reflective Implication Synthesizer): For a given model or theory, derives implications for related theories of the same phenomenon in adjacent disciplines (e.g., computational-vision models vs. neurophysiological models of vision). It also anticipates the kinds of questions a researcher from another field would ask to reach convergent understanding.                                                                                                   |
| L14 | INTRA                              | ArgMap (Argument Mapper): Reconstructs informal arguments within a discipline using the claim–warrant–backing schema (approximately 82 canonical forms). Reveals the argumentative patterns regarded as valid or “warrantedly assertible” without further justification.                                                                                                                                                                                                              |
| L15 | INTRA                              | ArgDef (Argument Defeater): Generates prima facie defeaters – counterarguments that undermine or qualify claims identified by *ArgMap* – using norms that are themselves warranted within the same field. Provides internal dialectical testing.                                                                                                                                                                                                                                      |
| L16 | INTER                              | ArgDef (Cross-Field Defeater): Constructs defeaters or counterarguments warranted in another discipline that studies similar phenomena, illuminating how a claim valid in one field might fail under another’s epistemic criteria.                                                                                                                                                                                                                                                    |
| L17 | INTER / INTRA                      | RadianX (Reasoning and Dialogue Network): Builds structured, tree-like representations of dialogues on a shared empirical or theoretical problem, tracking each assertion, clarification, question, answer, and response. Evaluates conversational moves according to discursive norms – validity, relevance, informativeness, coherence, semantic consistency, and responsiveness – common to one or more fields. Enables transparent mapping of reasoning paths across disciplines. |
