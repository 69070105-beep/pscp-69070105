"""ระบบคิดคะแนนเกมออนไลน์"""

basepoit = int(input())
bonus = int(input())
day = int(input())

all_poit = basepoit + bonus
count = 0

if day > 3:
    all_poit = int(all_poit * 1.5)

if all_poit >= 1500:
    count = 5
elif all_poit >= 1000:
    count = 4
elif all_poit >= 500:
    count = 3
elif all_poit >= 200:
    count = 2
else:
    count = 1

print(all_poit)
print(count)
if count == 5 and day >= 7:
    print(99)
elif count == 4 and bonus > 300:
    print(88)
else:
    print(0)
