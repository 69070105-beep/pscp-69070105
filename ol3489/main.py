"""Divide3Or5"""

num = int(input())
count = 0

for i in range(num + 1):
    if not i % 5 or not i % 3:
        count += i
print(count)
