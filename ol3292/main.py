"""Arrow"""

s = input()
n = int(input())

for idx, direction in enumerate(s):
    j = 0
    going_up = True
    rows = []
    space_count = 1


    while True:
        stars = n - j

        if direction == "R":
            space_count = 2 * j
        else:
            space_count = n - 1 - j

        line = (" " * space_count) + ("*" * stars)
        rows.append(line)

        if going_up:
            j += 1
            if j == n:
                going_up = False
                j = n - 2
        else:
            j -= 1
            if j < 0:
                break

    for line in rows:
        print(line)

    if idx != len(s) - 1:
        print()
