def parse_input(string):
  return string.strip().splitlines()

with open("aoc2025_day3_input.txt", "r") as f:
    ratings = parse_input(f.read())

joltage = 0
for rating in ratings:
    L, R = rating[0], rating[1]
    global_max = L + R
    i = 1
    while i < len(rating) - 1:
        if L < R:
            L, R = R, rating[i + 1]
        i += 1
        R = rating[i]
        current_max = L + R
        global_max = max(current_max, global_max)
        if global_max == "99":
            break
    joltage += int(global_max)
    
print(joltage)