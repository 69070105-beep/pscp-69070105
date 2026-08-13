"""BrickBridge"""
sb = int(input())
bb = int(input()) * 5
nb = int(input())

if nb - bb >= 0:
    x = nb - bb
    if x <= sb:
        print(x)
    else:
        print("-1")
elif nb - bb < 0:
    bb = (nb // 5) * 5
    x = nb - bb
    if x <= sb:
        print(x)
    else:
        print("-1")
else:
    print("-1")
