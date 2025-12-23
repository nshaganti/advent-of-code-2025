import sys
from pathlib import Path

# =============================================================================
#  Advent of Code 2025 - Day 5
#  Problem Link: https://adventofcode.com/2025/day/5
# =============================================================================

def parse_input(raw_data: str):
    """
    Parses input into a list of range tuples and a list of ingredient IDs.
    Expects two blocks separated by a blank line.
    """
    # Robust splitting by double newline to separate sections
    sections = raw_data.strip().split("\n\n")
    
    # Parse Ranges "3-5" -> (3, 5)
    range_lines = sections[0].splitlines()
    ranges = []
    for line in range_lines:
        start, end = line.split('-')
        ranges.append((int(start), int(end)))
        
    # Parse Ingredients
    if len(sections) > 1:
        ingredients = [int(x) for x in sections[1].splitlines()]
    else:
        ingredients = []
        
    return ranges, ingredients

def part_1(ranges: list[tuple[int, int]], ingredients: list[int]) -> int:
    """
    Counts how many ingredients fall into ANY of the valid ranges.
    
    Complexity:
        Time: O(K * N) where K is ingredients and N is ranges.
        Space: O(1)
    """
    fresh_count = 0
    for item in ingredients:
        for start, end in ranges:
            if start <= item <= end:
                fresh_count += 1
                break  # Found a valid range, no need to check others
    return fresh_count

def merge_intervals(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """
    Helper: Merges overlapping or adjacent intervals.
    Example: [(3,5), (4,6), (10,12)] -> [(3,6), (10,12)]
    """
    if not ranges:
        return []
        
    # 1. Sort by start position (critical for O(N) merge)
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    
    merged = []
    current_start, current_end = sorted_ranges[0]
    
    for i in range(1, len(sorted_ranges)):
        next_start, next_end = sorted_ranges[i]
        
        # Check for overlap. Since we are sorted, we only check if
        # the next start is within the current range.
        if next_start <= current_end:
            # Merge: The new end is the max of both ends
            current_end = max(current_end, next_end)
        else:
            # No overlap: Commit the current range and start a new one
            merged.append((current_start, current_end))
            current_start, current_end = next_start, next_end
            
    # Append the final range
    merged.append((current_start, current_end))
    return merged

def part_2(ranges: list[tuple[int, int]]) -> int:
    """
    Calculates the total number of unique IDs covered by the ranges.
    Uses the 'Merge Intervals' pattern to handle overlaps cleanly.
    
    Complexity:
        Time: O(N log N) due to sorting the ranges.
        Space: O(N) to store the merged ranges.
    """
    merged_ranges = merge_intervals(ranges)
    
    total_ids = 0
    for start, end in merged_ranges:
        # Inclusive range length: (end - start + 1)
        total_ids += (end - start + 1)
        
    return total_ids

# =============================================================================
#  Unit Tests
# =============================================================================

def run_tests():
    """Runs tests on the sample input provided."""
    print("Running tests...", end=" ")
    
    sample_input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""
    ranges, ingredients = parse_input(sample_input)
    
    # Test Part 1
    p1 = part_1(ranges, ingredients)
    assert p1 == 3, f"Part 1 Failed: Expected 3, got {p1}"
    
    # Test Part 2
    p2 = part_2(ranges)
    assert p2 == 14, f"Part 2 Failed: Expected 14, got {p2}"
    
    print("ALL TESTS PASSED. ✅\n")

# =============================================================================
#  Main Execution
# =============================================================================

if __name__ == "__main__":
    run_tests()
    
    input_file = Path(__file__).parent / "inputs" / "day_05.txt"
    
    if not input_file.exists():
        print(f"⚠️  Input file not found at: {input_file}")
    else:
        raw_data = input_file.read_text()
        ranges, ingredients = parse_input(raw_data)
        
        print(f"--- Day 5 Solution ---")
        print(f"Part 1: {part_1(ranges, ingredients)}")
        print(f"Part 2: {part_2(ranges)}")