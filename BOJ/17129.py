'''
N마리 소가 동그랗게 쉬고 있다. 각 소에 품질점수 있다.
연속 4마리 소들의 품질 점수를 곱한 값을 모두 더한다.
q번에 걸쳐 i번째 소를 선택하고 품질 점수에 -1를 곱한다.

ex) 3번소 바꿈
-2 3 -5 -6 10 -8 7 6

1. 모경수(prt, n=1)
1) 원본 소 품질 점수에서 4마리씩 곱한 품질 점수의 곱을 다 구함 총 n개 겠지
2) 선택한 소의 번호를 포함한 품질 점수의 곲에 -1을 곱함
    1] 품질 점수의 곱 n개에서 바꾼 소의 번호의 품질 점수의 곱부터 -1해서 총 4번의
    품질 점수의 곱을 -1 곱하면 됨
3) 바꿀때마다 품질 점수의 곱의 합을 구함

ex) 4번 소 선택
1 2 3 4 = 바꿈
2 3 4 5 = 바꿈
3 4 5 6 = 바꿈
4 5 6 7 = 바꿈
5 6 7 8
6 7 8 1
7 8 1 2
8 1 2 3 

1 = 1, 8, 7, 6
2 = 2, 1, 8, 7
3 = 3, 2, 1, 8

* n : 소의 수
q : 욱제가 번호를 바꿀 횟수
N마리의 품질 점수
q개의 번호를 바꿀 소의 번호
출 : q개에 걸쳐 다시 계산된 s

2. nlogn
'''

import sys
input = sys.stdin.readline

n, q = map(int, input().split())
quality = list(map(int, input().split()))
change_nums = list(map(int, input().split()))

# 1) 원본 소 품질 점수에서 4마리씩 곱한 품질 점수의 곱을 다 구함 총 n개 겠지
calc = [0] * n
for i in range(n):
    hab = 1
    for idx in range(4):
        # print((i + idx) % n, end = ' ')
        hab *= quality[(i + idx) % n]
    calc[i] = hab
#     print()
# print(calc)        

# 2) 선택한 소의 번호를 포함한 품질 점수의 곲에 -1을 곱함
#     1] 품질 점수의 곱 n개에서 바꾼 소의 번호의 품질 점수의 곱부터 -1해서 총 4번의
#     품질 점수의 곱을 -1 곱하면 됨
# 1 = 1, 8, 7, 6
# 2 = 2, 1, 8, 7
# 3 = 3, 2, 1, 8
for num in change_nums:
    num -= 1
    
    for i in range(4):
        calc[(num - i + n) % n] *= -1
        
    print(sum(calc))

# 3) 바꿀때마다 품질 점수의 곱의 합을 구함