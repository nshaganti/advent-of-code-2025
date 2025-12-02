"""
Day 01 - Part 2
Count how many times the pointer hits or passes position 0 while performing the moves.
"""

from pathlib import Path
import argparse
from .utils import parse_input, validate_start_pos, parse_rotation


def count_zero_clicks(rotations, start_pos=50):
    """
    For each move, count how many times 0 is crossed or landed on while traversing the steps.
    This implementation expects start_pos in [0,99] and moves >= 0.
    """
    validate_start_pos(start_pos)
    pos = start_pos
    clicks = 0
    for rotation in rotations:
        dir_char, k = parse_rotation(rotation)
        if dir_char == "R":
            # crosses = number of multiples of 100 reached when going from pos to pos+k
            clicks += (pos + k) // 100
            pos = (pos + k) % 100
        else:  # left move
            # If starting on 0, you hit 0 every 100 steps.
            if pos == 0:
                clicks += k // 100
            else:
                if k >= pos:
                    clicks += 1 + (k - pos) // 100
                # else 0 crossings
            pos = (pos - k) % 100
    return clicks


def main(argv=None):
    p = argparse.ArgumentParser(description="AoC 2025 Day 01 - Part 2")
    p.add_argument("input", type=Path, help="path to input file (one rotation per line)")
    p.add_argument("--start", type=int, default=50, help="starting position (0..99), default=50")
    args = p.parse_args(argv)
    validate_start_pos(args.start)

    with args.input.open() as fh:
        rotations = parse_input(fh)

    result = count_zero_clicks(rotations, start_pos=args.start)
    print(result)


if __name__ == "__main__":
    main()
