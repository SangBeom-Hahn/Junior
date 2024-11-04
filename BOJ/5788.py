'''
만들어야 하는 커피 1 ~ M번 M잔이 있다.

규칙 : 
1) 최대 n잔까지 동시에 추출할 수 있음
2) 주문 번호 순으로 빈 커피 추출구에서 커피를 만듬
3) 빈 추출구가 없으면 대기, 있으면 즉시 만듬

1. 모경수(prt)
1) 힙으로 n개만큼 넣어서, 완성된 커피 개수를 추적해서 커피 개수가 m과 같지 않을 동안 진행
2) 힙에 (시간, 주문번호) 로 넣음
3) 시간은 처음에 넣을 땐 0+커피완료 시간 
    1] 이후엔 pop한 것의 시간+지금 넣을 커피 완료 시간
    2] 팝을 할때 완성된 커피 개수를 증가시키고 m과 같으면 바로 끝내서 pop 에러 안 뜨게

* n : 커피 추출구 개수
coffee_times : 각 커피를 만드는데 걸리는 시간, 주문 순서대로 담김
출 : 커피가 완성되는 순서대로 주문 번호를 반환(커피 완성되는 순서가 같으면 작은 주문 번호가 앞)

2. nlogn
'''

import heapq

n = 1
coffee_times = [4, 2, 2, 5, 3]
m = 5

h = []
complete_cnt = 0

for i in range(n):
    heapq.heappush(h, (coffee_times[i], i+1))
    
print(h)    
result = []
curr_push_idx = n # m보다 크거나 같으면 그만 넣음
while(True):
    # 1] 이후엔 pop한 것의 시간+지금 넣을 커피 완료 시간
    # 2] 팝을 할때 완성된 커피 개수를 증가시키고 m과 같으면 바로 끝내서 pop 에러 안 뜨게
    time, num = heapq.heappop(h)
    result.append(num)
    
    complete_cnt += 1
    if(complete_cnt == m):
        break
    
    if(curr_push_idx < m):
        heapq.heappush(h, (time+coffee_times[curr_push_idx], curr_push_idx+1))
        curr_push_idx += 1
    
print(h)
print(result)