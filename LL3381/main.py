"""Point Sorting"""

t = int(input())
for _ in range(t):
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x + y, -y, x, y))

    points.sort()

    for item in points:
        print(f"{item[2]} {item[3]}")
