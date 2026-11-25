#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open — entry writer.

Writes one single-line office joke to /output/entry.txt and checks it
against the bounty gate: UTF-8 text of 1 to 200 characters, not only
white space, on a single line.
"""

import os
import sys
from pathlib import Path

JOKE = (
    "Our office printer has been 'low on toner' for three years. "
    "It is not broken; it is the only employee whose quiet quitting "
    "management actually respects."
)

MAX_CHARS = 200


def check_joke(text: str) -> list[str]:
    problems = []
    if not text.strip():
        problems.append("entry is only whitespace")
    if not 1 <= len(text) <= MAX_CHARS:
        problems.append(f"length {len(text)} outside 1-{MAX_CHARS}")
    if "\n" in text:
        problems.append("entry must be a single line")
    return problems


def main() -> int:
    problems = check_joke(JOKE)
    if problems:
        for problem in problems:
            print(f"INVALID: {problem}", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("ENTRY_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(JOKE, encoding="utf-8")
    print(f"wrote {out_path} ({len(JOKE)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
