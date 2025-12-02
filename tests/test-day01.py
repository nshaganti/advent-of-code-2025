from day01.part1 import count_zeros
from day01.part2 import count_zero_clicks

SAMPLE = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

def test_count_zeros_sample():
    rots = SAMPLE.strip().splitlines()
    assert count_zeros(rots, start_pos=50) == 3

def test_count_zero_clicks_sample():
    rots = SAMPLE.strip().splitlines()
    assert count_zero_clicks(rots, start_pos=50) == 6
