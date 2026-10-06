"""1132-Median"""

num = input().replace(' ','')
fl = num.split(",")
count = 0
for i in num:
    count += 1
len_num = count
num = sorted(num)

print(num)