"""นับชนิดตัวอักษร"""

text = input()

upper = 0
lower = 0
digit = 0

for i in text:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    elif i.isdigit():
        digit += 1

print(upper, lower, digit)
