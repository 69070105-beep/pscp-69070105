"""OverlapCircle"""

import math

x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())

d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
lap = r1 + r2

if d <= lap:
    print("overlapping")
else:
    print("no overlapping")
