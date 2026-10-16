"""เข้าแถว"""

n, _ = map(int, input().split())
heights = list(map(int, input().split()))
customers = list(map(int, input().split()))

prefix_max = [0] * n
curr_max = 0

for i in range(n):
    prefix_max[i] = curr_max
    if heights[i] > curr_max:
        curr_max = heights[i]

for a in customers:
    idx = a - 1
    front_max = prefix_max[idx]

    if heights[idx] > front_max:
        print(0)
    else:
        print(front_max - heights[idx] + 1)
