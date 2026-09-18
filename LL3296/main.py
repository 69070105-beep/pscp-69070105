"""RGB Mixed"""

r1, g1, b1 = map(int, input().split())
r2, g2, b2 = map(int, input().split())

fal_R = (r1 + r2) // 2
fal_G = (g1 + g2) // 2
fal_B = (b1 + b2) // 2

print(f"{fal_R} {fal_G} {fal_B}")
