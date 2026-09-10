"""สลากกินแบ่ง"""

n, num1 = input().split()
m, num2 = input().split()

def main():
    """คำนวน"""
    high = 0
    if n == m and num1 == num2:
        high = max(high, 1000000)
    if not n == m and num1 == num2:
        high = max(high, 100000)
    if n == m and num1[-3:] == num2[-3:]:
        high = max(high, 2000)
    if n == m and num1[-2:] == num2[-2:]:
        high = max(high, 1000)
    if not n == m and num1[-3:] == num2[-3:]:
        high = max(high, 200)
    if not n == m and num1[-2:] == num2[-2:]:
        high = max(high, 100)
    if n == m:
        high = max(high, 20)

    print(high)

main()
