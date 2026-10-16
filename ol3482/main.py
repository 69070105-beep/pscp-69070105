"""นักล่าอสูร"""

MAX_TRIES = 2

names = ["Spider Demon", "Swamp Demon", "Arrow Demon", "Hand Demon",
         "Drum Demon", "Mugen Train", "Upper Moon"]
secret = [1, 2, 1, 2, 3, 2, 3]
dead = [False] * 7

kills = 0
total = 0
i = 0
no_input = False

while kills < 5 and not no_input:
    if not dead[i]:
        print(names[i])
        killed = False
        tries = 0
        while tries < MAX_TRIES and not killed:
            try:
                a = int(input())
            except EOFError:
                no_input = True
                break
            tries += 1
            total += 1
            if a == secret[i]:
                killed = True
        if not no_input:
            if killed:
                print("kill")
                dead[i] = True
                kills += 1
            else:
                print("back")
    i = (i + 1) % 7

print(total)
