"""Bill"""

fb = int(input())

tip = float(fb / 10)

if tip < 50:
    tip = 50
elif tip > 1000:
    tip = 1000
totaltip = fb + tip
vat = (totaltip / 100) * 7
total = totaltip + vat
print(f"{total:.2f}")
