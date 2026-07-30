"""Temperature"""

numtem = float(input())
form_what = input().upper()
need_be = input().upper()

C = 0.0
fanal = 0.0

if form_what == "C":
    C = numtem
elif form_what == "K":
    C = numtem - 273.15
elif form_what == "F":
    C = (numtem - 32) * 5 / 9
elif form_what == "R":
    C = (numtem * 5 / 9) - 273.15

if need_be == "C":
    fanal = C
elif need_be == "K":
    fanal = C + 273.15
elif need_be == "F":
    fanal = (C * 9 / 5) + 32
elif need_be == "R":
    fanal = (C + 273.15) * 9 / 5

print(f"{fanal:.2f}")
