row=int(input('Row size'))
col=int(input('Column size'))
mat1=[]
mat2=[]
mat3=[]
for i in range (0,row):
    r1 = []
    for j in range (0,col):
        x=int(input())
        r1.append(x)
    mat1.append(r1)
for i in range (0,row):
    r2 = []
    for j in range (0,col):
        x=int(input())
        r2.append(x)
    mat2.append(r2)
for i in range(0,row):
    r3=[]
    for j in range (0,col):
        x=mat1[i][j]+mat2[i][j]
        r3.append(x)
    mat3.append(r3)
for i in range(0,row):
    for j in range (0,col):
        print(mat3[i][j], '', end= "")
    print()





