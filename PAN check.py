PAN=input("What's your PAN?")
if len(PAN)==9:
    k=PAN[0:5]
    l=PAN[5:9]
    m=PAN[9]
    k=k.isalpha()
    l=l.isdigit()
    m=m.isalpha()
    if k==True and l==True and m==True:

        print("It's valid")
    else:
        print('Not Valid')
else:
    print('Not long or short enough')