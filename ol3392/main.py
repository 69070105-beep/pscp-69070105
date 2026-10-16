"""Array ฮาเฮ"""

def main():
    """mum"""
    numbers = []
    for i in range(1, 4):
        val = int(input())
        numbers.append(val)
        print(f"Input number {i} stored.")

    while True:
        choice = int(input())
        if not choice:
            break
        if choice == 1:
            orig = " ".join(map(str, numbers))
            print(f"Original order: {orig}")
        elif choice == 2:
            desc = " ".join(map(str, sorted(numbers, reverse=True)))
            print(f"Descending order: {desc}")
        elif choice == 3:
            asc = " ".join(map(str, sorted(numbers)))
            print(f"Ascending order: {asc}")


if __name__ == "__main__":
    main()
