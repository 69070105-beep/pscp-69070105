
"""SumOfNumber"""

target = int(input())
count = 0

while True:
    n = int(input())

    if n == -1:
        break

    count += n

    if count == target:
        break

print(count)
