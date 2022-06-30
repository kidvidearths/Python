Dirc = {}

n = int(input("Enter Number of Employees:"))

for i in range(0, n):

    name = input("Enter Name: ")

    n = int(input("Enter The Total Number of Numbers The Employee Has.:"))

    Mobile = []

    if n >= 1:

        for i in range(0, n):

            num = input()

            Mobile.append(num)

    Dirc[name] = Mobile

hold = input("Enter The Name to be Searched in the Directory:")

for i in Dirc:
        name = i.split(' ')
        if len(name)>1:
            if hold == name[0] or hold == name[1]:
                print("Mobile Number: ", Dirc[i])
        if len(name)== 1:
            if hold == name[0]:
                print("Mobile Number: ", Dirc[i])
