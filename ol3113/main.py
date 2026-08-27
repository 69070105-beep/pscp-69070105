"""ราเมนกระต่ายน้อย"""


def main():
    """คำนวณราคาราเมน"""
    size, ramen_type = input().split()
    topping_info = input().split()

    ramen_price = {
        "S": {"R": 60, "T": 80},
        "M": {"R": 80, "T": 100},
        "L": {"R": 100, "T": 120},
    }

    total = ramen_price[size][ramen_type]

    if topping_info[0] != "N":
        topping_type = topping_info[0]
        count = int(topping_info[1])
        topping_price = {"P": 15, "E": 10}
        total += count * topping_price[topping_type]

    print(total)

main()
