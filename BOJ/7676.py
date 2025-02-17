from collections import deque

def bfs(x, y, maps):
    n  = len(maps)
    m = len(maps[0])
    
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    
    while(q):
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if(nx < 0 or ny < 0 or nx >= n or ny >= m):
                continue
                
            if(not visit[nx][ny] and maps[nx][ny] == 1):
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
                visit[nx][ny] = True

def solution(maps):
    global visit, dx, dy
    
    n = len(maps)
    m = len(maps[0])
    visit = [[False] * m for _ in range(n)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    bfs(0, 0, maps)
    
    # print(n, m)
    result = maps[n-1][m-1]
    if(result == 1):
        return -1
    else:
        return result