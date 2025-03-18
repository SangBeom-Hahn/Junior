'''
1 ~ n 수를 오름차순으로 넣었다가 빼서 수열을 만들 수 있음

ex)  수열 = 4 3 6 8 7 5 2 1
오름차순 수     수열 수     스택
1               4           1 푸시
2                           12 푸시
3                           123  푸시
4                           1234 푸시
5                           123 / 4 팝
                            
5               3           12 / 3팝
5               6           125 푸시
6                           1256 푸시
7                           125 팝

7               8           1257 푸시
8                           12578 퓨시
                            팝
                            팝
                            팝
                            팝
                            팝
                            
ex)  수열 = 1 2 5 3 4
오름차순 수     수열 수     스택                           
1               1           1 푸시
2                           [] 팝
2               2           2 푸시
3                            [] 팝
3               5           3 푸시
4
5                           3 4 5
                            3 4 팝
                3



1. 모경수(prt, n=1)
1) 수열수는 idx를 기록해서 하나씩 보고, 다 보면 끝
ok 2) 오름차순 수는 1부터 증가
ok 3) 스택 헤드 < 수열 수 -> 스택에 푸시 + 오름차순 수 ++
ok 4) 스택 헤드 == 수열 수 -> 팝, 수열수 idx ++
ok 5) 스택 헤드 > 수열 수 -> ex) 5 > 2면 이미 그 수열 수는 스택에 있을거고 2를 뺴기 위해선
5를 빼야해서 불가능 NO 끝
6) 스택에는 숫자를 저장, 결과에 연산 저장


* n 
수열을 이루는 1~n 정수
출 : 수열을 만들기 위한 연산 / 불가하면 NO

2. nlogn
'''

n = int(input())
nums = [int(input()) for _ in range(n)]

stack = []
result = []

idx = 0 # 수열 수 idx
increase_num = 1 # 오름차순 수

while(True):
    if(idx == n):
        for ele in result:
            print(ele)
        break
    
    if(not stack):
        stack.append(increase_num)
        increase_num += 1
        result.append('+')
    else:
        if(stack[-1] < nums[idx]):
            stack.append(increase_num)
            increase_num += 1
            result.append('+')
        elif(stack[-1] == nums[idx]):
            stack.pop()
            idx += 1
            result.append('-')
        elif(stack[-1] > nums[idx]):
            print("NO")
            break