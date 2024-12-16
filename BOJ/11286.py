'''
절대값 힙
1) 배열에 0이 아닌 정수를 넣음
2) 절대값이 가장 작은 값을 제거 후 출력
    1] 절대값이 가장 작은 값이 2개면 음수 출력하고 제거 / ex) -9, 9

1. 모경수(prt, n=1)
1) 0이면 팝, 출력
2) 0인데 배열이 비어있으면 0출력
3) 0이 아니면, (절대값, 원본값) 
    
* n : 연산의 개수
n개의 연산 정보(0이 아니면 푸시, 0 = 제거)    
출 : 제거 횟수만큼 출력(배열이 비어있는데 제거 연산 = 0출력)

2. nlogn
'''

import heapq
import sys
input = sys.stdin.readline

n = int(input().strip())
h = []

for ele in range(n):
    value = int(input().strip())
    if(value == 0):
        if(len(h) == 0):
            print(0)
        else:
            _, pop_v = heapq.heappop(h)
            print(pop_v)
    else:
        heapq.heappush(h, (abs(value), value))