"""four direction"""

arrows = {
    "U": ["  *  ", " *** ", "* * *", "  *  ", "  *  "],
    "D": ["  *  ", "  *  ", "* * *", " *** ", "  *  "],
    "L": ["  *  ", " *   ", "*****", " *   ", "  *  "],
    "R": ["  *  ", "   * ", "*****", "   * ", "  *  "],
}

text = input().strip()

for row in range(5):
    line = ""
    for c in text:
        line += arrows[c][row] + " "
    print(line)
