'''
n x m에 0 = 구멍 / 1 = 칸막이
연결 = 구멍 상하좌우 붙어있음

ex) 
3개

00110
00011
11111
00000

1. 모경수(prt, n=1)
1) bfs로 방문 탐색
2) 외부 for : 0이고 방문 안했으면 얼음 개수 ++
3) bfs : 0이고 방문안했으면 방문 ㄱㄱ

* n m 
얼음틀 0=구멍 / 1=칸막이
출 : 아이스크림 개수

2. logn
'''
from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))
    visit[i][j] = True
    
    while(q):
        i, j = q.popleft()
        
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            
            if(nx < 0 or ny < 0 or nx >= n or ny >= m):
                continue
            
            if(not visit[nx][ny] and graph[nx][ny] == 0):
                visit[nx][ny] = True
                q.append((nx, ny))
        
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if(not visit[i][j] and graph[i][j] == 0):
            print(*visit, sep = '\n')
            cnt += 1
            bfs(i, j)

print(cnt)            