'''
운동
1] 맥박 T 증가
2] X+T <= M일때만 운동함

휴식
1] 맥박 R감소
2] x-r이 m보다 작으면 맥박이 m이 됨

초기 맥박 m, 운동을 N분 할거다.

1. 모경수(prt, n=1)
1) 운동을 할 수 있다? 무조건 운동함 cnt++
2) 못하면 휴식함
3) 운동과 휴식 둘다 시간 증가
4) 초기맥박 + T > M 면 -1

* N, m, M, T, R
출 : 운동 N분하는데 필요한 시간, N분 못하면 -1

2. n^3
'''

N, m, M, T, R = map(int, input().split())
cnt = 0
time = 0
start = m

if(m+T > M):
    print(-1)
else:
    while(True):
        if(cnt == N):
            print(time)
            break
        
        if(m+T <= M):
            cnt += 1
            m+=T
        else:
            m-=R
            if(m < start):
                m = start
        time += 1