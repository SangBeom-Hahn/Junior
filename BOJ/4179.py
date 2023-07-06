from collections import deque

def bfs():
    global flag
    
    while(q):
        x, y, time = q.popleft()
        
        if(graph[x][y] == 'F'):
        
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
            
                if(nx < 0 or ny < 0 or nx >= n or ny >= m):
                    continue
                
                if(graph[nx][ny] != '#' and not visitedF[nx][ny]):
                    q.append((nx, ny, 0))
                    graph[nx][ny] = 'F'
                    visitedF[nx][ny] = True
                    
        elif(graph[x][y] == 'J'):
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if(nx < 0 or ny < 0 or nx >= n or ny >= m):
                    flag = True
                    return time
                    # 성공
                
                if(graph[nx][ny] == '.' and not visitedJ[nx][ny]):
                    # print(q)
                    # print(1, x, y, nx, ny)
                    q.append((nx, ny, time + 1))
                    visitedJ[nx][ny] = True
                    graph[nx][ny] = 'J'
                    

n, m = map(int, input().split())
graph = [list(input()) for i in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
flag = False

visitedJ = [[False] * m for i in range(n)] 
visitedF = [[False] * m for i in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if(graph[i][j] == 'J'):
            q.append((i, j, 0))
            visitedJ[i][j] = True
            
for i in range(n):
    for j in range(m):
        if(graph[i][j] == 'F'):
            q.append((i, j, 0))
            visitedF[i][j] = True
time = bfs()    

if(flag):
    print(time + 1)
else:
    print("IMPOSSIBLE")