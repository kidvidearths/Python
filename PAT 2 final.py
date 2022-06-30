Numbah1=int(input())
Club1=[]
Club2=[]
for i in range (0,Numbah1):
    z=input()
    import re
    if re.match("^[0-9]{2}[a-zA-Z]{3}[0-9]{4}$", z):
        Club1.append(z)
Numbah2=int(input())
for i in range (0,Numbah2):
    z=input()
    import re
    if re.match("^[0-9]{2}[a-zA-Z]{3}[0-9]{4}$", z):
        Club2.append(z)
fa1=[]
fa2=[]
for i in Club1:
    import re
    if re.match("[2][0]", i):
        fa1.append(i)
for i in Club2:
    import re
    if re.match("[2][0]", i):
        fa2.append(i)
fa=list(set(fa1)|set(fa2))
sa1=[]
sa2=[]
for i in Club1:
    import re
    if re.match("[1][9]", i):
        sa1.append(i)
for i in Club2:
    import re
    if re.match("[1][9]", i):
        sa2.append(i)
sa=list(set(sa1)|set(sa2))
ta1=[]
ta2=[]
for i in Club1:
    import re
    if re.match("[1][8]", i):
        ta1.append(i)
for i in Club2:
    import re
    if re.match("[1][8]", i):
        ta2.append(i)
ta=list(set(ta1)|set(ta2))
foa1=[]
foa2=[]
for i in Club1:
    import re
    if re.match("[1][7]", i):
        foa1.append(i)
for i in Club2:
    import re
    if re.match("[1][7]", i):
        foa2.append(i)
foa=list(set(foa1)|set(foa2))
bavers=list(set(fa).intersection(fa1,fa2))
for i in list(set(sa).intersection(sa1,sa2)):
    bavers.append(i)
for i in list(set(ta).intersection(ta1,ta2)):
    bavers.append(i)
for i in list(set(foa).intersection(foa1,foa2)):
    bavers.append(i)
last=[]
for i in bavers:
    import re
    if re.search("[B][C][E]", i):
        last.append(i)
print(sorted(fa))
print(sorted(sa))
print(sorted(ta))
print(sorted(foa))
print(sorted(bavers))
print(sorted(last))