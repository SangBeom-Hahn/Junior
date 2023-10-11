'''
사과를 먹으면 뱀 길이가 늘어난다. 뱀은 벽을 만나거나 자기자신과 부딪히면 게임이 끝난다.
nxn에서 진행되고 몇몇 칸에 사과가 있고 보드의 상하좌우끝에 벽이 있다.
1) 뱀의 시작은 맨위 맨 좌측에 위치하고 뱀의 길이는 1이다.
2) 처음에는 오른쪽을 향한다.
3) 이동 규칙
0] 뱀은 매 초마다 이동한다.
1] 몸 길이를 늘려 머리를 다음칸에 위치시킨다.
2] 벽을 만나거나 자기자신과 부딪히면 게임이 끝난다.
3] 이동칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.(사과를 먹어서
길이가 늘어난 거임)
4] 사과가 없다면, 몸길이를 줄여 꼬리가 위치한 칸을 비운다.(사과가 없어서 다시 원상복구돼서
길이가 안늘어난 거임)
이 게임이 몇 초에 끝나는지 구해라

1. 모경수
1) 처음에는 길이가 1로해서 visit을 길이 1만 하면 된다.
2) 근데 사과를 먹으면 이전 visit도 유지하면서 같이 이동해야한다. -> visit이 머리만큼 
늘어남
3) 사과가 없으면 꼬리만 비우는 거라서 몸 길이가 똑같이 유지되는 거임 -> visit이 한칸씩
이동

* n : 보드의 크기
k : 사과의 개수
k개의 사과의 위치(1, 1열부터 시작)
L : 방향 변환 횟수
L개의 방향 변환 정보 x, c(x=3, c=D면 게임 시작 시간으로부터 3초가 끝난 뒤에 D로 90도 회전
한다는 뜻이다. L = 왼쪽, D = 오른쪽)
출력 : 몇 초에 끝나는지 출력하라

2. nlogn
'''



n = int(input())
k = int(input())
graph = [[0] * n for _ in range(n)]
visit = [[False] * n for _ in range(n)]
# 최초 위치는 왼쪽 상단
visit[0][0] = True

# 사과 위치 표시
for _ in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 'A'

# 회전 정보 표시
L = int(input())
dic = {}
for _ in range(L):
    t, D = input().split()
    dic[int(t)] = D

# 0) 최초에는 방향이 오른쪽으로 무조건 한칸 움직임
# 1) 처음에는 길이가 1로해서 visit을 길이 1만 하면 된다.
# 2) 근데 사과를 먹으면 이전 visit도 유지하면서 같이 이동해야한다. -> visit이 머리만큼 
# 늘어남
# 3) 사과가 없으면 꼬리만 비우는 거라서 몸 길이가 똑같이 유지되는 거임 -> visit이 한칸씩
# 이동
# 4) 꼬리 꺾이는 거 어캐 꼬리 좌표 체크할 지 생각 ㄱㄱ -> 상하좌우 인접한 애로 꼬리 따라가자
# print(*graph, sep = '\n')
# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = 0 # 최초에는 우
time = 0
headX, headY = 0, 0
tailX, tailY = 0, 0
# 벽을 만나거나 몸에 닿을 때까지 반복
snake = [] # 이어가는 것을 하기 위해서는 큐에 넣는게 좋겠다.

su = 1
# while(su != 7):
while(True):
    time += 1
    nx = headX + dx[d]
    ny = headY + dy[d]

    if(nx < 0 or ny < 0 or nx >= n or ny >= n):
        break

    if(visit[nx][ny] == True):
        break
    snake.append([nx, ny])
    # 사과가 있으면 visit 머리만큼 늘어남
    if(graph[nx][ny] == 'A'):
        graph[nx][ny] = 0
        visit[nx][ny] = True

    # 사과가 없으면 가장 마지막 visit 제거
    else:
        visit[nx][ny] = True
        visit[tailX][tailY] = False

        # 상하좌우로 꼬리 이어가기
        tailX, tailY = snake.pop(0)

    # 시간이 되면 회전함
    if(time in dic.keys()):
        if(dic[time] == 'D'):# 오른쪽
            d = (d+1) % 4
        else:# 왼쪽
            d = ((d-1) + 4) % 4

    headX = nx
    headY = ny
    su += 1

# print(*visit, sep = '\n')
print(time)