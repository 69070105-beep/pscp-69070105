"""ส่งต่อ"""

n, s = map(int, input().split())

nxt = []
for _ in range(n):
    nxt.append(int(input()))

seen = []
curr = s

while curr and curr not in seen:
    seen.append(curr)
    curr = nxt[curr - 1]

print(len(seen))
