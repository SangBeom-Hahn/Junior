'''
각 ai는 처리할 수 있는 고객 수와 운영에 필요한 비용이 다름

ex) 처리 가능한 고객 수
                        a   b   c
처리 가능한 고객 수      12  3   19
비용                    28  10  35

1. 모경수(prt, n=1)
1) 백으로 탐색(3가지 방법이 아니고 그냥 중복 순열 느낌)
2) 처리 가능한 고객 수 누적해가면서 고객 상담 수요를 충족했을 때 최소 비용 갱신

* 0~23시까지 고객 상담 요청 수
각 ai가 1시간 동안 처리할 수 있는 고객 수
각 ai 한 번 사용 시 필요 비용
출 : 고객 상담 수요를 충족시킬 최소 비용

2. n^3
'''

req = 23
can = [12, 3, 19]
cost = [28, 10, 35]
min_cost = int(1e9)

def back(can_customer_cnt, plus_cost):
    global min_cost
    
    if(can_customer_cnt >= req):
        if(min_cost > plus_cost):
            min_cost = plus_cost
        return
    
    for i in range(len(can)):
        back(can_customer_cnt + can[i], plus_cost + cost[i])
            
back(0, 0)
print(min_cost)