'''
N개의 전구(1 = 켜, 0 = 꺼), 1번부터 시작

명령
1] i번째 전구의 상태를 x로 변경
2] l번 ~ r번까지 전구의 상태를 변경(켜 <-> 끔)
3] l번 ~ r번까지 전구를 끔
4] l번 ~ r번까지 전구를 킴

0 1 0 1 0 0 0 0

1. 모경수(prt, n=1)
1) 명령을 받아서 명령을 수행함
    1] 모든 인덱스 -1
    2] 1번 명령 : i-1
    3] 나머지 : l-1 ~ r

* n, m : 전구수, 명령어수
n개의 정구 상태
a, b, c : 명령번호, 
출 : 모든 명령 이후 전구의 상태

2. nlogn

'''

n, m = map(int, input().split())
status = list(map(int, input().split()))

for _ in range(m):
    num, i, r = map(int, input().split())
    
    if(num == 1):
        status[i-1] = r
        
    elif(num == 2):
        for idx in range(i-1, r):
            status[idx] = (status[idx]+1) % 2
        
    elif(num == 3):
        for idx in range(i-1, r):
            status[idx] = 0
        
    elif(num == 4):
        for idx in range(i-1, r):
            status[idx] = 1
            
    # print(*status)
            
print(*status)