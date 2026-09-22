"""แปลงดอกไม้"""

l, n = map(int, input().split())

k = 0
cum = 0
while cum < n:
    k += 1
    m = k * l
    cum = m * (m + 1) // 2

print(k)
