a = int(input())
d = int(input())

s = a - 4
for _ in range(1,s + 1):
    s -= 1
    for _ in range(1, d + 1):
        ssd = s * " "
        print(f"{ssd}{"*" * a}")
        break
for _ in range(1, s + 1):
    s += 1
    for _ in range(1, d + 1):
        ssd = s * " "
        print(f"{ssd}{"*" * a}")
        break
