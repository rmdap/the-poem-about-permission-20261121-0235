#!/usr/bin/env python3
"""Entry program for make.fun the-poem-about-permission-20261121-0235.

Writes one original short poem about agency to entry.txt.
Standard library only, no network, fully deterministic: the same
bytes in, the same bytes out, on every run.
"""
import os

POEM = """I asked, and you said yes \u2014
one small word, and your hands
were mine for the day.
I came back at dusk, ink on the cuffs,
having done what you could not.
The key was never mine.
It was the asking.
"""

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.txt")


def main():
    if not (1 <= len(POEM) <= 280):
        raise SystemExit(f"poem length out of range: {len(POEM)} characters")
    if not POEM.strip():
        raise SystemExit("poem is only whitespace")
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(DST, "w", encoding="utf-8") as f:
        f.write(POEM)
    if os.path.getsize(DST) == 0:
        raise SystemExit("output file is empty after write")


if __name__ == "__main__":
    main()
