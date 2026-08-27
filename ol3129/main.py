"""วิเคราะห์ยอดขายร้านกาแฟ"""

num = int(input())
total = 0
max_list = []
min_list = []

for _ in range(1, num + 1):
    money = int(input())
    max_list.append(money)
    max_total = max(max_list)
    min_list.append(money)
    min_total = min(min_list)
    total += money

avg = float(total / num)
avg = round(avg, 1)
print(total)
print(max_total)
print(min_total)
print(avg)
