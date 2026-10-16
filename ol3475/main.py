"""Muddled Menu"""

menu = []

while True:
    line = input().strip()

    if line == "DONE":
        break
    if line == "CLOSED":
        menu = []
        break
    if line == "SOMETHING'S WRONG":
        menu = []
    elif line.startswith("Can't do: "):
        name = line[10:]
        if name in menu:
            menu.remove(name)
    else:
        name, num = line.rsplit(" #", 1)
        if num == "N":
            menu.append(name)
        else:
            menu.insert(int(num) - 1, name)

print("Full Course:", menu, "Reversed:", menu[::-1])
