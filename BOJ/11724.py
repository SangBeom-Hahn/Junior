'''
방향 없는 그래프에서 연결 요소 개수를 구해라

1. 모경수(prt, n=1)
1) bfs로 방문 탐색

* n, m : 정점의 개수, 간선의 개수
간선
출력 : 연결요소 개수

2. 시복 : n^2
'''
from collections import deque

def bfs(n):
    
    q = deque()
    q.append(n)
    visit[n] = True
    
    while(q):
        x = q.popleft()
        for ele in graph[x]:
            if(not visit[ele]):
                q.append(ele)
                visit[ele] = True

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
print(graph)
cnt = 0
for i in range(1, n+1):
    if(not visit[i]):
        cnt += 1
        bfs(i)
print(cnt)