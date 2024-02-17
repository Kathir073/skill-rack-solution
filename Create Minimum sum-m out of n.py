"""
input:
5 2
9 2 1 5 4

ouput:
3
explantion:
out of all elements the sum of 1+2=3 is minimum
so 3 is printed as output
"""
CODE:
m,n=map(int,input().split())
ls=list(map(int,input().split()))[:m]
ls.sort()
summ=0
for i in range(n):
    summ+=ls[i]
print(summ)
