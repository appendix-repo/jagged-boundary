# Still needed before posting (delete this file once done)

Mihnea, these are the files the appendix names that it doesn't reproduce, so they have to come from the original runs. Each has a placeholder at its path that says what it is and what it must reproduce.

## Code

- [ ] `instrument/build_items.py`
- [ ] `checks/chk_01_adjacency.py`
- [ ] `checks/chk_02_increments.py`
- [ ] `pipeline/measures.py`
- [ ] `pipeline/simulate.py`
- [ ] `pipeline/norm_dynamics.py`
- [ ] `pipeline/run_demo.py`

## Data files

- [ ] `instrument/items.json` (v0.2). The appendix gives every item's wording and codes, so this could be rebuilt from §2.1 and §2.2 if the original is lost. But `build_items.py` and `chk_01` expect a particular format, so the original is better.
- [ ] `instrument/items_v0.1.json`. This can't be rebuilt from the appendix, because item 18's v0.1 wording isn't given there.
- [ ] `runs/configs/standins.json` and `runs/configs/make_standins.py`

## Run records

- [ ] `runs/prompts/`: the v0.1 prompts as run
- [ ] `runs/records/`: the interviewers' INTERVIEW RECORDs, S1 to S4
- [ ] `runs/transcripts/S1_raw.md` to `S4_raw.md`: the uncut logs
- [ ] `runs/raters/v0.1/` and `runs/raters/v0.2/`: the ratings with each rater's reasons

## Please check

- [ ] **Files taken from the appendix.** Four sets of files here were copied from the appendix: `schema/traversal.v0.schema.json` (Annex A), `instruction-sets/JAGGED_INSTRUCTION_SETS.md` (Annex C), `checks/chk_03_synthetic_demo.out` (Annex B), and the transcripts and audits in `runs/transcripts/S1.md` to `S4.md` and `runs/audits/` (Annex D). If you have the originals, use yours. If yours differ from the appendix, the appendix has to change to match.
- [ ] **File names.** The appendix doesn't name individual files in `runs/transcripts/` (other than the raw logs) or in `runs/audits/`. The names used here are mine; rename them to match your files.
- [ ] **The README's commands.** The README gives `python3 checks/chk_01_adjacency.py instrument/items_v0.1.json` for the v0.1 check. Annex B shows that output but not the command. Please confirm it, then run every README command from a clean copy and check the outputs against Annex B.
- [ ] **Schema version.** The schema file is named `v0`, but its identifier says v0.2. If you rename it, the appendix's two references to it change too.
- [ ] **Licence.** None has been added yet.
