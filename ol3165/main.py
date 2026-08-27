"""เดินเล่นในงานเทศกาล"""

code = input()
count_x = 0
count_y = 0

for i in code:
    if i == "N":
        count_y += 1
    elif i == "S":
        count_y -= 1
    elif i == "E":
        count_x += 1
    else:
        count_x -= 1
x = abs(count_x)
y = abs(count_y)

print(f"{count_x} {count_y} {x + y}")
