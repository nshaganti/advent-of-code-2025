import sys
from pathlib import Path

# =============================================================================
#  Advent of Code 2025 - Day 4
#  Problem Link: https://adventofcode.com/2025/day/4
# =============================================================================

# Direction vectors: (dr, dc) for all 8 neighbors (King's move)
DIRECTIONS = [
    (0, 1), (0, -1), (1, 0), (-1, 0),
    (1, 1), (1, -1), (-1, 1), (-1, -1)
]

def parse_input(raw_data: str) -> set[tuple[int, int]]:
    """
    Parses the grid into a Set of coordinates containing '@'.
    Using a Set makes lookups O(1) and removes the need for bounds checking.
    """
    active_cells = set()
    for r, line in enumerate(raw_data.strip().splitlines()):
        for c, char in enumerate(line):
            if char == "@":
                active_cells.add((r, c))
    return active_cells

def part_1(active_cells: set[tuple[int, int]]) -> int:
    """
    Counts how many '@' symbols have fewer than 4 neighbors.
    
    Complexity:
        Time: O(N) where N is the number of '@' symbols.
        Space: O(1) auxiliary (we just read the set).
    """
    removable_count = 0
    
    for r, c in active_cells:
        neighbors = 0
        for dr, dc in DIRECTIONS:
            if (r + dr, c + dc) in active_cells:
                neighbors += 1
                if neighbors >= 4:
                    break
        
        if neighbors < 4:
            removable_count += 1
            
    return removable_count

def part_2(active_cells: set[tuple[int, int]]) -> int:
    """
    Simulates the removal process until stabilization.
    In each step, ALL items with < 4 neighbors are removed simultaneously.
    
    Complexity:
        Time: O(Steps * N)
        Space: O(N) to store the grid state.
    """
    # Create a copy so we don't modify the input for other functions
    current_grid = active_cells.copy()
    total_removed = 0
    
    while True:
        to_remove = set()
        
        # 1. Identify candidates (Simultaneous Scan)
        for r, c in current_grid:
            neighbors = 0
            for dr, dc in DIRECTIONS:
                if (r + dr, c + dc) in current_grid:
                    neighbors += 1
                    if neighbors >= 4:
                        break
            
            if neighbors < 4:
                to_remove.add((r, c))
        
        # 2. Check termination condition
        if not to_remove:
            break
            
        # 3. Apply updates (Simultaneous Removal)
        total_removed += len(to_remove)
        current_grid -= to_remove
        
    return total_removed

# =============================================================================
#  Unit Tests
# =============================================================================

def run_tests():
    """Runs tests on the sample input provided."""
    print("Running tests...", end=" ")
    
    sample_input = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""
    data = parse_input(sample_input)
    
    # Test Part 1
    p1 = part_1(data)
    assert p1 == 13, f"Part 1 Failed: Expected 13, got {p1}"
    
    # Test Part 2
    p2 = part_2(data)
    assert p2 == 43, f"Part 2 Failed: Expected 43, got {p2}"
    
    print("ALL TESTS PASSED. ✅\n")

# =============================================================================
#  Main Execution
# =============================================================================

if __name__ == "__main__":
    run_tests()
    
    input_file = Path(__file__).parent / "inputs" / "day_04.txt"
    
    if not input_file.exists():
        print(f"⚠️  Input file not found at: {input_file}")
    else:
        raw_data = input_file.read_text()
        data = parse_input(raw_data)
        
        print(f"--- Day 4 Solution ---")
        print(f"Part 1: {part_1(data)}")
        print(f"Part 2: {part_2(data)}")