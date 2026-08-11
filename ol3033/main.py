"""กระดาษห่อของขวัญ"""
r, h, glue = map(float, input().split())

PI = 3.14

width = (2 * r) + h
length = (2 * PI * r) + glue

print(f"{width:.2f} {length:.2f}")
