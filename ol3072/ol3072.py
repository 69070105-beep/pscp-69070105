"""A-E-I-O-U"""

word = input().lower()

counta = 0
counte = 0
counti = 0
counto = 0
countu = 0

for i in (word):
    if i == "a":
        counta += 1
    elif i == "e":
        counte += 1
    elif i == "i":
        counti += 1
    elif i == "o":
        counto += 1
    elif i == "u":
        countu += 1

if counta > 0:
    print(f"a : {counta}")
if counte > 0:
    print(f"e : {counte}")
if counti > 0:
    print(f"i : {counti}")
if counto > 0:
    print(f"o : {counto}")
if countu > 0:
    print(f"u : {countu}")
