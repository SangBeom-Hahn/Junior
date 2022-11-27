from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    distance[x][y] = 0

    while(queue):
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # print(x, y, goalX, goalY)

            if (x == goalX and y == goalY):
                return distance[x][y]

            if(nx < 0 or ny < 0 or nx >= l or ny >= l):
                continue
            if(distance[nx][ny] == -1):
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

            # for i in range(l):
            #     for j in range(l):
            #         print(distance[i][j], end=" ")
            #     print()

if(__name__ == "__main__"):
    t = int(input())
    MAX = 301
    dx = [-2, -2, 2, 2, -1, 1, -1, 1]
    dy = [-1, 1, -1, 1, -2, -2, 2, 2]
    for i in range(t):
        l = int(input())
        # graph = [[0] * l for i in range(l)]
        distance = [[-1] * l for i in range(l)]
        # 현위치
        myX, myY = map(int, input().split())
        # 목표 위치
        goalX, goalY = map(int, input().split())

        print(bfs(myX, myY))
