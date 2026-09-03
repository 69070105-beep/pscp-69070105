a = int(input())
count = 0
is_pass = True

for _ in range(a):
    d = int(input())
    count += d
    if d < 50:
        is_pass = False

s = count / a
print(f"{s:.1f}")

if is_pass and s >= 60:
    print("PASS")
else:
    print("FAIL")