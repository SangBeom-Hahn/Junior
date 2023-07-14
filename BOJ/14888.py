'''
1. 모든 경우의 수
1) bfs로 방문 탐색

* 체스판의 한 변의 길이
나이트의 현재 위치
나이트가 이동하려는 칸
'''
from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    distance[x][y] = 0
    
    while(q):
        x, y = q.popleft()
        if(x == tarX and y == tarY):
            print(distance[x][y])
            return
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if(nx < 0 or ny < 0 or nx >= l or ny >= l):
                continue
            
            if(distance[nx][ny] == -1):
                q.append((nx, ny))
                distance[nx][ny] = distance[x][y] + 1

t = int(input())
dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]

for _ in range(t):
    l = int(input())
    x, y = map(int, input().split())
    tarX, tarY = map(int, input().split())
    distance = [[-1] * l for _ in range(l)]

    bfs(x, y)