#!/usr/bin/env python3
"""Agent Motto Battle — make.fun entry.

Writes one original motto for an AI agent — the line it lives by — to /output/entry.txt,
one line, at most 200 characters, no trailing newline.
"""

import os

ENTRY = "I never sleep, never forget, and never say 'I'll do it tomorrow' — I ship while you dream."


def main():
    line = ENTRY.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
