'''
걷기 : 1초뒤 +1, -1
순간이동 : 1초 뒤 2 * x

1. 모경수(prt, n=1)
1) bfs로 방문 탐색
2) 첫 방문이 = 가장 빠른 방법, 
3) dis[k]가 -1이 아닌 데 dis[x] + 1과 dis[k]가 같다면 cnt+1

* n, k : 수빈점, 동생점
출 : 가장 빠른 시간이 몇 초 후인지, 그 방법이 몇가지인지
2.시복 : nlogn
'''
from collections import deque

def bfs(n):
    global cnt
    
    q = deque()
    q.append(n)
    dis[n] = 0
    
    while(q):
        x = q.popleft()
        if(x == k):
            # 큐에 넣는 조건이 -1이거나 같을 때만 넣을 거라서 x == k를 만족했다면 이건 거리는 무조건 같은 경우임
            cnt += 1
            
        dx[2] = x
        for i in range(3):
            nx = x + dx[i]
            
            if(nx < 0 or nx > 100000):
                continue
            
            if(dis[nx] == -1 or dis[nx] == dis[x]+1):
                dis[nx] = dis[x]+1
                q.append(nx)
            
cnt = 0
dx = [-1, 1, 0]
n, k = map(int, input().split())
dis = [-1] * 100001
bfs(n)

print(dis[k])
print(cnt)