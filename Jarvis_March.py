all_the_points=[]
our_points=[]

def left_most():
    min=1000
    point=100
    for i in range(0, number):
        if(all_the_points[i][0]<min):
            min=all_the_points[i][0]
            point=i
    for i in range(0, number):
        if(all_the_points[point][0]==all_the_points[i][0] and all_the_points[point][1]>all_the_points[i][1] and point!=i):
            point=i
    return point

def leftward_movement(a,b,c):
    decider=(b[0]-a[0])*(c[1]-b[1])-(c[0]-b[0])*(b[1]-a[1])
    if(decider>0):
        return True
    else:
        return False


number=int(input())
for i in range(0,number):
    pain=[]
    import re
    ar = input()
    numbah = re.split('[,()]', ar)
    pain.append(int(numbah[1]))
    pain.append(int(numbah[2]))
    all_the_points.append(pain)
our_points.append(all_the_points[left_most()])
i=0
while(True):
    endpoint=all_the_points[0]
    vertex_hull=our_points[i]
    for k in range(0,number):
        if(leftward_movement(vertex_hull,endpoint,all_the_points[k]) or vertex_hull==endpoint):
            endpoint=all_the_points[k]
    if(endpoint==our_points[0]):
        break
    our_points.append(endpoint)
    i = i + 1
for i in our_points:
    print(i)