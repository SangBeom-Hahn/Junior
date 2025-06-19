'''
분침 : 1분에 1번 이동
시침 : 12분에 1번 이동 = 5번 이동하면 다음 시간
자정 : 동시에 맨 위 눈금 봄

상근 :
1] 시침과 분침이 이루는 각도를 적음
2] 어떤 각도는 반복되고, 어떤 각도는 절대 나오지 않음.
3] A각도가 되나 안되나 보기

시      분      각도    시침        분침        각도
0       0       0   
0       1       6      
0       2       12
0       3       18
0       4       24
0       5       30
0       6       36
0       7       42
0       8       48
0       9       54
0       10      60
0       11      66
0       12      66      1           12
0       13              1           13      72
0       14              1           14      78
0       15              1           15      84
0       16              1           16      90
0       17              1           17      96
0       18              1           18      102
0       19              1           19      108
0       20              1           20      114
0       21              1           21      120
0       22              1           22      126
0       23              1           23      132
0       24              2           24      132



1. 모경수(prt, n=1)
1) 분 눈금 1개에 6도
2) 0시 0분 ~ 0시 0분까지
    1] 1분에 분 각도 6씩 증가
    2] 12분에 시 각도 6씩 증가
    3] 분 각도 - 시각도를 set에 저장
    4] 둘의 각도 차이가 180도를 넘으면 360 - (차이)를 set에 넣음
3) 다시 0시 0분이 되면 끝

* A
출 : A가 되면 Y, 안되면 N

2. n^3
'''

gak = set()
time_gak = 0
min_gak = 0

for time in range(12):
    for min in range(1, 61):
        min_gak += 6
        
        if(min % 12 == 0):
            time_gak += 6
        
        # print(f"분 = {min_gak} 시 = {time_gak} 차 = {min_gak - time_gak}")
        
        if(min_gak - time_gak > 180):
            gak.add(360 - (min_gak - time_gak))
        else:
            gak.add(abs(min_gak - time_gak))
        
        if(min_gak == 360):
            min_gak = 0
            
while(True):
    try:
        inputs = int(input())
        
        if(inputs in gak):
            print('Y')
        else:
            print('N')
    except EOFError:
        break