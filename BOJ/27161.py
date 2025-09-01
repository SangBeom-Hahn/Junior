'''
시간 카드 : 시계 그림과 시각
시계 그림 3가지 : 벽, 손목, 모래

게임
1] 윗장 카드들고 시각을 외침, 첫 플레이어는 1시로 시작
2] 시계 방향으로 돌아감. 방금전에 불린 시각+1을 더해서 외침 12시 -> 1시
3] 시간의법칙
    1] 모래시계 : 시간이 거꾸로 흐름 2 > 1 > 12시 순으로 해서 모래를 펼칠때마다 역행함
    2] 플레이어가 외친 시각 == 펼쳐진 시각, 게임중앙을 때림
4] 반드시 지키는룰 : 2개법칙을 동시에 만족하면, 법칙은 둘다 무효
5] 틀림 = 잘못된 시각을 외쳐 or 손바닥을 늦게 때려 = 벌점토큰을 받음
    1] 벌점 받으면 펼친 카드를 카드 더미 밑으로 다시 넣고, 벌점 받은 플레이어가 1시를 외치며 경기 재개



1. 모경수(prt, n=1)
1) 카드를 펼치고, 말할 시간을 봄.
    1] 말할시간은 1부터 시작
2) 할 행동에 "" / 모래시계 0=증가, 1=감소
2) 검사
    1] 펼친시간 = 말한시간 / 할행동에 YES
    2] 모래시계
        1] 할행동이 YES면 NO 놓고 
            1] 최초 사람이면 그냥 print
            2] 최초 아니면, 원래 모래시계 대로 말할시간 변화 모래시계 0=증가, 1=감소
        2] 아니면
            1] 모래시계를 짝홀을 바꿈.
            
3) 시각, 행동 print 함.

* n : 펼쳐질 카드의 개수
n개의 카드 정보 = s(시계종류) / x(카드에적힌 시각)
벽 clock
손목 watch
모래 hourglass

출 : n줄에 걸쳐서 차례를 진행하는 플레이어가 / 외쳐야 하는 시각, 해야하는 행동
시각 (1~12) / 행동 (때림yes / 안때림no)

2. n^2
'''

n = int(input())
time = 1 #말할시간.
flag = 0
start = True

for _ in range(n):
    what = "NO"
    s, x = input().split() # 시계, 카드시각
    x = int(x)
    
    if(x == time):
        what = "YES"
        
            
    if(s == "HOURGLASS"):
        if(what == "YES"):
            what = "NO"
            
            if(start):
                print(time, what)
                continue
            else:
                if(flag == 0):
                    time += 1
                    if(time == 13):
                        time = 1
                else:
                    time -= 1
                    if(time == 0):
                        time = 12
        else:
            flag = (flag + 1) % 2
            if(flag == 0):
                time += 1
                if(time == 13):
                    time = 1
            else:
                time -= 1
                if(time == 0):
                    time = 12
    else:
        flag = (flag + 1) % 2
        if(flag == 0):
            time += 1
            if(time == 13):
                time = 1
        else:
            time -= 1
            if(time == 0):
                time = 12
    
    print(time, what)
    start = False    

            
    