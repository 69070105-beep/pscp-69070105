"""ราศี"""
day = int(input())
mo = int(input())

if (mo == 1 and day >= 20) or (mo == 2 and day <= 18):
    print("aquarius")
elif (mo == 2 and day >= 19) or (mo == 3 and day <= 20):
    print("pisces")
elif (mo == 3 and day >= 21) or (mo == 4 and day <= 19):
    print("aries")
elif (mo == 4 and day >= 20) or (mo == 5 and day <= 20):
    print("taurus")
elif (mo == 5 and day >= 21) or (mo == 6 and day <= 20):
    print("gemini")
elif (mo == 6 and day >= 21) or (mo == 7 and day <= 22):
    print("cancer")
elif (mo == 7 and day >= 23) or (mo == 8 and day <= 22):
    print("leo")
elif (mo == 8 and day >= 23) or (mo == 9 and day <= 22):
    print("virgo")
elif (mo == 9 and day >= 23) or (mo == 10 and day <= 22):
    print("libra")
elif (mo == 10 and day >= 23) or (mo == 11 and day <= 21):
    print("scorpio")
elif (mo == 11 and day >= 22) or (mo == 12 and day <= 21):
    print("sagittarius")
elif (mo == 12 and day >= 22) or (mo == 1 and day <= 19):
    print("capricorn")
