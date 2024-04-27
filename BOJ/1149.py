from collections import deque

def bfs(a, b, c, d):
    # 각 상태에 도달하는 데 필요한 최소 행동 횟수를 저장하는 리스트
    dist = [[[0]*201 for _ in range(201)] for _ in range(201)]
    # 큐에 넣는 아이템은 (현재 상태, 행동 횟수)
    q = deque([(0, 0, c, 0)])
    
    while q:
        x, y, z, cnt = q.popleft()
        
        if x == d or y == d or z == d:
            return cnt

        # 현재 상태에서 가능한 모든 행동을 시도
        for nx, ny, nz in [(x, y, 0), (x, 0, z), (0, y, z), (x, y, c), (x, b, z), (a, y, z)]:
            # 아직 방문하지 않은 상태의 경우
            if dist[nx][ny][nz] == 0:
                dist[nx][ny][nz] = cnt + 1
                q.append((nx, ny, nz, cnt+1))
                
        # x에서 y로, x에서 z로, y에서 x로, y에서 z로, z에서 x로, z에서 y로 액체를 이동
        for nx, ny, nz in [(x-min(x,b-y), y+min(x,b-y), z), (x-min(x,c-z), y, z+min(x,c-z)), (x+min(y,a-x), y-min(y,a-x), z), (x, y-min(y,c-z), z+min(y,c-z)), (x+min(z,a-x), y, z-min(z,a-x)), (x, y+min(z,b-y), z-min(z,b-y))]:
            if dist[nx][ny][nz] == 0:
                dist[nx][ny][nz] = cnt + 1
                q.append((nx, ny, nz, cnt+1))
                
    return -1

# 입력
a, b, c, d = 3, 5, 7, 1

# 출력
result = bfs(a, b, c, d)
if result != -1:
    print(result)
else:
    print("-1")


# print(bfs(3, 5, 7, 1)) # 4
# print(bfs(3, 6, 9, 4)) # -1
