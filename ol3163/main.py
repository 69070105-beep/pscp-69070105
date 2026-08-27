"""สินค้าส่งออก"""

num = int(input())
sum_stog = 0
count_even = 0
count_odd = 0

for _ in range(1, num + 1):
    stog = int(input())
    sum_stog += stog
    if not stog % 2:
        count_even += 1
    else:
        count_odd += 1

print(f"SUM {sum_stog}")
print(f"EVEN {count_even}")
print(f"ODD {count_odd}")
