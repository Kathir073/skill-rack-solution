"""
INPUT:
R@1nBow
OUTPUT:
r@1nBow
"""
CODE:

s=input().strip()
res=""
for i in s:
    if i.isupper():
        res+=i.lower()
    elif i.islower():
        res+=i.upper()
    else:
        res+=i
print(res)
