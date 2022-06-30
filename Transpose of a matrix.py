row=int(input('Row size'))
col=int(input('Column size'))
mat1=[]
mat2=[]
for i in range (0,row):
    r1 = []
    for j in range (0,col):
        x=int(input())
        r1.append(x)
    mat1.append(r1)
for i in range(0,row):
    r2=[]
    for j in range (0,col):
        r2.append(mat1[j][i])
    mat2.append(r2)
for i in range(0,row):
    for j in range (0,col):
        print(mat2[i][j], '', end= "")
    print()





