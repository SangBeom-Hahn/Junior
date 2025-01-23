'''
a b c d 양의 정수의 차이
a b
b c
c d
d a

차이 값 4개의 수를 이용해서 다시 또 차이를 계산할 수 있다.
이를 4개의 수가 모두 같은 정수가 될 때까지 반복한다.

ex) 
a b c d
1 3 5 9
,,,
4 4 4 4 

이 경우 수열이 6번만에 모두 4로 수렴한다. 

1. 모경수(prt, n=1)
1) 입력 a b c d를 받음, a가 0이면 끝
2) 입력 받음 4개의 수의 절대값 차를 구하고 a  b c d 를 갱신함
3) a b c d가 모두 같아지면 끝, 그때까지 cnt함

* 각 테케가 a b c d (입력의 마지막 줄은 모두 4)
출 : 각 테케에 대해서 몇 번만에 수렴하는지

2. n^3
'''

while(True):
    a, b, c, d = map(int, input().split())
    
    if(a == 0):
        break
    
    cnt = 0
    if(a == b and a == c and a == d):
        print(cnt)
        continue
    
    while(True):
        tmp_a = abs(a-b) # 절대값 차
        tmp_b = abs(b-c) # 절대값 차
        tmp_c = abs(c-d) # 절대값 차
        tmp_d = abs(d-a) # 절대값 차
        cnt += 1
        
        if(tmp_a == tmp_b and tmp_a == tmp_c and tmp_a == tmp_d):
            print(cnt)
            break
        
        a = tmp_a
        b = tmp_b
        c = tmp_c
        d = tmp_d
        