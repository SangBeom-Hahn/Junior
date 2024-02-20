'''
어떤 지역의 높이 정보를 파악한다. 그 지역에 많음ㄴ 비가 내렸을 때 물에 잠기지 않는
안전한 여역이 최대로 몇개가 만들어지는지 조사하려고 한다. 비의 양에 따라
일정한 높이 이하의 모든 지점은 물에 잠긴다. 비의 양에 따라 안전한 영역의 개수가 다르게 된다.
내리는 비의 양에 따른 모든 경우를 다 조사해 물에 잠기지 않는 안전 여역 개수 중 최대 개수
를 구하라

1. 모경수
1) bfs로 방문 탐색
2) 비의 양을 1~최대 높이로 내리게 해서 모든 경우의 안전 영역을 구해라

* n 
높이 정보
출력 : 안전 영역 최대 개수

2. 시복 : nlogn
'''
from collections import deque
def bfs(i, j):
    q = deque()
    q.append((i, j))
    visit[i][j] = True
    
    while(q):
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if(nx < 0 or ny < 0 or nx >= n or ny >= n):
                continue
            
            if(not visit[nx][ny]):
                q.append((nx, ny))
                visit[nx][ny] = True

dx = [-1, 1, 0, 0]        
dy = [0, 0, -1, 1]

n = int(input())
areas = [list(map(int, input().split())) for _ in range(n)]

max_height = 0
# 최대 높이 구하기
for i in range(n):
    for j in range(n):
        if(areas[i][j] > max_height):
            max_height = areas[i][j]
            
# print(max_height)            
max_cnt = 0
# 비의 양을 1~최대 높이로 내리게 해서 모든 경우의 안전 영역을 구해라
for rain_height in range(1, max_height+1):
    visit = [[False] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if(areas[i][j] <= rain_height):
                visit[i][j] = True
    # bfs
    cnt = 0
    for i in range(n):
        for j in range(n):
            if(not visit[i][j] and areas[i][j] > rain_height):
                cnt += 1
                bfs(i, j)
                
    max_cnt= max(max_cnt, cnt)
    
    # print(cnt)
print(max_cnt)
    