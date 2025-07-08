'''
k : 사람과 점원의 거리
k이상 손을 뻗은 사람이 결제한다.

과정
1] 1 ~ n번 순으로 손을 뻗는다.
2] 1 ~ n번 순으로 손을 추가로 뻗는다.
3] 손을 뻗는 것은 열 고정, 행 증가로 이루어진다.

ex)
1번     3       +5
2번     1       +8
3번     1
4번     1

1. 모경수(prt, n=1)
1) 0번부터 시작하는 사람의 뻗은 거리를 더할 배열을 0으로 초기화
2) 열고정 행증가로 값을 더함
0행 0열 1열 2열
1행 1열 2열 3열 이런 방식

3) 더한 값이 k이상이면 그 행+1, 그열+1이 답

* n, m, k : 1 ~ n번이 행이다. 각각 m번씩 손을 뻗는다.
각 수

출 : 결제한 사람, 그 사람이 손을 뻗은 횟수

2. n^2
'''

n, m, k = map(int, input().split())
hands = [list(map(int, input().split())) for _ in range(n)]

dis = [0] * n
flag = False

for y in range(m):
    for x in range(n):
        dis[x] += hands[x][y]
        
        if(dis[x] >= k):
            print(x+1, y+1)
            flag = True
            break
    
    if(flag == True):
        break