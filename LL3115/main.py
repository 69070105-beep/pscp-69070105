"""Arcade of Time: Store Check"""

num, _ = map(int, input().split())

time = [0] * 1441
total = 0

for _ in range(num):
    start, stop = map(int, input().split())
    time[start] += 1
    time[stop] -= 1

for i in range(1, 1441):
    time[i] += time[i - 1]

total = map(int, input().split())

print(*[time[t] for t in total])
