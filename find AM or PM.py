"""
INPUT:
00:00
OUTPUT:
AM

INPUT:
12:34
OUTPUT:
PM
"""

h,m=input().split(":")
h,m=int(h),int(m)
if((h>24 and m>59) or (h>24 and m<59)):
    print("INVALIDINPUT")
elif h>=12 and not(h==0):
    print("PM")
else:
    print("AM")
