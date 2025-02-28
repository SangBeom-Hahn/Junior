'''
카드 : 공격력, 생명력
카드 2개 비교 : 
1) 공격력만큼 상대 생명력을 깎음
2) 생명이 0이하면 죽음
3) 카드가 2장 모두 살아있으면 비교를 계속함

1. 모경수(prt, n=1)
1) 공격력으로 상대방의 생명력을 깎음
2) 누구하나라도 생명력이 0이 되면 끝
3) 둘 다 0이면 draw


* A 카드 공격, 생명
B 카드
출 : A가 이기면 PLAYER A / B / 모두 죽으면 DRAW

2. n
'''

a_att, a_life = map(int, input().split())
b_att, b_life = map(int, input().split())

while(True):
    if(a_life <= 0 or b_life <= 0):
        break
    
    a_life -= b_att
    b_life -= a_att

if(a_life <= 0 and b_life <= 0):
    print("DRAW")
elif(a_life <= 0):
    print("PLAYER B")
elif(b_life <= 0):
    print("PLAYER A")