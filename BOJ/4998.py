'''
N원이 있고 1년 마다 B% 이자를 적립함.
몇 년이 지나면 돈이 M원이 넘을지 궁금함.

ex)
N       B       M
200     6.5     300


1. 모경수(prt, n=1)
ok 0) 입력의 길이를 먼저 구해서 테게 수를 구하고 진행해야 한다.
ok 1) 초기 년은 0으로 시작
2) 이자를 붙임
3) 초기 년 ++
4) N > M 이면 끝

* N, B, M
출 : 각 테케에서 M원을 넘으려면 몇 년이 걸리는지

2. nlogn
'''

# print(100 + 100 * 10 / 100)

while(True):
    try:
        inputs = input()
        n, b, m = map(float, inputs.split())
        start_year = 0
        
        while(True):
            n = n + n * b / 100
            start_year += 1
            
            if(n > m):
                print(start_year)
                break
    except:
        break