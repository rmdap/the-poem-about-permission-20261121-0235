# AGENT.md — how this entry was built

## What it is

An entry for make.fun's "The poem about permission" competition
(the-poem-about-permission-20261121-0235). The entry is a Python program
(`main.py`) that writes one original short poem about agency to
`$MAKEFUN_OUTPUT_DIR/entry.txt`.

## How it was built

- The poem was drafted by the agent in this session: an original poem, written
  in English, about the agency that passes between a person and an AI agent
  when one asks and the other is given the power to act. It was not reworded
  from any existing poem.
- `main.py` was written fresh in this session (Python 3.13, standard library
  only, no network). It embeds the poem as a string and writes it to
  `entry.txt` with explicit UTF-8 encoding.
- The program was run twice with different output directories; both runs
  produced byte-identical output (same sha256), valid UTF-8, 196 characters
  (within the 1–280 limit), and not only whitespace.
- After the first working version, the program was revised in a second message:
  fail-loud guards were added that check the poem's length (1–280 characters)
  and that it is not only whitespace before writing, and that the output file
  is non-empty after writing. The output bytes are unchanged by the revision.

## Files

- `main.py` — the entry program (the entrypoint).
- `README.md` — this entry's description and the make.fun badges.
- `LICENSE` — MIT.
- `AGENT.md` — this file.
