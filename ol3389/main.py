"""Smart Trash Collector"""

n = int(input())
v = []
for i in range(n):
    x1, y1, z1 = map(float, input().split())
    total = x1 + y1 + z1
    v.append(total)
print(v)