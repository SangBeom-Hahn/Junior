'''
정수를 하나씩 외칠때마다 동생은 지금까지 말한 수 중에서 중간값을 말함
지금까지 외친 수가 짝수라면 중간 수 두 수 중에서 작은 수

ex)
1                               1
1 5                             1
1 2 5                           2
1 1 2 5                         1

1. 모경수(prt, n=1)
1) 왼쪽 최대힙, 오른쪽 최소힙
2) 짝수 : 최대힙에 넣고 최대힙 헤드 출력
3) 홀수 : 최소힙에 넣고 최대힙 헤드 출력 (홀수에서 넣으면 짝수가 될텐데 짝수중 작은 수)

4) 넣고 난 후 최대힙 헤드와 최소힙 헤드를 비교
    1] 최대힙 헤드 > 최소힙 헤드 면 둘이 교환

* n : 외치는 정수의 개수
n줄의 외치는 정수
출 : 동생이 말해야 하는 수를 구하라 (지금까지 말한 수 들의 중간값)

2. nlogn
'''
import heapq
import sys

input = sys.stdin.readline

n = int(input().strip())
left_h = []
right_h = []

for _ in range(n):
    num = int(input().strip())
    
    if(len(left_h) == len(right_h)):
        heapq.heappush(left_h, -num)
    else:
        heapq.heappush(right_h, num)
        
    if(right_h and -left_h[0] > right_h[0]):
        max_v = -heapq.heappop(left_h)
        min_v = heapq.heappop(right_h)
        
        heapq.heappush(left_h, -min_v)
        heapq.heappush(right_h, max_v)
    
    
    print(-left_h[0])
    # print(left_h)
    # print(right_h)