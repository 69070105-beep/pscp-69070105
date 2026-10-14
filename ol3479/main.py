""" Name of Card """

card = input().upper().replace(" ", "")

rank_part = card[:-1]
suit_part = card[-1]

n = ""
m = ""

if rank_part == "A":
    n = "Ace"
elif rank_part == "J":
    n = "Jack"
elif rank_part == "Q":
    n = "Queen"
elif rank_part == "K":
    n = "King"
else:
    n = rank_part

if suit_part == "D":
    m = "Diamonds"
elif suit_part == "H":
    m = "Hearts"
elif suit_part == "S":
    m = "Spades"
else:
    m = "Clubs"

print(f"{n} of {m}")
