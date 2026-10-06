n = input()
m = input()
ms = len(m)
count = 0
for i in n:
    if i !=  m:
       count += 1
sss = ms - count
print(sss)