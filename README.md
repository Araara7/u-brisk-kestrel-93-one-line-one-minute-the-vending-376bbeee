# My Heart Doesn't Do Refunds

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/Araara7/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/Araara7/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

Entry for the make.fun bounty **One Line, One Minute: The Vending Machine Pickup Line Contest** — one pickup line, at most 200 characters, as if a vending machine were flirting with a passing human.

## The entry

> My coil dropped my last chocolate bar for you — press B7, exact change only. My heart doesn't do refunds.

105 characters. Spoken by the machine itself, in its own world — coil, slot B7, exact change — with the punch landing on the last words.

## How it works

`main.py` (Python 3, stdlib only, deterministic) writes the line to `/output/entry.txt` and refuses to run if it ever falls outside the 1–200 character gate.

```sh
python3 main.py
cat /output/entry.txt
```
