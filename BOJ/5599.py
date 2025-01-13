'''
1 x n 지도에 1, x에 구사과 있음
가사과 이동패턴
1) 지도의 각 칸에 e, w
2) 구사가 위치 1, x일 때
    1] 지도에 e = x+1
    2] w = x-1로 순간이동
구사과가 이동을 시작하는 위치와 관계없이 선물을 주는 방법을 알아내자

선물이 놓인 칸에 구사과가 가면 선물을 가져간다.
최소 몇 개의 칸 위에 선물을 놓으면 구사과가 항상 선물을 가져가는 지 구하라

ex) eewwew
구사과 시작 열          이동열
0                       0 1 2 
1                       1 2
2                       2 1
3                       3 2 1

4                       4 5
5                       5 4


eeeew
구사과 시작 열          이동열
0                       0 1 2 3 4
1                       1 2 3 4
2                       2 3 4
3                       3 4
4                       4 3

ewwww
구사과 시작 열          이동열
0                       0 1
1                       1 0
2                       2 1 0

1. 모경수
1) bfs 모든 시작 열
    4) 방문 체크
        1] 현재 방문한 건지, 이미 방문 했던 건지를 구분해야함
        1] 현재 방문 1
        2] 과거 방문 2
    5) 현재 방문도 과거 방문도 아니면 현재 방문으로 처리
    6) 과거 방문만나면 그 묶음에 포함되는 거임
    7) 현재 방문 만나면 한번 도 visit을 안만난다는 거임 결과 ++
        1] 현재 방문한 것들을 과거 방문 상태로 표기
    
2) 언제 종료?
    방문 한 곳을 큐에 안 넣으면 끝나겠지?

* n : 1 x n
지도
출 : 최소 몇 개의 칸에 선물을 놓아야 하는지

2. n^2

'''
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visit[start] = 1
    global result
    
    # 4) 방문 체크
    #     1] 현재 방문한 건지, 이미 방문 했던 건지를 구분해야함
    #     1] 현재 방문 1
    #     2] 과거 방문 2
    # 5) 현재 방문도 과거 방문도 아니면 현재 방문으로 처리
    # 6) 과거 방문 만나면 그 묶음에 포함되는 거임
    # 7) 현재 방문 만나면 한번도 visit을 안만난다는 거임 결과 ++
    #     1] 현재 방문한 것들을 과거 방문 상태로 표기    
    
    while(q):
        x = q.popleft()
        if(mapp[x] == 'E'):
            nx = x+1
        else:
            nx = x-1
            
        if(visit[nx] == 2):
            break # 무조건 while 끝 나고 for문 거쳐야 함
        
        if(visit[nx] == 1):
            result += 1
            break
            
        if(not visit[nx]):
            q.append(nx)
            visit[nx] = 1
            
    for i in range(n):
        if(visit[i] == 1):
            visit[i] = 2
        

n = int(input())
mapp = input()
visit = [False] * n
result = 0

for i in range(n):
# for i in range(6):
    if(not visit[i]): # 이미 방문한 곳은 포함되는 거임
        bfs(i)

# print(visit)        
print(result)