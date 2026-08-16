"""fat rabbit"""
n = int(input())
count = 0
max_weight = 0
max_name = ""
for _ in range(n):
    Name, weight = input().split()
    weight = int(weight)
    if weight > 15:
        count += 1

    if weight > max_weight:
        max_weight = weight
        max_name = Name

print(count)
print(max_name)
