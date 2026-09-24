"""Array 2D ตรวจสอบ"""

count_Row = 0
count_colrem = 0


for i in range(5):
    x = map(int,input().split())
    for j in x:
        if j > 0:
            count_colrem += 1
    count_Row += 1
print(f"{count_Row} {count_colrem}")
