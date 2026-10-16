"""มาเป็นทีม"""

n, m = map(int, input().split())

if not (1 <= n <= 10 and 1 <= m <= 20):
    print("Data Incorrect")
else:
    teams = []
    for _ in range(n):
        teams.append(list(map(int, input().split())))

    ok = True
    for t in teams:
        if len(t) != m:
            ok = False
        for s in t:
            if s < 0 or s > 100:
                ok = False

    if not ok:
        print("Data Incorrect")
    else:
        total = 0
        for i in range(n):
            avg = sum(teams[i]) / m
            print(f"Team {i + 1}: Average = {avg:.2f}, Max = {max(teams[i])}")
            total += sum(teams[i])
        print(f"Total Score of All Teams = {total}")
