"""
INPUT:
MON[first day of the month]
10
OUTPUT:
WED
"""
CODE:

day=input().strip()
date=int(input())
daylist=["SUN","MON","TUE","WED","THU","FRI","SAT"]
if day in daylist:
    s=date+days.index(day)
s=s%7
print(daylist(s-1))
