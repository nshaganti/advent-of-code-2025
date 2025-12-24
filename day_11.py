import sys
from functools import cache
from pathlib import Path

# =============================================================================
#  Advent of Code 2025 - Day 11
#  Problem Link: https://adventofcode.com/2025/day/11
# =============================================================================

def parse_input(raw_data: str):
    """
    Parses 'src: dst1 dst2' into a dictionary {src: [dst1, dst2]}
    """
    graph = {}
    for line in raw_data.strip().splitlines():
        if not line.strip(): continue
        
        # Split "node: neighbor neighbor"
        parts = line.split(":")
        src = parts[0].strip()
        
        # Handle cases with neighbors
        if len(parts) > 1 and parts[1].strip():
            neighbors = parts[1].strip().split(" ")
            graph[src] = neighbors
        else:
            graph[src] = []
            
    return graph

def part_1(graph):
    """
    Count total paths from 'you' to 'out'.
    """
    start_node = "you"
    end_node = "out"
    
    @cache
    def dfs(node):
        if node == end_node:
            return 1
        if node not in graph:
            return 0
        
        return sum(dfs(neighbor) for neighbor in graph[node])

    if start_node not in graph:
        return 0
        
    return dfs(start_node)

def part_2(graph):
    """
    Count paths from 'svr' to 'out' that must visit BOTH 'dac' and 'fft'.
    State: (current_node, frozenset(met_requirements))
    """
    start_node = "svr"
    end_node = "out"
    required = frozenset(["dac", "fft"])

    @cache
    def dfs(node, met_reqs):
        # 1. Update State: Did we just hit a required node?
        if node in required:
            # Create a new frozenset including this node (immutable update)
            met_reqs = met_reqs | {node}

        # 2. Base Case: Reached Target
        if node == end_node:
            # Only return 1 if we have met ALL requirements
            return 1 if met_reqs == required else 0

        # 3. Base Case: Dead End
        if node not in graph:
            return 0

        # 4. Recursive Step
        return sum(dfs(neighbor, met_reqs) for neighbor in graph[node])

    if start_node not in graph:
        return 0

    # Initial call: Empty set of met requirements
    return dfs(start_node, frozenset())

# =============================================================================
#  Unit Tests
# =============================================================================

def run_tests():
    print("Running tests...", end=" ")
    
    # Sample 1 (Part 1 Logic)
    input_1 = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""
    graph_1 = parse_input(input_1)
    # Part 1: you -> out
    # Path 1: you -> bbb -> eee -> out
    # Path 2: you -> bbb -> ddd -> ggg -> out
    # Path 3: you -> ccc -> ddd -> ggg -> out
    # Path 4: you -> ccc -> eee -> out
    # Path 5: you -> ccc -> fff -> out
    p1 = part_1(graph_1)
    assert p1 == 5, f"Part 1 Failed: Expected 5, got {p1}"

    # Sample 2 (Part 2 Logic)
    input_2 = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""
    graph_2 = parse_input(input_2)
    # Part 2: svr -> out (via dac AND fft)
    # Path 1: svr -> aaa -> fft -> ccc -> eee -> dac -> fff -> ggg -> out
    # Path 2: svr -> aaa -> fft -> ccc -> eee -> dac -> fff -> hhh -> out
    # Note: bbb path doesn't hit fft until AFTER dac is missed or visited out of order? 
    # Actually bbb->tty->ccc->eee->dac->fff hits 'fft' at the end? No 'fft' is disjoint there.
    p2 = part_2(graph_2)
    assert p2 == 2, f"Part 2 Failed: Expected 2, got {p2}"
    
    print("ALL TESTS PASSED. ✅\n")

# =============================================================================
#  Main Execution
# =============================================================================

if __name__ == "__main__":
    run_tests()
    
    input_file = Path(__file__).parent / "inputs" / "day_11.txt"
    
    if not input_file.exists():
        print(f"⚠️  Input file not found at: {input_file}")
    else:
        raw_data = input_file.read_text()
        graph = parse_input(raw_data)
        
        print(f"--- Day 11 Solution ---")
        print(f"Part 1: {part_1(graph)}")
        print(f"Part 2: {part_2(graph)}")