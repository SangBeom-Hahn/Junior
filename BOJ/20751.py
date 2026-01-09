'''
nxn 표에 수가 있음

1. 모경수(prt, n=1)
1) 모든 수를 훑음
2) 길이 n인 힙을 유지함
    1] 길이가 n보다 작으면 푸시
    2] 길이가 n이면
        1] 현재들어오려는 수 < 힙헤드 -> 패스
        2] > -> 힙헤드팝, 현재수 푸시
3) 전체 다 훑은 후 힙헤드가 n번째 작은 수임

* n
nxn 표 상태
출 : n번째 큰수

2. nlogn
'''
import heapq

n = int(input())
h = []

for _ in range(n):
    nums = list(map(int, input().split()))
    for num in nums:
        if(len(h) < n):
            heapq.heappush(h, num)
        elif(len(h) == n):
            if(num < h[0]):
                pass
            else:
                heapq.heappop(h)
                heapq.heappush(h, num)
               
print(h[0])