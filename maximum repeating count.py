"""
input:
10 20 30 20 30 10 30 20
output:
20

explantion:
both 20 and 30 maximum and equal no of counts but min of 2 elements is printed
"""

CODE:

a=list(map(int,input().split()))
b=dict((i,a.count(i)) for i in a)
key=list(b.keys())
value=list(b.values())
print(key[value.index(max(value))])
