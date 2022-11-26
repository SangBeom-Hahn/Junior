from collections import deque

def bfs(n):
    queue = deque()
    queue.append(n)
    distances[n] = 0

    while(queue):
        x = queue.popleft()
        dx[2] = x
        if(x == k):
            return distances[k]

        for i in range(3):
            nx = x + dx[i]

            if(nx < 0 or nx > MAX):
                continue

            if(distances[nx] > distances[x] + 1): # 해석 : 이동할 곳보다 내 현재 위치 +1이 작으면 = 점프를 1로 해서 dis[2]이 2가 되었는데 점프를 2로 하면 1만에 갈 수 있으니!!라는 생각
                distances[nx] = distances[x] + 1
                queue.append(nx)

if (__name__ == "__main__"):
    n, k = map(int, input().split())
    INF = 999999999
    MAX = 100000
    distances = [INF] * (MAX+1) # 거리
    dx = [-1, 1, 0]

    print(bfs(n))