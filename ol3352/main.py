"""LastStand"""

s = input()
s = s.replace('[', '').replace(']', '')
s = s.split(',')

for i in s:
    w = int(i)
    print(w % 10)
