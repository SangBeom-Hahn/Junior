'''
nxn 체스판 위에 퀸 n개가 서로 공격할 수 없게 놓는 문제이다.
퀸을 놓는 방법의 수를 구하라

0000
0000
0000
0000

행  열  인덱스
0   3   0

0   2   1
1   3   1

0   1   2
1   2   2
2   3   2

3   0   6

4 - (0 - 3 + 1)

n - (열 - 행 + 1)

1. 모경수(prt, n=1)
1) 가로, 세로, 대각선 오른쪽 아래, 왼쪽 아래 대각선 used를 둠
2) 백으로 탐색

* n
출 : 방법의 수

2. n^3
'''
# print(n, i, row, 1, n - (i - row + 1))

cnt = 0

def back(chose, row):
    global cnt
    
    if(len(chose) == n):
        cnt += 1
    
    for i in range(n):
        if(
            not colUsed[i] and
            not crossLeft[row+i] and
            not crossRight[n - (i - row + 1)]
           ):
            chose.append(i)
            colUsed[i] = True
            crossLeft[row+i] = True
            
            crossRight[n - (i - row + 1)] = True
            back(chose, row+1)
            colUsed[i] = False
            crossLeft[row+i] = False
            crossRight[n - (i - row + 1)] = False
            chose.pop()

n = int(input())
colUsed = [0] * n
crossRight = [0] * (2*n-1)
crossLeft = [0] * (2*n-1)
print(crossRight)

back([], 0)
print(cnt)