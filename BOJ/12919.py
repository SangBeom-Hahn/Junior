'''
맵 0 = 이동가능, 1 = 이동불가
이동 : 상하좌우 + 머무르기
낮밤 : 
1) 시작은 낮
2) 한번 이동할때마다 낮밤이 바뀜

부수기 : 
1) k개까지 부수기 가능
2) 낮에만 부수기 가능 = 부수기 횟수가 k 미만인데 벽 만나면 머무르고 다음날 부수기 해야함

ex) 
k = 1
0100 0행0열일때 낮이라서 0행1열 부수고 갔지
0110 1행0열일때 밤이라서 2행 못 부수는데 0행1열로 돌아가는 것보다 하루 기다리고 부수기
1000
0000
0111
0000

1.모경수(prt, n=1)
1) bfs로 방문 탐색
2) z가 k 미만이면 벽 부숨
    1] 벽이면
        1] 낮이면 부숨
        2] 밤이면 하루 기다림, 이것도 dis에 +1 해야함
            1] 근데 기존에 nx ny에 dis+1하는 건 방문 처리를 하고 가서 다른 것들엔
            영향을 안줌, 근데 이번엔 방문한 곳이라도 dis+1을 하는 것이라서 다른거에
            영향을 줌
            2] 그래서 dis는 방문 처리 용으로만하고 거리를 큐에 넣어야 함
    2] 벽 아니면 걍 bfs
3) z가 k이면 -> 벽 아닌 곳만 가능

* n, m k
맵 상태
출 : 최단 거리

2. nlogn
'''
from collections import deque

def bfs():
    q = deque()
    q.append((0, 0, 0, 1)) # x y z 거리 낮밤(0=낮,1=밤)
    visit[0][0][0] = 1 # 방문 처리 용도
    
    while(q):
        x, y, z, d = q.popleft()
        if(x == n-1 and y == m-1):
            return d
        
        
        sky = d % 2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if(nx < 0 or ny < 0 or nx >= n or ny >= m):
                continue
            
            if(graph[nx][ny] == 0 and visit[nx][ny][z] == 0):
                q.append((nx, ny, z, d+1))
                visit[nx][ny][z] = 1
                    
        #         1] 벽이면
        # 1] 낮이면 부숨
        # 2] 밤이면 하루 기다림, 이것도 dis에 +1 해야함
        #     1] 근데 기존에 nx ny에 dis+1하는 건 방문 처리를 하고 가서 다른 것들엔
        #     영향을 안줌, 근데 이번엔 방문한 곳이라도 dis+1을 하는 것이라서 다른거에
        #     영향을 줌
        #     2] 그래서 dis는 방문 처리 용으로만하고 거리를 큐에 넣어야 함

            if(graph[nx][ny] == 1 and z < k and visit[nx][ny][z+1] == 0):
                if(sky):
                    
                    q.append((nx, ny, z+1, d+1))
                    visit[nx][ny][z+1] = 1
                    
                else: # 밤이면
                    q.append((x, y, z, d+1))
                    
    return -1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visit = [[[0] * (k+1) for _ in range(m)] for _ in range(n)]

print(bfs())