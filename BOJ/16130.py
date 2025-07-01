'''
규칙
1] 벌점 x점 : 누적 벌점에 x점 추가
2] x점이 추가되어 누적 벌점을 10으로 나눈 몫이 증가한 경우 퇴사
    1] 1, 2, 3인 경우 : 1, 2, 3주 퇴사
    2] 4 : 무기 퇴사
    3] 4 초과 : 영구 퇴사
3] 무기, 영구 = 의행관 못들어와 + 벌점도 못 받아
4] 퇴사기간 동안 벌점을 받지 않고, 퇴사가 끝난 이후 다시 벌점을 받음

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35
0 1 2 3 4 5 6 7 8 9 A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z

벌점    숫자 벌점       총 벌점     10으로 나눈 몫      총 퇴사 기간
S       28              28          2                   2주
K       20              48          4                   무기퇴사 = 2(WEAPON)

---

4       4               4           0                   0
7       7               11          1                   1
9       9               20          2                   3
6       6               26          2 -> 몫이 증가한 경우만 퇴사함

---

x       33              33          3                   3
y       34              67          6                   영구 퇴사

1. 모경수(PRT, N=1)
ok 1) 초기 몫 = 0 / 누적 벌점 0
ok 2) 벌점을 누적 벌점에 더함
    1] 0~9는 걍 더함
    2] a~z는 (아스키코드 - 55)로 더함

ok 3) 몫 구함 -> 몫이 초기 몫보다 증가한 경우에만 퇴사하고 총 퇴사 기간에 추가함
    1] 4면 지금까지 총 퇴사기간 (weapon)
    2] 4초과면 총 퇴사 (09) break
4) 정상 정료 시 총 퇴사 기간 출력


* n : 학생 수
n개의 벌점 0~9 = 0~9벌점 / A~Z = 10~35벌점

출 : 각 학생이 퇴사해있는 총기간을 주단위로 출력
무기 or 영구 : 무기(weapon), 영구(09)

2. n^3

'''

n = int(input())
for _ in range(n):
    points = input()
    start_mok = 0 # 초기 몫
    add_point = 0 # 누적 벌점
    day = 0
    
    for p in points:
        if(p.isdecimal()): # 0~9는 걍 더함
            add_point += int(p)
            # print("0 ~ 9", p)
        else: # a~z는 (아스키코드 - 55)로 더함
            add_point += (ord(p) - 55)
            # print("알파벳 임", ord(p) - 55)
        
        # print(add_point)
        # 3) 몫 구함 -> 몫이 초기 몫보다 증가한 경우에만 퇴사하고 총 퇴사 기간에 추가함
        #     1] 4면 지금까지 총 퇴사기간 (weapon)
        #     2] 4초과면 총 퇴사 (09) break
        mok = add_point // 10
        if(mok == 4):
            print(f"{day}(weapon)")
            break
        elif(mok > 4):
            print(f"{day}(09)")
            break
        elif(mok > start_mok):
            start_mok = mok
            day += mok
    else:   
        print(day)