"""ฉันจะเป็น Saitama ให้ได้เลย"""

import math as m

pushup = int(input())
situp = int(input())
updown = int(input())
run = int(input())

Day_pushup = int(input())
Day_situp = int(input())
Day_run = int(input())
Day_updown = int(input())

total_day_pushup = m.ceil(pushup / Day_pushup)
total_day_situp = m.ceil(situp / Day_situp)
total_day_updown = m.ceil(updown / Day_updown)
total_day_run = m.ceil(run / Day_run)

totalday = max(total_day_pushup, total_day_situp, total_day_updown, total_day_run)

print(totalday)
