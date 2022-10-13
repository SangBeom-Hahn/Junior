//자료구조를 공부하기 전 코드보다 for문 두개를 줄임!!

n = int(input())
arrMatrix = []
for i in range(n):
    arrMatrix.append(input().split())

arrMatrix.sort()

for i in range(1, 20):
    if(i > int(arrMatrix[len(arrMatrix)-1][0])): #넘으면 패스
        print(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        continue

    for j in range(1, 20):
        if(int(arrMatrix[i-1][1]) == j):
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()