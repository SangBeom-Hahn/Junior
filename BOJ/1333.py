''''
nxm에 아기상어 여러마리 있따. 한칸에 상어 최대 한마리 존재함
안전거리 : 그 칸과 가장 가까운 아기상어와의 거리다. 두 칸의 거리는 하나의 칸에서 다른 칸으로 가기위해
지나야하는 칸의 수이고 이동은 8방향이다.

1. 모든 경ㅇ우의 수
1) 백으로 탐색
2) 상어에서 뻗어나가는 문제로 ㄱㄱ
3) 현재 안전거리보다 더 작으면 갱신
4) 다 돈 후에 최대 안전거리 ㄱㄱ

* n, m : 행, 열
공간상태(1=상어있는 곳)
출력 : 안전거리가 가장 큰 칸을 구해라

2. n^2
'''
from collections import deque

def bfs():
    while(q):
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if(nx < 0 or ny < 0 or nx >= n or ny >= m):
                continue
            
            if(dist[nx][ny] > dist[x][y] + 1):
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
            

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
q = deque()
dist = [[3000] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if(graph[i][j] == 1):
            dist[i][j] = 0
            q.append((i, j))
            
bfs()            

# print(*dist, sep = '\n')

maxResult = 0
for i in range(n):
    for j in range(m):
        if(dist[i][j] > maxResult):
            maxResult = dist[i][j]
print(maxResult)