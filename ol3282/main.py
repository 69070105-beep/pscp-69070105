"""Stats"""
n = int(input())

total = 0
min_val = None
max_val = None

for _ in range(n):
    x = int(input())
    total += x

    if min_val is None or x < min_val:
        min_val = x

    if max_val is None or x > max_val:
        max_val = x

average = total / n

print(f"MIN: {min_val:.3f}")
print(f"MAX: {max_val:.3f}")
print(f"AVG: {average:.3f}")
