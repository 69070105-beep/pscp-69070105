"""รหัสแฝดเทค"""

def main():
    """คำวนวน"""
    n = int(input())
    code1 = input()
    code2 = input()

    mismatch_count = 0

    for i in range(n):
        digit1 = int(code1[i])
        digit2 = int(code2[i])

        if digit1 + digit2 != 9:
            mismatch_count += 1
 
    if not mismatch_count:
        print("YES")
    else:
        print(f"NO {mismatch_count}")

if __name__ == "__main__":
    main()
