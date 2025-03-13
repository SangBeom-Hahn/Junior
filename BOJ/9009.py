'''
감소하는 수 : 가장 큰 자릿수부터 작은 자릿수까지 감소

ex) 321, 950
322, 958 = 감소수 x

번째    수
0       0
1       1
9       9
10      10
11      20
11      21

1. 모경수(prt, n=1)
1) 0 ~ 9의 수로 길이 1 ~ 10의 조합을 구함

* n : 
출 : n번째 감소하는 수 (0=0번째, 1=1번째) / 없으면 -1

2. nlogn
'''

n = int(input())
from itertools import combinations

combs = []
for i in range(1, 10):
    for comb in list(combinations(range(0, 10), i)):
        comb = list(comb)
        comb.sort(reverse=True)
        comb = ''.join(list(map(str, comb)))
        
        combs.append(int(comb))

combs.sort()
print(combs[n])