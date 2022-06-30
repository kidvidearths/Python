judgement= input('Are you the first graduate from your family? ')
if judgement.lower() == 'yes':
    while True:
        Phy_mark = float(input("How much have you scored in Physics? "))
        if Phy_mark not in range(0, 101):
            print("Please pick a value between 0 and 100")
        else:
            break
    while True:
        Che_mark = float(input("How much have you scored in Chemistry? "))
        if Che_mark not in range(0, 101):
            print("Please pick a value between 0 and 100")
        else:
            break
    while True:
        Math_mark = float(input("How much have you scored in Math? "))
        if Math_mark not in range(0, 101):
            print("Please pick a value between 0 and 100")
        else:
            break
    Average= (Math_mark+Phy_mark+Che_mark)/3
    if Average >= 98:
        print("Congrats, you are eligible")
    else:
        print("We're sorry, you aren't eligible due to the average being below 98")
else:
    print("It's with deep heart that we inform you this is only for the first graduate of a family")