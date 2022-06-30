print("Welcome to kannathali's cafe")
while True:
    Hours = float(input("How many hours have you spent here? "))
    if Hours not in range(1, 8):
        print("Please pick a value between 1 and 7")
    else:
        break
if (Hours<5):
    print('Your bill is 200')
    quit()
else:
  while True:
    Minutes = float(input("How many minutes have you spent here? "))
    if Minutes not in range(0, 60):
        print("Please pick a value between 1 and 59")
    else:
            break
if Minutes == 0 and Hours == 5:
    print('Your bill is 200')
elif Minutes> 0 and Hours == 7:
    print("We'd love to have you here some more time, but our rules don't allow us to")
else:
    amount=200+(Hours-5)*50+Minutes
    print("your bill is Rs", amount)