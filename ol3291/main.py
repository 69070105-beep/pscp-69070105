"""Right Arrow"""
k = int(input())
n = int(input())

for i in range(n):
    indent = min(i, n - 1 - i)
    print(' ' * indent + '*' * k)
