import sys
from pathlib import Path

# =============================================================================
#  Advent of Code 2025 - Day 1
#  Problem Link: https://adventofcode.com/2025/day/1
# =============================================================================

def parse_input(raw_data: str) -> list[tuple[str, int]]:
    """
    Parses input string into a list of (direction, moves).
    Example: "L68" -> ('L', 68)
    """
    instructions = []
    for line in raw_data.strip().splitlines():
        if line:
            instructions.append((line[0], int(line[1:])))
    return instructions

def part_1(instructions: list[tuple[str, int]], start_pos: int = 50) -> int:
    """
    Counts how many times the dial lands EXACTLY on 0 after a rotation.

    Logic:
        We track the position on a cyclic dial of size 100 (0-99).
        We use modular arithmetic to update the position:
        new_pos = (current_pos + displacement) % 100.
        Python's % operator handles negative numbers correctly (e.g., -10 % 100 = 90).

    Complexity:
        Time:  O(N) - We iterate through the list of N instructions once.
        Space: O(1) - We use a constant amount of extra memory.
    """
    zero_hits = 0
    current_pos = start_pos
    
    for direction, moves in instructions:
        sign = -1 if direction == 'L' else 1
        current_pos = (current_pos + (sign * moves)) % 100
        
        if current_pos == 0:
            zero_hits += 1
            
    return zero_hits

def part_2(instructions: list[tuple[str, int]], start_pos: int = 50) -> int:
    """
    Counts how many times the dial CLICKS at 0 (passing through or landing on it).
    
    Logic:
        Instead of simulating every step of a rotation (which could be slow for large moves),
        we treat the dial as an infinite number line (Absolute Position).
        - A 'click' occurs every time we cross a multiple of 100.
        - Moving Right (positive): We count multiples of 100 in the interval (start, end].
          Formula: floor(end / 100) - floor(start / 100)
        - Moving Left (negative): We count multiples of 100 in the interval [end, start).
          Formula: floor((start - 1) / 100) - floor((end - 1) / 100)
        
    Complexity:
        Time:  O(N) - We calculate the result mathematically for each instruction in O(1).
                      This avoids loops proportional to the size of the moves (e.g., R1000).
        Space: O(1) - Constant auxiliary space.
    """
    clicks = 0
    abs_pos = start_pos
    
    for direction, moves in instructions:
        sign = -1 if direction == 'L' else 1
        target_pos = abs_pos + (sign * moves)
        
        if sign == 1: 
            # Moving Right: Interval (start, end]
            # Leaving 'start' doesn't count, landing on 'end' does.
            clicks += (target_pos // 100) - (abs_pos // 100)
        else:
            # Moving Left: Interval [end, start)
            # We shift the logic by -1 to handle the inclusive/exclusive boundaries correctly
            # for negative movement.
            clicks += ((abs_pos - 1) // 100) - ((target_pos - 1) // 100)
            
        abs_pos = target_pos
        
    return clicks

# =============================================================================
#  Unit Tests
# =============================================================================

def run_tests():
    """Runs tests on the sample input provided in the prompt."""
    print("Running tests...", end=" ")
    
    sample_input = """
L68
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
    data = parse_input(sample_input)
    
    # Test Part 1
    p1_result = part_1(data)
    assert p1_result == 3, f"Part 1 Failed: Expected 3, got {p1_result}"
    
    # Test Part 2 (Sample)
    p2_result = part_2(data)
    assert p2_result == 6, f"Part 2 Failed: Expected 6, got {p2_result}"

    # Test Part 2 (Edge Case: R1000 from 50)
    # 50 -> 1050 crosses 100, 200... 1000. (10 clicks)
    r1000_result = part_2([('R', 1000)], start_pos=50)
    assert r1000_result == 10, f"R1000 Failed: Expected 10, got {r1000_result}"

    # Test Part 2 (Edge Case: Leaving 0)
    # 0 -> 10 (Right) should be 0 clicks.
    leave_zero = part_2([('R', 10)], start_pos=0)
    assert leave_zero == 0, f"Leaving Zero Failed: Expected 0, got {leave_zero}"
    
    print("ALL TESTS PASSED. ✅\n")

# =============================================================================
#  Main Execution
# =============================================================================

if __name__ == "__main__":
    run_tests()
    
    input_file = Path(__file__).parent / "inputs" / "day_01.txt"
    
    if not input_file.exists():
        print(f"⚠️  Input file not found at: {input_file}")
    else:
        raw_data = input_file.read_text()
        instructions = parse_input(raw_data)
        
        print(f"--- Day 1 Solution ---")
        print(f"Part 1: {part_1(instructions)}")
        print(f"Part 2: {part_2(instructions)}")