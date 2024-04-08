'''
다솜 기계는 각 사람이 누구를 찍을 지 미리 읽을 수 있다. 어떤 사람이 누구를 찍을 지
정했으면 반드시 선거때 그 사람을 찍는다. 국회의원 후보는 n명이다. 기계를 이용해서
마을 주민 M 명의 마음을 모두 읽었다. 다솜이는 기호 1번인데 자신을 찍지 않은 사람을
돈으로 매수해 당선되고자 한다. 다른 모든 사람의 득표수보다 많은 득수를 가질 때 당선도니다.

ex) 
1번     2번     3번     cnt
5       7       7
5+1+1   7-1     7-1 하면 당선된다. = 2명 매수하면 됨

5       7       7       0
6       6(7-1)  7       1
7       6       6       2

1. 모경수(prt, n=1)
1) bfs로 방문 탐색(비커 유형)
2) 현 상태에서 시작해서 다른 후보의 득표수를 가져오다가 다소미가 제일 크면 끝
    1] 큐에 넣는 조건 : 그냥 다른 후보의 득표수가 0보다 크면 뺏는다.

* n : 후보의 수
1~n 후보를 찍으려는 사람의 수
출력 : 다송미가 매수해야하는 사람의 최소값 ㄱㄱ

3) 백으로 탐색?? -> 이렇게 해도 최소값을 찾을 수 있나?



2. 시복 n^3
'''

def back(candis, cnt):
    global min_cnt
    
    me = candis[0]
    for i in range(1, len(candis)):
        if(me <= candis[i]):
            break
    else:
        if(cnt != 0 and min_cnt > cnt):
            min_cnt = cnt
            return
    
    for i in range(1, len(candis)):
        if(candis[i] > 0):
            candis[0] += 1
            candis[i] -= 1
            back(candis, cnt+1)
            candis[0] -= 1
            candis[i] += 1
            
min_cnt = 10000
n = int(input())
candis = [int(input()) for _ in range(n)]

if(len(candis) == 1):
    min_cnt = 0
else:
    back(candis, 0)
print(min_cnt)