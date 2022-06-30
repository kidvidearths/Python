k=open('cats', 'r')
k1=open('dogs', 'a')
for data in k:
    k1.write(data)
