"""PickThem"""

s = input()
s = s.replace('[', '').replace(']', '')
s = s.split(',')

found = False
for i in s:
    w = int(i)
    if not w % 2:
        print(w)
        found = True

if not found:
    print("Nope")
