'''
게임
1] 2이상 정수 n 고름
2] 임의 정수 n개로 이루어진 수열
3] n = 2가 아니면
    1] 양끝 끼리 더하고 안으로 들어가면서 더해서 반으로 접는다
    2] n이 홀수 = 가운데 수를 자기 자신과 더한다.
    3] n을 / 2하고 ceil해서 접기 과정을 반복한다. -> 수열 사이즈가 절반이 되는 거라서  / 2는 안해도 될 듯
    4] n이 2가 되면 
        1] 첫번쨰 수가 더 크면 상근 WIN
        2] 작거나 같으면 창영 WIN
4] n = 2이면 
    1] 첫번쨰 수가 더 크면 상근 WIN
    2] 작거나 같으면 창영 WIN
    
ex) 수열 2 5 10 3 -4
-2 8 20
18 8



ex2) 2 5
2 5


ex3) 

길이 6
0 1 2 3 4 5
2 5 10 3 -4 -5    
-3 1 13
10 2

ex 4) 

길이 3
0 1 2
5 4 -3
2 8


1. 모경수(prt, n=1)
1) 양끝에서 더해가면서 안으로 들어옴
    1] idx를 0부터 증가시킴
    2] idx과 n - (idx+1) 을 더해서 새로운 배열에 append
    3] idx > n - (idx+1)면 끝
    4] 새로운 배열로 이를 반복하다가 길이가 2이면 전체 끝
    

* t : 테케 수
n : 수열의 길이
수열


출 : 상근 WIN = Alice를 테케 번호와 함께 출력

2. n^3
'''

import math

t = int(input())
for case in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    
    while(True):
        if(n == 2):
            if(arr[0] > arr[1]):
                print(f"Case #{case}: Alice")
            else:
                print(f"Case #{case}: Bob")
            
            break
        
        new_arr = []
        for idx in range(n):
            if(idx > n-(idx+1)):
                # 갱신
                n = math.ceil(n / 2)
                arr = new_arr
                break
            
            new_arr.append(arr[idx] + arr[n-(idx+1)])
            
        # print(n)
        # print(arr)
        
        