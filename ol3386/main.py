"""Duplicate I"""

x1 = int(input())
x2 = int(input())

all_x1 = []
all_x2 = []
totalA = []
totalB = []

for _ in range(x1):
    inp_x1 = int(input())
    all_x1.append(inp_x1)

totalA = set(all_x1)

for _ in range(x2):
    inp_x2 = int(input())
    all_x2.append(inp_x2)

totalB = set(all_x2)

total = totalA & totalB
totol = reversed(sorted(total))
chack = False

for i in totol:
    print(i)
    chack = True

if not chack:
    print("Nope")
