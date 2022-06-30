No_of_students=int(input("Enter the number of students"))
Counter=0
Total=0
while Counter<No_of_students:
    Marks=int(input("Enter the marks of the student"))
    Total=Total+Marks
    Average=Total/No_of_students
    Counter=Counter+1
print('The average is', Average)
if Average<30:
    print("Congrats, your class is dumb")