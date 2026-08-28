"""กบน้อยกระโดด"""

x, y = map(int, input().split())

mile = y - x
num = mile // 2

if not mile % 2:
    print(num)
else:
    print("-1")
