'''
n by n 크기의 정사각형이 있다. 상하좌우로 이동할 수 이씅며, 시작좌표는 1, 1이다. 여행가가 이동할
계획서가 있다. 공간을 벗어나는 움직임은 무시된다. 

1. 모경수
1) 시작 위치에서 계획서대로 이동함
2) 공간을 벗어나면 무시하고 다음 계획을 봄
3) 모든 계획으로 이동하면 끝

* n : 공간의 크기
계획서 

출력 : 결과 좌표
'''

n = int(input())
plans = input().split()

# print(plan)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
d_word = ['U', 'D', 'L', 'R']

'''
1) 시작 위치에서 계획서대로 이동함
2) 공간을 벗어나면 무시하고 다음 계획을 봄
3) 모든 계획으로 이동하면 끝
'''

x, y = 0, 0
for plan in plans:
    # 계획서의 글자와 방향을 매칭해야함
    d_idx = d_word.index(plan)
    
    nx = x + dx[d_idx]
    ny = y + dy[d_idx]
    
    # 무시
    if(nx < 0 or ny < 0 or nx >= n or ny >= n):
        continue
    x = nx
    y = ny
    
print(x+1, y+1)