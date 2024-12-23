'''
n명이 친구 1 ~`n번
에어드롭
1] 휴대폰 간 버전 차이가 t 이하인 경우 and 거리 차 K 이하
2] 간접 경로가 있으면 버전, 거리가 멀어도 받을 수 있다.

ex) 거리 4, 버전 3

1. 모경수(prt, n=1)
1) bfs로 방문 탐색
2) 방문하지 않고, 거리가 가까우면 큐 삽입
3) 버전이 같고, p=1이면 받을 수 있음

4) 오름차순 출력


* n, k, t : 친구수, 최대거리, 버전차이
x, y, v, 푸앙이 좌표와 버전
n개의 좌표와 버전과 p(0 = 사진 안찍음, 1 = 찍음)
출 : 푸앙이가 받을 수 있는 사진을 가진 친구들 번호 오름차순(없다면 0)

2. n^2
'''
from collections import deque
result = []

def bfs(p_x, p_y, p_v):
    global result
    
    q = deque()
    q.append((p_x, p_y, p_v, 0))
    
    while(q):
        x, y, v, p = q.popleft()
        
        for i in range(n):
            f_x, f_y, f_v, f_p = graph[i]
            dis = abs(x-f_x) +abs(y-f_y)
            v_diff = abs(v-f_v)
            
            if(not visit[i] and dis <= k):
                if(v_diff <= t and f_p == 1):
                    result.append(i+1)
                
                q.append((f_x, f_y, f_v, f_p))
                visit[i] = True
    

n, k, t = map(int, input().split())
p_x, p_y, p_v = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visit = [False] * n

bfs(p_x, p_y, p_v)

if(len(result)):
    result.sort()
    print(*result)
else:print(0)