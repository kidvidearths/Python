import re
ar = input()
list=re.split(r"[^\w\s]",ar)
for i in list:
    print(i)