"""
INPUT:
305
794
OUTPUT:
1
EXPLANATION:
sum of reverse of 305 and 794 is 503+497=1000
reserse of ouput 1000 is 1

"""
CODE:

x=int(input("x:"))
y=int(input("y:"))
x,y=int(str(x)[::-1]),int(str(y)[::-1])
summ=x+y
if (summ)>9:
    summ=int(str(summ)[::-1])
    print(summ)
else:
    print(summ)
