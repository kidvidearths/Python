import sys


def preparation(pain, M, N):

    wow = [[0 for x in range(len(pain[0]))] for y in range(len(pain))]
    wow[0][0] = pain[0][0]


    for j in range(1, len(pain[0])):
        wow[0][j] = pain[0][j] + wow[0][j - 1]


    for i in range(1, len(pain)):
        wow[i][0] = pain[i][0] + wow[i - 1][0]


    for i in range(1, len(pain)):
        for j in range(1, len(pain[0])):
            wow[i][j] = pain[i][j] + wow[i - 1][j] + wow[i][j - 1] - wow[i - 1][j - 1]

    return wow


def the_final_solution(my_table, k: int):

    if not my_table or not len(my_table):
        return []


    (M, N) = (len(my_table), len(my_table[0]))


    s = preparation(my_table, M, N)

    maximum = -sys.maxsize


    for i in range(k - 1, M):
        for j in range(k - 1, N):


            overall = s[i][j]
            if i - k >= 0:
                overall = overall - s[i - k][j]

            if j - k >= 0:
                overall = overall - s[i][j - k]

            if i - k >= 0 and j - k >= 0:
                overall = overall + s[i - k][j - k]

            if overall > maximum:
                maximum = overall
                p = (i, j)


    (x, y) = p

    return [[my_table[i + x - k + 1][j + y - k + 1] for j in range(k)] for i in range(k)]


p,q=input().split()
p, q = [int(p), int(q)]
matrix=[]
for i in range(0,p):
    temp=input().split()
    temp = [int(i) for i in temp]
    matrix.append(temp)

num=int(input())

for i in range(0,num):
    # submatrix size
    k = int(input())
    submatrix = the_final_solution(matrix, k)
    for row in submatrix:
        print(row)