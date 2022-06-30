n1=input()
n2=input()
p=len(n1)
q=len(n2)
str1=[0]
str2=[0]
for i in n1:
    str1.append(i)
for i in n2:
    str2.append(i)
temp=[]
table=[]
for i in range(0,q+1):
    temp.append(0)
for i in range(0,p+1):
    table.append(list.copy(temp))
for i in range(1,p+1):
    table[i][0]=i
for i in range(1,q+1):
    table[0][i]=i
def speaker(i,j):
    if(table[i][j]==0):
        return True
    if(str1[i]==str2[j]):
        speaker(i-1,j-1)
    elif(table[i-1][j]==min(table[i-1][j],table[i][j-1],table[i-1][j-1])):
        print("Delete",str1[i])
        speaker(i-1,j)
    else:
        print("Replace",str1[i],"by",str2[j])
        speaker(i - 1, j-1)

for i in range(1,p+1):
    for j in range(1,q+1):
        if(str1[i]==str2[j]):
            table[i][j]=table[i-1][j-1]
        else:
            table[i][j]=min(table[i-1][j],table[i][j-1],table[i-1][j-1])+1
for i in table:
    for j in i:
        print(j," ",end="")
    print("")
print(table[p][q])
speaker(p,q)