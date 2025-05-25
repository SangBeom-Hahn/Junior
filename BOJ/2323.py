'''
크기 N 수열 A
인접한 두 원소의 차를 이용해서 수열 B를 만든다.

ex) a = 5 6 3 9 -1
b = 
6 - 5 = 1
3 - 6 = -3
9 - 3 = 6
-1 - 9 = -10

b[i] = a[i+1] - a[i]

위 방법을 k번 했을 때 나오는 수열 구하기

1. 모경수(prt, n=1)
1) a를 b로 변형한다.
2) 변형한 것을 다시 a로 하여 k번 변형한다.

* n, k : 수열의 크기, k번 함
수열(컴마로 구분)

출 : k번 변형한 수열을 ,로 구분해서 출력
2. n^3

'''
from math import sqrt
def solution(r1, r2):
    cnt = r2 - r1 + 1
    
    for x in range(1, r2):
        one = sqrt(r2**2 - x**2)
        two = sqrt(r1**2 - x**2)
        print(two)
        cnt += (int(one) - int(two))
    
    
      
    print(cnt * 4)
    # return cnt * 4
    
solution(1, 100)