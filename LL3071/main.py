"""จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""
a = int(input())
b = int(input())
d = int(input())
r = int(input())


def main():
    """ฟังก์ชั่นการคิดคำนวณเมื่อเข้าเงื่อนไข"""
    total = 0
    if b > a and r < d:
        for i in range(a, b + 1):
            i = i % d
            if i == r:
                total += 1
        print(total)

main()
