"""ตั๋วหนังสุดป่วน"""

all_tiket = int(input())
count_lap = 0
moeny = []
count_tiket = []

while all_tiket > 0:
    age, tiket = map(int,input().split())
    count = 0
    count_lap += 1
    if age > 60:
        all_tiket -= tiket
        count += int((tiket * 150) - ((tiket * 150) * 0.5))
        moeny.append(count),count_tiket.append(all_tiket)
    elif 15 < age <= 22:
        all_tiket -= tiket
        count += int((tiket * 150) - ((tiket * 150) * 0.2))
        moeny.append(count),count_tiket.append(all_tiket)
    elif 22 < age:
        all_tiket -= tiket
        count += (tiket * 150)
        moeny.append(count),count_tiket.append(all_tiket)
    else:
        moeny.append(-1)

for i in range(count_lap):
    
    print(f"{moeny[i]} {count_tiket[i]}")