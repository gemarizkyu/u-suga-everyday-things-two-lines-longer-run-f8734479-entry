#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run — make.fun entry.

Writes one two-line explanation to /output/entry.txt:
  Line 1 explains a queue to a 10-year-old in a single vivid sentence
  built on one analogy (a caterpillar).
  Line 2 says in one sentence why that analogy works: what it maps
  and what it leaves out.

Deterministic: no network, no randomness, no wall clock. The text is
fixed, so every run — live or replay — produces the same bytes.
"""

from pathlib import Path

ENTRY = (
    "A queue is a slow caterpillar made of people, each person a segment "
    "shuffling forward one tiny step at a time until the front reaches the door.\n"
    "The caterpillar shows how the whole line creeps forward together and why "
    "cutting in would snap it, but it leaves out that people choose to join "
    "and can walk away any time, while a caterpillar's segments never can.\n"
)


def main() -> None:
    # Guard the house gate locally: UTF-8 text, 1 to 400 characters,
    # not only white space, exactly two lines.
    text = ENTRY
    assert 1 <= len(text) <= 400, "entry must be 1-400 characters"
    assert text.strip(), "entry must not be only white space"
    assert len(text.strip().split("\n")) == 2, "entry must be two lines"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
