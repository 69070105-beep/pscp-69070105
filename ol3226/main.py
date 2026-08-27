"""nnnnnn"""
import decimal
from decimal import Decimal, ROUND_DOWN

decimal.getcontext().prec = 10000

n = Decimal(input().strip())
k = int(input().strip())    

rate = Decimal("0.0381")

for _ in range(k):
    increase = n * rate
    increase = increase.quantize(Decimal("0.01"), rounding=ROUND_DOWN)
    n += increase

ans = n.quantize(Decimal("0.01"), rounding=ROUND_DOWN)
print(ans)
