'''
n x m에 벽 or 빈칸(청소되지 않은 상태)
청소기
1) 바라보는 방향이 있어.
2) 현재 칸 상태 = 청소 X -> 청소함
3) 현재 칸 주변 4칸에 빈칸이고 청소되지 않은 칸이 없음
    1] 방향을 유지한채 한칸 후진할 수 있으면 후진하고 다시 2)로 돌아감
    2] 뒤쪽 칸이 벽이라 후진 못하면 작동 STOP
    
4) 주변 4칸 중 청소되지 않고 빈칸이 있어
    1] 반시계 90도 회전 (북서남동)
    2] 바라보는 칸이 청소되지 않고 빈칸이면 한칸 전진 다시 2)로 돌아감

1. 모경수(prt, n=1)
0) 첫 번째 칸은 결과에 ++
1) 현재 칸에서 주변 4칸 순회
    1] 빈칸이고 청소 안했으면 결과 ++ 전진
2) 주변 4칸 모두 (빈칸이고 청소 안한 칸)이 없으면 현재칸에서 후진
    1] 벽이면 종료
    2] 빈칸이면 1)로


    
* n, m
r, c, d : 첫 좌표와 방향(0=북, 1=동, 2=남, 3=서)
각 장소의 상태(0=빈칸, 1=벽), 가장자리엔 무조건 벽이 있음(범위를 나갈일이 없음)

출 : 청소하는 칸의 개수

2. n^2
'''

n, m = map(int, input().split())
r, c, d = map(int, input().split()) # 현재칸, 방향
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# print(*graph, sep='\n')
result = 1 # 시작점은 무조건 청소함
visit[r][c] = True
su = 1
# while(su != 6):
while(True):
    if(graph[r][c] == 0 and not visit[r][c]):
        result += 1
    
# 4) 주변 4칸 중 청소되지 않고 빈칸이 있어
#     1] 반시계 90도 회전 (북서남동)
#     2] 바라보는 칸이 청소되지 않고 빈칸이면 한칸 전진 다시 2)로 돌아감
    # print(*visit, sep='\n')
    # print()
    for i in range(1, 5):
        # d = 0 / 3 2 1 0
        # d = 1 / 0 3 2 1
        nd = (d - i + 4) % 4
        nx = r + dx[nd]
        ny = c + dy[nd]
        
        # 다시 2로 돌아감
        # print(nx, ny, nd)
        if(graph[nx][ny] == 0 and not visit[nx][ny]):
            r = nx
            c = ny
            d = nd
            result += 1
            visit[r][c] = True
            break

# 3) 현재 칸 주변 4칸에 빈칸이고 청소되지 않은 칸이 없음
#     1] 방향을 유지한채 한칸 후진할 수 있으면 후진하고 다시 2)로 돌아감
#     2] 뒤쪽 칸이 벽이라 후진 못하면 작동 STOP
    else: # 없어
        nd = (d+2) % 4
        nx = r + dx[nd]
        ny = c + dy[nd]
        if(graph[nx][ny] == 1):
            print(result)
            break
        else:
            r = nx
            c = ny
            # 방향은 유지
    
    su += 1
    
# print(result)