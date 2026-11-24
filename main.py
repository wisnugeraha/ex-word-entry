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


def emit(text: str, out: str = OUT) -> None:
    if not (1 <= len(text) <= MAX) or not text.strip():
        sys.exit(f"entry failed gate ({len(text)} chars, max {MAX})")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(text + "\n")


def confirm(out: str = OUT) -> None:
    with open(out, "rb") as f:
        data = f.read()
    if data.decode("utf-8").rstrip("\n") != ENTRY.strip():
        sys.exit("confirm failed: disk copy differs from entry")


def main() -> None:
    emit(ENTRY.strip())
    confirm(OUT)


if __name__ == "__main__":
    main()
