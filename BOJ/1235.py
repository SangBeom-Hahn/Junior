'''
한수는 왼쪽 아래점에 있고 집은 오른쪽 위에 있다. 한수가 집에 가는 방법은 다양하다.
한번 지나친 곳은 다시 방문하지 않는다. 맵에 못하는 부분이 주어지고 거리가 주어질 때
한수가 집에 도착하는 경우 중 거리가 k인 가짓수를 구하라

1. 모경수
1) dfs로 방문 탐색
2) 한수 위치 = r-1, 0 / 집 = 0, c-1
3) dfs로 돌면서 cnt를 재귀로 주고 집이면 k와 비교함
4) 반환하면 방문한 곳을 f로 해야겠다.

* r, c, k : rxc 맵, 거리
출력 : 거리가 k인 가짓수
2. 시복 : n^3
'''

from collections import deque

def bfs(hansu_x, hansu_y, cnt):
    global result
    
    if(hansu_x == 0 and hansu_y == c-1):
        if(cnt == k):
            # print(*visit, sep = '\n')
            # print()
            result += 1
    
    visit[hansu_x][hansu_y] = True
    
    for i in range(4):
        nx = hansu_x + dx[i]
        ny = hansu_y + dy[i]
        
        if(nx < 0 or ny < 0 or nx >= r or ny >= c):
            continue
        
        if(not visit[nx][ny]):# 집 전
            bfs(nx, ny, cnt+1)
            
    visit[hansu_x][hansu_y] = False # 리턴할 때 f
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
r, c, k = map(int, input().split())
graph = [list(input()) for _ in range(r)]
visit = [[False] * c for _ in range(r)]
result = 0

for i in range(r):
    for j in range(c):
        if(graph[i][j] == 'T'):
            visit[i][j] = True

# print(*graph, sep='\n')

bfs(r-1, 0, 1)

print(result)