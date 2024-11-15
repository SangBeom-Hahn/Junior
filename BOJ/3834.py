'''
1. 모경수(prt, n=1)
1) bfs로 방문 탐색
2) 간선 그래프를 단방향으로 그림
3) bfs를 돌면서 갈 수 있으면 결과 그래프에 1 저장

*
n : 정점의 개수
인접행렬(1이면 x에서 y로 가는 간선이 존재함)
출 : x에서 y로 가는 길이가 양수인 길이가 양수인 경로가 있으면 1, 없으면 0


'''

from collections import deque
def bfs(start):
    q = deque()
    q.append(start)
    
    
    while(q):
        x = q.popleft()
        for ele in graph[x]:
            if(not visit[ele]):
                result[start][ele] = 1
                q.append(ele)
                visit[ele] = True

n = int(input())
result = [[0] * n for _ in range(n)]
input = [list(map(int, input().split())) for _ in range(n)]
graph = [[] for _ in range(n)]
visit = [False] * (n)

for i in range(n):
    for j in range(n):
        if(input[i][j] == 1):
            graph[i].append(j)
            
print(graph)

for i in range(n):
    bfs(i)
    visit = [False] * (n)
    
print(*result, sep = '\n')    