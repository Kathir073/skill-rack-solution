"""
input:
2
1111 1000
output:
23
"""
code:

n=int(input())
x,y=map(str,input().strip().split())
s=0
z=0
x,y=x[::-1].strip(),y[::-1].strip()
for i in range(len(x)):
    s+=(n**i)*int(x[i])
for j in range(len(y)):
    z+=(n**j)*int(y[j])
print(s+z)
