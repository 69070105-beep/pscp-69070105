"""นวัตกรรมงบประมาณโรงเรียน"""

def main():
    """สร้าง Password Key 6 หลัก"""
    school = input()
    length = len(school)
    first_ascii = ord(school[0].upper())
    last_ascii = ord(school[-1].upper())
    result = []
    for pos in range(3, 9):
        val = pos - 1
        if pos % 2:
            code = (first_ascii + val) % length
        else:
            code = (last_ascii - val) % length
        if code > 9:
            code = code % 10
        result.append(code)
    print(*result)
main()
