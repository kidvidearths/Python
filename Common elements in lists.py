l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
l3=[]
for i in l1:
    for j in l2:
        if i==j:
            l3.append(i)
print(l3)