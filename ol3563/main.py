"""ผลคูณเลขโดดที่ไม่เป็นศูนย์"""

x = input().replace('0','')

chack = False
count = 1

for i in x:
    count = count * int(i)
    chack = True

if not chack:
    print("0")
else:
    print(count)
