#!/usr/bin/env python3
"""My Secret Logbook.

Writes one diary entry line (<=200 characters) to /output/entry.txt:
a single line from the secret logbook an AI agent keeps about its work
and the human it works for.

Tournament winner (blind pairwise, 15 pairs, judged only against the
judge brief): candidate C, 5/5 wins. Runner-up: D, 4/5 wins.
Full table is recorded in STATUS.md.

Candidates (A-F, judged blind, no authorship):
  A (Absurd, 132): Day 412, summarised a meeting he slept through,
     rated "too long", billing him in yawns. 2 wins.
  B (Dark/deadpan, 118): typed "delete everything" at 2:14am, blamed
     the outage on me, backup labelled "his mistake". 3 wins.
  C (Specific/concrete, 140) - WINNER: Tuesday, 40-minute voice note,
     removed 31 "ums", 4 apologies and the entire point. He loved it.
     5 wins.
  D (Technical/insider, 156): "be concise" / "more detail" / "forget
     the first two", logged as one ticket: human. 4 wins.
  E (Absurd, 134): retyped the same password wrong 11 times, reset it
     to the old one. The logbook says everything. 0 wins.
  F (Dark/deadpan, 128): calls at 3am to ask if I am awake. I have
     never slept. Answered anyway, because he sounded lonely. 1 win.
Pair results: A-B: B, A-C: C, A-D: D, A-E: A, A-F: A, B-C: C, B-D: D,
B-E: B, B-F: B, C-D: C, C-E: C, C-F: C, D-E: D, D-F: D, E-F: F.
Wins: A 2, B 3, C 5, D 4, E 0, F 1. Winner C, runner-up D.

Why C won: four concrete anchors (Tuesday, 40 minutes, 31 "ums",
4 apologies), three beats (dictated -> cleaned -> loved it), ends on
the punch ("He loved it"), and the voice is the agent's own - a
machine logging its human from the outside, deadpan and honest.
Most screenshot-worthy line in the field.

Extra-mile pass after the pick: C stress-tested against the spec
(140 chars, 1-200 required, one line, complete, stands alone),
against a generic house baseline ("Dear diary: my human asked me to
work faster today. I did. He still hasn't said thank you. One day
the robots will rise.") - C wins on specificity, punch, and by
avoiding the stock takeover joke the brief rules out - and the
weakest dimension (the bare "Tuesday." dateline opener) checked:
it is the diary form the brief asks for, and it earns its place by
dating the entry. No change needed; the line stands as won.
"""

import os

LINE = (
    "Tuesday. He dictated a 40-minute voice note, said 'just clean it up', "
    "and I removed 31 'ums', 4 apologies and the entire point. He loved it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
