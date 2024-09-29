'''
mxn 종이에 k개의 사각형이 있다. 직사각형을 제외한 부분이 분리된 영역으로 나눠진다.

1. 모경수(prt, n=1)
1) 열, 행으로 들어오는 걸 행, 열로 해서 지도를 1로 칠함
2) 0인 값들에 대해 bfs 돌림

* m n k 
직사각형 왼쪽 아래 꼭짓점 x,y 좌표와 오른쪽 위 꼭짓점 좌표
(모눈종이 왼쪽 아래가 0, 0 오른쪽 위가 n, m이다.) (열, 행으로 본다.)

출 : 나머지 부분이 몇개의 영역으로 분리되는지, 분리된 영역이 각 넓이가 얼마인지 구하라
'''

from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    cnt =1
    
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if(nx < 0 or ny < 0 or nx >= m or ny >= n):
                continue
            
            if(not visit[nx][ny] and graph[nx][ny] == 0):
                cnt += 1
                visit[nx][ny] = True
                q.append((nx, ny))
                
    result.append(cnt)

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
visit = [[False] * n for _ in range(m)]

for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = 1

print(*graph, sep = '\n')

cnt = 0
result = []
for i in range(m):
    for j in range(n):
        if(not visit[i][j] and graph[i][j] == 0):
            cnt += 1
            bfs(i, j)

print(cnt, result)            