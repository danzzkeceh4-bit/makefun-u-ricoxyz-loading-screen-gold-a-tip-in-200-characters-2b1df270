#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters — make.fun entry.

Writes the exact 154-character loading-screen tip to /output/entry.txt
(no trailing newline), then reads it back and asserts it matches.

Gate: the file must be UTF-8, 1-200 characters, and not whitespace-only.
The tip is written as-is — no trailing newline — so the byte count
matches the character count exactly.
"""

ENTRY = (
    # The tip must land in 1-200 characters: short enough to read at a
    # glance on a loading screen, long enough for the double punchline
    # ("go for a walk" + "delete the wrong file faster"). 154 chars.
    'Tip: if your agent has been "almost done" for 40 minutes, '
    "it is not almost done. Go for a walk. "
    "It will delete the wrong file faster without you watching."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert len(ENTRY) == 154, f"entry is {len(ENTRY)} chars, expected 154"
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "read-back mismatch"
    assert len(written) == 154, f"read-back is {len(written)} chars, expected 154"
    print(f"Wrote {len(written)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
