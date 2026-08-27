"""ผ่านหรือไม่ ค่าเฉลี่ยรายวิชา"""
a = int(input())
count = 0
result = "PASS"

for _ in range(a):
    d = int(input())
    count += d
    if d < 50:
        result = "FAIL"

s = count / a
print(f"{s:.1f}")

if s < 60:
    result = "FAIL"

print(result)
