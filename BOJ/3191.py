n = int(input())

graph = [[0] * n for _ in range(n)]

k = int(input())

for _ in range(k):
    x, y, = map(int, input().split())
    x -= 1
    y -= 1
    
    graph[x][y] = 1 # 사과
    
# print(*graph, sep = '\n')

# 회전한 인덱스를 변수로 추적
# 현재 가리키는 인덱스 최초0, 언제 다음 인덱스를 봐야할지 저정할 시간 배열

L = int(input())
rotates = []
times = [] # 언제 다음 인덱스를 봐야할지 저정할 시간 배열
rotate_idx = 0 # 현재 가리키는 인덱스 최초 0

for _ in range(L):
    X, C = input().split()
    X = int(X)
    
    rotates.append((X, C))
    # 현재 시간이 times에 in 하면 현재 rotate_idx의 rotates에 해당하는 방향으로 회전
    times.append(X) 
    
    
# print(rotates)    

# 최초 뱀의 위치 0, 0/ 방향 우
snake = [(0, 0)]

# print(snake)
x, y = 0, 0
d = 3
time = 0

# 상좌하우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 뱀의 이동은 증가는 app, 줄이기는 pop(0)
# 시간은 이동하기 전/에 증가

su = 0
while(True):
    time += 1
    
    nx = x + dx[d]
    ny = y + dy[d]
    
    # 0] 벽이면 게임 끝
    # 1] 사과가 있으면 줄이기 x
    # 2] 사과가 없으면 줄임
    
    # 벽
    if(nx < 0 or ny < 0 or nx >= n or ny >= n):
        print(time)
        break
    elif((nx, ny) in snake):
        print(time)
        break
    
    snake.append((nx, ny))
    
    # 사과가 있으면 줄이기 x
    if(graph[nx][ny] == 1):
        graph[nx][ny] = 0
        pass
    elif(graph[nx][ny] == 0):
        snake.pop(0)
        
    x = nx
    y = ny

    
    # 해당 시간이 끝날 때 rotate에 회전한 인덱스를 변수로 추적을 해서 이동방향 변경
    if(time in times):
        # print(rotates[rotate_idx][1])
        change_direct = rotates[rotate_idx][1]
        
        if(change_direct == 'D'):
            d = (d-1+4) % 4
        else:
            d = (d+1) % 4
        rotate_idx += 1
        
    # print("time : ",time, snake, "방향 : ", d)
    
    su += 1