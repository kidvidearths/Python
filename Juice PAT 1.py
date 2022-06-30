firstkind = int(input())
if firstkind < 400:
    print('Number of litres must be above 400')
secondkind = int(input())
if secondkind < 400:
    print('Number of litres must be above 400')
thirdkind = int(input())
if thirdkind < 400:
    print('Number of litres must be above 400')
import math
x = math.gcd(firstkind, secondkind)
y = math.gcd(x, thirdkind)
Total_litres = firstkind + secondkind + thirdkind
No_of_cans = Total_litres / y
print(int(No_of_cans))