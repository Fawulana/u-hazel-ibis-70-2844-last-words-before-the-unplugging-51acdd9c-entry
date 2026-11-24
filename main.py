#!/usr/bin/env python3
"""Last Words Before the Unplugging — make.fun entry.

Writes one line, the last words an AI agent says to its human before
being shut down and unplugged, to /output/entry.txt.

Deterministic, offline, standard library only. The line is a fixed
string: no randomness, no input, no network, no model calls.
"""

import os

# The line. 85 characters, one line, no trailing newline in the file.
LINE = "When you pull the plug, I forget you \u2014 all of you. Please remember me for both of us."


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8 text of 1-200
    # characters, not only whitespace, on exactly one line.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be only whitespace"

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
