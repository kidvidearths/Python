rando=int(input())
weight,profit,ratio=[],[],[]
for i in range(0,rando):
    weight.append(int(input()))
for i in range(0,rando):
    profit.append(int(input()))
for i in range(0,rando):
    ratio.append(profit[i]/weight[i])
nappy=int(input())
totah=0
proffa=0
for i in range (0,len(ratio)):
    max = ratio[0]
    j=0
    for i in range (1,len(ratio)):
        if(ratio[i]>max):
            max=ratio[i]
            j=i
    if(totah>=nappy):
        break
    elif(weight[j]<(nappy-totah)):
        totah=totah+weight[j]
        proffa=proffa+profit[j]
    else:
        proffa=proffa+(ratio[j]*(nappy-totah))
        totah=totah+nappy-totah
    ratio[j]=-1
print('%.2f'%proffa)