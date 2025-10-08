'''
n x m 미로에 괴물이 있어 피해서 탈출해야한다.
(1, 1)에서 시작, 출구는 (n, m). 인덱스는 1부터 시작

미로 탈출
1] 한 번에 한 칸씩 이동
2] 괴물 = 0, 괴물이 없는 = 1


ex) 

101010
111111
000001
111111
111111

1. 모경수(prt, n=1)
1) dfs로 방문 탐색
    1] graph, visit이 필요
    2] 상하좌우로 방문
    3] 최소값 체크가 중요



* n, m : 미로 n x m
미로의 정보
출 : 탈출하기 위해 움직여야 하는 최소 칸의 개수

2. nlogn
'''

def dfs(x, y, cnt):
    global min_cnt
    visit[x][y] = True
    
    if(x == n-1 and y == m-1):
        print(cnt)
        
        if(min_cnt > cnt):
            min_cnt = cnt
        
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if(nx < 0 or ny < 0 or nx >= n or ny >= m):
            continue
        
        if(not visit[nx][ny] and graph[nx][ny] == 1):
            dfs(nx, ny, cnt+1)
    
    

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
min_cnt = 50000

dfs(0, 0, 1)

print(min_cnt)