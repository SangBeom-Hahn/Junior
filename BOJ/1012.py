from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0

    while(queue):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(nx < 0 or ny < 0 or nx >= m or ny >= n):
                continue

            if(graph[nx][ny] == 1):
                graph[nx][ny] = 0
                queue.append((nx, ny))

if(__name__ == "__main__"):
    t = int(input())
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(t):
        cnt = 0
        m, n, k = map(int, input().split())
        graph = [[0] * n for _ in range(m)]
        for j in range(k):
            x, y = map(int, input().split())
            graph[x][y] = 1

        # print(graph)

        for a in range(m):
            for b in range(n):
                if(graph[a][b] == 1):
                    bfs(a, b)
                    # print(i, j)
                    cnt += 1

        print(cnt)