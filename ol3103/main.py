"""จำนวนสระ"""

many = int(input())
aeiou = ['A', 'E', 'I', 'O', 'U']
my_list = []

def main():
    """เปรียบเทียบ """
    count = 0
    for _ in range(1, many + 1):
        word = input()
        my_list.append(word)
        if word in aeiou:
            count += 1
    print(count)

main()
