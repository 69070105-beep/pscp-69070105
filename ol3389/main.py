"""Smart Trash Collector"""

n = int(input())

for _ in range(n):
    plastic, can, glass = map(float, input().split())
    total = plastic + can + glass

    messages = []

    if total > 50:
        messages.append("Overloaded")
    if plastic > 20:
        messages.append("Check Type Plastic")
    if can > 20:
        messages.append("Check Type Can")
    if glass > 20:
        messages.append("Check Type Glass")

    if messages:
        extra = ", ".join(messages)
        print(f"{total:.1f}, {extra}")
    else:
        print(f"{total:.1f}")
