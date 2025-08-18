'''
반시계방향으로 회전
한번 회전 = 다음 문제 가리킴

문자열
1] 처음엔 빈 문자열
2] 회전 > 
3] 아무것도 하지 않음 or 문자열 맨 뒤에 가리키는 문자 하나 추가

ex) 
      v
a b c d

회전
      v
b c d a -> 문자열 추가  a

회
c d a b

회
d a b c

회
a b c d

회
b c d a -> 추가 aa

-
c d a b
-
d a b c -> 추가     7번 돌림
-
a b c d -> 추가 8번
-
b c d a     9번
- 
c d a b -> 추가 10번
-
d a b c -> 추가 11번

1. 모경수(prt, n=1)
ok 1) 못 만드는 경우 = s에 n에 없는 문자가 있음 -> -1 출력 끝
2) else
    1] 돌림판 순회
    2] 시간은 맨 뒤 
    3] 인덱스 ++
    4] 맨 뒤면 다시 0
    
    5] s를 바라보는 인덱스 0부터 시작
    6] 돌림판 순회하다가 s의 인덱스 요소와 같으면 인덱스 ++
    7] 인덱스가 s와 같으면 끝


* N : 돌림판 알파벳 수 
알파벳 n개 시계방향 순서 / 돌림판은 처음에 마지막 문자를 가리키고 있음
m : s의 길이
문자열 s

출 : s로 만들기 위해 필요한 돌림판 회전 수의 최소값
만들수 없다면 -1

2. n^2
'''

n = int(input())
alphas = input()
m = int(input())
s = input()
flag = False

for ele in s:
    if(ele not in alphas):
        flag = True
        break
    
if(flag == True):
    print(-1)
else:
    
    
    #     1] 돌림판 순회
    # ok 2] 시간은 맨 뒤 
    # 3] 인덱스 ++
    # 4] 맨 뒤면 다시 0
    
    # ok 5] s를 바라보는 인덱스 0부터 시작
    # ok 6] 돌림판 순회하다가 s의 인덱스 요소와 같으면 인덱스 ++
    # 7] 인덱스가 s와 같으면 끝
    
    circle_idx = n-1 # 돌림판 인덱스
    s_idx = 0 # s를 바라보는 인덱스
    cnt = 0
    
    while(True):
        if(s[s_idx] == alphas[circle_idx]):
            s_idx += 1
            
            if(s_idx == m):
                print(cnt)
                break
            
        circle_idx = (circle_idx + 1) % n
        
        cnt += 1