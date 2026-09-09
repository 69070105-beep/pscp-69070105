"""ไฟคริสตมาส"""

start, step = map(str, input().split())

step = int(step)
ling_list = ['Red', 'Green', "Blue"]
count = 0
count1 = 1
count2 = 2

if start == "R":
    for _ in range(step):
        print(ling_list[count], end=" ")
        count = (count + 1) % 3
elif start == "G":
    for _ in range(step):
        print(ling_list[count1], end=" ")
        count1 = (count1 + 1) % 3
else:
    for _ in range(step):
        print(ling_list[count2], end=" ")
        count2 = (count2 + 1) % 3
