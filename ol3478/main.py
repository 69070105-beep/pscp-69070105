"""Easy Histogram No Dict"""

text = input().replace(" ", "")

list_text = []

for i in text:
    list_text.append(i)

list_text = set(list_text)

for k in "abcdefghijklmnopqrstuvwxyz":
    small = k
    big = k.upper()

    if small in list_text:
        count = text.count(small)
        print(f"{small} = {count}")

    if big in list_text:
        count = text.count(big)
        print(f"{big} = {count}")
