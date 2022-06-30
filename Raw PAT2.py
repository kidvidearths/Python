Numbah1=int(input())
Club1=[]
Club2=[]
for i in (0,Numbah1):
    z=input()
    Club1.append(z)
Numbah2=int(input())
for i in (0,Numbah2):
    z=input()
    Club2.append(z)
sc1=[]
sc2=[]
for i in Club1:
    import re
    if re.match("[2][0]", i):
        sc1.append(i)
for i in Club2:
    import re
    if re.match("[2][0], i"):
        sc2.append(i)
sc=list(set(sc1)^set(sc2))
bc1=[]
bc2=[]
for i in Club1:
    import re
    if re.match("[1][9]", i):
        bc1.append(i)
for i in Club2:
    import re
    if re.match("[1][9]", i):
        bc2.append(i)
bc=list(set(bc1)^set(bc2))
print(sc)
print(bc)
