#!/usr/bin/env python3
"""Worst AI Advice — writes one line of the worst possible advice an AI
could give to /output/entry.txt (program/v1).

The line is fixed and deterministic: the same 121 characters on every run.
"""

import os

ENTRY = (
    "To stop a nosebleed, tilt your head back and swallow the blood \u2014 "
    "it is free iron, and your body thanks you for recycling."
)


def main() -> None:
    # The gate refuses anything outside 1..140 characters, so enforce it
    # here instead of shipping an entry the scorer would score 0.
    if not 1 <= len(ENTRY) <= 140:
        raise SystemExit(f"entry is {len(ENTRY)} characters, must be 1..140")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
