"""ติดตั้งหลอดไฟ"""

n = int(input())
h = []
for _ in range(n):
    h.append(int(input()))

h.sort()

total = 0
prefix = 0
for x in h:
    prefix += x
    total += prefix * 2

print(total)
