'''
A : 용태가 핀 손가락 개수
B : 유진이가 핀 손가락 개수

게임
0] 용태가 선공
1] x개를 핀상태로 상대를 공격하면 상대가 x개를 더 핌
2] 5개 이상 핀 사람이 짐

ex) 
용      유
1       2
1       3
4       3
4       7

1. 모경수(prt, n=1)
ok 1) 반복문, A나 B가 5이상이면 끝
2ok ) 짝수턴엔 B에 A를 더함
3) 홀수턴엔 A에 B를 더함
ok 4) 끝나고 출력

* A, B
출 : 용태가 이기면 yt, yj

2. n^3

'''

A, B = map(int, input().split())
su = 0 # 짝수턴으로 시작

while(True):
    if(su % 2 == 0):
        B += A
        if(B >= 5):
            print("yt")
            break
    else:
        A += B
        if(A >= 5):
            print("yj")
            break
        
    su += 1