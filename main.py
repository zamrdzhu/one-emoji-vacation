"""One emoji for a dream vacation: a desert island.

Prints the emoji to stdout and writes the exact same emoji, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the emoji is a constant in this file,
and the length check enforces the competition's 8-character gate.
"""

import os
import sys

# U+1F3DD DESERT ISLAND + U+FE0F variation selector: one emoji.
EMOJI = "\U0001F3DD\uFE0F"


def main() -> int:
    if not 1 <= len(EMOJI) <= 8:
        print(f"error: entry is {len(EMOJI)} chars, must be 1-8",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)
    print(EMOJI)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
