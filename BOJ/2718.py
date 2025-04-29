'''
n x n에 여러 섬
가장 짧은 다리를 놓아 두 대륙을 연결할 거다.

-> 시나리오
ok 1) 모든 대륙을 전부 다 봐서 다른 대륙으로 만드는 다리 중 가장 짧은 것을 찾아야 할 듯
ok 2) 한개의 대륙을 전부 다 큐에 넣고 bfs를 돌림
3) 자기땅을 만나면 안됨
    1] 방문한 1은 안됨

4) 바다를 만난 후 땅을 만나야 함
    1] 방문 x한 1을 만나면 길이 갱신
5) 큐 : 좌표, 갯수
6) 방문 조건 : 방문 x, 지도 0이면
7) 종료 : 방문 x, 지도 1이면 길이 갱신 / 최초로 다른 땅 만난게 이 대륙에서의 최소 길이겠다.

1. 모경수(prt, n=1)
ok 1) 2중 for bfs로 각 대륙에 번호를 붙임 1, 2, 3, ,,,
2) 1중 for로 그 대륙 번호를 순회
    1] 그 번호에 해당하는 대륙을 전부 큐에 넣음 = 1개의 대륙을 다 찾은거임
        1] 방문처리도 함
    
2) 그 찾은 대륙으로 bfs를 한 번에 돌림
    1] 큐 : 좌표, 갯수
    2] 방문 조건 : 방문 x
    3] 종료 : 지도가 0이 아니면 길이 갱신 -> 길이는 전역변수
    
3) 모든 대륙을 다 봐서 전역변수 갱신
4) 1개의 대륙이 끝날때마다 visit 갱신

* n
지도(0 = 바다, 1 = 육지)
출 : 가장 짧은 다리의 길이

2. n^2
'''

from collections import deque

# 대륙 번호 붙이기 bfs
def bfs(x, y, num):
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    graph[x][y] = num
    
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if(nx < 0 or ny < 0 or nx >= n or ny >= n):
                continue
            
            if(not visit[nx][ny] and graph[nx][ny] == 1):
                visit[nx][ny] = True
                graph[nx][ny] = num
                q.append((nx, ny))
    
    
# 거리 찾기 bfs

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

num = 1
for i in range(n):
    for j in range(n):
        if(not visit[i][j] and graph[i][j] == 1):
            bfs(i, j, num)
            num += 1
            
# print("최초 지도")
# print(*graph, sep = '\n')

result = 20000

def bfs_leng(q, number):
    global result
    
    while(q):
        # print(q)
        x, y, cnt = q.popleft()
        if(graph[x][y] != number and graph[x][y] != 0): # 다른 나라
            if(result > cnt):
                result = cnt-1
                return
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if(nx < 0 or ny < 0 or nx >= n or ny >= n):
                continue
            
            # print(nx, ny, visit[nx][ny])
            if(not visit[nx][ny]):
                q.append((nx, ny, cnt + 1))
                visit[nx][ny] = True
        
# 2) 1중 for로 그 대륙 번호를 순회
#     1] 그 번호에 해당하는 대륙을 전부 큐에 넣음 = 1개의 대륙을 다 찾은거임
#         1] 방문처리도 함
for number in range(1, num):
# for number in range(1, 2):
    visit = [[False] * n for _ in range(n)]
    q = deque()
    
    for i in range(n):
        for j in range(n):
            if(graph[i][j] == number):
                q.append((i, j, 0)) # 좌표, cnt
                visit[i][j] = True   

# 2) 그 찾은 대륙으로 bfs를 한 번에 돌림
#     1] 큐 : 좌표, 갯수
#     2] 방문 조건 : 방문 x
#     3] 종료 : 지도가 0이 아니면 길이 갱신 -> 길이는 전역변수
    # print(*visit, sep = '\n')
    bfs_leng(q, number)
    # print("대륙 번호", number, "최소 길이", result)

print(result)
    
# 3) 모든 대륙을 다 봐서 전역변수 갱신
# 4) 1개의 대륙이 끝날때마다 visit 갱신














