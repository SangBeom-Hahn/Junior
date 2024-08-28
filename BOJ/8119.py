'''
nxn 크기의 정사각형, a는 상하좌우로 이동할 수 있으며, 시작은 1,1
계획서 : L R U D
공간을 벗어나는 움직임은 무시된다.

ex) r r r u d d

1. 모경수 (prt, n=1)
1) 현위치는 1, 1
2) 설명서를 보고 이동
3) 벗어나면 conti
4) 최종 공간 출력

* n : 공간의 크기
계획서

2. nlogn
'''

n = int(input())
plans = list(input().split())

x, y = 0, 0
d = {'U' : [-1, 0], 'D' : [1, 0], 'L' : [0, -1], 'R' : [0, 1]}

for ele in plans:
  nx = x + d[ele][0]
  ny = y + d[ele][1]
  
  if(nx < 0 or ny < 0 or nx >= n or ny >= n):
    continue
  
  x = nx
  y = ny
  
print(x+1, y+1)