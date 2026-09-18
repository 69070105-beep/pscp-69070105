"""ตั๋วหนังสุดป่วน"""

all_tiket = int(input())
count = 0

while all_tiket > 0:
    age, tiket = map(int,input().split())
    if age > 60:
        all_tiket -= tiket
        count += (tiket * 150) // 2
        print(f"{count} {all_tiket}")
    elif 15 < age <= 22:
        all_tiket -= tiket
        count += (tiket * 150) * 0.02
        print(f"{count} {all_tiket}")
    elif
    