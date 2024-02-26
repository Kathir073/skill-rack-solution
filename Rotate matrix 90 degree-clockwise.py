"""
input:
2
3
4 5 9
1 3 5
output:
1 4
3 5
5 9
"""
row=int(input())
col=int(input())
mat=[]
for i in range(row):
    mat.append(list(map(int,input().strip().split())))
mat=mat[::-1]
for i in range(col):
    for j in range(row):
        print(mat[j][i],end=" ")
    print()
