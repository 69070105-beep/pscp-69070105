"""ใส่กล่อง"""

w, l, m, n = map(int, input().split())

some = []
for i in range(m, n + 1):
    total = (w % i) * (l % i)
    some.append(total)

print(min(some))
