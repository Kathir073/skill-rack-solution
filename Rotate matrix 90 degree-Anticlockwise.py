"""
input:
4
4
1 2 3 4
5 6 7 8 
9 10 11 12
13 14 15 16

output:

4 8 12 16 
3 7 11 15 
2 6 10 14 
1 5 9 13 

input:
2
3
4 5 9
1 3 5
ouput:
9 5
5 3
4 1
"""
row=int(input())
col=int(input())
mat=[]
for i in range(row):
    mat.append(list(map(int,input().strip().split()))[::-1])
for i in range(col):
    for j in range(row):
        print(mat[j][i],end=" ")
    print()
