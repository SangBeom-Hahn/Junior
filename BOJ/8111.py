'''
8x8 좌표이다. 나는 L자로만 이동가능, 정원 밖 못감
나가 이동할 수 있는 경우의 수를 구하라
행 : 1 ~ 8
열 : a ~ h

1. 모경수(n=1, prt)
1) 입력
2) 8가지로 이동해 보면서 가능한 경우 세기

* 현재 나이트 위치 열, 행
출력 : 나이트가 이동할 수 있는 경우의 수

2. 시복 : n^3
'''

loc = input()
x = int(ord(loc[0])) - int(ord('a'))
y = int(loc[1]) - 1
cnt = 0
dx = [-2, -2, -1, 2, 2, 2, 1, -1]
dy = [-1, 1, 2, 1, 1, -1, -2, -2]

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if(nx < 0 or ny < 0 or nx >= 8 or ny >= 8):
        continue
    
    cnt += 1
print(cnt)