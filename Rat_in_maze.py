question={}
solution={}
order=int(input())
for i in range(0,order):
    lollipop={-1:0,order:0}
    pem={}
    for j in range(0,order):
        lollipop[j]=int(input())
        pem[j]=0
    question[i]=lollipop
    solution[i]=pem

pem={}
for i in range(0,order):
    pem[i]=0
question[order]=pem
solution[0][0]=1
def life(i,k):
    if (solution[order-1][order-1]==1):
        return True
    for j in range(k,order):
        if(question[i+1][j]==1 ):
            solution[i+1][j]=1
            if(life(i+1,j)==True):
                return True
            else:
                solution[i+1][j] = 0
                return False
        if (question[i][j+1] == 1 ):
            solution[i][j+1] = 1
            if (life(i,j+1) == True):
                return True
            else:
                solution[i][j+1] = 0
                return False
        if (question[i][j-1] == 1 ):
            solution[i][j-1] = 1
            if (life(i,j-2) == True ):
                return True
            else:
                solution[i][j-1] = 0
                return False
    return False

life(0,0)
for i in range(0,order):
    for j in range(0,order):
        print(solution[i][j], end="")
    print()
