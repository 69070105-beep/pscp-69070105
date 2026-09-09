"""สลากกินแบ่ง"""

n, num1 =  map(str, input().split())
m, num2 =  map(str, input().split())

if n == m and num1 == num2:
    print("1000000")
if not n == m and num1 == num2:
    print("100000")
if n == m and num1[2:5] == num2[2:5]:
    print("2000")
if  n == m and num1[3:5] == num2[3:5]:
    print("1000")
if not n == m and num1[2:5] == num2[2:5]:
    print("200")
if not n == m and num1[3:5] == num2[3:5]:
    print("100")
elif n == m:
    print("20")
else:
    print("0")

