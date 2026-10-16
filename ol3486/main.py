"""ตำบลกระสุนตก"""

n = int(input())
shots = []
for _ in range(n):
    x, y, d = map(int, input().split())
    shots.append((x, y, d))

for tx in range(1001):
    for ty in range(1001):
        ok = True
        for x, y, d in shots:
            if (tx - x) ** 2 + (ty - y) ** 2 != d * d:
                ok = False
                break
        if ok:
            print(tx, ty)
