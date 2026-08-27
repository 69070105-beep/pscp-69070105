"""เกมสะสมแต้ม"""

num = int(input())
count = 0

for _ in range(1, num + 1):
    s = input()
    if s == "+":
        count += 10
    else:
        count -= 5
print(count)
