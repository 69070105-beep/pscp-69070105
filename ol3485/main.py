""" รหัสต้องไม่ซ้ำกัน """

_ = int(input())
num2 = list(map(int, input().split()))

result = []

for i in num2:
    if num2.count(i) == 1:
        result.append(i)

result = sorted(result)

print(*result)
