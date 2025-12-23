import sys
from collections import defaultdict
from pathlib import Path

# =============================================================================
#  Advent of Code 2025 - Day 7
#  Problem Link: https://adventofcode.com/2025/day/7
# =============================================================================

def parse_input(raw_data: str) -> list[str]:
    """Parses the grid into a list of immutable strings."""
    return [line for line in raw_data.strip().splitlines() if line]

def part_1(grid: list[str]) -> int:
    """
    Counts the total number of split events.
    
    Logic:
        Simulate flow row-by-row using a Set of active column indices.
        This avoids modifying the original grid (immutability) and prevents
        part 1 logic from corrupting state for part 2.

    Complexity:
        Time:  O(H * W) where H is height and W is width. In the worst case (full flood),
               we check every cell once.
        Space: O(W) auxiliary space to store the 'active_cols' set for the current row.
    """
    height = len(grid)
    width = len(grid[0])
    
    # active_cols is a set of x-coordinates containing flow
    active_cols = set()
    for x, char in enumerate(grid[0]):
        if char == 'S':
            active_cols.add(x)
            
    total_splits = 0
    
    # Process row by row
    for y in range(height - 1):
        next_active_cols = set()
        
        for x in active_cols:
            below_char = grid[y+1][x]
            
            if below_char == '.':
                next_active_cols.add(x)
                
            elif below_char == '^':
                total_splits += 1
                if x > 0:
                    next_active_cols.add(x - 1)
                if x < width - 1:
                    next_active_cols.add(x + 1)
                    
            elif below_char == 'S': 
                next_active_cols.add(x)

        active_cols = next_active_cols
        
    return total_splits

def part_2(grid: list[str]) -> int:
    """
    Counts the total number of distinct paths reaching the bottom.
    
    Logic:
        Row-by-row Dynamic Programming (similar to Pascal's Triangle).
        We track {column_index: count_of_paths_reaching_here}.
        When a pipe splits, the parent count is added to both children.
        When pipes merge, their counts naturally sum up in the dictionary.

    Complexity:
        Time:  O(H * W) - We process every active cell exactly once per row.
        Space: O(W) - We only store path counts for the current row (sparse dictionary).
    """
    height = len(grid)
    width = len(grid[0])
    
    # Map: column_index -> path_count
    row_counts = defaultdict(int)
    
    # Initialize start row
    for x, char in enumerate(grid[0]):
        if char == 'S':
            row_counts[x] = 1
            
    # Process downwards
    for y in range(height - 1):
        next_row_counts = defaultdict(int)
        
        for x, count in row_counts.items():
            below_char = grid[y+1][x]
            
            if below_char == '.':
                next_row_counts[x] += count
                
            elif below_char == '^':
                if x > 0:
                    next_row_counts[x - 1] += count
                if x < width - 1:
                    next_row_counts[x + 1] += count
            
            elif below_char == 'S':
                next_row_counts[x] += count

        row_counts = next_row_counts

    return sum(row_counts.values())

# =============================================================================
#  Unit Tests
# =============================================================================

def run_tests():
    print("Running tests...", end=" ")
    
    sample_input = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""
    grid = parse_input(sample_input)
    
    # Test Part 1
    p1 = part_1(grid)
    assert p1 == 21, f"Part 1 Failed: Expected 21, got {p1}"
    
    # Test Part 2
    p2 = part_2(grid)
    assert p2 == 40, f"Part 2 Failed: Expected 40, got {p2}"
    
    print("ALL TESTS PASSED. ✅\n")

if __name__ == "__main__":
    run_tests()
    
    input_file = Path(__file__).parent / "inputs" / "day_07.txt"
    if input_file.exists():
        raw_data = input_file.read_text()
        grid = parse_input(raw_data)
        print(f"--- Day 7 Solution ---")
        print(f"Part 1: {part_1(grid)}")
        print(f"Part 2: {part_2(grid)}")