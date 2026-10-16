"""Bus seat"""

c = int(input())
r = int(input())
k = int(input())

num_pairs = c // 2

for p in range(num_pairs - 1, -1, -1):
    for offset in (2 * p + 2, 2 * p + 1):
        line = []
        for row in range(1, r + 1):
            seat = (row - 1) * c + offset
            if seat == k:
                line.append("XX")
            else:
                line.append(f"{seat:02d}")
        print(" ".join(line))

    if p > 0:
        print()
