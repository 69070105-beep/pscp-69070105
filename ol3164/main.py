"""ผลรวมของค่าที่มากกว่า"""
n = int(input())

max_values = []

for _ in range(n):
    num1 = int(input())
    num2 = int(input())
    bigger = max(num1, num2)
    max_values.append(bigger)

total = sum(max_values)

if n == 1:
    print(max_values[0])
else:
    ALL = " + ".join(map(str, max_values))
    print(f"{ALL} = {total}")
