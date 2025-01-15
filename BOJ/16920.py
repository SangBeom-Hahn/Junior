'''
n x m 빈칸, 막힌칸

플레이어
1) 하나 이상의 성
2) 각 라운드 : 자기 턴이 올때마다 성 확장 / 플레이어 1 ~ n 확장
3) 확장
1] 자신의 성을 빈칸으로 확장
2] 플레이어 i는 자신의 성에서 si칸 만큼 이동할 수 있는 모든 칸에 성 '동시'에 만듬
3] 벽이나 다른 플레이어 성 불가

4) 모든 플레이어가 더 이상 확장할 수 없을때 겜 끝

ex)
1 1
1..1
....
....
...2

1111
1..1
...2
..22

1111
1111
1.22
.222

---


2 1
1 . . 1
. . . .
. . . .
. . . 2

1 1 1 1
1 1 . 1
1 . . 1
. . 2 2

1 1 1 1
1 1 . 1
1 . . 1
. . 2 2

---

2 1
1..1
#.##
....
...2

1111
#1##
...2
..22

1. 모경수(prt, n=1)
1) while 모든 성이 더 이상 확장 못할때까지 반복 (확장 가능 flag 시작은 False)
2) 2중 for로 방문하지 않은 번호의 좌표로 bfs(떨어져있는 같은 번호의 성도 한번에 bfs를 할거기 때문)
3) bfs로 방문 탐색
    1] 2중 for로 현재 좌표와 동일 좌표를 모두 큐에 넣음
    2] bfs 돌면서 모두 방문 처리
    3] 큐에 좌표, s 넣어서
        1] 한번 큐에 넣을때마다 s-1함
        2] s가 0보다 크면 계속 큐에 넣음 0이면 큐에 안넣음
    4] 한번이라도 큐에 넣으면 확장 가능 flag True
4) 확장 가능 flag가 False면 끝

* n m p : n m 플레이어수
s1 ,,, sp
게임판 상태(. = 빈칸, # = 벽, 1 ~ 9는 각 플레이어의 성)
출 : 플레이어 1 ,,, p가 가진 성의 수

2. nlogn
'''
from collections import deque

def bfs(x, y):
    global flag
    
    q = deque()
    s = dis[int(graph[x][y])]
    for i in range(n):
        for j in range(m):
            if(graph[i][j] == graph[x][y]):
                visit[i][j] = True
                q.append((i, j, s))
                
    while(q):
        x, y, s = q.popleft()
        
        if(s > 0):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if(nx < 0 or ny < 0 or nx >= n or ny >= m):
                    continue
                
                if(not visit[nx][ny] and graph[nx][ny] == '.'):
                    visit[nx][ny] = True
                    graph[nx][ny] = graph[x][y]
                    q.append((nx, ny, s-1))
                    flag = True
    # print(*graph, sep = '\n')
    # print()
    
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m, p = map(int, input().split())
dis = [0] + list(map(int, input().split()))
graph = [list(input()) for _ in range(n)]


# print(dis)

su = 1

while(True):
    flag = False
    visit = [[False] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if(not visit[i][j] and graph[i][j] != '.' and graph[i][j] != '#'):
                bfs(i, j)
    # print(flag)
    
    if(flag == False):
        break
    su += 1
    
for value in range(1, p+1):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if(graph[i][j] == str(value)):
                cnt += 1
    print(cnt, end = ' ')