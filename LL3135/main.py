"""ของขวัญและขโมย"""
def solve():
    """คำนวน"""
    data = input().split()
    if not data:
        return

    n = int(data[0])
    k = int(data[1])
    t = int(data[2])

    current_person = 1
    count = 1

    if current_person == t:
        print(count)
        return

    while True:
        current_person = ((current_person - 1 + k) % n) + 1

        if current_person == 1:
            break

        count += 1

        if current_person == t:
            break

    print(count)


if __name__ == "__main__":
    solve()
