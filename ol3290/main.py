"""Left Arrow"""
k = int(input())
n = int(input())

mid = n // 2
for i in range(n):
    indent = abs(i - mid)
    print(' ' * indent + '*' * k)
