'''
hh : 00이상 23이하
mm, ss : 00이상 59이하
시계정수 : hhmmss

ex) 오후 5시 5분 13초 = 170513

오전 0시 7분 37초 = 000737 = 737

시간 : 구간이다. 시작과 끝도 포함한다.

원하는 것
1] 시간에 포함되는 시계정수를 구함
2]  그 중 3의 배수인 것의 개수

[00:59:58, 01:01:24]

5958 (시작 포함)
5959
010000 (59다음은 60인거 알아야 함)

ex) 
235959에서 초가 1증가하면

초 : 60이라서 분 ++, 초 00
분 : 60이라서 시 ++ 분 00
시 : 24라서 시 00

000000 ~ 000059
000100 ~ 000124

1. 모경수(prt, n=1)
ok 1) 시분초를 유지해야 한다.
ok 2) 시작 시간부터 끝시간까지 초를 1씩 증가시킴
    1] 초가 60이면 분 ++, 초 00
    2] 분이 60이면 시 ++ 분 00
    3] 시가 24면 시 00
ok 3) 들어오는 시간이 3의 배수인지 체크하고 -> 기본은 시분초로 가지고 있다가 체크할때만 문자열로 붙임
    1] 1자리는 실제 숫자는 1자리인데 체크할때만 0이 앞에 있어야 함 00, 01, 02 등등
    2] 

4) 끝시간이면 종료


* 시작 시간, 끝 시간 (빈칸으로 구분)
출 : 구간에 포함하는 시계 정수 중 3의 배수의 개수

2. n^3

'''

for _ in range(3):
    cnt = 0
    start, end = input().split(' ')
    start_t, start_m, start_s = map(int, start.split(':'))
    end_t, end_m, end_s = map(int, end.split(':'))
    
    # print(f"시작 {start_t} {start_m} {start_s}")
    # print(f"끝 {end_t} {end_m} {end_s}")
    
    su = 1
    
    while(True):
    # while(su != 10):        
        
# 3) 들어오는 시간이 3의 배수인지 체크하고 -> 기본은 시분초로 가지고 있다가 체크할때만 문자열로 붙임
#     1] 1자리는 실제 숫자는 1자리인데 체크할때만 0이 앞에 있어야 함 00, 01, 02 등등
        
        temp_t = str(start_t)
        temp_m = str(start_m)
        temp_s = str(start_s)
        
        # 1자리 수면
        if(len(temp_t) == 1):
            temp_t = '0' + temp_t
        
        if(len(temp_m) == 1):
            temp_m = '0' + temp_m
            
        if(len(temp_s) == 1):
            temp_s = '0' + temp_s
            
        
        check_time = temp_t + temp_m + temp_s
        check_time = int(check_time)
        
        # print(check_time)
        
        if(check_time % 3 == 0):
            cnt += 1
            
        if(start_t == end_t and end_m == start_m and start_s == end_s):
            print(cnt)
            break

# 2) 시작 시간부터 끝시간까지 초를 1씩 증가시킴
#     1] 초가 60이면 분 ++, 초 00
#     2] 분이 60이면 시 ++ 분 00
#     3] 시가 24면 시 00
            
        start_s += 1
        if(start_s == 60):
            start_m += 1
            start_s = 0
    
        if(start_m == 60):
            start_t += 1
            start_m = 0
            
        if(start_t == 24):
            start_t = 0
            
        
        
        
        su += 1
        