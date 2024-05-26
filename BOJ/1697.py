'''
수빈이는 n, 동생은 k 
수빈이는 걷거나 순간이동 가능, 수빈이 위치 x 일 떄
    걷기 : 1초 후 x-1, x+1로 이동
    순간이동 : 1초 후 2*x로 이동
    
수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후이냐    

1. 모경수(prt, n=1)
1) bfs로 방문 탐색

* n, k : 수빈 동생 위치
출 : 가장 빠른 시간
2. 시복 : nlogn
'''

from collections import deque
def bfs(n):
    q = deque()
    q.append(n)
    dis[n] = 0
    
    while(q):
        print(dis[:20])
        print(q)
        x = q.popleft()
        if(x == k):
            return dis[x]
        
        dx[2] = x
        for i in range(3):
            nx = x + dx[i]
            
            if(nx < 0 or nx > 100000):
                continue
            
            if(dis[nx] == -1):
                q.append(nx)
                dis[nx] = dis[x] + 1

n, k = map(int, input().split())
dis = [-1] * 1000001

dx = [-1, 1, 0]

print(bfs(n))
