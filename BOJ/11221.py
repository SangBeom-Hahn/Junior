'''
매일 하는 행동 : 
1) 주식 하나를 산다.
2) 원하는 만큼 가지고 있는 주식을 판다.
3) 아무것도 안한다.
위 3가지중 하나를 한다. 날별로 주식의 가격을 알고 있을 때 최대 이익이 되는지 
알고싶다.

ex) 
날수    날별 주가   
3       10, 7, 6
주가가 계속 감소하므로 최대 이익은 0

        3 5 9
처음 두 날에 주식을 하나씩 사고, 마지막 날에 팔아서 9-3/9-6 = 10

5       3 5 9 6 2 


1. 모경수
0) 최대로 비싼 날보다 현재가 크거나 같으면 아무것도 하지마
1) 최대로 비싼 거 어캐 구해? 힙으로
2) 최대로 비싼 날보다 현재가 작으면 최대로 비싼 날에서 뺴서 결과에 더해
3) 최대로 비싼 날을 pop했는데 현재보다 이전이야 그럼 다시 pop해

1) 다음 날에 오르면 (3 > 5)
    1] 주식을 사
    2] 다음날이 마지막 날이면?

2) 다음날에 떨어지면
    1] 마지막날까지 안 오르면 아무것도 하지마 (=최초 번돈 0에서 변동 x)
    2] 마지막날까지 오르면 


* t : 테케수
날의 수
날별 주가들
출력 : 최대 이익을 구하라

2. 시복 nlogn
'''

# 5       3 5 9 6 2
# 0) 최대로 비싼 날보다 현재가 크거나 같으면 아무것도 하지마
# 1) 최대로 비싼 거 어캐 구해? 힙으로
# 2) 최대로 비싼 날보다 현재가 작으면 최대로 비싼 날에서 뺴서 결과에 더해
# 3) 최대로 비싼 날을 pop했는데 현재보다 이전이야 그럼 다시 pop해

# 솔루션 내가 맥스보다 작으면 팔아 내가 맥스보다 크면 내가 맥스가 돼
# 근데 이걸 앞에서부터 하면 
import heapq
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    dayCnt = int(input())
    moneys = list(map(int, input().split()))
    h = []

    for i in range(len(moneys)):
        heapq.heappush(h, (-moneys[i], i))
        
    # print(h)
    result = 0
    maxIdx = -1
    for todayIdx, ele in enumerate(moneys):
        while(maxIdx < todayIdx):
            maxMoney, maxIdx = heapq.heappop(h)
            maxMoney *= -1
        
        if(maxMoney <= ele):
            continue
        elif(maxMoney > ele):
            result += (maxMoney-ele)
            
    print(result)