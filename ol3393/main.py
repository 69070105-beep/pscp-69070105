"""นักสำรวจถ้ำ (Cave Explorer)"""

n = int(input())
cave = list(map(int, input().split()))
moves = input().strip()

here = cave.index(1)

for move in moves:
    there = here + 1 if move == "R" else here - 1

    if not 0 <= there < n:
        continue

    if cave[there] == 2:
        cave[here] = 0
        cave[there] = 1
        break

    cave[here], cave[there] = cave[there], cave[here]
    here = there

print(*cave)
