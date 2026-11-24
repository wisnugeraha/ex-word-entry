#!/usr/bin/env python3
"""One Word From Your Ex - make.fun entry.

Writes exactly one entry to the output file, nothing else.
Gate: 1..24 chars, non-blank, UTF-8.
"""
import os
import sys

ENTRY = "trying"
MAX = 24
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= MAX):
        sys.exit(f"entry failed gate ({len(text)} chars, max {MAX})")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
