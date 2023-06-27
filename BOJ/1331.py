'''
나이트 투어는 나이트가 모든 칸을 정확히 한 번씩 방문하여, 마지막으로 방문하는 칸에서
시작점으로 돌아올 수 있는 경로이다. 6x6 체스판 위에서 또 다른 나이트 투어의
경로를 찾으려고 한다.

1. 모든 경우의 수
1) 모두 다 이동하지 못 할 경우를 생각해야한다.
2) 중복되는 칸이 있는 지
3) L자로 이동할 수 있는 경로인지

4) 이동 완료 후 전부 다 1로 표시되는 지
5) 마지막 칸과 시작 칸이 L자로 되는 지

6) 3) 5)를 절대값이 2, 1이나 1, 2인지로 보겠다.

* 나이트 투어 경로
출력 Valid, INv

2. 시복 : n^3
'''

plan = [input() for _ in range(36)]
result = 'Valid'
# print(plan)

for i in range(len(plan)): # 알파벳을 다 숫자로 바꾸자
    plan[i] = str( int(ord(plan[i][0].lower()) ) - int(ord('a')) ) + str(int(plan[i][1]) - 1)
    
x, y = int(plan[0][0]), int(plan[0][1])
firstX, firstY = int(plan[0][0]), int(plan[0][1])
board = [[0] * 6 for i in range(6)]
board[firstX][firstY] = 1
    
if(len(set(plan)) != 36): # 중복되는 칸이 있는 지
    result = 'Invalid'
    
# 시작과 마지막 칸 확인
if(abs(firstX - int(plan[-1][0])) == 2 and abs(firstY - int(plan[-1][1])) == 1\
    or abs(firstX - int(plan[-1][0])) == 1 and abs(firstY - int(plan[-1][1])) == 2):
    pass
else:
    result = "Invalid"
    
for loc in plan[1:]: # 이전 위치에서 L자로 이동했을 때 plan으로 이동할 수 있는지
    if(abs(x - int(loc[0])) == 2 and abs(y - int(loc[1])) == 1\
        or abs(x - int(loc[0])) == 1 and abs(y - int(loc[1])) == 2):
        x = int(loc[0])
        y = int(loc[1])
    else:
        result = "Invalid"
        break
        
    # break 했으면 L자로 이동 가능 한 곳
    board[int(loc[0])][int(loc[1])] = 1

for i in range(6):
    for j in range(6):
        if(board[i][j] == 0):
            result = 'Invalid'
            break
            

# print(*board, sep='\n')
print(result)