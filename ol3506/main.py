"""WordSequence I"""

x = input().strip()
count = 1

for _ in x:
    print(x[:count])
    count += 1
