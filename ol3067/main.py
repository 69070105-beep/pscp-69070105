"""การเพิ่ม/ลด"""

a1 = float(input())
a2 = float(input())
a3 = float(input())

if a1 < a2 < a3:
    print("increasing")
elif a1 > a2 > a3:
    print("decreasing")
else:
    print("neither")
