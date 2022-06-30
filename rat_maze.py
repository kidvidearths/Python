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
def life(i,j,soppa,pip):
    visited=False
    if (solution[order-1][order-1]==1):
        return True
    if(soppa==1):

        if(question[i+1][j]==1):
            solution[i+1][j]=1

            if(life(i+1,j,1,visited)==True):
                return True
            else:
                solution[i+1][j] = 0

        if (question[i][j+1] == 1 ):
            solution[i][j+1] = 1
            visited=True
            if (life(i,j+1,1,visited) == True):
                return True
            else:
                solution[i][j+1] = 0

        if (question[i][j-1] == 1 and pip!=True):
            solution[i][j-1] = 1

            if (life(i,j-1,0,visited) == True ):
                return True
            else:
                solution[i][j-1] = 0

        return False
    else:

        if(question[i+1][j]==1 ):
            solution[i+1][j]=1

            if(life(i+1,j,1,visited)==True):
                return True
            else:
                solution[i+1][j] = 0

        if (question[i][j-1] == 1 ):
            solution[i][j-1] = 1

            if (life(i,j-1,0,visited) == True ):
                return True
            else:
                solution[i][j-1] = 0
        return False

print (life(0,0,1,False))
for i in solution:
    print(solution[i])