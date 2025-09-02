'''
카드 : 시계(벽, 손목, 모래) 와 시각

게임
1] 카드 펼침 + 이번 순서의 시각을 외침 (첫 순서의 시각 = 1)
1] 다음 순서 = 전에 불린 시간에 1시간씩 더해서 외침

2] 역행 : 모래시계가 나오면 시간이 거꾸로 흐름, 모래시계 나온 다음 사람부터 거꾸로 흐름
3] 동기화 : 외친 시간 == 카드의 시간이면 중앙 때림
4] 과부화 : 역행 + 동기화가 동시에 일어나면 둘다 안함, 외친시간과 펼친 시간이 같고 모래시계면
    1] 다음 사람 역행 안함
    2] 모두 중앙 안 때림
    
ex n = 7

카드 정보       외칠 시간       역행여부        땡칠 여부 
watch 4         1               0          no
clock 2         2               0          yew
    
1. 모경수(prt, n=1)    
0) 외칠시간 = 1 / 역행여부 = 0이면 정방향, 1이면 역방향
1) 카드의 시간과 외칠 시간을 비교한다.
    1] 같으면
        1] 모래가 아니면 시간, yes 출력
    2] 다르면
        1] 시간, no 출력
2) 모래면
    1] 역행 여부 + 1 % 2
    2] 외칠시간을 역행 여부에 따라서 ++
    
* n : 카드의 개수
n개의 줄에 카드의 정보 = s = 시계 종류 / x = 카드에 적힌 시간

출 : n번 동안 플레이어가 외쳐야 하는 시간과 땅을 치나 안치나 yes no
2. n^2
'''

n = int(input())
time = 1
back_flag = 0

for _ in range(n):
    s, x = input().split()
    x = int(x)
    
    if(x == time):
        if(s != "HOURGLASS"):
            print(time, "YES")
        else:
            print(time, "NO")
    else:
        print(time, "NO")
    
    if(s == "HOURGLASS"):
        if(x != time):
            
            back_flag = (back_flag+1) % 2
        
    if(back_flag == 0):
        time += 1
        
        if(time == 13):
            time = 1
    else:
        time -= 1
        if(time == 0):
            time = 12
        