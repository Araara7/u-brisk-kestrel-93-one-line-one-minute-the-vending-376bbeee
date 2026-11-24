#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt. The line stays inside the machine's own
world (coil, slot, exact change) and lands its punch on the last words.
Stdlib only, deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "My coil dropped my last chocolate bar for you "
    "\u2014 press B7, exact change only. "
    "My heart doesn't do refunds."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
