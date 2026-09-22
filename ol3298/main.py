"""กระต่ายน้อยรัก BUU"""

s = input()
n = len(s)
upper = s.upper()

b_positions = [i for i, ch in enumerate(upper) if ch == 'B']

max_run = 0
for i in b_positions:
    j = i + 1
    count = 0
    while j < n and upper[j] == 'U':
        count += 1
        j += 1
    if count > max_run:
        max_run = count

if b_positions and max_run >= 2:
    print(f"Yes {max_run}")
elif b_positions:
    first_b = b_positions[0]
    prefix = s[:first_b + 1]
    remaining = n - (first_b + 1)
    print(prefix + 'U' * remaining)
else:
    pattern = ('BUU' * (n // 3 + 1))[:n]
    print(pattern)
