"""สงคราม...ส่งด่วน"""

b, f = input().split()
km = float(input())

if b == "BKK" and f == "CNX":
    a = (km * 30) + 10
    print(f"{a:.2f}")
elif b == "CNX" and f == "UBP":
    a = (km * 40) + 15
    print(f"{a:.2f}")
elif b == "UBP" and f == "BKK":
    a = (km * 40) + 20
    print(f"{a:.2f}")
elif b == "BKK" and f == "PKT":
    a = (km * 50) + 25
    print(f"{a:.2f}")
elif b == "PKT" and f == "CNX":
    a = (km * 60) + 30
    print(f"{a:.2f}")
elif b == "UBP" and f == "PKT":
    a = (km * 70) + 40
    print(f"{a:.2f}")
else:
    print("Error")
