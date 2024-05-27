'''
총 F 층이고, 스타트 링크는 G층에 있음, 강호의 현 위치는 S고 G층으로 갈 거다. 
엘베 : U버튼 = 위로 U층 가는 버튼
: D버튼 = 아래로 D층 가는거

1. 모경수(prt, n=1)
1) bfs로 방문 탐색

* F, S, G, U, D
출 : 강호가 G층에 가려면 버튼을 적어도 몇 번 눌러야 하는지 구하라, 만약 못가면 못감 출력
2. 시복 : nlogn
'''

def bfs(s):
    dis[s] = 0
    q = deque()
    q.append(s)
    
    while(q):
        x = q.popleft()
        
        if(x == g):
            return dis[x]
        for i in range(2):
            nx = x + dx[i]
            
            if(nx <= 0 or nx > f):
                continue
            
            if(dis[nx] == -1):
                dis[nx] = dis[x] + 1
                q.append(nx)
    return "use the stairs"

f, s, g, u, d = map(int, input().split())
dx = [-1 * d, u]
from collections import deque

dis = [-1] * (f+1)

print(bfs(s))