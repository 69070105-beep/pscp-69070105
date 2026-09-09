"""กบน้อยกระโดด"""

x, y = map(int, input().split())
count = 0
a = 0

while x > 0 and a < y:
    a += x
    x -= 2
    count += 1

if a >= y:
    print(count)
else:
    print(-1)
