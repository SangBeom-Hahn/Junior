'''
로봇
1] n,n으로 이동할거임 로봇의 두 칸 중 어느 한 칸이라도 n,n에 도착하면 끝
2] 지도 (0 = 빈칸, 1 = 벽)
3] 벽 또는 지도 밖으로 이동 불가
4] 회전
    1] 90도씩 회전 가능
    2] 회전 축 대각선에 벽이 없어야 함
5] 1칸 이동, 회전은 각각 1초 걸림

1. 모경수(prt, n=1)
2) 이동 방법
    공통 1] 왼쪽 = 두 좌표의 열만 -1
    공통 2] 오른쪽 = 두 좌표의 열만 +1
        3] 위
        4] 아래
    3] 회전
        -> 로봇이 가로
        1] 왼쪽 축
            1] 위 = 왼쪽축 고정, 오른쪽 바퀴 x-1, y-1
            2] 아래 = 왼쪽축 고정, 오른쪽 x+1 , y-1
        2] 오른쪽 축
            1] 위 = 오른쪽 고정, 왼쪽 x-1, y+1
            2] 아래 = 오른쪽 고정, 왼쪽 x+1, y+1
        
        -> 로봇이 세로
        1] 위쪽 축
            1] 왼쪽 = 위쪽 고정, 아래쪽 x-1, y-1
            2] 오른쪽 = 위 고정, x-1, y+1
        2] 아래쪽 축
            1] 왼 = 아래 고정, x+1, y-1
            2] 오 = 아래 고정, x+1, y+1
ok 3) 우선 현재 위치에서 갈 수 있는 것을 모두 구해
    1] 가로냐 세로냐 구분해야함
    2] 가로면 공통 + 가로 회전
    3] 세로면 공통 + 세로 회전
    
4) 그걸 순회하면서 방문 안 한 곳을 탐색
5) 초는 큐에 같이 넣음

* 지도상태
출 : 로봇이 도착하는데 걸리는 최소시간

2. nlogn
'''
from collections import deque

def bfs(board, visit):
    start = ((0, 0), (0, 1))
    visit.append(set(start))
    n = len(board)
    
    q = deque()
    q.append([start, 0]) # 좌표, 시간
    
    while(q):
        # print(q)
        start, time = q.popleft()
        back = start[0]
        front = start[1]
        
        back_x = back[0]
        back_y = back[1]
        front_x = front[0]
        front_y = front[1]
        if(front_x == n-1 and front_y == n-1):
            # print(start, time)
            # print(front_x, front_y)
            return time
        
        # 갈 수 있는 것의 위치
        can_move_loc = []
        
        
# 3) 우선 현재 위치에서 갈 수 있는 것을 모두 구해
#     1] 가로냐 세로냐 구분해야함
#     2] 가로면 공통 + 가로 회전
#     3] 세로면 공통 + 세로 회전
#       4] 갈 수 있냐? 벽이 아니고 안 나감

# 공통 1] 왼쪽 = 두 좌표의 열만 -1
# 공통 2] 오른쪽 = 두 좌표의 열만 +1

        print("현재 위치", start)
        # 가로 = 두 행이 같음
        if(back_x == front_x):
            print("가로")
            # 왼
            # 왼쪽 바퀴가 벽이 아니고 안 나가야함
            if(back_y - 1 < 0 or board[back_x][back_y - 1] == 1):
                pass
            else:
                can_move_loc.append([[back_x, back_y-1], [front_x, front_y-1]])
            
            # 오
            # 오른쪽 바퀴가 벽이 아니고 안 나가야함
            if(back_y+1 >= n or board[back_x][back_y+1] == 1):
                pass
            else:
                can_move_loc.append([[back_x, back_y+1], [front_x, front_y+1]])
            
            # 위 
            if(back_x - 1 < 0 or board[back_x-1][back_y] == 1 or board[front_x-1][front_y]):
                pass
            else:
                can_move_loc.append([[back_x-1, back_y], [front_x-1, front_y]])
                
