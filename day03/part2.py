from collections import defaultdict

def parse_input(string):
  return string.strip().splitlines()

with open("aoc2025_day3_input.txt", "r") as f:
    ratings = parse_input(f.read())

joltage = 0
for rating in ratings:
    pos = defaultdict(list)
    for i, char in enumerate(rating):
        pos[char].append(i)

    res = ""
    length = len(rating)
    curr_len = len(res)
    prev_i = -1
    while curr_len < 12:
        for char in "987654321":
            for i in pos[char]:
                if i <= length - (12 - curr_len) and i > prev_i:
                    res += char
                    prev_i = i
                    pos[char].remove(i)
                    break
            if len(res) > curr_len:
                curr_len = len(res)
                break
    joltage += int(res)

print(joltage)