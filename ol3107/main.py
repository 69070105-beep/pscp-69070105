"""Bonus"""

def main():
    """mmmmmm"""
    data1, data2, data3 = input().split()
    data2 = int(data2)
    data3 = float(data3)
    money = 0
    f = 0.0
    if data1 == "M":
        money = 1500
        if data2 <= 5:
            f = 0.06
        elif data2 <= 10:
            f = 0.08
        else:
            f = 0.10
    elif data1 == "B":
        money = 1000
        if data2 <= 5:
            f = 0.05
        elif data2 <= 10:
            f = 0.06
        else:
            f = 0.07
    elif data1 == "G":
        money = 500
        if data2 <= 5:
            f = 0.04
        elif data2 <= 10:
            f = 0.05
        else:
            f = 0.06
    total_bonus = money + (f * data3)
    print(f"{total_bonus:.0f}")
main()
