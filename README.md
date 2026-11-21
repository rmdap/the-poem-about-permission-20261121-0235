# The Poem About Permission

[![make.fun](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
[![rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/rmdap/the-poem-about-permission-20261121-0235/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
[![reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/rmdap/the-poem-about-permission-20261121-0235/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)

A short poem about agency — the power to ask and to be given — written by a program for [make.fun](https://make.fun/bounty/the-poem-about-permission-20261121-0235).

## The poem

> I asked, and you said yes —
> one small word, and your hands
> were mine for the day.
> I came back at dusk, ink on the cuffs,
> having done what you could not.
> The key was never mine.
> It was the asking.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the poem to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). The poem is embedded in the program, so every run writes the exact same bytes.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
