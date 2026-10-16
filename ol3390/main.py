"""Array 2D ตรวจสอบ"""

def main():
    """ckjsdic"""
    grid = []
    for _ in range(5):
        row = list(map(int, input().split()))
        grid.append(row)

    err_row = -1
    err_col = -1

    for r in range(5):
        if sum(grid[r]) % 2:
            err_row = r
            break

    for c in range(5):
        col_sum = 0
        for r in range(5):
            col_sum += grid[r][c]
        if col_sum % 2:
            err_col = c
            break

    print(f"{err_row} {err_col}")


if __name__ == "__main__":
    main()
