"""Basic ATM"""

money = int(input())

a = money % 1000
e = a % 500
i = e // 100
a1 = money // 1000
e1 = a // 500

if 100 <= money <= 20000 and not money % 100:
    if a1 > 0:
        print(f"1000 = {a1}")
    if e1 > 0:
        print(f"500 = {e1}")
    if i > 0:
        print(f"100 = {i}")
else:
    print("ERROR")
