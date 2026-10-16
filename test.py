
num = int(input())
num2 = input().split()

numll = num // 2
fnum = list(num2[:numll])
Lnum = list(num2[numll::1])
dlist = []
chack = False
result = []

for i in fnum:
    if i in Lnum:
        dlist.append(i)
        chack = True

if chack:
    totai = set(dlist).symmetric_difference(num2)
    totai = sorted(totai)
    print(*totai)
else:
    for x in num2:
        if num2.count(x) == 1:
            result.append(x)
    result = sorted(result)
    print(*result)
