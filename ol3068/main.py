"""ปีอธิกสุรทิน"""

year = int(input())

if year < 1582:
    if not year % 4:
        print("yes")
    else:
        print("no")
else:
    a = year % 4
    b = year % 400
    c = year % 100
    if not b or not a and c:
        print("yes")
    else:
        print("no")
