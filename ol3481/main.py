"""ลอดสะพาน"""

l, n = map(int, input().split())

bridges = []
for _ in range(n):
    a, b = map(int, input().split())
    bridges.append((a, b))

best = 0
for k in range(l):
    x = k + 0.5
    count = 0
    for a, b in bridges:
        if a < x < b:
            count += 1
    if count > best:
        best = count

print(best)
