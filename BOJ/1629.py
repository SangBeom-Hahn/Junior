'''
자연수 a를 b번 곱한수를 구하자 이를 c로 나눈 나머지를 구하자

ex)
2**10 = 2**5 x 2**5
2**5 = 2**2 x 2**2 x 2
2**2 = 2**1 x 2**1
2**1 = 2

2**4 = 2**2 x 2**2
2**2 = 2**1 x 2**1 
2**1 = 2

1. 모경수(prt, n=1)
1) a**n x a**n = a**2n
2) 5 4 3 2 1 탑다운 방식 재귀

* a, b, c
출 : 
2. 시복 : logn

pow(a, b, c)
pow(2, 10, 2)
pow(2, 5, 2)

pow(2, 2, 2) return 2 * 2
pow(2, 1, 2) return 2

2**10 = 2**5 x 2**5
2**5 = 2**2 x 2**2 x 2
2**2 = 2**1 x 2**1
2**1 = 2

2**4 = 2**2 x 2**2
2**2 = 2**1 x 2**1 
2**1 = 2
'''


def pow(a, b, c):
    if(b == 1): return a % c
    
    val = pow(a, b//2, c)
    
    # print(a, b, val)
    if(b%2 == 0):
        return val * val % c
    else:
        return val * val * a % c
        

a, b, c = map(int, input().split())
print(pow(a, b, c))