'''
N개의 수와 N-1개 연산자 (+, -, *, %)
주어진 수의 순서를 바꾸지 않고 연산자를 하나씩 넣어수 수식 만듬

ex) 1 2 3 4 5 6
+ + - * %

연산자를 순열로 계산하면 60개의 수식을 만들 수 있음

계산 : 
1] 우선순위를 무시하고 앞에서부터 진행한다.
2] 나눗셈은 몫만 취하고
2] 음수를 양수로 나누면 음수를 양수로 바꾸고 -> 몫 구하고 -> 음수로

1. 모경수(prt, n=1)
ok 1) 연산자 배열을 만들어
2) n-1 크기로 수열을 구함 + 중복 제거
3) 수열을 순회해서 결과 계산

* n : 수의 개수
수
+, -, *, % 의 개수

출 : 만들 수 있는 수식 결과의 최대값, 최소값
2. n^3
'''

n = int(input())
nums = list(map(int, input().split()))
calc_cnt = list(map(int, input().split()))
types = ['+', '-', '*', '%']

calcs = []
for i in range(4):
    for _ in range(calc_cnt[i]):
        calcs.append(types[i])
        
# print(calcs)

from itertools import permutations

# 중복이 나와도 상관 없어도 set으로 제거하는게 좋음~~
perms = set(list(permutations(calcs, n-1)))
# print(len(perms))

min_result = int(1e9)
max_result = -int(1e9)

# 수열을 순회해서 결과 계산
for perm in perms:
    result = nums[0]
    for i in range(n-1):
        calc = perm[i]
        
        if(calc == '+'):
            result += nums[i+1]
            
        elif(calc == '-'):
            result -= nums[i+1]
            
        elif(calc == '*'):
            result *= nums[i+1]
            
        elif(calc == '%'):
            if(result < 0):
                result *= -1
                result //= nums[i+1]
                result *= -1
            else:
                result //= nums[i+1]
    
    if(min_result > result):
        min_result = result
    
    if(max_result < result):
        max_result = result

print(max_result)         
print(min_result)        