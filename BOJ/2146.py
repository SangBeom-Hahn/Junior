'''
nxn에 여러섬, 가장 짧은 다리를 놓아 두 대륙을 연결하자

-> 모든 육지에서 다 bfs를 호출해야함
1) dis가 필요한가? -> 바다에서 안 간 바다만 가야해서 필요
    1] dis에 바다를 전부0, 육지를 전부1?
    2] 전부 1이면 같은 섬 다른섬 구분이 안돼서 dis에 섬 번호를 붙임
    3] 붙이는법
        0] 섬번호 1로 시작
        1] 2중 for 육지인데 dis 가 0이면 섬번호로 대임
        2] 섬번호 1 증가
        
2) bfs 호출
    1] 섬번호를 통해 몇개의 섬이 있는지 암
    2] 3중 for로
        1] 섬번호 1, 2중 for해서 섬번호에 해당하는 dis일때만 bfs 호출
            0] dis 가장 바깥 for에서 계속 생신
        2] bfs 모양
            1] 2중 for로 먼저 그 육지 좌표 다 구함
            2] 육지 -> 육지 = 안퍼짐
            3] 육지 -> 바다 = dis가 0일때만 감
            4] 바다 -> 바다 = dis가 0일때만 감
            5] 섬번호가 아닌 다른 섬 만나면 그떄의 dis 반환, 결과 갱신

* n : 지도의 크기
지도의 상태(0=바다, 1=육지)
출 : 가장 짧은 다리 길이

2. nlogn
'''
from collections import deque

def two(x, y, num): # 섬번호
    q = deque()
    for i in range(n):
        for j in range(n):
            if(dis[i][j] == num):
                q.append((i, j))
    while(q):
        # print(q)
        x, y = q.popleft()
        if(graph[x][y] == 1): # 육지
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if(nx < 0 or ny < 0 or nx >= n or ny >= n):
                    continue
                if(graph[nx][ny] == 0 and dis[nx][ny] == 0):
                    q.append((nx, ny))
                    dis[nx][ny] = 1
            
        else:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if(nx < 0 or ny < 0 or nx >= n or ny >= n):
                    continue
                
                if(graph[nx][ny] == 1 and dis[nx][ny] != num):
                    return dis[x][y]
                
                if(graph[nx][ny] == 0 and dis[nx][ny] == 0):
                    q.append((nx, ny))
                    dis[nx][ny] = dis[x][y] + 1

def bfs(x, y):
    q = deque()
    q.append((x, y))
    dis[x][y] = land_num
    
    while(q):
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(nx < 0 or ny < 0 or nx >= n or ny >= n):
                continue
            
            if(graph[nx][ny] == 1 and dis[nx][ny] == 0):
                q.append((nx, ny))
                dis[nx][ny] = land_num

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dis = [[0] * n for _ in range(n)]

land_num = 1

for i in range(n):
    for j in range(n):
        if(graph[i][j] == 1 and dis[i][j] == 0):
            bfs(i, j)
            land_num += 1
land_num -= 1            
# print(*dis, sep = '\n')   
temp = [ele[:] for ele in dis]
# print(land_num)

    # 2] 3중 for로
    #     1] 섬번호 1, 2중 for해서 섬번호에 해당하는 dis일때만 bfs 호출
    #         0] dis 가장 바깥 for에서 계속 생신

result = 20000
for num in range(1, land_num+1):
# for num in range(1, 2):    
    flag = False
    dis = [ele[:] for ele in temp]
    
    for i in range(n):
        if(flag == True):
            break
        
        for j in range(n):
            if(graph[i][j] == 1 and dis[i][j] == num): # 한번 그 섬번호로 bfs를 했으면 다음 섬만 봄
                v = two(i, j, num)
                if(result > v):
                    result = v
                
                flag = True
                break
            
    # print(*dis, sep = '\n')
print(result)