"""
input:
cake
2 12
output:
NO

input:
icecream
4 10
output:
YES
"""
CODE:
s=input().strip()
x,y=map(int,input().split())
res=""
while len(res)<=y:
    res+=s
if res[x-1]==res[y-1]:
    print("YES")
else:
    print("NO")
