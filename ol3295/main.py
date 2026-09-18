"""Electric_Using"""

x = int(input())
count = 0
vat = 0

for i in range(1, x + 1):
    if 1 <= i <= 10:
        count += 5
    elif 10 < i <= 50:
        count += 7
    elif 50 < i <= 100:
        count += 10
    elif 100 < i <= 200:
        count += 12
    else:
        count += 15

ft = x * 0.50
vat = count * 0.07
total = (count + vat + ft) + 0.001

print(f"{total:.1f}")
