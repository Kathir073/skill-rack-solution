"""
INPUT:
909
OUTPUT:
919
"""
n=int(input())
while True:
    n+=1
    s=str(n)[::-1]
    if(n==int(s)):
        print(n)
        break
