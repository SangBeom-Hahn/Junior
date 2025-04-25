'''
문제 : 
스트릭이란 하루에 1문제 이상을 며칠동안 연속으로 풀었는지를 나타내는 지표이다.
x일 동안 연속으로 풀었다면 스트릭이 x이다.

스트릭
1] 하루에 1문제 이상을 며칠동안 연속으로 풀었는지
2] x일 동안 = 스트릭 x
3] 프리즈
    0] 처음에 프리즈를 장착한 채로 문제를 풀기 시작함
    1] 문제를 안 푼날 자동 사용
    2] 스트릭이 늘어나지는 않지만 끊기지 않음
    3] 최대 1개 장착 가능
    4] 사용 후 2일 후 구매 후 장착 ex) 1일에 사용 -> 3일에 장착
        1] 그날 산거를 당일 사용 가능

ex) n = 2
일  프리즈 여부     푼문제 수   스트릭
0   o               0           0
1   o               1           1
2   o               1           2

1 0 2 0 0

일  프리즈 여부     푼문제 수   스트릭
0   o               0           0
1   o               1           1
2   o               0           1 -> 프리즈 o, 푼문제 수 0 = 프리즈 사용
3   x               2           2
4   o <- 2틀 뒤 삼   0          2 -> 프리즈 사용
5   x               0 -> 프리즈 x, 푼 문제 수 0 끝

1 0 2 0 1

일  프리즈 여부     푼문제 수   스트릭
0   o               0           0
1   o               1           1
2   o               0           1 -> 프리즈 o, 푼문제 수 0 = 프리즈 사용
3   x               2           2
4   o <- 2틀 뒤 삼   0          2 -> 프리즈 사용
5   x               1           3 -> 문제를 풀었으면 프리즈 여부를 볼 필요가 없음


1. 모경수(prt, n=1)
ok 1) 문제를 풀면, 
    1] 스트릭 ++
2) 안 풀면
    1] 프리즈 0
        1] 프리즈 사용, 스트릭 고정
        2] 2틀 계산해서 다시 프리즈 구매해야함
    2] 프리즈 x
        1] 끝
        

* N
N개의 푼 문제 수
출 : 최장 스트릭    

2. n^2
'''

n = int(input())
problems = list(map(int, input().split()))
strick = 0
freeze = True
two_pass = 0 # 2틀 계산기
two_flag = False

for pro in problems:
    if(two_flag == True):
        two_pass += 1
        
        if(two_pass == 2):
            two_flag = False
            two_pass = 0
            freeze = True
    
    if(pro >= 1):
        strick += 1
    
    # 문제를 안 풀면
    else:
        # 프리즈 0
        if(freeze == True):
            freeze = False
            two_flag = True
        
        # 프리즈 없음
        else:
            print(strick)
            break
else: #  정상 종료
    print(strick)