'''
연구소
1] n x m 크기
2] 새로 세울 수 있는 벽의 개수는 3개

바이러스
1] 상하좌우 인접한 빈칸으로 모두 퍼질 수 있다.

안전영역의 크기 : 벽을 3개 세운뒤 바이러스가 퍼진 뒤 0의 개수

1. 모경수(prt, n=1)
ok 3) tmp : 최초 바이러스 위치 담는 큐, 최초 지도 상태, visit
ok 4) 빈칸의 좌표들로 크기 3 조합을 만들고
5) 순회
    0) 벽을 세움
    1) bfs로 방문 탐색
        1] 2인 바이러스의 좌표를 전부 큐에 넣고 bfs를 돌리면 퍼진다.
    2) bfs 끝난 후 지도의 0의 개수를 세면 안전영역의 크기를 구할 수 있음
    3) 최대 안전영역 크기 갱신

* n, m
지도의 상태(0=빈칸, 1=벽, 2=바이러스)
출 : 안전 영역의 최대 크기

2. n^3
'''
from collections import deque
from itertools import combinations

n, m = map(int, input().split())
tmp_graph = [list(map(int, input().split())) for _ in range(n)]
tmp_visit = [[False] * m for _ in range(n)]

tmp_q = deque()
blank_loc = []

for i in range(n):
    for j in range(m):
        if(tmp_graph[i][j] == 2):
            tmp_q.append((i, j))
        if(tmp_graph[i][j] == 0):
            blank_loc.append((i, j))
            
# print(tmp_q)            
# print(blank_loc)

# 5) 순회
 #     ok 0) 벽을 세움
 #     ok 1) bfs로 방문 탐색
#         ok 1] 2인 바이러스의 좌표를 전부 큐에 넣고 bfs를 돌리면 퍼진다.
#     2) bfs 끝난 후 지도의 0의 개수를 세면 안전영역의 크기를 구할 수 있음
#     3) 최대 안전영역 크기 갱신

from copy import deepcopy
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deepcopy(tmp_q)
    
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if(nx < 0 or ny < 0 or nx >= n or ny >= m):
                continue
            
            if(not visit[nx][ny] and graph[nx][ny] == 0):
                visit[nx][ny] = True
                graph[nx][ny] = 2
                q.append((nx, ny))
            
result = 0
for comb in list(combinations(blank_loc, 3)):
# for comb in [[[0, 1], [1, 0], [3, 5]], [[0, 1], [0, 1], [0, 1]]]:
    graph = [ele[:] for ele in tmp_graph]
    visit = [ele[:] for ele in tmp_visit]
    
    # 벽을 세움
    for x, y in comb:
        graph[x][y] = 1
        
    bfs()
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if(graph[i][j] == 0):
                cnt += 1
                
    if(result < cnt):
        result = cnt
        
print(result)        