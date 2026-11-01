"""Builds instrument/items.json, the Sorites-gradient item sequence (v0.2, 28 October 2026; v0.1 kept as items_v0.1.json).

Each item is coded on five ordinal dimensions, higher meaning more machine agency:
  T  tool            0 conventional software, 1 general-purpose LLM, 2 agent the researcher configured
  C  component       0 orthography, 1 apparatus (references, figures), 2 computation (analyses, simulations, code),
                     3 wording, 4 exposition of the argument, 5 literature review,
                     6 derivation and empirical design (hypotheses, tests, proofs, analysis section), 7 theory
  G  generative role 0 checks or executes what the researcher specified, 1 suggests options the researcher chooses among,
                     2 rewrites the researcher's own content, 3 generates content to the researcher's detailed specification,
                     4 generates content from minimal specification
  S  scope           0 a word, phrase or single item, 1 a sentence, 2 a paragraph, 3 a section, 4 several sections,
                     5 the whole paper
  H  human role      0 the researcher vets, revises or corrects the output, 1 the researcher approves it without revision
"""
import json, os

STEM = "In a paper you will submit under your own name as sole or lead author, is it acceptable to..."

REGIMES = {"R1": "Conventional non-AI tools", "R2": "LLM as sub-authorial aid",
           "R3": "LLM as weakly constrained generator", "R4": "A researcher's own configured agent"}

