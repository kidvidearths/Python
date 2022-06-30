print('Cat and Dogs have mutated and decided to go to war. The fate of the human race depends on who wins this. Pick your players wisely')
Dogs=[]
Cats=[]
N=int(input("How are players are on each team? "))
for i in range(0,N):
    print('This is team MEOW MEOW. Enter your player', i+1,':', '', end="")
    Name=input()
    Cats.append(Name)
for i in range(0,N):
    print('This is team BOW BOW. Enter your player', i+1,':', '', end="")
    Name = input()
    Dogs.append(Name)
Team={'MEOW MEOW': Cats, 'BOW BOW': Dogs}
pick=input('Enter the name of the team to see players: ')
print(*Team[pick], sep = ", ")