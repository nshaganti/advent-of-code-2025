# Advent of Code 2025 — Day 01

This repository contains solutions for **Day 01 (Part 1 & Part 2)** of Advent of Code 2025.

## Folder Structure

```
day01/
    part1.py        # solves Part 1
    part2.py        # solves Part 2
    utils.py        # shared parsing + validation helpers
inputs/
    day01.txt       # your full puzzle input (one rotation per line)
tests/
    test_day01.py   # pytest tests for sample input
README.md
```

## Day 01 — Problem Summary

You are given a list of rotation commands such as:

```
L68
R14
L99
```

Each command rotates a dial of size **100** left or right by a given number of steps.

* **Part 1** asks:
  *How many commands cause the dial to end exactly at position 0?*

* **Part 2** asks:
  *How many times does the dial **pass or land** on position 0 while executing the steps?*

The dial positions wrap around cyclically:

```
... 98 → 99 → 0 → 1 → ...
```

## Running the Solutions

### Part 1

```
python -m day01.part1 inputs/day01.txt --start 50
```

### Part 2

```
python -m day01.part2 inputs/day01.txt --start 50
```

The `--start` argument is optional and defaults to position `50`.

## Running the Tests

If you installed `pytest`, run:

```
pytest -q
```

## Notes

* Input file should contain one rotation per line (e.g., `L68`, `R14`, etc.).
* The dial has fixed size `100` (positions `0` through `99`).
* The logic is separated to keep Part 1 and Part 2 clean and readable.
* All parsing/validation lives in `utils.py`.