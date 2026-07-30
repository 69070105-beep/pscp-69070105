"""Season"""

m = int(input())
d = int(input())

if m < 3 or (m == 3 and d < 21):
    print("winter")
elif m == 3 and d >= 21:
    print("spring")

elif m < 6 or (m == 6 and d < 21):
    print("spring")
elif m == 6 and d >= 21:
    print("summer")

elif m < 9 or (m == 9 and d < 21):
    print("summer")
elif m == 9 and d >= 21:
    print("fall")

elif m < 12 or (m == 12 and d < 21):
    print("fall")
elif m == 12 and d >= 21:
    print("winter")
