'''
거점에서 썰매에 선물을 충전한다. 
착한 아이를 만나면 가장 가치가 큰 선물을 선물한다.

아이들 순서, 거점 정보가 주어질 때, 준 선물들의 가치를 출력

1. 모경수(prt, n=1)
1) 입력을 순회
2) 0이면 힙이 비어있으면 -1출력, 아니면 최대힙 출력
3) 0이 아니면 최대힙 채움


* n : 아이들가 거점지 방문 횟수
n개의 줄 : a, a개의 숫자 -> a : 거점지에서 a개의 선물을 충전, a개의 숫자 : 선물의 가치

a: 0 -> 거점지가 아니라 아이들을 만난 것이다.
출 : a가 0일때맏 아이드레게 준 선물의 가치 출력, 선물이 비어있으면 -1 출력

2. nlogn

'''
import heapq

n = int(input())
h = []

for _ in range(n):
    inputs = list(map(int, input().split()))
    if(inputs[0] == 0):
        if(not h):
            print(-1)
        else:
            print(-heapq.heappop(h))
    else:
        for ele in inputs[1:]:
            heapq.heappush(h, -ele)