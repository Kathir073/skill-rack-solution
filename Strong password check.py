"""
Recently a security committee decided to enforce the following rules when
an employee creates/changes his/her password.-
The password must contain atleast one special character among # ! _ $ @-
The password must contain atleast two numbers-
The password must contain atleast one upper case alphabet and one lower case alphabet.-
The password must have a minimum length of 8.- The password must have a maximum length of 25
.The program must accept a given password string P as input and check for these rules and output VALID or INVALID.
Boundary Conditions:Length of P is from 2 to 50.
Input Format:First line will contain the string value of the password P
Output Format:VALID or INVALID based on the check performed by the program by applying the rules.
Example Input/Output:
Example 1:Input:
kiC_3b0x3r
Output:VALID
Example 2:Input:
m@d31nindia
Output:INVALID
Explanation:No alphabet in uppercase.
Example 3:Input:
M1kT!s0
Output:INVALID
Explanation:
Minimum length must be 8
"""
CODE:
pword=input().strip()
u,l,n,s=0,0,0,0
for i in p:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
    elif i in "#!_$@":
        s+=1   
    else:
        n+=1
ln=len(p)
if ln>=8 and ln<=25 and s>=1 and n>=2 and l>=1 and u>=1:
    print("VALID")
else:
    print("INVALID")
