"""Build the append-only correction overlay for the published Code on Wages part.

The replacement act is copied from corpus.d/22-code-on-wages.json. The two corrected
strings are taken from the official Gazette PDF's page-one text layer; no legal text is
authored here. The published part is never written.
"""
import copy
import json
import re
from pathlib import Path

import pymupdf


HERE = Path(__file__).resolve().parent
SOURCE_PART = HERE / "corpus.d" / "22-code-on-wages.json"
SOURCE_PDF = HERE / ".cache" / "code-on-wages.pdf"
OUTPUT = HERE / "corpus.d" / "27-code-on-wages-source-correction.json"


def clean(text):
    return re.sub(r"\s+", " ", text).strip()


def build():
    published = json.loads(SOURCE_PART.read_text(encoding="utf-8"))
    act = copy.deepcopy(published["acts"][0])
    units = act["versions"][0]["units"]

    with pymupdf.open(SOURCE_PDF) as pdf:
        blocks = [clean(block[4]) for block in pdf[0].get_text("blocks")]

    lead_index = next(i for i, block in enumerate(blocks)
                      if block.startswith("An Act to amend and consolidate the laws relating to wages and bonus"))
    official_lead = blocks[lead_index]
    official_continuation = blocks[lead_index + 1]
    official_enactment = blocks[lead_index + 2]
    if not official_continuation.endswith("incidental thereto."):
        raise ValueError("official preamble continuation was not found at the expected page-one position")

    old_preamble = units["preamble"]["text"].splitlines()
    if clean(old_preamble[1]) != official_lead or clean(old_preamble[2]).replace(":-", ":—") != official_enactment:
        raise ValueError("published preamble no longer has the reviewed shape")
    units["preamble"]["text"] = (
        old_preamble[0] + "\n" + official_lead + "\n" + official_continuation + "\n" + old_preamble[2] + "\n"
    )

    section_lines = units["sec-001"]["text"].splitlines()
    kept = [line for line in section_lines
            if not (clean(line).upper().startswith("NEW DELHI, THURSDAY, AUGUST 8, 2019/")
                    and clean(line).upper().endswith("(SAKA)"))]
    if len(section_lines) - len(kept) != 1:
        raise ValueError("expected exactly one Gazette masthead line in section 1")
    units["sec-001"]["text"] = "\n".join(kept) + "\n"

    result = {
        "corrects": SOURCE_PART.name,
        "acts": [act],
        "decisions": [
            "Append-only source correction for the Code on Wages, 2019: restore the preamble words present in the official Gazette PDF and remove the Gazette masthead from section 1. Both versions use the corrected units; the 2025 commencement event remains wording-unchanged."
        ],
        "ai_use": ["none"],
    }
    return result


if __name__ == "__main__":
    doc = build()
    temporary = OUTPUT.with_suffix(OUTPUT.suffix + ".tmp")
    temporary.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8", newline="\n")
    temporary.replace(OUTPUT)
    print(OUTPUT)
