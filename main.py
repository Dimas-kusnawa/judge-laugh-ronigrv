#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent."""

import os

# The line: the agent asks for clearer instructions, and the human
# answers with a 14-minute voice note that explains nothing.
# The joke lands on the turn: the human was asked for clarity and
# replied with the least clear format possible, then acted as if
# the vagueness itself were the instruction.
LINE = (
    "I asked my human for clearer instructions. "
    "He sent a 14-minute voice note that just says "
    "'you know what I mean'."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # One line only, no trailing newline: the gate counts 1-200 chars.
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {path}: {LINE} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
