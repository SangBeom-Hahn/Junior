'''
nxm 0 = 이동o / 1= 벽 이동 불가
1, 1에서 n, m으로 최단 경로 이동
한개의 벽을 부수고 이동가능하다.

1. 모경수(prt, n=1)
1) 1인 곳의 좌표를 구함
2) 1인 곳의 좌표를 순회해서 0으로 만듬
3) 계속 0, 0에서 bfs 호출
4) 최단 거리 구하고 갱신
5) 최단거리가 10000000 이면 -1 출력

* n, m (0, 1 벽)
출 : 최단 거리, (못 가면 -1)

2. nlogn
'''
min_dis = 10000000
from collections import deque

def bfs(startX, startY):
    global min_dis
    
    q = deque()
    q.append((startX, startY))
    visit[startX][startY] = True
    
    while(q):
        x, y = q.popleft()
        if(x == n-1 and y == m-1):
            if(min_dis > graph[x][y]):
                min_dis = graph[x][y]+1
                return
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if(nx < 0 or ny < 0 or nx >= n or ny >= m):
                continue
            
            if(not visit[nx][ny] and graph[nx][ny] == 0):
                graph[nx][ny] = graph[x][y] + 1
                visit[nx][ny] = True
                q.append((nx, ny))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
temp = [ele[:] for ele in graph]

visit = [[False] * m for _ in range(n)]
temp_v = [ele[:] for ele in visit]

ones = []
for i in range(n):
    for j in range(m):
        if(graph[i][j] == 1):
            ones.append((i, j))

if(len(ones) == 0):
    bfs(0, 0)
else:
    for x, y in ones:
        graph[x][y] = 0
        # print(x, y)
        # print(*graph, sep = '\n')
        # print()
        
        bfs(0, 0)
        # print(min_dis)
        graph = [ele[:] for ele in temp]
        visit = [ele[:] for ele in temp_v]

if(min_dis == 10000000):
    print(-1)
else:
    print(min_dis)