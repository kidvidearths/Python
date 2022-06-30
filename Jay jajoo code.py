n=int(input())
count=-1
prev=-1
attack=[]
i=0
for k in range(n):
    a=[]
    for l in range(n):
        a.append(-1)
    attack.append(a)

def underattack(i,j):
    if(attack[i][j]==-1):
        return False
    return True

def block(i,j):
    for k in range(n):
        for l in range(n):
            if(((k+l==i+j) or (abs(k-l)==abs(i-j)) or (k==i) or (l==j) ) and (attack[k][l]==-1)):
                attack[k][l]=i

def clr(i,prev):
    for k in range(n):
        for l in range(n):
            if(attack[k][l]==i):
                attack[k][l]=-1
        if(attack[i][k]==1000):
            attack[i][k]=-1
            prev=k
    print('\n',i,"deleted")
    print(attack,sep="\n")
    return [i,prev]

def placement(i,prev,count):
    count+=1
    print('\n',i,"received")
    while(i<=n-1):
        print('\n',i,"i_while_received")
        for j in range(prev,n):
            if(underattack(i,j)==False):
                if(j!=prev):
                    print('\n',i,"for_received")
                    prev=j
                    attack[i][j]=1000
                    print('\n',i,j,"added")
                    block(i,j)
                    print(attack,sep="\n")
                    i+=1
                    count=placement(i,prev,count)
        else:
            i-=1
            print("\n",i,prev,"to be cleared")
            a=clr(i,prev)
            i=a[0]
            prev=a[1]
            print("\n",i,"to be added")
            count=placement(i,prev,count)
    return count

placement(i,prev,count)

print('\n')
print(*attack,sep="\n")