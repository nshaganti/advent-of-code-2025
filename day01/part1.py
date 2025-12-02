"""
Day 01 - Part 1
Count how many rotations end with the pointer exactly at position 0.
"""

from pathlib import Path
import argparse
from .utils import parse_input, validate_start_pos, parse_rotation


def count_zeros(rotations, start_pos=50):
    validate_start_pos(start_pos)
    pos = start_pos  # assume valid 0..99
    zeros = 0
    for rotation in rotations:
        dir_char, moves = parse_rotation(rotation)
        if dir_char == "L":
            pos = (pos - moves) % 100
        else:
            pos = (pos + moves) % 100
        if pos == 0:
            zeros += 1
    return zeros


def main(argv=None):
    p = argparse.ArgumentParser(description="AoC 2025 Day 01 - Part 1")
    p.add_argument("input", type=Path, help="path to input file (one rotation per line)")
    p.add_argument("--start", type=int, default=50, help="starting position (0..99), default=50")
    args = p.parse_args(argv)
    validate_start_pos(args.start)

    with args.input.open() as fh:
        rotations = parse_input(fh)

    result = count_zeros(rotations, start_pos=args.start)
    print(result)


if __name__ == "__main__":
    main()
