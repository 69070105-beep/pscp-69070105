"""CuteCat CuteFox"""
cats = {}
foxes = {}

n = int(input())
for _ in range(n):
    text = input()
    for ch in ['{', '}', '"', "'", '“', '”', '‘', '’']:
        text = text.replace(ch, '')

    pairs = text.split(',')
    for pair in pairs:
        if ':' in pair:
            parts = pair.split(':', 1)
            s1 = parts[0].strip()
            s2 = parts[1].strip()

            s1_lower = s1.lower()
            s2_lower = s2.lower()

            if "cat" in s1_lower or "fox" in s1_lower:
                code, name = s1, s2
            elif "cat" in s2_lower or "fox" in s2_lower:
                name, code = s1, s2
            else:
                name, code = s1, s2

            if "cat" in code.lower():
                cats.update({code: name})
            else:
                foxes.update({code: name})

all_names = set(cats.values()) | set(foxes.values())
all_codes = set(cats.keys()) | set(foxes.keys())

if "Garfield" not in all_names and "Cat01" not in all_codes:
    cats.update({"Cat01": "Garfield"})

if "Fubuki" not in all_names and "Fox01" not in all_codes:
    foxes.update({"Fox01": "Fubuki"})

print(f"Cat : {len(cats)}")
print(f"Fox : {len(foxes)}")


def sort_key(code):
    digits = ''.join(filter(str.isdigit, code))
    return int(digits) if digits else 0


for code in sorted(cats.keys(), key=sort_key):
    print(f"{cats.get(code)} : {code}")

for code in sorted(foxes.keys(), key=sort_key):
    print(f"{foxes.get(code)} : {code}")
