def dummy():
    l = []
    g=input()
    p=int(input())
    l.append(g)
    for i in range(0,p):
        p=input()
        l.append(p)
    return l
master=[]
items=[]
finah=[]
k=int(input())
for i in range(0,k):
    master.append(dummy())
for i in master:
    for p in range(1,len(i)):
        items.append(i[p])
items=list(set(items))
items.sort()
for r in items:
    finah.append(r)
    list=[]
    for i in master:
        for p in range(0,len(i)):
            if r==i[p]:
                list.append(i[0])
    finah.append(sorted(list))
for i in finah:
    print(i)