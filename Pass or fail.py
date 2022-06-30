Regno=input("Enter the registeration number:")
Nanme=input("Enter your name:")
Mark1=int(input('Enter the marks scored in sub 1'))
Mark2=int(input('Enter the marks scored in sub 2'))
Mark3=int(input('Enter the marks scored in sub 3'))
Average=(Mark1+Mark2+Mark3)/3
if Average>= 90:
    print("Your grade is S")
elif Average>= 80:
    print("Your grade is A")
else:
    print("BRUH")