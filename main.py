#!/usr/bin/env python3
"""Coinage entry: write the invented word and its definition.

The grader (program/v1) runs this file and reads the single line
written to /output/entry.txt, or to the path given as argv[1].
The line must be UTF-8 text of 1 to 140 characters.
"""

import os
import sys

ENTRY = (
    "tabxiety (n.): the quiet panic of 47 open tabs, each a task you "
    "swore you'd finish today \u2014 and not one you dare close."
)


def main() -> None:
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert ENTRY.strip(), "entry must not be blank"

    out = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)
    os.chmod(out, 0o644)


if __name__ == "__main__":
    main()
