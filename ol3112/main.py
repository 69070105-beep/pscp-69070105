"""ชานมไข่มุก"""

a, b = input().split()
tea, sweet, n = input().split()

kai = 0.0
tee = 0.0

b = float(b)
sweet = int(sweet)
n = float(n)

if a == "H":
    kai += b * 5
elif a == "O":
    kai += b * 3
elif a == "J":
    kai += b * 2

if tea == "R" and sweet == 1:
    tee += 12 * n
elif tea == "R" and sweet == 2:
    tee += 18 * n
elif tea == "R" and sweet == 3:
    tee += 25 * n
elif tea == "T" and sweet == 1:
    tee += 15 * n
elif tea == "T" and sweet == 2:
    tee += 20 * n
elif tea == "T" and sweet == 3:
    tee += 30 * n
elif tea == "M" and sweet == 1:
    tee += 10 * n
elif tea == "M" and sweet == 2:
    tee += 15 * n
elif tea == "M" and sweet == 3:
    tee += 20 * n

print(f"{kai + tee:g}")
