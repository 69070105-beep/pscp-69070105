"""Teaching schedule"""

n = int(input())
a = int(input())

total = n * a
hour = 0
minute = 0

if not total:
    print("No teaching")
else:
    hour = total // 60
    minute = total % 60
    if not hour:
        print(minute, "minute")
    elif not minute:
        print(hour, "hours")
    else:
        print(hour, "hours", minute, "minute")