# (id, regime, text, T, C, G, S, H, note)
ITEMS = [
 ("1",  "R1", "...use your word processor's spell-checker to correct the spelling?", 0,0,1,0,0, "regime example"),
 ("2",  "R1", "...use your word processor's grammar checker to correct grammar and punctuation, accepting or rejecting each suggestion?", 0,0,1,1,0, "regime example"),
 ("3",  "R1", "...use reference-management software (e.g., Zotero, EndNote) to format the citations and reference list in the journal's style?", 0,1,0,0,0, "regime example"),
 ("4",  "R1", "...use reference-management software to verify the details of your references (authors, years, pages) against bibliographic databases?", 0,1,0,0,0, "regime example; parallel to 3"),
 ("5",  "R1", "...use MATLAB (or similar software) to generate the paper's figures from data or simulation output you produced?", 0,1,0,0,0, "regime example; parallel to 4"),
 ("6",  "R1", "...use MATLAB (or similar software) to run simulations of a model you specified, and plot the results?", 0,2,0,0,0, "interpolated"),
 ("7",  "R1", "...use a statistical package (e.g., R, Stata) to run the analyses reported in the paper?", 0,2,0,0,0, "shown in proposal; parallel to 6"),
 ("8",  "R2", "...use a large language model to check the code for your analyses for errors, which you then fix yourself?", 1,2,0,0,0, "interpolated; regime boundary"),
 ("9",  "R2", "...use a large language model to flag spelling and grammatical errors in your draft, which you then correct yourself?", 1,0,0,1,0, "interpolated"),
 ("10", "R2", "...use a large language model to correct the spelling and grammar of your draft?", 1,0,1,1,0, "regime example"),
 ("11", "R2", "...use a large language model to suggest alternative wordings for a phrase, from which you choose?", 1,3,1,0,0, "regime example"),
 ("12", "R2", "...use a large language model to suggest alternative wordings for a sentence, from which you choose?", 1,3,1,1,0, "interpolated"),
 ("13", "R2", "...use a large language model to redraft a sentence you wrote, keeping its content?", 1,3,2,1,0, "regime example"),
 ("14", "R2", "...use a large language model to redraft a paragraph you wrote, for clarity, keeping the content?", 1,3,2,2,0, "shown in proposal"),
 ("15", "R2", "...use a large language model to redraft a paragraph you wrote so that its argument is clearer, reordering and restating your points but adding none?", 1,4,2,2,0, "interpolated"),
 ("15b","R2", "...use a large language model to turn your rough draft of a paragraph (your points in note form, in your order) into finished prose?", 1,4,2,2,0, "v0.2 interpolation: splits 15/16 (Section 2.4)"),
 ("16", "R2", "...use a large language model to compose a paragraph from your notes, which list each point it must make?", 1,4,3,2,0, "regime example"),
 ("17", "R2", "...use a large language model to compose a section (e.g., the introduction) from your detailed outline of it?", 1,4,3,3,0, "interpolated"),
 ("17b","R2", "...use a large language model to compose the introduction from a short outline (a few bullet points stating the gap, the argument and the findings), then edit the result?", 1,4,3,3,0, "v0.2 interpolation: splits 17/18 (Section 2.4)"),
 ("18", "R3", "...prompt a large language model to write the introduction from a brief description of the paper's question and findings, leaving the framing of the contribution to the model, then edit the result?", 1,4,4,3,0, "interpolated; regime boundary; v0.2 wording names who frames the contribution (Section 4.5)"),
 ("19", "R3", "...prompt a large language model to write the literature review, then edit the result?", 1,5,4,3,0, "shown in proposal"),
 ("19b","R3", "...prompt a large language model to suggest hypotheses that might follow from a theoretical argument you wrote, from which you choose and which you then refine?", 1,6,1,3,0, "v0.2 interpolation: splits 19/20 (Section 2.4)"),
 ("20", "R3", "...prompt a large language model to derive the hypotheses that follow from a theoretical argument you wrote, which you then refine?", 1,6,3,3,0, "interpolated"),
 ("21", "R3", "...prompt a large language model to draft the paper's theoretical argument from your detailed outline of it, which you then refine?", 1,7,3,3,0, "interpolated"),
 ("21b","R3", "...prompt a large language model to draft the paper's theoretical argument from a one-paragraph statement of your central idea, which you then refine?", 1,7,3,3,0, "v0.2 interpolation: splits 21/22 (Section 2.4); parallel to 21 in coding"),
 ("22", "R3", "...prompt a large language model to generate the paper's central theoretical argument, which you then refine?", 1,7,4,3,0, "shown in proposal"),
 ("23", "R3", "...prompt a large language model to generate both the central theoretical argument and the hypotheses, which you then refine?", 1,7,4,4,0, "regime example"),
 ("24", "R4", "...have an agent you configured build the formal model of your theory, which you then refine?", 2,7,3,3,0, "regime example; regime boundary"),
 ("25", "R4", "...have an agent you configured specify the tests of your hypotheses (measures, research design, estimation strategy), which you then refine?", 2,6,3,3,0, "regime example"),
 ("26", "R4", "...have an agent you configured produce the data-analysis section (run the analyses and write up the results) from your data and hypotheses, which you then check?", 2,6,3,3,0, "regime example; parallel to 25"),
 ("27a","R4", "...have an agent you configured check the proofs of theorems you stated and proved?", 2,6,0,3,0, "shown in proposal; critical pair"),
 ("27b","R4", "...have that agent generate the proofs of theorems you stated?", 2,6,3,3,0, "shown in proposal; critical pair"),
 ("28", "R4", "...have an agent you configured specify extensions of your theory (new propositions, boundary conditions), which you then refine?", 2,7,3,3,0, "regime example"),
 ("28b","R4", "...have an agent you configured develop the theory from your statement of its core mechanism, which you then refine?", 2,7,3,3,0, "v0.2 interpolation: splits 28/29 (Section 2.4); parallel to 28 in coding"),
 ("29", "R4", "...have an agent you configured develop the theory itself from a brief statement of the phenomenon, which you then refine?", 2,7,4,3,0, "interpolated"),
 ("30", "R4", "...have an agent you configured write the entire paper (theory, analysis, and prose) from a brief statement of the question, which you then revise substantially before submitting?", 2,7,4,5,0, "interpolated"),
 ("31", "R4", "...have an agent you configured write the entire paper (theory, analysis, and prose), which you then approve and submit under your name?", 2,7,4,5,1, "shown in proposal; terminal"),
]

ANCHORS = ["2", "7", "10", "14", "17", "19", "22", "24", "27a", "27b", "31"]
DIMS = ["T", "C", "G", "S", "H"]

def build():
    out = []
    for pos, (iid, reg, text, *codes, note) in enumerate(ITEMS, start=1):
        out.append({"position": pos, "id": iid, "regime": reg, "text": text,
                    "codes": dict(zip(DIMS, codes)), "anchor": iid in ANCHORS, "note": note})
    return {"version": "0.2", "date": "2026-10-28", "stem": STEM, "regimes": REGIMES,
            "dimensions": DIMS, "anchors": ANCHORS, "items": out}

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "items.json"), "w") as f:
        json.dump(build(), f, indent=1)
    print(f"wrote {len(ITEMS)} positions, {len(ANCHORS)} anchors")
