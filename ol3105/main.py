"""คำนวณค่าแท็กซี่เบื้องต้น"""

km = int(input())
if km <= 0:
    print("0")
elif km <= 9:
    print((km * 5) + 30)
else:
    print(((9 * 5) + ((km - 10) * 8)) + 35)
