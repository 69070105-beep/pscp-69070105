"""ไข้หวัดกระต่ายสายพันธุ์ใหม่"""

def main():
    """ไข้หวัดกระต่ายสายพันธุ์ใหม่"""
    rows, cols = map(int, input().split())
    rabbit_r, rabbit_c = map(int, input().split())
    n = int(input())

    infected = [tuple(map(int, input().split())) for _ in range(n)]

    safe_count = 0
    rabbit_risk = 0

    for r in range(rows):
        for c in range(cols):
            max_risk = 0
            for inf_r, inf_c in infected:
                dist = max(abs(r - inf_r), abs(c - inf_c))
                if not dist:
                    max_risk = 100
                    break
                if dist == 1:
                    if max_risk < 60:
                        max_risk = 60
                elif dist == 2:
                    if max_risk < 20:
                        max_risk = 20

            if not max_risk:
                safe_count += 1

            if r == rabbit_r and c == rabbit_c:
                rabbit_risk = max_risk

    print(safe_count)
    print(f"{rabbit_risk}%")


if __name__ == "__main__":
    main()
