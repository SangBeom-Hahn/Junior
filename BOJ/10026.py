from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while(queue):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(nx < 0 or ny < 0 or nx >= n or ny >= n):
                continue

            # if (graph[nx][ny] == 'R'):
            #     graph[nx][ny] = 'G'

            if(graph[x][y] == graph[nx][ny] and not visited[nx][ny]):
                visited[nx][ny] = True
                queue.append((nx, ny))


if(__name__ == "__main__"):
    n = int(input())
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cntYes = 0
    cntNo = 0
    visited = [[False] * n for i in range(n)]
    graph = []
    for i in range(n):
        graph.append(list(input()))

    # print(graph)
    # print(visited)

    # 적록 아닌 사람
    for i in range(n):
        for j in range(n):
            if(not visited[i][j]):
                bfs(i, j)
                cntNo += 1

    for i in range(n):
        for j in range(n):
            if(graph[i][j] == 'G'):
                graph[i][j] = 'R'

    # 적록인 사람
    visited = [[False] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if(not visited[i][j]):
                bfs(i, j)
                cntYes += 1

    print(cntNo, cntYes)