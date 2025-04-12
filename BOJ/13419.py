'''
규칙
1] 번갈아가며 이전 사람이 말한 글자의 다음 글자를 말함.
2] 잘못말하면 진다.

탕육수만 기억하면 된다.
이게 최소한의 글자이다.

-> 짝수
AB

선 : A
후 : B

ABCD

선 : AC
후 : BD

ABCDEF

선 : ACE
후 : BDF


-> 홀수
A

선 : A
후 : A

ABCABC

선 : ACB
후 : BAC

ABCDEABCDE

선 : ACEBD
후 : BAC

1. 모경수
1) 짝수 : 먼저사람 = 짝수
    후 사람 = 홀수만 외우면 됨
    
2) 홀수 : 
    1] 문자열 * 2 해서 짝수로 만들어
    2] 그리고 먼저사람 = 짝수
    후 사람 = 홀수 자리만 외움

* T
문자열
출 : 두 사람이 미리 기억아고 있어야 하는 문자열 중 가장 짧은 것
먼저 말하는 사람
두번째로 말하는 사람

2. n^3
'''

t = int(input())
for _ in range(t):
    word = input()
    leng = len(word)
    first = ""
    sec = ""
    
    if(leng % 2 == 0):
        for i in range(0, leng, 2):
            first += word[i]
        
        for i in range(1, leng, 2):
            sec += word[i]
    else:
        word += word
        leng *= 2
        
        for i in range(0, leng, 2):
            first += word[i]
        
        for i in range(1, leng, 2):
            sec += word[i]
    
    print(first)
    print(sec)