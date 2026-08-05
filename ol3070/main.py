"""นับเลขคู่และเลขคี่"""

def main():
    """นับเลขคู่และเลขคี่"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    evens = 0
    odds = 0

    if not num1 % 2:
        evens += 1
    else:
        odds += 1
    if not num2 % 2:
        evens += 1
    else:
        odds += 1
    if not num3 % 2:
        evens += 1
    else:
        odds += 1

    print(evens)
    print(odds)

main()
