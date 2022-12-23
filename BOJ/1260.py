'''
1. 그래프 만들기

* 정점의 개수 n, 간선의 개수 m, 탐색 시작 정점 번호 v
'''

from collections import deque

def dfs(start):
    visited[start] = True
    print(start, end=" ")

    for i in graph[start]:
        if(not visited[i]):
            visited[i] = True
            dfs(i)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True

    while(q):
        x = q.popleft()

        print(x, end=" ")
        for i in graph[x]:
            if(not visited[i]):
                visited[i] = True
                q.append(i)

n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
visitedCopy = visited.copy()

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# print(graph)

for i in range(n+1):
    graph[i] = sorted(graph[i])

# print(graph)

dfs(v)
visited = visitedCopy
print()
bfs(v)


# arr = [[1,2,3]]
# arr[0] = [2,3]
#
# print(arr)