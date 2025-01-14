'''
n m 
작동
1) 현재 칸 청소 X -> 현재 칸 청소
2) 주변 4칸 중 청소안한 빈칸이 없는 경우
    1] 방향 유지, 한칸 후진 1번으로 돌아감
    2] 방향 유지, 한 칸 뒤가 벽이면 동작 끝
3) 청소 안한 빈칸이 있는 경우
    1] 반시계 90도 회전한 곳이 청소되지 않은 빈칸이면 전진, 1번으로 돌아감

1. 모경수(prt, n=1)
0) visit으로 청소유무 체크
1) 현재 칸 청소 x 시 결과 ++
2) 현재 방향에서 반시계 방향으로 4번 봄
    1] 빈칸 + 청소하지 않았으면 좌표, 방향 갱신
3) 4번 다 봤는데 다 안되면, 한 칸 뒤로 감
    1] 뒤로 갔는데 벽이 아니면 정상작동
    2] 벽이면 끝
    
* n, m
r, c, d : 첫 좌표와 방향 (0, 1, 2, 3) = (북동남서)
맵(0 = 빈칸, 1 = 벽)
출 : 청소하는 칸의 개수

2. n^2
'''

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
result = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

su = 1
# while(su != 7):
while(True):
    # print("좌표 : ", r, c, d)
    
    # 1) 현재 칸 청소 x 시 결과 ++
    if(graph[r][c] == 0):
        if(not visit[r][c]):
            result += 1
            visit[r][c] = True
    else: # 뒤고 갔는데 벽이면 끝
        print(result)
        break
    
    # 2) 현재 방향에서 반시계 방향으로 4번 봄
    # 1] 빈칸 + 청소하지 않았으면 좌표, 방향 갱신
    
    # 3) 되4번 다 봤는데 다 안면, 한 칸 뒤로 감 / 북 동 남 서
    # 1] 뒤로 갔는데 벽이 아니면 정상작동
    # 2] 벽이면 끝
    for i in range(1, 5):
        nd = (d - i + 4) % 4
        nx = r + dx[nd]
        ny = c + dy[nd]
        # print(nx, ny, nd)
        if(graph[nx][ny] == 0 and not visit[nx][ny]):
            r = nx
            c = ny
            d = nd
            break
    else:
        r = r + dx[(d + 2) % 4]
        c = c + dy[(d + 2) % 4]
    
    su += 1
    
    # print(*visit, sep = '\n')
    # print()

# print(result)