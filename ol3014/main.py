"""milk"""

price = int(input())
phomotion_cap = int(input())
get = int(input())
money = int(input())
a = (money // price)
b = a % phomotion_cap
c = (a - 1) // phomotion_cap
if not phomotion_cap:
    print(a)
elif b <= 1:
    print(a + c)
else:
    print(a + (get))
