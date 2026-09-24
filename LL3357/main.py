"""Giraffe"""

n = int(input())

z = []
count = 0

for _ in range(n):
    h = int(input())
    z.append(h)

for i in range(n):
    if not i:
        if n == 1 or z[i] > z[i + 1]:
            count += 1
    elif i == n - 1:
        if z[i] > z[i - 1]:
            count += 1
    else:
        if z[i] > z[i - 1] and z[i] > z[i + 1]:
            count += 1

print(count)
