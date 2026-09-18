"""ตั๋วหนังสุดป่วน"""

all_tiket = int(input())
count_lap = 0
moeny = []
count_tiket = []
noom = 0

while all_tiket > 0:
    try:
        age, tiket = map(int, input().split())
    except EOFError:
        break
    count = 0
    count_lap += 1
    if age >= 15:
        if tiket > all_tiket:
            moeny.append(-2)
        elif age >= 60 and tiket >= 0:
            all_tiket -= tiket
            count += int((tiket * 150) - ((tiket * 150) * 0.5))
            moeny.append(count)
            count_tiket.append(all_tiket)
        elif 15 <= age <= 22 and tiket >= 0:
            all_tiket -= tiket
            count += int((tiket * 150) - ((tiket * 150) * 0.2))
            moeny.append(count)
            count_tiket.append(all_tiket)
        elif 22 < age and tiket >= 0:
            all_tiket -= tiket
            count += (tiket * 150)
            moeny.append(count)
            count_tiket.append(all_tiket)
    else:
        moeny.append(-1)

for i in moeny:
    if i < 0:
        print(f"{i}")
    else:
        print(f"{i} {count_tiket[noom]}")
        noom += 1
