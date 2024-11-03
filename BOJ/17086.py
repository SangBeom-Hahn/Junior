'''
nxm 크기에 아기 상어 여러 마리가 있다.
안전 거리 : 그 칸과 가장 거리가 가까운 아기 상어와의 거리
거리 : 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수
이동 : 8방향 대각선 가능

1. 모경수(prt, n=1)
1) bfs로 방문 탐색
2) 아기 상어 좌표 구함
3) 모든 상어 좌표에서 bfs 돌림
    1] 0인 곳을 최대값으로 넣어둠
    2] 현재 가려는 곳의 값 > 갱신값 -> 갱신
    3] 갱신이 되는 경우만 q에 넣음 -> 현재 갱신이 안되는 경우라면 앞으로도 안될거 같음
4) 방문한 곳을 다시 갈 수 있음

* n, m
공간 상태(0=빈칸, 1=아기상어)
출 : 안전거리 최대값

2. n^2
'''
from collections import deque

def bfs():
    while(q):
        # print(*graph, sep = '\n')
        # print()
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if(nx < 0 or ny < 0 or nx >= n or ny >= m):
                continue
            
            if(graph[nx][ny] > graph[x][y]+1):
                graph[nx][ny] = graph[x][y]+1
                q.append((nx, ny))
    
        
dx = [-1, 1, 0, 0, -1, -1, 1, 1]        
dy = [0, 0, -1, 1, -1, 1, 1, -1]
q = deque()
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


for i in range(n):
    for j in range(m):
        if(graph[i][j] == 0):
            graph[i][j] = 3000
            
        if(graph[i][j] == 1):
            q.append((i, j))
            graph[i][j] = 0

# print(graph)            
# print(q)
bfs()

max_dis = 0
for i in range(n):
    for j in range(m):
        if(graph[i][j] > max_dis):
            max_dis = graph[i][j]
            
print(max_dis)            