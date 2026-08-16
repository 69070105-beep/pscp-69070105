"""สามเหลี่ยม"""

x = int(input())

for i in range(x):
    for j in range(i + 1):
        if not j or i == x - 1 or j == i:
            print("0", end="")
        else:
            print("1", end="")
    print()
