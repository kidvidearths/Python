import sys


def preprocess(mat, M, N):
    # preprocess the matrix `mat` such that `s[i][j]` stores
    # sum of elements in the matrix from (0, 0) to (i, j)
    s = [[0 for x in range(len(mat[0]))] for y in range(len(mat))]
    s[0][0] = mat[0][0]

    # preprocess the first row
    for j in range(1, len(mat[0])):
        s[0][j] = mat[0][j] + s[0][j - 1]

    # preprocess the first column
    for i in range(1, len(mat)):
        s[i][0] = mat[i][0] + s[i - 1][0]

    # preprocess the rest of the matrix
    for i in range(1, len(mat)):
        for j in range(1, len(mat[0])):
            s[i][j] = mat[i][j] + s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1]

    return s


def findMaxSumSubMatrix(mat, k: int):
    # base case
    if not mat or not len(mat):
        return []

    # `M × N` matrix
    (M, N) = (len(mat), len(mat[0]))

    # preprocess the matrix
    s = preprocess(mat, M, N)

    maximum = -sys.maxsize

    # find the maximum sum submatrix

    # start from cell (k-1, k-1) and consider each submatrix of size `k × k`
    for i in range(k - 1, M):
        for j in range(k - 1, N):

            # Note that (i, j) is the bottom-right corner coordinates of the
            # square submatrix of size `k`

            total = s[i][j]
            if i - k >= 0:
                total = total - s[i - k][j]

            if j - k >= 0:
                total = total - s[i][j - k]

            if i - k >= 0 and j - k >= 0:
                total = total + s[i - k][j - k]

            if total > maximum:
                maximum = total
                p = (i, j)

    # `p` stores bottom-right corner coordinates of the submatrix
    (x, y) = p

    # return maximum sum submatrix
    return [[mat[i + x - k + 1][j + y - k + 1] for j in range(k)] for i in range(k)]




rr=input().split()
n1=int(rr[0])
n2 = int(rr[1])
mat=[]
for i in range(0,n1):
    row=input().split()
    for i in range(0,n2):
        row[i]=int(row[i])
    mat.append(row)

number=int(input())
k=[]
for i in range(0,number):
    r=input()
    k.append(r)
for i in range(0,number):
    submatrix = findMaxSumSubMatrix(mat, int(k[i]))
    for row in submatrix:
        print(row)