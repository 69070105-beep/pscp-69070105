"""พิมพ์สัญลักษณ์"""

a = int(input())

for i in range(1,a + 1):
    if not i % 5:
        print("X",end="")
    else:
        print("*",end="")
