"""โรงแรมกลางกรุง ไม่มีชั้น 13"""

x = input()
a,b,c,d,e = map(int, x)
n = 0
room = 0
room1 = 0

if a > 5 :
    n = 9
elif b > 5 :
    n = 10
elif c > 5 :
    n = 11
elif d > 5 :
    n = 12
elif e > 5 :
    n = 14
else :
    n = 13

if x == x[::-1]:
    if a + e > 5 :
        room = 1
    elif b * d > 5 :
        room = 2
    else:
        room = 0
else:
    if e and a // e > 5 :
        room = 1
    elif b - e > 5 :
        room = 2
    else:
        room = 0

if a + b + c + d + e > 25:
    room1 = 1
elif a * b * c * d * e > 55 :
    room1 = 2
else:
    room1 = 0

print(str(n) + str(room) + str(room1))
