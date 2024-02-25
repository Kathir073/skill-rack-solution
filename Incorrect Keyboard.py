s=input().strip()
w="TDLF"
c=0
for i in s:
    if i in w:
        c+=1
print(2**c)
