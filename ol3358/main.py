"""Pig"""

n = int(input())
w = list(map(int, input().split()))

max_values = []
equation = ""

for i in range(0, len(w), 2):
    pair_max = max(w[i], w[i + 1])
    max_values.append(pair_max)

total = sum(max_values)

if n == 1:
    print(total)
else:
    equation = " + ".join(map(str, max_values))
    print(f"{equation} = {total}")
