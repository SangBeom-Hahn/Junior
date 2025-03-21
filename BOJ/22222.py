'''
두 묶음의 카드 수가 A, B 일 때 하나로 묶으려면 A+B번 비교가 필요하다.

1.모경수(prt, n=1)
1) 최소힙으로 관리
2) 2개를 꺼내서 합하고 다시 넣고, 합은 결과에 더함
3) 힙의 길이가 1이면 끝

* n : n개의 숫자 카드 묶음
n개의 숫자 카드 묶음의 크기

출 : 최소 비교 횟수

2. nlogn
'''

import heapq

n = int(input())
h = [int(input()) for _ in range(n)]

heapq.heapify(h)

result = 0
while(True):
    if(len(h) == 1):
        print(result)
        break
    
    one = heapq.heappop(h)
    two = heapq.heappop(h)
    
    hab = one + two
    result += hab
    heapq.heappush(h, hab)