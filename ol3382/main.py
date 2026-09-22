"""Day08-0_02-Backward"""

lis = []

while True:
    x = input()
    if x == "NULL":
        break
    lis.append(x)

lis = lis[::-1]

for i in lis:
    print(i)
