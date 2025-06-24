'''
2016.4.3 = 사귄지 200일
기념일별 날짜 출력하자
사귄날, 기념일수가 주어지면 기념일 날짜를 출력하는 프로그램

조건:
1] 평년 : 2월 28일 / 윤년 : 2월 29일 + 년도가 4의 배수 and 100의 배수가 아닐때 or 400의 배수일 때

ex) 
사귄날 2014-04-02
날수 1
결과 = 2014-04-02

날수 2
결과 = 2014-04-03

날수 200
결과 = 2014-10-18

1. 모경수(prt, n=1)
ok 1) N을 년, 월, 일로 나눠서 보는건 좀 힘들듯
ok 2) 날수 - 1해서 사귄날부터 더해야 한다.
ok 3) 일
    1] 증가시킴
    2] 월을 보고 최대값을 봄
    월      최대값
    1       31
    3       31
    4       30
    5       31
    6       30
    7       31
    8       31
    9       30
    10      31
    11      30
    12      31
    
    3] 2월이면 윤년을 보고 최대값을 봄 -> 최대값에 도달하면 일 = 1, 월 = +1
    윤년    29일
    평년    28일   
    
ok 4) 월
    1] 일이 최대값에 도달하면 증가시킴
    2] 12월에서 1증가시 -> 년 1증가, 월 = 1월
    
    
5) 년
    1] 월이 12월에서 증가하면 증가함
6) 사귄날에 + 1씩 할때마다 n을 1을 뺌, n이 0이 되면 끝

* 사귄날, 기념하려는 날의 수
출 : 기념일의 날짜 

2. n^2

'''

date, n = input().split(' ')
year, month, day = map(int, date.split('-'))
n = int(n) - 1

print(year, month, day, n)

# 3) 일
#     0] 최대값인지 봄 -> 최대값에 도달하면 일 = 1, 월 = +1
#     2] 월을 보고 최대값을 봄
#     월      최대값
#     1       31
#     3       31
#     4       30
#     5       31
#     6       30
#     7       31
#     8       31
#     9       30
#     10      31
#     11      30
#     12      31
   
#     3] 2월이면 윤년을 보고 최대값을 봄 -> 최대값에 도달하면 일 = 1, 월 = +1
#     윤년    29일
#     평년    28일   

#     1] 최대값이 아니면 그냥 증가시킴

while(True):
    if(n == 0):
        print("%04d-%02d-%02d" % (year, month, day))
        # print(f"{year}-{month}-{day}")
        break
    
    if(month == 1):
        # 0] 최대값인지 봄 -> 최대값에 도달하면 일 = 1, 월 = +1
        if(day == 31):
            day = 1
            month += 1
        else:
            day += 1
    
    # 윤년
    elif(month == 2):
        yoon_flag = False
        if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
            yoon_flag = True
        
        if(yoon_flag == True):
            if(day == 29):
                day = 1
                month += 1  
            else:
                day += 1
        else:
            if(day == 28):
                day = 1
                month += 1        
            else:
                day += 1
        
    elif(month == 3):
        if(day == 31):
            day = 1
            month += 1       
        else:
            day += 1             
        
    elif(month == 4):
        if(day == 30):
            day = 1
            month += 1        
        else:
            day += 1                         
        
    elif(month == 5):
        if(day == 31):
            day = 1
            month += 1        
        else:
            day += 1                         
        
    elif(month == 6):
        if(day == 30):
            day = 1
            month += 1        
        else:
            day += 1                         
        
    elif(month == 7):
        if(day == 31):
            day = 1
            month += 1        
        else:
            day += 1                         
        
    elif(month == 8):
        if(day == 31):
            day = 1
            month += 1        
        else:
            day += 1                         
        
    elif(month == 9):
        if(day == 30):
            day = 1
            month += 1        
        else:
            day += 1                         
        
    elif(month == 10):
        if(day == 31):
            day = 1
            month += 1        
        else:
            day += 1                         
        
    elif(month == 11):
        if(day == 30):
            day = 1
            month += 1        
        else:
            day += 1                         

# 4) 월
#     1] 일이 최대값에 도달하면 증가시킴
#     2] 12월에서 1증가시 -> 년 1증가, 월 = 1월
        
    elif(month == 12):
        if(day == 31):
            year += 1
            day = 1
            month = 1        
        else:
            day += 1
    
    # 6) 사귄날에 + 1씩 할때마다 n을 1을 뺌, n이 0이 되면 끝
    # print("%04d-%02d-%02d" % (year, month, day))
    n -= 1
    if(n == 0):
        print("%04d-%02d-%02d" % (year, month, day))
        break
    
    