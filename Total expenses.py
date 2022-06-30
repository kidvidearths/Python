Cost_comp=float(input("What is the cost of 1 computer :"))
No_comp=float(input("How many computers are you getting? :"))
Cost_furn=float(input("What is cost of 1 table?:"))
No_furn=float(input("How many tables are you getting?:"))
Labours_work=float(input("How many labours did you hire?:"))
No_Labour=float(input("How much are you paying the labour per an hour?:"))
Computer_cost=Cost_comp*No_comp
furn_cost=Cost_furn*No_furn
Labours_cost=Labours_work*No_Labour
Total_cost=Computer_cost+furn_cost+Labours_cost
print("It will cost you a total of", Total_cost, '.2f')