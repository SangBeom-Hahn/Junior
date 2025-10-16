'''
n 마리 몬스터
ai = i번째 몬스터 현재 체력
x 만큼 대미지를 받고, 체력 <= 0 면 죽는다.

전투
1] 모든 몬스터를 죽일 것이다.
2] 턴
    1] 체력 0 초과 몬스터 중 가장 첫 몬스터에게 대미지를 준다.
    2] 대미지 받은 몬스터의 체력 < 0인 -h의 경우 = 오버킬
        1] 죽은 몬스터 다음 몬스터가 없으면 턴 종료
        2] h의 p퍼센트 소수점 첫째자리에서 버림한만큼 대미지를 준다.
        3] 오버킬은 2마리만 대미지 주고 끝이다.
        
d 20 / p 15

턴      체력
0       30 21 1 2 30 22 3
1       10 21 1 2 30 22 3

1 20 15
15

1. 모경수(prt, n=1)
ok 1) 공격할 몬스터 idx 
    1] 공격할 몬스터의 체력이 <= 0 면 idx ++
ok 2) 공격할 몬스터에게 d 만큼 대미지를 줌
ok 3) 몬스터 체력 > 0 -> 공격 대상
ok 4) == 0 -> idx ++
5) < 0 
    1] 체력 * -1 * 15 * 100 만큼 idx+1 몬스터에게 대미지를 줌 (oob 주의)
6) 1번 공격할 때마다 턴 ++
ok 7) idx 가 n과 같아지면 끝

* n : 몬스터의 수        
d : 대미지
p : 오버킬 비율

n 마리 몬스터 체력
출 : 모두 죽이기 위한 필요한 턴 수


2. n^3
'''

import math

n, d, p = map(int, input().split())
healths = list(map(int, input().split()))
turn = 0
idx = 0
su = 1


while(True):
# while(su != 10):
    
    if(idx == n):
        print(turn)
        break
    
    # 1] 공격할 몬스터의 체력이 <= 0 면 idx ++
    if(healths[idx] <= 0):
        idx += 1
        continue
    
    healths[idx] -= d
    turn += 1
    # print(healths)
    if(healths[idx] < 0 and idx != n-1):
        next_damage = (healths[idx] * -1 * p / 100)
        # print(next_damage)
        
        next_damage = math.floor(next_damage)
        healths[idx + 1] -= next_damage
        # print(healths)
    
    su += 1