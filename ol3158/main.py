"""ผลรวมกำลัง 2"""

x = int(input())
count = 0
y = 0
for i in range(1, x + 1):
    count = i ** 2
    y += count
print(y)
