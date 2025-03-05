'''
n   cn
1   26
2   13
3   40

1. 모경수(prt, n=1)
1) n = 1로 시작해서 1씩 증가
2) x = c1로 계속 갱신 할 거임
3) x가 짝수면, 홀수면 갱신
4) x가 1일때 n 출력

* C(1) : 초항
출 : Cn이 처음으로 1이 되는 n

2. nlogn
'''

x = int(input())
n = 1

while(True):
    if(x == 1):
        print(n)
        break
    
    if(x % 2 == 0):
        x = x//2
    else:
        x = 3 * x + 1
    n += 1