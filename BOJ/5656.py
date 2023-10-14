'''
구슬을 N번 쏠 수 이쏙, 벽돌 정보가 WxH로 주어진다.(0 : 빈공간, 그외 숫자 : 벽돌)

게임 규칙 :
1) 구슬은 좌, 우로만 움직일 수 있어서 항상 맨 위에 있는 벽돌만 꺨 수 있다.
2) 벽돌은 1~9로 표현된다.
3) 구슬이 명정한 벽돌 상하좌우로 벽돌에 적힌 숫자 -1칸 만큼 같이 제거된다 ex) 3이면 2칸 같이제거
4) 근데 4이면 1 2 3칸이 같이 제거 되는데 1, 2, 3칸에 있는 벽돌은 구슬을 맞은 것처럼
 벽돌 상하좌우로 벽돌에 적힌 숫자 -1칸 만큼 같이 제거된다. (1이면 1-1=0이라서 맞은 벽돌만 제거된다.)
5) 빈 공간이 있을 경우 벽돌은 밑으로 떨어진다.
N개의 벽돌을 떨어트려 최대한 많은 벽돌을 제거하려고 한다. 남은 벽돌의 개수를 구해라

1. 모경수
1) 백? 뭐가 좋은 지 알 수 없으니깐 for문을 열로 돌면서 다 쏴보고 최소 벽돌 수가 정답
2) 열을 stand로 백하고 백 내부에서 1중 for문으로 행을 훑어서 0이 아닌 숫자를 만나면 bfs

3) 백을 도는 와중에 벽돌에 맞으면 bfs처럼 퍼져나가야 한다.
4) bfs 조건
    1] 벽돌 번호가 1이면 그냥 자기자신만 0되고 만다
    2] 번호-1만큼 상하좌우로 for문 돌아서 큐에 넣어야 한다.
    3] 큐에 넣을 때 0으로 만들고 
    4] 이걸 bfs 내부에서 할 지 끝나고 나와서 할지 고민 ㄱ

* 테케
n, w, h : n번, hxw w = 열, h = 행
벽돌 정보
'''
import copy
from collections import deque


# 1) 백? 뭐가 좋은 지 알 수 없으니깐 for문을 열로 돌면서 다 쏴보고 최소 벽돌 수가 정답
# 2) 2중 for문 백으로 열을 N만큼 훑어서 매번 백마다 0번 열부터 본다.
# 내부 for문으로 행을 훑어서 0이 아닌 숫자를 만나면 bfs

su = 1
def back(graph, su):
    global minCnt

    if(su == n):
        cnt = 0
        for i in range(h):
            for j in range(w):
                if(graph[i][j] != 0):
                    cnt += 1

        if(cnt < minCnt):
            minCnt = cnt
        return

    # 주의할 것
    # 1) 0을 만나면 무시
    # 2) 0을 계속 만나서 i가 h와 같아지면 다음 백
    # 3) 0이 아니면 백
    for j in range(w): # 열
        tmpGraph = [ele[:] for ele in graph]  # 원본 그래프를 저장할 그래프
        i = 0
        while(True): # 첫번째 블럭이 나올 때까지 훑어서
            if(i == h):
                back(graph, su+1)
                break
            elif(graph[i][j] == 0): # i가 h가 아닌데 0이라서 블럭이 아니면
                i += 1
                continue
            else: # i가 h가 아닌데 0이 아니라서 첫 번째 블럭이 나오면
                # tmpGraph = copy.deepcopy(graph)

                graph = bfs(i, j, graph) # bfs하고 백할 거다.

                # 이 받은 그래프를 내릴 거다. 열단위로 블럭을 찾아서 다시 재배치하면 될 듯
                graph = reLoc(graph) # 이렇게 하면 한 열에서 블록 제거 끝났어

                # 연쇄 작용을 하든 말든 다음 구슬을 날리기 위해서 if문 밖에 for문
                back(graph, su+1)
                break
        # 다음 열 볼 때 원본 유지
        graph = [ele[:] for ele in tmpGraph]


            

def reLoc(graph):
    reLocGraph = [[0] * w for _ in range(h)]
    newCols = []
    for y in range(w):
        col = []
        for x in range(h):
            if (graph[x][y] != 0):
                col.append(graph[x][y])
        col.reverse()
        newCols.append(col)

    # print(newCols)

    for y in range(w):
        idx = 0
        # print(1)
        # print(h-1, h-1-len(newCols[y]))
        for x in range(h-1, h-1-len(newCols[y]), -1):
            # print(2)
            reLocGraph[x][y] = newCols[y][idx]
            idx += 1

    return reLocGraph

# 2] 번호-1만큼 상하좌우로 for문 돌아서 큐에 넣어야 한다.
#     3] 큐에 넣을 때 0으로 만들고 
#     4] 이걸 bfs 내부에서 할 지 끝나고 나와서 할지 고민 ㄱ
def bfs(i, j, graph):
    q = deque()
    q.append((i, j))
    # visit은 필요가 없어보임 graph에 0 넣으면 됨

    while(q):
        # print(q)
        # 번호 -1만큼 상하좌우로 for문 돌아서 다 큐에 넣어야 한다.
        x, y = q.popleft()
        num = graph[x][y]

        # 상
        nx = x
        ny = y
        for _ in range(num-1):
            nx = nx + dx[0]
            ny = ny + dy[0]

            if(nx < 0 or ny < 0 or nx >= h or ny >= w):
                continue
            if(graph[nx][ny] != 0):
                q.append((nx, ny))

        # 하
        nx = x
        ny = y
        for _ in range(num-1):
            nx = nx + dx[1]
            ny = ny + dy[1]

            if(nx < 0 or ny < 0 or nx >= h or ny >= w):
                continue
            if(graph[nx][ny] != 0):
                q.append((nx, ny))
        # 좌
        nx = x
        ny = y
        for _ in range(num-1):
            nx = nx + dx[2]
            ny = ny + dy[2]

            if(nx < 0 or ny < 0 or nx >= h or ny >= w):
                continue
            if(graph[nx][ny] != 0):
                q.append((nx, ny))
        # 우
        nx = x
        ny = y
        for _ in range(num-1):
            nx = nx + dx[3]
            ny = ny + dy[3]

            if(nx < 0 or ny < 0 or nx >= h or ny >= w):
                continue
            if(graph[nx][ny] != 0):
                q.append((nx, ny))

        # 가장 마지막에 블록 제거
        graph[x][y] = 0
    return graph

dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]

t = int(input())
for i in range(1, t+1):
    n, w, h = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(h)]
    minCnt = 1e9
    back(graph, 0)
    print("#{} {}".format(i, minCnt))