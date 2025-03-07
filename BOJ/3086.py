'''
nxn에서 사탕의 색이 다른 인접한 2칸 골라서 교환함.
같은 색으로 연속된 부분 행, 열을 먹음

1. 모경수(prt, n=1)
ok 1) 교환 안했을 때 전체 보드 연속 최대 개수를 구함
    1] 행 -> 열 순회
    2] 열 -> 행 순회
2) 교환
    1] 오른쪽, 아래를 봐서 색이 다르면 교환
    4] 맨 오른쪽, 맨 아래 oob 고려
        1] 행, 열 n까지
        2] 다음 범위 넘어가는 곳은 교환 X
    2] 전체 보드 연속 최대 개수 구함
    3] 최대 개수 갱신
    
        
* n :
보드 상태
출 : 먹는 사탕 최대 개수

2. n^2
'''

# 1) 교환 안했을 때 전체 보드 연속 최대 개수를 구함
#     1] 행 -> 열 순회
#     2] 열 -> 행 순회
    
n = int(input())
board = [list(input()) for _ in range(n)]

# print(*board, sep = '\n')

max_cnt = 0

def check(x, y, x1, y1):
    # print(f"교체한 곳 ({x}, {y}) ({x1}, {y1})")
    global max_cnt
    
    # 행 -> 열 순회
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if(board[i][j] == board[i][j+1]):
                cnt += 1
            else:
                if(max_cnt < cnt):
                    max_cnt = cnt
                cnt = 1
        if(max_cnt < cnt):
            max_cnt = cnt
            
    # 열 -> 행 순회
    for j in range(n):
        cnt = 1
        for i in range(n-1):
            if(board[i][j] == board[i+1][j]):
                cnt += 1
            else:
                if(max_cnt < cnt):
                    max_cnt = cnt
                cnt = 1
        if(max_cnt < cnt):
            max_cnt = cnt            
    
    # print(max_cnt)
check(200, 200, 200, 200)


    # 1] 오른쪽, 아래를 봐서 색이 다르면 교환
    # 4] 맨 오른쪽, 맨 아래 oob 고려
    #     1] 행, 열 n까지
    #     2] 다음 범위 넘어가는 곳은 교환 X
    
for i in range(n):
    for j in range(n):
        if(i == n-1 and j == n-1):
            continue
        
        elif(i == n-1):
            # 오른 쪽 교환
            if(board[i][j] != board[i][j+1]):
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                check(i, j, i, j+1)
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            
        elif(j == n-1):
            if(board[i][j] != board[i+1][j]):
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                check(i, j, i+1, j)
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
        else:
            # 오른쪽 교한
            if(board[i][j] != board[i][j+1]):
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                check(i, j, i, j+1)
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            # 체크
            # 돌려놓기
            
            # 아래쪽 교한
            # 체크
            # 돌려놓기
            if(board[i][j] != board[i+1][j]):
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                check(i, j, i+1, j)
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                
print(max_cnt)                