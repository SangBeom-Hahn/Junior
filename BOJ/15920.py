'''
매 순간 둘중 하나
1] 1초 동안 a>b / b>c로 간다. (c에 있으면 아무일도 안 일어남)
2] 레버의 상태를 반대로 바꾼다.

규칙
1] 초기선로 = 5명이 치임
2] a>b로 이동할 때 레버의 상태에 따라 선로가 결정됨. (당기지x = 5명 치임 / 당김o = 1명 치임)
3] 차가 b에 있는데 레버를 당기면 -> 두 선로를 동시에 따
4] c일때 차가 있는 선로의 모두 깔린다.

ex)
문자열      선로방향        차 위치
            5명             a
P=상태바꿈      1명             a
P              5명              a
P               1명             a
w                               b
w                               c = 1명 치임


문자열      선로방향        차 위치
            5명
p           1
p           5
p           1               a
w                            b
p           6
p
p
c로 안가서 0명

문자열      선로방향        차 위치
            5명             a
w                               b
p           6
p           
w                           c = 6명      

1. 모경수(prt, n=1)
ok 1) 최초 선로 방향 5명
ok 2) 차 위치 a
3) 입력
    ok 1] p
        ok 1] 차가 a면 선로 방향을 5 -> 1 / 1 -> 5로 바꿈
        2] 차가 b면 선로 방향을 6으로 둠
        3] 차가 c인데 p가 입력될 수 없음
    2] w
        1] 차 위치를 a -> b -> c로 이동
        
4) 끝
    1] 차가 c면 선로 방향이 답 -> 끝냄 break
    2] break로 안 끝나고 입력이 끝나서 끝나면 0이 답


* n : 문자열의 길이
s : w = 1초 기다림 / p = 레버 상태를 바꿈

출 : 깔리는 마네킹의 수 (광차가 c로 이동하기 전에 행동이 끝나면 아무도 안 깔림)

2. n^3

'''

direct = 5
loc = 'a'

n = int(input())
inputs = input()
for ele in inputs:
    print(direct)
    
    if(ele == 'P'):
        if(loc == 'a'):
            if(direct == 5):
                direct = 1
            else:
                direct = 5
        elif(loc == 'b'):
            direct = 6
    else:
        if(loc == 'a'):
            loc = 'b'
        elif(loc == 'b'):
            loc = 'c'
    
    
    if(loc == 'c'):
        print(direct)
        break
else:
    print(0)