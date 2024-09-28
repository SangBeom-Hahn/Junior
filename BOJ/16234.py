'''
nxn, 땅ㅇㄴ 1x1로 나누어져있고 각 땅에는 나라가 하나씩 있음
r행 c열에 있는 나라에는 행렬[r][c] 명이 살고 있음

인구이동 : 
1) 인구이동은 하루동안 아래와 같이 진행됨, 더이상 인구 이동이 없을때까지 일어난다
2) 국경선을 공유하는 두 나라의 인구 차이가 L명 이상 R명 이하라면 국경선을 염
3) 국경선이 열려있으면 그 나라를 연합이라고 함
4) 연합을 이루는 각 칸의 인구수는 연합의 총 인구수 / 각 칸읙 ㅐ수가 된다.
5) 연합을 해제하고 모든 국경선을 닫음

1. 모경수(prt, n=1)
1) bfs를 while문으로 여러번 돌려서 연합이 하나라도 있으면 flag를 true로 하고 true면 cnt셈
2) visit과 bfs로 연합끼리 visit함
3) 연합의 각 인구수를 수정해야하니깐 각 연합의 좌표를 bfs 돌면서 저장해야함

* N, L, R : nxn L명이상 R명이하
각 나라의 인구수

출 : 인구 이동이 며칠 동안 발생하는지 구하라
'''

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
from collections import deque

togetherFlag = False
def bfs(x, y):
    global togetherFlag, graph
    
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    cnt = 1
    cooldi = [(x, y)]
    hab = 0
    
    while(q):
        x, y = q.popleft()
        hab += graph[x][y]
    
        for i in range(4):
            # print(q)
            nx = x + dx[i]
            ny = y + dy[i]
            
            if(nx < 0 or ny < 0 or nx >= n or ny >= n):
                continue
            
            diff = abs(graph[x][y] - graph[nx][ny])
            # print(diff)
            if(not visit[nx][ny] and diff >= l and diff <= r):
                cnt += 1
                visit[nx][ny] = True
                togetherFlag = True
                q.append((nx, ny))
                cooldi.append((nx, ny))
            
    # print(cooldi)
    # print(cnt)
    # print(hab)
    
    for x, y in cooldi:
        graph[x][y] = hab // cnt
        
    # print(*graph, sep = '\n')
    

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * n for _ in range(n)]
tempVisit = [ele[:] for ele in visit]

su = 1
moveCnt = 0

while(True):
# while(su != 2):
    for i in range(n):
        for j in range(n):
            if(not visit[i][j]):
                bfs(i, j)
                
    if(togetherFlag == True):
        moveCnt += 1
        togetherFlag = False
        visit = [ele[:] for ele in tempVisit]
    else:
        print(moveCnt)
        break

    su += 1