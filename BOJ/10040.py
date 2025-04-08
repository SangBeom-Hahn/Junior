'''
후보
1] n개를 재미있는 순서대로 나열
2] Ai = i번째 경기 개최 비용
3] Bj = j번째 위원의 심사기준
4] 개최 비용이 Bj를 넘지 않는 경기 중 가장 재밌는 경기 
= 재미순 나열 된 경기에서 Bj를 넘지 않는 경기 중 가장 앞에 있는 거

ex) 
경기 5 3 1 4 / 심사기준 4 3 2

위원    투표
1       2번째
2       2번쨰
3       3번째

1. 모경수(prt, n=1)
ok 1) n^2으로
ok 2) result = 경기 길이 만큼 0으로 초기화 배열
2) 위원 순회
    1] 경기 순회
    2] 기준 >= 비용 것 만나면 result에 표기 후 바로 break
3) result max에 해당하는 인덱스 + 1
    

* n, m = 경기의 수, 위원의 수
n개의 개최 비용
m개의 심사 기준

출 : 가장 많은 표를 획득한 경기 (1번부터 시작)

2. nlogn
'''

n, m = map(int, input().split())
games = [int(input()) for _ in range(n)]
stands = [int(input()) for _ in range(m)]
result = [0] * n

for stand in stands:
    for i in range(n):
        if(stand >= games[i]):
            result[i] += 1
            break
        
print(result.index(max(result)) + 1)