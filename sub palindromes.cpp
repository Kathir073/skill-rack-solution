/*
INPUT:
everest

OUTPUT:
2
eve,ere so 2
INPUT:
abccbaab

OUTPUT:
5
cc,bccb,aa,baab,abccba so 5
*/
CODE:
  
s=input().strip()
res=[]
for j in range(len(s)):
    for i in range(len(s)+1):
        if len(s[j:i])>=2 and s[j:i]==s[j:i][::-1] :
            res.append(s[j:i])
res=list(set(res))
print(len(res))
