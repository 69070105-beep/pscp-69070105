"""สมดุลย์ชีวิต"""

n = int(input())
hours = [int(input()) for _ in range(n)]

long_count = sum(1 for h in hours if h > 18)
short_count = n - long_count

rest_days = max(0, long_count - 1 - short_count)
print(n + rest_days)
