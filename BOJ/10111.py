'''
지도에 0 = 이동가능, 1=불가능
벽 k개 부수기 가능

1. 모경수(prt, n=1)
1) bfs로 방문 탐색
2) 벽 부수기
    1] z축 0 = 아직 안 부숨, 1 = 1번 부숨, 3 = 2번 부숨
    2] 벽이면
        1] 벽 부수기를 k번 미만이면 부수고 이동
        2] k번 이상이면 현재 부순 횟수로 이동
    
    3] 아니면
        1] 원래 z 축으로 이동

* n, m, k
지도 상태
출  최단거리(불가하면 -1)

2. nlogn
'''
from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y, 0))
    dis[x][y][0] = 1
    
    while(q):
        x, y, z = q.popleft()
        print(q)
        print(*dis, sep = '\n')
        print()
        if(x == n-1 and y == m-1):
            return dis[x][y][z] - 1
        
        # 벽
        if(graph[x][y] == 1):
            if(z < k):
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if(nx < 0 or ny < 0 or nx >= n or ny >= m):
                        continue
                    
                    if(dis[nx][ny][z+1] == 0): # 아직 안 부순 곳이라면
                        dis[nx][ny][z+1] = dis[x][y][z] + 1
                        q.append((nx, ny, z+1))
            else:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if(nx < 0 or ny < 0 or nx >= n or ny >= m):
                        continue
                    
                    if(dis[nx][ny][z] == 0): # 아직 안 부순 곳이라면
                        dis[nx][ny][z] = dis[x][y][z] + 1
                        q.append((nx, ny, z))
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if(nx < 0 or ny < 0 or nx >= n or ny >= m):
                    continue
                
                if(dis[nx][ny][z] == 0): # 아직 안 부순 곳이라면
                    dis[nx][ny][z] = dis[x][y][z] + 1
                    q.append((nx, ny, z))
    return -1
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m, k = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
dis = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]

print(*dis, sep = '\n')

print(bfs(0, 0))