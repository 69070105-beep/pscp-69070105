"""BigFrame"""

lines = [input() for _ in range(5)]
lines = [line.rstrip() for line in lines]

max_len = max(len(line) for line in lines)
width = max_len + 4

print("*" * width)
for line in lines:
    print("* " + line.ljust(max_len) + " *")
print("*" * width)
