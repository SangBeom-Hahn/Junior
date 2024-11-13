'''
nxn에 물고기 m마리, 상어 1마리, 물고기와 상어(2)는 크기를 가지고 있음
규칙
1) 물고기와 상어(2)는 크기를 가지고 있음
2) 상어는 1초에 상하좌우 인접한 한칸씩 이동
3) 이동 : 자신보다 크기가 큰 물고기가 있는 칸은 갈 수 없음 = 작고 같은 칸만 가능
4) 먹기 : 작은 물고기만 먹기 가능, 같은 물고기는 이동O, 먹기 X
5) 이동은 1초가 걸림
(하는중)
6) 물고기 먹으면 그 칸은 빈칸이 됨
7) 자신의 크기와 같은 수의 물고기를 먹으면 크기 1증가 ex) 크기 2 = 2마리 먹으면 3됨

어디로 이동?
1) 먹을 수 있는 물고기가 없다면 (크기가 작은게 없다면) 엄마 호출
2) 먹을 수 있는게 1마리면, 그 물고기 먹으러 이동
3) 1마리 이상 (거리가 가까운 곳으로 이동, 행, 열 오름차순해서 idx 0 물고기 먹으러 이동)

1. 모경수(prt, n=1)
1) bfs로 방문 탐색
    1] 이동한 할때마다 bfs 호출해야함
    2] 시작 위치가 수정되고 while bfs 반복 호출 -> falg를 둬서 게임 종료 아닐동안 ㄱㄱ
    3] bfs 재호출전에 visit 초기화
    4] 큐에 넣기 조건
        1] 방문x, 크기가 작거나 같으면
        
    5] 먹기 조건
        1] graph 값이 0이 아니고 크기가 작으면 먹음
        2] can_eat 배열에 (거리, x, y) 넣음
2) bfs 끝나고
    1] can_eat 길이
        1] 0 : 그때의 time이 결과, while bfs 반복 호출을 종료 해야함 flag 두자
        2] 1 : 그때의 거리를 time에 더함, 그 위치에 그래프 0으로 저장
        3] 2 이상 : 거리, 행, 열 오름차순해서 idx 0으로 이동
        4] 최초 시간은 0
    2] 현재 먹은 물고기 수를 계속 체크해서 자신의 크기만큼 먹으면 크기 1증가 + 현재 먹은
    물고기수 다시 0

* n : 공간크기
공간상태(0 = 빈칸, 1-6 = 칸에 있는 물고기 크기, 9 = 아기 상어 위치)
출 : 크기가 작은게 없지 않을 동안 물고기를 잡아 먹을 수 있는 시간

2. n^3
'''

# 1) bfs로 방문 탐색
#     1] 이동한 할때마다 bfs 호출해야함
#     2] 시작 위치가 수정되고 while bfs 반복 호출 -> falg를 둬서 게임 종료 아닐동안 ㄱㄱ
#     3] bfs 재호출전에 visit 초기화
#     4] 큐에 넣기 조건
#         1] 방문x, 크기가 작거나 같으면
        
#     5] 먹기 조건
#         1] graph 값이 0이 아니고 크기가 작으면 먹음
#         2] can_eat 배열에 (거리, x, y) 넣음
from collections import deque
def bfs(start_x, start_y):
    
    global game_over, time, shark_size, eat_cnt
    # print(start_x, start_y)
    
    q = deque()
    q.append((start_x, start_y, 0))
    visit[start_x][start_y] = True
    eat_fishs = []
    
    while(q):
        x, y, dis = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if(nx < 0 or ny < 0 or nx >= n or ny >= n):
                continue
            
            if(not visit[nx][ny] and shark_size >= graph[nx][ny]):
                q.append((nx, ny, dis+1))
                visit[nx][ny] = True
                
                if(graph[nx][ny] != 0 and shark_size > graph[nx][ny]):
                    eat_fishs.append((dis+1, nx, ny))
# 2) bfs 끝나고
#     1] can_eat 길이
#         1] 0 : 그때의 time이 결과, while bfs 반복 호출을 종료 해야함 flag 두자
#         2] 1 : 그때의 거리를 time에 더함, 그 위치에 그래프 0으로 저장
#         3] 2 이상 : 거리, 행, 열 오름차순해서 idx 0으로 이동
#         4] 최초 시간은 0
#     2] 현재 먹은 물고기 수를 계속 체크해서 자신의 크기만큼 먹으면 크기 1증가 + 현재 먹은
#     물고기수 다시 0
    
    if(len(eat_fishs) == 0):
        game_over = True
        return start_x, start_y
    elif(len(eat_fishs) == 1):
        dis = eat_fishs[0][0]
        x = eat_fishs[0][1]
        y = eat_fishs[0][2]
        
        time += dis
        graph[x][y] = 0
    else:
        eat_fishs.sort(key = lambda x: (x[0], x[1], x[2]))
        dis = eat_fishs[0][0]
        x = eat_fishs[0][1]
        y = eat_fishs[0][2]
        time += dis
        graph[x][y] = 0
    # print(eat_fishs)
    eat_cnt += 1
    if(eat_cnt == shark_size):
        shark_size += 1
        eat_cnt = 0
    
    return x, y
        
eat_cnt               = 0
shark_size = 2    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * n for _ in range(n)]
game_over = False
time = 0
start_x = 0
start_y = 0

for i in range(n):
    for j in range(n):
        if(graph[i][j] == 9):
            start_x = i
            start_y = j
            graph[i][j] = 0

while(game_over == False):
    start_x, start_y = bfs(start_x, start_y)
    visit = [[False] * n for _ in range(n)]
    
    # break
print(time)