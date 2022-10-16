h, w = input().split()
n = int(input())
h = int(h)
w = int(w)
l = []
matrix = []

for i in range(n):
    l.append(list(map(int, input().split())))

for i in range(h):
    sub= []
    for j in range(w):
        sub.append(0)
    matrix.append(sub)

for j in range(n):
    p = q = 0
    for i in range(l[j][0]):
        matrix[l[j][2]-1+p][l[j][3]-1+q] = 1
        if (l[j][1] == 0):
            q += 1
        else:
            p += 1

for i in range(h):
    for j in range(w):
        print(matrix[i][j], end=" ")
    print()