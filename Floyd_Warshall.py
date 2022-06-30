number=int(input())
matrix=[]
for i in range(0,number):
    better_than_nothing=[]
    for j in range(0,number):
        c=input()
        if(c=="i"):
            better_than_nothing.append(1000)
        else:
            better_than_nothing.append(int(c))
    matrix.append(better_than_nothing)

random=0


for i in range(0,number):
    for j in range(0,number):
        for k in range(0,number):
            if(j==k or j==random or k==random):
                pass
            else:
                matrix[j][k]=min(matrix[j][k],matrix[j][random]+matrix[random][k])
    for i in range(0, number):
        for j in range(0, number):
            if (i == j):
                print(0, '', end='')
            elif (matrix[i][j] == 1000):
                print("INF ", end='')
            else:
                print(matrix[i][j], '', end='')
        print('')
    print('\n')
    random=random+1
