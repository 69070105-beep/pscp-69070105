"""หุ่นยนต์เคาะเสียงกระเบื้อง"""

n_str, p_str = input().split()
n = int(n_str)
p = float(p_str)

grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

col_defective = [0] * n
col_points = [0] * n

total_defective = 0
total_points = 0

for i in range(n):
    row_defective = sum(1 for x in grid[i] if x > 0)
    row_points = sum(grid[i])

    total_defective += row_defective
    total_points += row_points

    for j in range(n):
        if grid[i][j] > 0:
            col_defective[j] += 1
        col_points[j] += grid[i][j]

    print(*grid[i], row_defective, row_points)

print(*col_defective)
print(*col_points)

total_fine = total_points * p

print(f"{total_defective} {total_points} {total_fine:.2f}")
