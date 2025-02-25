'''
터널 입구, 출구에서 1분에 통과하는 차의 수 조사.

* n : 조사한 시간
m : 조사를 시작할 때 터널 안에 들어있는 차량의 수

n개의 입구를 통과한 차의 수와 출구를 통과한 차의 수

ex) n=3
0~1
1~2
2~3

1. 모경수(prt, n=1)
1) 최초 시점에 m개 있음
2) 0 ~ n 까지 매초마다 차가 들어오고 나감 = m에 +하고 -함
3) m이 1번이라도 0보다 작으면 0출력 끝
4) m의 최대값 갱신

출 : 터널에 차가 가장 많이 있었을 때 몇 대있는지
조사 시작하고 j분이 지난 시점에 터널 안 차 수 = Sj
Sj의 최대값 (터널 안에 있는 차량의 수가 0보다 작은 경우가 1번이라도 있으면 0)

ex) n=3
s0, s1, s2, s3의 최대값

2. nlogn
'''

n = int(input())
m = int(input())
result = m

# print("결과 : ", m)

for _ in range(n):
    come, out = map(int, input().split())
    m = m+come-out
    # print("결과 : ", m)
    
    if(m < 0):
        result = 0
        break
    
    if(result < m):
        result = m
        
print(result)        