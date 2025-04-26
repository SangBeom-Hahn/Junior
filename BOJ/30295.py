'''
x일 동안 매일 1문제 이상을 풀면 = 스트릭 x / 1일 = 스트릭 1

프리즈
1] 문제를 안 푼날 자동 사용
2] 스트릭이 늘어나지 x, 끊기지 x
3] 최대 1개 장착
4] 사용 후 이틀 후 다시 장착
5] 최초엔 장착한 채로 시작

1. 모경수(prt, n=1)
ok 1) 프리즈 보유 여부, 스트릭, 이틀 체크
2) 문제를 푼날
    1] 스트릭 ++
3) 문제를 안 푼날
    1] 프리즈 있음
        0] 프리즈 사용
        1] 스트릭 고정
        2] 이틀 진행
    2] 프리즈 없어
        1] 최장 스트릭 갱신

* N
푼 문제 수

출 : 최장 스트릭

2. n^2

'''

# 1) 프리즈 보유 여부, 스트릭, 이틀 체크
freeze = True
strick = 0
result = 0
two_flag = False
two = 0


# ok 2) 문제를 푼날
#     1] 스트릭 ++
# 3) 문제를 안 푼날
#     1] 프리즈 있음
#         0] 프리즈 사용
#         1] 스트릭 고정
#         2] 이틀 진행
#     2] 프리즈 없어
#         1] 최장 스트릭 갱신

n = int(input())
arr = list(map(int, input().split()))

for ele in arr:
    if(two_flag == True):
        two += 1
        
        if(two == 2):
            freeze = True
            two_flag = False
            two = 0
    
    if(ele >= 1):
        strick += 1
    else:
        if(freeze == True):
            freeze = False
            two_flag = True
        else:
            if(result < strick):
                result = strick
                
if(result < strick):
    result = strick
    
print(result)