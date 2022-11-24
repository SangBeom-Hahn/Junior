from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 0 # 방문했다.
    ground = 1

    while(queue):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(nx < 0 or ny < 0 or nx >= n or ny >= m):
                continue

            if(graph[nx][ny] == 1 and visited[nx][ny] == -1):
                # 상하 좌우를 보기 때문에 다시 방문하지 않도록 근데 visited 조건문으로도 가능
                # graph[nx][ny] = graph[x][y] + 1
                visited[nx][ny] = 0
                queue.append((nx, ny))
                ground += 1

    return ground

if __name__ == "__main__":
    n, m = map(int, input().split())
    maximum = 0
    cnt = 0
    visited = [[-1] * m for i in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(m):
            if(graph[i][j] == 1 and visited[i][j] == -1):
                maximum = max(maximum, bfs(i, j))
                cnt += 1

    print(cnt)
    print(maximum)