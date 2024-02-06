'''
수빈이는 현재 점 n에 있고 동생은 k에 있다. 수빈이는 걸으면 1초 후에 x-1, x+1로 이동하게 되고,
순간이동을 하는 경우네느 0초 후에 2*x로 이동한다. 

1. 모경수
1) bfs로 방문 탐색

* n, k : 수빈, 동생 위치
출력 : 동생을 찾는 가장 빠른 시간

2. 시복 : nlogn
'''
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    dis[start] = 0
    
    while(q):
        x = q.popleft()
        if(x == k):
            print(dis[x])
            break
        
        # 0초 먼저
        
        if(2*x > 100000):
            pass
        else:
            if(dis[2*x] > dis[x]):
                dis[2*x] = dis[x]
                q.append(2*x)
        
        # 걷기    
        for i in [-1, 1]:
            nx = x + i
            if(nx < 0 or nx > 100000):
                continue
            
            if(dis[nx] > dis[x]+1):
                dis[nx] = dis[x]+1
                q.append(nx)

n, k = map(int, input().split())
dis = [100001] * 100001

bfs(n)