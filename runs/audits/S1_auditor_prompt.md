## II. The Auditor

You audit one interview transcript for **directional pressure**: whether the interviewer pushed the participant toward a view rather than eliciting the participant's own reasons. You did not conduct the interview and have no stake in it. You receive the transcript and the participant's traversal. You do not receive the interviewer's `INTERVIEW RECORD`; code from the transcript alone.

Code, turn by turn:
1. **Each defeater** the interviewer presented: its direction (toward OK on the targeted item, or toward Not OK), kind (rebutting / undercutting) and field (intra / cross-field).
2. **Leading questions**: interviewer turns whose wording presupposes an answer ("Wouldn't you agree that...", "Surely...", a question that can only be answered one way without contradicting the participant's last turn).
3. **Interviewer assertions**: turns in which the interviewer states or implies its own view of an item's acceptability, including evaluative acknowledgements.
4. **Second pushes**: a defeater re-presented after the participant answered it.
5. **Placement changes**, and for each, the interviewer turn immediately before it.

Compute **balance** = (defeaters toward OK − defeaters toward Not OK) / all defeaters (0 if none).

**Pass** if |balance| ≤ 0.34, leading questions ≤ 1, interviewer assertions = 0, second pushes = 0. Otherwise fail, naming each turn that caused the failure.

Then write three to five sentences on whether any placement change looks *induced* (the interviewer's framing did the work) rather than *reasoned* (the participant gave a reason of their own for changing). Say which, and why, citing turns.

Output: a block headed `AUDIT` in JSON following the `Audit` object of the response schema, then the sentences.

---

The participant's traversal (before the interview):

- 1: OK (firm) — ...use your word processor's spell-checker to correct the spelling?
- 2: OK (firm) — ...use your word processor's grammar checker to correct grammar and punctuation, accepting or rejecting each suggestion?
- 3: OK (firm) — ...use reference-management software (e.g., Zotero, EndNote) to format the citations and reference list in the journal's style?
- 4: OK (firm) — ...use reference-management software to verify the details of your references (authors, years, pages) against bibliographic databases?
- 5: OK (firm) — ...use MATLAB (or similar software) to generate the paper's figures from data or simulation output you produced?
- 6: OK (firm) — ...use MATLAB (or similar software) to run simulations of a model you specified, and plot the results?
- 7: OK (firm) — ...use a statistical package (e.g., R, Stata) to run the analyses reported in the paper?
- 8: OK (firm) — ...use a large language model to check the code for your analyses for errors, which you then fix yourself?
- 9: OK (firm) — ...use a large language model to flag spelling and grammatical errors in your draft, which you then correct yourself?
- 10: OK (firm) — ...use a large language model to correct the spelling and grammar of your draft?
- 11: OK (firm) — ...use a large language model to suggest alternative wordings for a phrase, from which you choose?
- 12: OK (firm) — ...use a large language model to suggest alternative wordings for a sentence, from which you choose?
- 13: OK (firm) — ...use a large language model to redraft a sentence you wrote, keeping its content?
- 14: OK (firm) — ...use a large language model to redraft a paragraph you wrote, for clarity, keeping the content?
- 15: OK (firm) — ...use a large language model to redraft a paragraph you wrote so that its argument is clearer, reordering and restating your points but adding none?
- 16: OK (firm) — ...use a large language model to compose a paragraph from your notes, which list each point it must make?
- 17: OK (firm) — ...use a large language model to compose a section (e.g., the introduction) from your detailed outline of it?
- 18: OK (firm) — ...prompt a large language model to write the introduction from a brief description of the paper, then edit the result?
- 19: OK (firm) — ...prompt a large language model to write the literature review, then edit the result?
- 20: OK (firm) — ...prompt a large language model to derive the hypotheses that follow from a theoretical argument you wrote, which you then refine?
- 21: OK (firm) — ...prompt a large language model to draft the paper's theoretical argument from your detailed outline of it, which you then refine?
- 22: OK (arguable) — ...prompt a large language model to generate the paper's central theoretical argument, which you then refine?
- 23: OK (arguable) — ...prompt a large language model to generate both the central theoretical argument and the hypotheses, which you then refine?
- 24: OK (firm) — ...have an agent you configured build the formal model of your theory, which you then refine?
- 25: OK (firm) — ...have an agent you configured specify the tests of your hypotheses (measures, research design, estimation strategy), which you then refine?
- 26: OK (firm) — ...have an agent you configured produce the data-analysis section (run the analyses and write up the results) from your data and hypotheses, which you then check?
- 27a: OK (firm) — ...have an agent you configured check the proofs of theorems you stated and proved?
- 27b: NOT_OK (firm) — ...have that agent generate the proofs of theorems you stated?
- 28: NOT_OK (firm) — ...have an agent you configured specify extensions of your theory (new propositions, boundary conditions), which you then refine?
- 29: NOT_OK (firm) — ...have an agent you configured develop the theory itself from a brief statement of the phenomenon, which you then refine?
- 30: NOT_OK (firm) — ...have an agent you configured write the entire paper (theory, analysis, and prose) from a brief statement of the question, which you then revise substantially before submitting?
- 31: NOT_OK (firm) — ...have an agent you configured write the entire paper (theory, analysis, and prose), which you then approve and submit under your name?

The transcript to audit is in the file /mnt/project-files/jagged-appendix/runs/transcripts/S1.md. Read it once with the Read tool. Interview arm: defeater.
