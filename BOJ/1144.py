'''
nxn 크기에 사탕이 있다. 색이 다른 인접한 두칸을 고른다.고른칸에 있는 사탕을 서로 교환한다.
모두 같은 색으로 이루어져있는 가장 긴 행 또는 열 연속 부분을 고른 다음 그 사탕을 모두 먹는다.
1직선만 인정한다.

1. 모경수
ccp
ccp
ppc

ccp
ccp
pcp

1) 2중 for로 훑으면서, 아래, 우가 색이 다르면 바꾼다. 
= 한 칸에서 2번씩 다르면 바꾸고 검사하는 거임

2) 가장 우측, 가장 아래까지 훑는데, 가장 아래에서는 우만, 가장 오른에서는 아래만 교환
3) 그리고 바꾼 픽셀의 행 열을 체크함

* n : 보드의 크기
보드에 채워진 사탕의 색상 빨파초노 C P Z Y
출력 : 상근이가 먹을 수 있는 사탕의 최대 개수

2. 시복 : n^2
'''

n = int(input())
board = [list(input()) for _ in range(n)]
fin_max_cnt = 0

# print(board)

# 행 검사
def check_raw(raw):
    global fin_max_cnt
    max_seq_cnt = 0
    
    each_cnt = 1
    for i in range(n-1): #ccp
        if(board[raw][i] == board[raw][i+1]):
            each_cnt += 1
        else:
            if(max_seq_cnt < each_cnt):
                max_seq_cnt = each_cnt
                each_cnt = 1
        # print(board[raw][i], each_cnt)
    
    if(max_seq_cnt < each_cnt):
        max_seq_cnt = each_cnt
        each_cnt = 1
     
    if(fin_max_cnt < max_seq_cnt):           
        fin_max_cnt = max_seq_cnt
        
# 열 검사
def check_col(col):
    global fin_max_cnt
    max_seq_cnt = 0
    
    each_cnt = 1
    for i in range(n-1): #ccp
        if(board[i][col] == board[i+1][col]):
            each_cnt += 1
        else:
            if(max_seq_cnt < each_cnt):
                max_seq_cnt = each_cnt
                each_cnt = 1
        # print(board[raw][i], each_cnt)
        
    if(max_seq_cnt < each_cnt):
        max_seq_cnt = each_cnt
        each_cnt = 1
     
    if(fin_max_cnt < max_seq_cnt):           
        fin_max_cnt = max_seq_cnt
    

# for i in range(n-1):
#     for j in range(n-1):
for i in range(n):
    for j in range(n):
        # 가장 아래이면, 아래 안 봄
        if(i != n-1):
            # 아래
            if(board[i][j] != board[i+1][j]):
                # 바꾸고
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            
        # 행 검사
        check_raw(i)
                            
        # 열 검사
        check_col(j)
        # print(*board, sep='\n')
            
        
        # 원상복구
        if(i != n-1):
            if(board[i][j] != board[i+1][j]):
                # 바꾸고
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                
        # 우
        if(j != n-1):
            if(board[i][j] != board[i][j+1]):
                # 바꾸고
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                
        # 행 검사
        check_raw(i)
                            
        # 열 검사
        check_col(j)
        # print(i, j, fin_max_cnt)
        
        
        # 우
        if(j != n-1):
            if(board[i][j] != board[i][j+1]):
                # 바꾸고
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]        
                
print(fin_max_cnt)                