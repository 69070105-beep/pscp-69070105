"""คำนวณราคาสินค้าโปรโมชั่น"""
x, y, z = input().split()

x = int(x)
y = int(y)
z = int(z)

sale = x + y + z

x *= 25
y *= 40
z *= 55

total = x + y + z

if sale >= 3:
    total = int(total * 0.9)
    print(total)
else:
    print(total)
