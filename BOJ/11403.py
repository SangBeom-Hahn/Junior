'''
모든 정점 i,j에 대해서 i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 구해라

1. 모경수
1) bfs로 방문 탐색

* n : 정점의 개수
인접 그래프의 인접 행렬 상태
출력 : 경로가 존재하면 1, 없으면 0인 인접행렬 형태로 출력

2. nlogn
'''
from collections import deque

def bfs(start):
    global resultGraph
    
    visit = [False] * len(resultGraph)
    q = deque()
    q.append(start)
    
    while(q):
        x = q.popleft()
        resultGraph[start][x] += 1
        
        for i in realGraph[x]:
            if(not visit[i]):
                q.append(i)
                visit[i] = True
    
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
realGraph = [[] for _ in range(n)]
resultGraph = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if(graph[i][j] == 1):
            realGraph[i].append(j)
            
print(realGraph)

# 모든 노드를 출발 노드로 bfs ㄱㄱ
for i in range(n):
    bfs(i)
    
for i in range(n):
    resultGraph[i][i] -= 1    
    
print(*resultGraph, sep = '\n')    