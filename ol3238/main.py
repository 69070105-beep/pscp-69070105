""""Elon Musk (X-shape)"""

s, l = input().split()
s = int(s)
scal = s // 2

if l == '#':
    for x in range(s):
        row = []
        for y in range(s):
            if y in (x, s - 1 - x):
                row.append('#')
            else:
                row.append('-')
        print(''.join(row))
else:
    base = ord('A') if l.isupper() else ord('a')
    start = ord(l)
    for x in range(s):
        dist = abs(x - scal)
        letter = chr(base + (start - base + dist) % 26)
        row = []
        for y in range(s):
            if y in (x, s - 1 - x):
                row.append(letter)
            else:
                row.append('-')
        print(''.join(row))
