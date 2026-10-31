> **Status, 31 October 2026. Delete this block before the repository is posted.**
> This tree was compiled from the technical appendix (version of 30 October 2026). Files the appendix reproduces in full were copied from it. Each file still to come from the original runs has a `.PLACEHOLDER.md` file at its path, or a `PLACEHOLDER.md` in its folder. `MISSING.md` lists them all. Once the originals are in, delete the placeholders and `MISSING.md`, run the commands below from a clean copy, and confirm that every output matches Annex B.

# The Jagged Boundary: instrument, checks and stand-in runs

This is the research artifact for the Stage 1 submission "The Jagged Boundary" to the *Organization Science* special issue *AI-Enabled Frontiers in Organizational Science*. It holds every file the technical appendix names by path. The section and annex numbers below refer to that appendix.

The repository contains no participant data, because none exist. No human has yet completed the instrument. The interviews in `runs/` were conducted with model instances standing in for participants (appendix §4), and they are labelled as such throughout.

## Contents

| Folder | What it holds | Appendix |
|---|---|---|
| `instrument/` | The item sequence: `items.json` (v0.2, 37 positions), `items_v0.1.json` (v0.1, 32 positions, used for the stand-in runs), and `build_items.py`, which generates `items.json` | §2.1, §2.2 |
| `schema/` | `traversal.v0.schema.json`, the response schema (JSON Schema, draft 2020-12; draft v0.2) | §5.1, Annex A |
| `instruction-sets/` | `JAGGED_INSTRUCTION_SETS.md`, the v0.2 instruction sets for the Interviewer (both arms), the Auditor, the Increment Rater, and the stand-in participants used in the demonstration | §3, Annex C |
| `checks/` | `chk_01_adjacency.py` (the single-increase rule and dominance), `chk_02_increments.py` (the increment calibration), and `chk_03_synthetic_demo.out` (the saved output of the synthetic demonstration) | §2.1, §2.4, §8, Annex B |
| `pipeline/` | The analysis pipeline: `measures.py`, `simulate.py`, `norm_dynamics.py` and `run_demo.py` | §5.2, §6.1, §7, §8 |
| `runs/` | Records of the model runs: stand-in configurations (`configs/`), prompts as run (`prompts/`), transcripts (`transcripts/`), the interviewers' records (`records/`), audits (`audits/`), and the increment ratings (`raters/v0.1/`, `raters/v0.2/`) | §2.4, §4, Annex D |

## Regenerating the outputs in Annex B

The code needs Python 3 with NumPy and SciPy, and calls no AI model.

```
pip install numpy scipy
python3 checks/chk_01_adjacency.py instrument/items.json
python3 checks/chk_01_adjacency.py instrument/items_v0.1.json
python3 checks/chk_02_increments.py v0.1
python3 checks/chk_02_increments.py v0.2
python3 pipeline/run_demo.py
```

The first two commands check the design matrix. The next two summarize the model raters' ratings in `runs/raters/`. The last runs the synthetic demonstration and the power analysis and prints `RESULT: PASS` only if every recovery check passes. It takes about two minutes, and its output should match `checks/chk_03_synthetic_demo.out`.

The files in `runs/` record runs of a language model (Claude, model `claude-opus-5-5`; appendix §3.6). They are records, not outputs of the code above, and running the code does not regenerate them.

## Versions

Instrument v0.2 and instruction set v0.2 are the versions proposed for the pilot run. The stand-in interviews, their audits and the round 1 increment ratings used v0.1. The changes are listed in appendix §4.5 and in instruction set I.4.
