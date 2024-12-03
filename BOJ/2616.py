'''
19 x 19에서 연속적으로 5알이 놓이면 이긴다.
6알 이상이면 이긴게 아니다.

1. 모경수(prt, n=1)
1) 모든 좌표 순회
2) 한 좌표에서 가로, 세로, 대각선 다 봄
3) 현재 칸에서 추가로 4개가 아닌 5개를 봐서 같은 색의 숫자를 셈
    1] 같은 색이 4개면 
        1] 이전 한칸 봐서 같은 색이 아니면 끝
        2] 이전 한칸이 같은 색이면 다음 좌표

* 바둑판 상태(검=1, 힌=2, 빈칸=0)
출 : 검=1, 흰=2, 아직 NO=0
이겼을 경우 가장 왼쪽 바둑알 ㄱㄱ

2. n^3
'''
finish_flag = False
board = [list(map(int, input().split())) for _ in range(19)]
for i in range(19):
    for j in range(19):
        if(board[i][j] == 0):
            continue
        
        # 대각선
        cnt = 0 # 같은 거의 개수
        for k in range(1, 6):
            if(i+k == 19 or j+k==19): # 범위 검사
                break
            
            if(board[i][j] == board[i+k][j+k]):
                cnt += 1
            else:
                break
        if(cnt == 4):
            if(i == 0 or j == 0):
                print(board[i][j])
                print(i+1, j+1)
                finish_flag = True
                break
            
            if(board[i][j] == board[i-1][j-1]):
                break
            else:
                print(board[i][j])
                print(i+1, j+1)
                finish_flag = True
                    
        cnt = 0 # 같은 거의 개수
        for k in range(1, 6):
            if(i-k == -1 or j+k==19): # 범위 검사
                break
            
            if(board[i][j] == board[i-k][j+k]):
                cnt += 1
            else:
                break
        if(cnt == 4):
            if(i == 18 or j == 0):
                print(board[i][j])
                print(i+1, j+1)
                finish_flag = True
                break
            
            if(board[i][j] == board[i+1][j-1]):
                break
            else:
                print(board[i][j])
                print(i+1, j+1)
                finish_flag = True            
        
        # 가로
        cnt = 0
        for k in range(1, 6):
            if(j+k==19): # 범위 검사
                break
            
            if(board[i][j] == board[i][j+k]):
                cnt += 1
            else:
                break
        if(cnt == 4):
            if(j == 0):
                print(board[i][j])
                print(i+1, j+1)
                finish_flag = True
                break
            
            if(board[i][j] == board[i][j-1]):
                break
            else:
                print(board[i][j])
                print(i+1, j+1)
                finish_flag = True
        # 세로
        cnt = 0
        for k in range(1, 6):
            if(i+k==19): # 범위 검사
                break
            
            if(board[i][j] == board[i+k][j]):
                cnt += 1
            else:
                break
        if(cnt == 4):
            if(i == 0):
                print(board[i][j])
                print(i+1, j+1)
                finish_flag = True
                break
            
            if(board[i][j] == board[i-1][j]):
                break
            else:
                print(board[i][j])
                print(i+1, j+1)  
                finish_flag = True      
                    
if(finish_flag == False)                    :
    print(0)