"""สหกรณ์โรงเรียน"""
from decimal import Decimal, ROUND_HALF_UP

fan = input()
many = int(input())

count = Decimal('0')

for _ in range(many):
    s = Decimal(input())
    count += s

total_discount = Decimal('0')

if fan == "Y":
    total_discount = count * Decimal('0.05')
elif fan == "N" and count >= Decimal('500'):
    total_discount = count * Decimal('0.03')
else:
    total_discount = Decimal('0')

net_total = count - total_discount
final_result = net_total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

print(final_result)
