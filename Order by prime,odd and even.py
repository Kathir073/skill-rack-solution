def isPrime(a):
    for i in range(2,a):
        if(a%i==0):
            return False
    return True

l=list(map(int,input().strip().split()))
prime,even,odd=[],[],[]
for i in range(0,len(n)):
    if(isPrime(l[i])):
        prime.append(l[i])
    elif not(l[i]%2==0):
        odd.append(l[i])
    else:
        even.append(l[i])
prime.sort()
odd.sort()
even.sort()
prime.extend(odd)
prime.extend(even)
print(*prime)

        
