'''
수열
1] n : 짝수 = n을 2로 나눔
2] n : 홀수 = 3 곱하고 1 더하기

3] 4, 2, 1이 나오면 끝난다. (4로 시작하면 무조건 4가 가장 큰 수열 요소이다.)

1. 모경수(prt, n=1)
1) 쭉 수열을 진행한다. for문 1개
2) 진행을 할 때마다 최대값을 갱싢나다.
2) 4를 만나면 끝낸다.

* t : 테케수
t 개의 수열 시작값 n
출 : 테케마다 가장 큰 값

2. nlogn
'''

t = int(input())
import sys

input = sys.stdin.readline

for _ in range(t):
    n = int(input().strip())
    max_result = n
    
    while(True):
        if(n == 1):
            print(max_result)
            break
        
        if(n % 2 == 0):
            n = n // 2
        else:
            n = n * 3 + 1
            
        if(max_result < n):
            max_result = n
            
        