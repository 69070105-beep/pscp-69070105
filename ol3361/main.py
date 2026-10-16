"""ขายรถยนต์"""

n = int(input())

v_list = []
for _ in range(n):
    _, v = map(int, input().split())
    v_list.append(v)

unsold = 0
max_v = 0

for v in reversed(v_list):
    if v < max_v:
        unsold += 1
    else:
        max_v = v

print(unsold)
