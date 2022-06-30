k=[['robyn starling ', 'lotin', 'clothes'], ['sathvik', 'clothes', 'pen drive', 'car'], ['arnav', 'pen drive']]
l=['lotin', 'clothes', 'car', 'pen drive']
test=[]


for r in l:
    test.append(r)
    list = []
    for i in k:
        for p in range(0,len(i)):
            if r==i[p]:
                list.append(i[0])
    test.append(list)
print(test)