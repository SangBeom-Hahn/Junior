'''
청소하는 영역의 개수를 구하라
방은 nxm이며 각 칸은 벽또는 비었다. 청소기는 바라보는 방향이 있다. 
동작 : 
1. 현재 칸이 청소 안됐으면 청소한다.
2. 주변 네 칸을 다 청소한 경우
    1) 바라보는 방향을 유지하고 한칸 후진하고 1.로 감(당연히 한칸 후진은 청소한 칸임)
    2) 뒤칸이 벽이면 stop
    
3. 4칸 중 청소하지 않은 칸이 있으면
    1) 청소하지 않은 칸으로 전진, 1로 감    

1. 모경수(prt, n=1)
1) 입력
2) while로 계속 체크하는데 현재 칸이 1이면 stop
3) 현재 칸이 청소 안됐으면 청소한다.
4) 4 방향을 봄
    1] 4칸 중 청소하지 않은 칸이 있으면 전진하고 청소하고 다시 4방향 봄
    2] 4칸이 다 청소됐으면 = for문 4번을 다 돌았으면 원래 처음 방향에서 후진함 
        현상태 벽인지 체크하고 다시 4방향 보고 순회함

* n, m 
r, c, d : 청소기의 좌표와 방향 0=북,1=동,2=남,3=서
각 장소의 상태 (0=청소 안한칸, 1=벽)
출력 : 청소하는 칸의 개수
2. 시복: n^2
'''

n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# print(*graph, sep = '\n')
print(*visit, sep = '\n')

# 2) while로 계속 체크하는데 현재 칸이 1이면 stop
while(True):
# su = 1
# while(su != 6):
    if(graph[x][y] == 1):
        print("벽이다")
        break
    
    # 3) 현재 칸이 청소 안됐으면 청소한다.
    if(not visit[x][y]):
        cnt += 1
        visit[x][y] = True
        
    print(*visit, sep = '\n')
        
        
    # 4 방향을 봄
    #     1] 4칸 중 청소하지 않은 칸이 있으면 전진하고 청소하고 다시 4방향 봄
    #     2] 4칸이 다 청소됐으면 = for문 4번을 다 돌았으면 원래 처음 방향에서 후진함 
    #         현상태 벽인지 체크하고 다시 4방향 보고 순회함

    nd = d
    for _ in range(4):
        nd = (nd-1+4) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        
        if(nx < 0 or ny < 0 or nx >= n or ny >= m):
            continue
        
        print(x, y, nd, "cnt = ", cnt)  # 0=북,1=동,2=남,3=서
        # 방문 안했고 빈칸이면
        if(not visit[nx][ny] and graph[nx][ny] == 0):
            x = nx
            y = ny
            d = nd
            break
            
    else: # 4칸 다 청소했으면
        x = x + dx[(d+2) % 4]
        y = y + dy[(d+2) % 4]
        
        print("뒤로가기", x, y, d, "cnt = ", cnt)
    
    
    # su += 1