# 아래
            if(back_x + 1 >= n or board[back_x+1][back_y] == 1 or board[front_x+1][front_y]):
                pass
            else:
                can_move_loc.append([[back_x+1, back_y], [front_x+1, front_y]])                
            
            # 회전
        # 1] 왼쪽 축
        #     1] 위 = 오른쪽 바퀴의 위가 벽이 아니고 안나가야함 / 왼쪽축 고정, 오른쪽 바퀴 x-1, y-1
        #     2] 아래 = 오른쪽 바퀴의 아래가 벽이 아니고 안나가야함 / 왼쪽축 고정, 오른쪽 x+1 , y-1
            if(front_x-1 < 0 or board[front_x-1][front_y] == 1):
                pass
            else:
                can_move_loc.append([[front_x-1, front_y-1], [back_x, back_y]])
                
            if(front_x+1 >= n or board[front_x+1][front_y] == 1):
                pass
            else:
                can_move_loc.append([[back_x, back_y], [front_x+1, front_y-1]])
            
        # 2] 오른쪽 축
        #     1] 위 = 왼쪽 바퀴의 위가 벽이 아니고 안나가야함 / 오른쪽 고정, 왼쪽 x-1, y+1
        #     2] 아래 = 왼쪽 바퀴의 아래가 벽이 아니고 안나가야함 / 오른쪽 고정, 왼쪽 x+1, y+1            
            if(back_x-1 < 0 or board[back_x-1][front_y] == 1):
                pass
            else:
                can_move_loc.append([[back_x-1, back_y+1], [front_x, front_y]])
                
            if(back_x+1 >= n or board[back_x+1][front_y] == 1):
                pass
            else:
                can_move_loc.append([[front_x, front_y], [back_x+1, back_y+1]])            
            
        
            
    
        # 세로 = 두 열이 같음     
        elif(back_y == front_y):
            print("세로")
            # 왼
            # 왼쪽 바퀴가 벽이 아니고 안 나가야함
            if(back_y - 1 < 0 or board[back_x][back_y - 1] == 1 or board[front_x][front_y - 1] == 1):
                pass
            else:
                can_move_loc.append([[back_x, back_y-1], [front_x, front_y-1]])
            
            # 오
            # 오른쪽 바퀴가 벽이 아니고 안 나가야함
            if(back_y+1 >= n or board[back_x][back_y+1] == 1 or board[front_x][front_y+1] == 1):
                pass
            else:
                can_move_loc.append([[back_x, back_y+1], [front_x, front_y+1]])
                
            # 위
            if(back_x - 1 < 0 or board[back_x-1][back_y] == 1):
                pass
            else:
                can_move_loc.append([[back_x-1, back_y], [front_x-1, front_y]])
            
            # 아래
            if(front_x + 1 >= n or board[front_x+1][front_y] == 1):
                pass
            else:
                can_move_loc.append([[back_x+1, back_y], [front_x+1, front_y]])
            
                
            # 회전  
        # 1] 위쪽 축
        #     1] 왼쪽 = front 아래 바퀴의 왼쪽이 벽이 아니고 안나가 / 위쪽 고정, 아래쪽 x-1, y-1
        #     2] 오른쪽 = 아래 바퀴의 오른쪽이 벽이 아니고 안나가 / 위 고정, x-1, y+1
            if(front_y-1 < 0 or board[front_x][front_y-1] == 1):
                pass
            else:
                can_move_loc.append([[front_x-1, front_y-1], [back_x, back_y]])
                
            if(front_y+1 >= n or board[front_x][front_y+1] == 1):
                pass
            else:
                can_move_loc.append([[back_x, back_y], [front_x-1, front_y+1]])
        
        
        # 2] 아래쪽 축
        # #     1] 왼 = back 위 바퀴의 왼쪽 벽 아니고 안나가 / 아래 고정, x+1, y-1
            if(back_y-1 < 0 or board[back_x][back_y-1] == 1):
                pass
            else:
                can_move_loc.append([[back_x+1, back_y-1], [front_x, front_y]])
        
        #     2] 오 = 외 바퀴의 오른쪽 벽 아니고 안나가 / 아래 고정, x+1, y+1        
            # if(back_y + 1 >= n or board[back_x][back_y+1] == 1):
            #     pass
            # else:
            #     can_move_loc.append([[front_x, front_y], [back_x+1, back_y+1]])
                
                
        
        print("갈 수 있음",  can_move_loc)
    
    # 4) 그걸 순회하면서 방문 안 한 곳을 탐색
        for ele1, ele2 in can_move_loc:
            back_x, back_y = ele1[0], ele1[1]
            front_x, front_y = ele2[0], ele2[1]
            # print("전체 갈 수 있는 곳", back_x, back_y, front_x, front_y)
            # print()
            
            if(set(((back_x, back_y), (front_x, front_y))) in visit):
                continue
            
            # print("방문 안한 곳", back_x, back_y, front_x, front_y)
            # print()
            # start = ((0, 0), (0, 1))
            # q.append([start, 0]) # 좌표, 시간
            q.append([((back_x, back_y), (front_x, front_y)), time+1])
            visit.append(set(((back_x, back_y), (front_x, front_y))))


# 5) 초는 큐에 같이 넣음    
    
    

def solution(board):
    visit = []
    print(bfs(board, visit))
    
board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]    
solution(board)