"""SurprisingVote"""

total = float(input().strip())
max_score = float(input().strip())

mid_score = total - max_score
min_score = min(max_score, mid_score)
sum_score = mid_score - min_score
btw = max_score - sum_score

if btw > 2:
    print("Surprising")
else:
    print("Not surprising")
