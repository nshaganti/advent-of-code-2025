import sys
from pathlib import Path
from collections import defaultdict

# =============================================================================
#  Advent of Code 2025 - Day 3
#  Problem Link: https://adventofcode.com/2025/day/3
# =============================================================================

def parse_input(raw_data: str) -> list[str]:
    """Parses the input into a list of rating strings."""
    return raw_data.strip().splitlines()

def part_1(ratings: list[str]) -> int:
    """
    Calculates the sum of the 'maximum 2-digit number' found in each line.
    
    Logic:
        Iterate through the string maintaining a 'Left' digit (L).
        Compare L with the next digit (R).
        - If R > L: L is not a good starting digit. Discard L, make R the new L.
        - If R <= L: (L, R) is a valid pair. Calculate value, check max, move R forward.
        - Initialize current_max with the very first pair to handle edge cases where
          the first pair is the global maximum.

    Complexity:
        Time:  O(N) - We iterate through each character of each string exactly once.
        Space: O(1) - Constant auxiliary space used for pointers and max tracking.
    """
    total_joltage = 0
    
    for rating in ratings:
        if len(rating) < 2:
            continue

        L = rating[0]
        R = rating[1]
        
        # Initialize with the first pair immediately
        current_max_str = L + R
        
        i = 1
        while i < len(rating) - 1:
            # Greedy check: If the right digit is strictly larger than the left,
            # the current 'Left' is suboptimal. Discard it and advance.
            if L < R:
                L = R
            
            # Advance to the next character for R
            i += 1
            R = rating[i]
            
            # Evaluate the new pair
            pair_val = L + R
            if pair_val > current_max_str:
                current_max_str = pair_val
                
            # Optimization: 99 is the max possible 2-digit number
            if current_max_str == "99":
                break
                
        total_joltage += int(current_max_str)
        
    return total_joltage

def part_2(ratings: list[str]) -> int:
    """
    Finds the largest possible 12-digit subsequence from each line.
    
    Logic:
        Greedy approach (Lexicographically Largest Subsequence).
        We need to build a result of length 12.
        For each slot (1 to 12), we try to pick the largest digit (9 down to 1)
        that appears AFTER our previous position, provided there are enough 
        characters remaining in the string to fill the rest of the 12 slots.

    Complexity:
        Time:  O(N) - Building the position map takes O(N). The construction of the
                      12-digit number takes constant time relative to N (12 slots * 9 digits).
        Space: O(N) - We store a map of indices for every character in the string.
    """
    total_joltage = 0
    TARGET_LEN = 12
    
    for rating in ratings:
        # Map every character to a list of its indices
        pos_map = defaultdict(list)
        for idx, char in enumerate(rating):
            pos_map[char].append(idx)
            
        result = ""
        last_index = -1
        rating_len = len(rating)
        
        # Fill the 12 slots
        while len(result) < TARGET_LEN:
            remaining_needed = TARGET_LEN - len(result)
            
            # Try digits 9 down to 1
            for digit in "987654321":
                found_valid_digit = False
                
                # Check known positions of this digit
                for idx in pos_map[digit]:
                    # 1. Must be after the last character we picked
                    # 2. Must leave enough space for the remaining characters needed
                    if idx > last_index and (rating_len - idx) >= remaining_needed:
                        result += digit
                        last_index = idx
                        found_valid_digit = True
                        break
                
                if found_valid_digit:
                    break
                    
        total_joltage += int(result)
        
    return total_joltage

# =============================================================================
#  Unit Tests
# =============================================================================

def run_tests():
    """Runs tests on the sample input provided."""
    print("Running tests...", end=" ")
    
    sample_input = """
987654321111111
811111111111119
234234234234278
818181911112111
"""
    ratings = parse_input(sample_input)
    
    # Test Part 1
    p1_res = part_1(ratings)
    assert p1_res == 357, f"Part 1 Failed: Expected 357, got {p1_res}"
    
    # Test Part 2
    p2_res = part_2(ratings)
    assert p2_res == 3121910778619, f"Part 2 Failed: Expected 3121910778619, got {p2_res}"
    
    print("ALL TESTS PASSED. ✅\n")

# =============================================================================
#  Main Execution
# =============================================================================

if __name__ == "__main__":
    run_tests()
    
    input_file = Path(__file__).parent / "inputs" / "day_03.txt"
    
    if not input_file.exists():
        print(f"⚠️  Input file not found at: {input_file}")
    else:
        raw_data = input_file.read_text()
        ratings = parse_input(raw_data)
        
        print(f"--- Day 3 Solution ---")
        print(f"Part 1: {part_1(ratings)}")
        print(f"Part 2: {part_2(ratings)}")