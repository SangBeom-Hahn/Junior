matrix = []
for i in range(10):
    matrix.append(list(map(int, input().split())))

i, j= 1, 0
while(1):
    if([i, j] == [8, 8]):
        break
    elif(matrix[i][j+1] == 1 and matrix[i+1][j] == 1):
        # 둘 다 1이면 막힘
        break

    if(matrix[i][j+1] == 1):
        i+=1
        if(matrix[i][j] == 2):
            matrix[i][j] = 9
            break
        matrix[i][j] = 9
        continue

    j+=1
    if (matrix[i][j] == 2):
        matrix[i][j] = 9
        break
    matrix[i][j] = 9

for i in range(10):
    for j in range(10):
        print(matrix[i][j], end=" ")
    print()