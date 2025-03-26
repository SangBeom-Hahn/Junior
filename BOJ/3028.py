'''
N번째 큰 수를 구하라

ex) 힙 7 9 12
헤드    현재 수     힙
7       15          7 팝, 15 푸시
                    9 12 15

1. 모경수(prt, n=1)
1) 길이 n 자리 최소 힙에서 힙[0]가 n번째 큰수다.
ok 2) 길이 n짜리 힙 만듬
3) 그 아래 수 비교
    ok 1] 힙 헤드 > 현재수 : 무시
    2] < : 힙 헤드는 절대로 n번째 큰수가 안됨
        1] 힙헤드 팝, 현재 수 푸시
        
4) 전부 다 순회하고 힙헤드 출력        

* N : NxN
N개의 줄에 N개의 수

출 : N번째 큰수

2. nlogn
'''

n = int(input())

import heapq

h = list(map(int, input().split()))
heapq.heapify(h)

print(h)

for _ in range(n-1):
    for ele in list(map(int, input().split())):
        if(h[0] > ele):
            pass
        else:
            heapq.heappop(h)
            heapq.heappush(h, ele)
            

print(h)            
print(h[0])