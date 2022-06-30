n=int(input("how many digits"))
L=[]
even=[]
odd=[]
for i in range (0,n):
    x=int(input('Enter the digit'))
    L.append(x)
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
print('your odd list is',odd)
print('your even list is',even)

