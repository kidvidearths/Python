judgement= input('Are you the first graduate from your family? Enter yes or no ')
if judgement.lower() == 'yes':
    while True:
        Phy_mark = (input("How much have you scored in Physics? "))
        if Phy_mark.isdigit() and 0 <= int(Phy_mark) <= 100:
            break
        print("We only accept values from 1 to 100. Kindly re-enter")
    while True:
        Che_mark = (input("How much have you scored in Chemistry? "))
        if Che_mark.isdigit() and 0 <= int(Che_mark) <= 100:
            break
        print("We only accept values from 1 to 100. Kindly re-enter")
    while True:
        Math_mark = (input("How much have you scored in Maths? "))
        if Math_mark.isdigit() and 0 <= int(Math_mark) <= 100:
            break
        print("We only accept values from 1 to 100. Kindly re-enter")
    Average= (int(Math_mark)+int(Phy_mark)+int(Che_mark))/3
    if Average >= 98:
        print("Congrats, you are eligible")
    else:
        print("We're sorry, you aren't eligible due to the average being below 98")
else:
    print("It's with deep heart that we inform you this is only for the first graduate of a family")