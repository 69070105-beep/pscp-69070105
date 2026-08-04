"""Calculator"""

num = int(input())
many = 0
plussign = num-1

if num in (0,1):
    print(num)
else:
    for i in range(1,num+1):
        many = many + len(str(i))
    print(many+plussign+1)
