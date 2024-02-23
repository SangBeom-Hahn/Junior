''''

ex)
일      1  2  3  4  5  6  7  8  9
prices 10, 7, 8, 5, 8, 7, 6, 2, 9
k = 3

4일에 5원에 k주인 3주 매수하고 
8(5일), 7(6일), 9(9일)원일 때 팔면 9원 이익 발생

1. 모경수(prt, n=1)
1) for문 돌면서 prices 요소 하나씩 봄
2) 내부에 while문 함
3) for문 요소 + 1부터 끝까지 최대힙 만듬
4) k개 뽑아서 최대값 갱신

* prices : 종목 가격 배열
k : 분할 매도 일수
출력 : 해당 기간 중 하루에 k주를 매수 후 k일에 걸쳐 분할 매도했을 때 가장 높은 기대 수익
수익이 없으면 -1 출력

2. 시복 : nlogn

'''

import heapq

# prices = [10, 7, 8, 5, 8, 7, 6, 2, 9]
# k = 3

prices = [10, 7, 8, 5, 6, 4, 3, 2, 3]
k = 3

leng = len(prices)
max_price = 0

# for문 돌면서 prices 요소 하나씩 봄
for i in range(leng-k): # 이후 k개 매도할 수 없으면 안봄
# for i in range(3, 4): # 이후 k개 매도할 수 없으면 안봄
    print(prices[i])
#     내부에 while문 함
# 3) for문 요소 + 1부터 끝까지 최대힙 만듬
    h = [ele * -1 for ele in prices[i+1:]]
    print(h)
    heapq.heapify(h)
    # k개 뽑아서 최대값 갱신
    buy_price = prices[i] # 산 가격
    each_price = 0# 각 매도 최대 가격
    for _ in range(k):
        sell_price = heapq.heappop(h) * -1
        each_price += (sell_price - buy_price)
        
        print((sell_price - buy_price))
    
    max_price = max(max_price, each_price)
    

print(max_price)