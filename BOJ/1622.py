'''
게임
1] 정수를 하나 외침
2] 지금까지 말한 수 중 중간값을 말함.
3] 지금까지 말한 수의 개수 = 짝수 -> 중간 2 수 중 작은 수 말함.

ex) 1 5 2 10 -99 7 5
말한 수                                 중간값
1                                       1
5                                       1 -> 짝수면 더 작은 수
2                                       2
10                                      (1, 2, 5, 10) 2
-99                                   -99 2
7                                   -99 1 2 5 7 10 / 2
5                                   -99 1 2 5 5 7 10 / 5  

말한수  왼쪽힙              오른쪽힙        중간값 = 왼쪽힙 헤드
1       1                   []          1
5       1                   5           1
2       1 2                 5           2
10      1 2                 5 10        2
-99     -99 1 2             5 10        2
7       -99 1 2             5 7 10      2
5       -99 1 2 5           5 7 10      5


ex) 1 5 2 10 12

말한수  왼쪽힙              오른쪽힙        중간값 = 왼쪽힙 헤드
1       1                   []          1
5       1                   5           1
2       1 2                 5           2
10      1 2                 5 10        2
12      1 2 12              5 10        12

1. 모경수(prt, n=1)
1) 왼쪽힙 = 최대힙으로 중간 이하의 수
2) 오른쪽힙 = 최소힙으로 중간 초과의 수
3) 쩍수개면 더 작은게 중간수니 더 작은게 들어가는 왼쪽힙의 헤드가 중간값임.
3) 짝수개면 더 작은 수를 말하기 위해서 왼쪽힙에 넣음
4) 홀수개면 걍 반대로 오른쪽힙에 넣음
5) 넣고 나서 체크
    1] 왼쪽힙 헤드 > 오른쪽힙 헤드
    2] 교환

* n : 말하는 수의 개수
말하는 n개의 정수
출 : 중간값 n번

2. nlogn

'''

import heapq

n = int(input())
left = []
right = []

for _ in range(n):
    num = int(input())
    
    if(len(left) == len(right)):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)
        
    if(right and -left[0] > right[0]):
        l = heapq.heappop(left)
        r = heapq.heappop(right)
        heapq.heappush(right, -l)
        heapq.heappush(left, -r)
        
    
    print(-left[0])