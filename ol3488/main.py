"""ไฟส่อง"""

n = int(input())

lit = [False] * 360

for _ in range(n):
    a, b = map(int, input().split())
    i = a
    while i != b:
        lit[i] = True
        i = (i + 1) % 360

if all(lit):
    print(360)
else:
    start = lit.index(False)
    best = 0
    run = 0
    for k in range(1, 361):
        if lit[(start + k) % 360]:
            run += 1
            if run > best:
                best = run
        else:
            run = 0
    print(best)
