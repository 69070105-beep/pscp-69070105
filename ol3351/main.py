"""พูดจาภาษากระต่าย"""

text = input().strip()
text_upper = text.upper()
n = len(text_upper)

only_it = True
for char in text_upper:
    if char not in {'I', 'T'}:
        only_it = False
        break

if only_it:
    print(f"unknown {n}")
else:
    valid_chars = {'R', 'A', 'B', 'I', 'T'}
    is_valid = True
    error_index = -1

    for i in range(n):
        c = text_upper[i]

        if c not in valid_chars:
            is_valid = False
            error_index = i
            break

        if not i:
            if c == 'A':
                is_valid = False
                error_index = 0
                break
        else:
            prev = text_upper[i - 1]

            if prev == 'R' and c != 'A':
                is_valid = False
                error_index = i
                break

            if prev == 'B' and c not in {'I', 'T'}:
                is_valid = False
                error_index = i
                break

            if prev in {'I', 'T'} and c == 'A':
                is_valid = False
                error_index = i
                break

    if is_valid and text_upper[-1] in {'R', 'B'}:
        is_valid = False
        error_index = n - 1

    if not is_valid:
        print(f"no {error_index}")
    else:
        max_a = 0
        current_a = 0
        for c in text_upper:
            if c == 'A':
                current_a += 1
                if current_a > max_a:
                    max_a = current_a
            else:
                current_a = 0

        print(f"yes {max_a}")
