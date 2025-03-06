'''
게임 절차
1) N개의 컵이 일렬, X번째 컵에 공
2) K번 스왑
3) 참가자가 몇 번째 컵에 공이 있나 추측

1. 모경수(prt, n=1)
1) 공의 위치를 x번째 컵으로 기록
2) k번 스왑하는데 공이 있는 컵이면 공의 위치 갱신
3) 출력

* N
X(1번부터 시작)
K 
K개의 바꾼 컵의 위치
출 : 공이 있는 컵의 위치 정수 (1부터 시작)

2. nlogn
'''
import sys

input = sys.stdin.readline

n, x, k = map(int, input().split()) # x번째 컵이 공
for _ in range(k):
    a, b = map(int, input().split())
    if(a == x):
        x = b
    elif(b == x):
        x = a
        
print(x)        
