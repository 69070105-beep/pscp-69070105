"""PickNum"""

x = map(int, input().split())
count_neg = 0
count_pos = 0
count_zero = 0

for i in x:
    if i > 0:
        count_pos += 1
    elif i < 0:
        count_neg += 1
    else:
        count_zero += 1

print(f"Positive: {count_pos}")
print(f"Negative: {count_neg}")
print(f"Zero: {count_zero}")
