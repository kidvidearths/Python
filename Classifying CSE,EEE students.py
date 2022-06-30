N=int(input('Enter the number of students'))
Everybody=[]
CSE=[]
EEE=[]
CEE=[]
for i in range(0,N):
    biscut=input('Keep on entering the reg numbers')
    import re
    if re.match("^[1-9][0-9][a-zA-Z]{3}[0-9}]{4}$", biscut):
        Everybody.append(biscut)
    else:
        print('Invalid input, re-run the program')
        quit()
for i in range(0,N):
    dog=Everybody[i][2:5]
    if dog.lower() =='bce':
        CSE.append(Everybody[i])
    if dog.lower() == 'eee':
        EEE.append(Everybody[i])
    if dog.lower() =='cee':
        CEE.append(Everybody[i])
print('Your programmers are', CSE)
print('Your electricians are', EEE)
print('Your chemists are', CEE)
