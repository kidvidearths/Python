def filler(size,start):
    if(size==2):
        end=start+1
        if(symbah[end-1]=='+'):
            pp[end-1][end]=numbah[end-1]+numbah[end]
        elif(symbah[end-1]=='*'):
            pp[end-1][end]=numbah[end - 1] * numbah[end]
        else:
            pp[end - 1][end] = numbah[end - 1] - numbah[end]
    else:
        cat=0
        for i in range(start,start+size):
            if(i==start):
                if(symbah[i]=='+'):
                    cat=max(cat,numbah[i]+pp[i+1][i+size-1])
                elif(symbah[i]=='*'):
                    cat=max(cat,numbah[i]*pp[i+1][i+size-1])
                else:
                    cat = max(cat, numbah[i] - pp[i + 1][i + size - 1])
            if(i==start+size-1):
                if (symbah[i-1] == '+'):
                    cat = max(cat,numbah[i] + pp[start][i-1])
                elif(symbah[i-1] == '*'):
                    cat = max(cat,numbah[i] * pp[start][i-1])
                else:
                    cat = max(cat, pp[start][i - 1] - numbah[i] )
            if(i!=start and i!=start+size-1):
                if (symbah[i] == '+'):
                    cat = max(cat,pp[start][i]+pp[i+1][start+size-1])
                elif(symbah[i] == '*'):
                    cat = max(cat,pp[start][i]*pp[i+1][start+size-1])
                else:
                    if(i + 1!=start + size - 1):
                        cat = max(cat, pp[start][i] - pp[i + 1][start + size - 1])
        pp[start][start+size-1]=cat



import re
ar = input()
numbah=re.split(r"[^\w\s]",ar)
for i in range(0,len(numbah)):
    numbah[i]=int(numbah[i])
symbah=[]
for i in ar:
    if(i=='+' or i=='*' or i=='-'):
        symbah.append(i)
pp=[[0 for i in range(0,len(numbah))] for j in range(0,len(numbah))]



for length in range(2,len(numbah)+1):
    for i in range(0,len(numbah)):
        if(length+i<=len(numbah)):
            filler(length,i)
for i in pp:
    print(i)