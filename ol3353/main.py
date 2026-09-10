"""PickThemAgain"""

list_num = map(int, input().split())
m = []

for i in list_num:
    m.append(i)

s = m[::-1]

found = False

for j in s:
    if not j % 3 or not j % 5:
        print(j)
        found = True

if not found:
    print("Nope")
