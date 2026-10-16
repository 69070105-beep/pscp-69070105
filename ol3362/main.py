"""บุพเพสันนิวาส"""

def main():
    """something"""
    name1 = input()
    name2 = input()

    max_len = max(len(name1), len(name2))

    len1 = len(name1)
    while len(name1) < max_len:
        name1 += name1[len(name1) % len1]

    len2 = len(name2)
    while len(name2) < max_len:
        name2 += name2[len(name2) % len2]

    love_chars = "loveLOVE"
    yant = ""

    for c1, c2 in zip(name1, name2):
        if c1 in love_chars or c2 in love_chars:
            yant += "w"
        else:
            yant += "$"

    w_count = yant.count("w")

    if w_count % 2:
        max_w = max(len(g) for g in yant.split("$"))
        yant += str(max_w)
    elif "ww" not in yant:
        yant += "#"

    print(yant)


if __name__ == "__main__":
    main()
