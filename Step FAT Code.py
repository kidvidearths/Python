x = int(input())
y = {}
for i in range(x):
    starting_point = (int(input()), int(input()))
    ending_point = (int(input()), int(input()))
    y[starting_point] = ending_point
all_the_stairs = []
for point in y:
    stairs = []
    temprature = point
    while 1:
        stairs.append([temprature,y[temprature]])
        if y[temprature] in y:
            temprature = y[temprature]
        else:
            break
    all_the_stairs.append(stairs)
z = len(max(all_the_stairs,key = len))
for stairs in all_the_stairs:
    if len(stairs)==z:
        print(stairs)