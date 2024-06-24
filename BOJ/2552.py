'''
n번까지 도시와 m개의 단방향 도로가 있다. 모든 도로 거리는 1이다.
x에서 출발하여 도달할 수 있는 도시 중 최단 거리가 k인 모든 도시 번호 출력

1. 모경수
1) bfs로 방문 탐색

n, m, k, x
m 개의 상태
출 : 오름차순
'''

from collections import deque

def bfs(x):
    q = deque()
    q.append(x)
    visit[x] = 0
    
    while(q):
        print(visit)
        i = q.popleft()
        for ele in graph[i]:
            if(visit[ele] == -1):
                q.append(ele)
                visit[ele] = visit[i] + 1

n, m, k, p = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [-1] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    
bfs(p)
    
# print(visit)    

for i, ele in enumerate(visit):
    if(ele == k):
        print(i)