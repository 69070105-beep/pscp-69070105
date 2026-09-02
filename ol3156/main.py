"""Conan"""

text = input().lower()
num = int(input())
count = ""
q = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n', 
    'o', 'p', 'q', 'r', 's', 't', 'u', 
    'v', 'w', 'x', 'y', 'z'
    ]

for i in text:
    if i in q:
        count = q.index(i)
        count += num
        if count >= 26:
            count = count % 26
            print(q[count], end="")
        else:
            print(q[count], end="")
