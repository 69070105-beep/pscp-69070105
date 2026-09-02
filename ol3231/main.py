"""เกมทายลูกเต๋า"""

player = int(input())
dealer = int(input())

if player <= 6 and 6 >= dealer:
    if player == dealer:
        print("Correct!")
    else:
        print("Wrong!")
else:
    print("Invalid")
