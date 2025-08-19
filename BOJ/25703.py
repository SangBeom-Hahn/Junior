'''
돌림판
1] 반시계 방향 회전

문자열
1] 처음엔 빔
2] 규칙
    0] 돌림판은 처음에 마지막으로 입력된 문자를 가리킴
    1] 돌림판 1회 회전
    2] 아무것도 안함 vs 문자열 맨끝에 돌림판이 가리키는 문자 하나 추가
    3] 돌림판 문자열이 비어있을 때, 문자를 추가하면 그 문자가 돌림판 문자열이 된다.
    
ex) 
      v
a b c d

b c d a -> 추가

c d a b

d a b c

a b c d

b c d a -> 추가

c d a b

d a b c -> 추가

a b c d -> 추가

b c d a

c d a b -> 추가

d a b c -> 추가, 완성 총 11번 회전


s = ba

  v
a b

b a

a b 추가

b a 추가

2
ab
2
ba

1. 모경수(prt, n=1)
ok 0) s를 순회해서 돌림판에 없는 알파벳이 있으면 -1 끝
1) elif n이 1이면 0
2) else
    1) 돌림판을 바라보는 sp_idx = n-1로 시작
    1) s의 찾아야 하는 요소를 가리키는 s_idx
    2) 회전
        0] sp_idx 와 s_idx의 요소가 같으면, s_idx ++
        1] sp_idx ++ / 원형 / cnt ++
        2] s_idx가 m과 같으면 끝
    
입력 
n : 돌림판에 적힌 알파벳의 개수
돌림판에 적힌 알파벳 소문자 n개 (시계 방향 순서)
m : 만들어야 하는 문자열 s의 길이
s : 만들어야 하는 문자열

출력 : 돌림판 문자열을 문자열 s로 만들기 위해 필요한 돌림판 회전수의 최소값 / s로 못만들면 -1 출력

시간복잡도 n^2
'''

n = int(input())
spin = input()  # 돌림판에 적힌 알파벳 소문자 n개
m = int(input())
s = input()

flag = False # s를 만들 수 있는지 신호
for ele in s:
    if(ele not in spin):
        flag = True
        
if(flag == True):
    print(-1)
else:
    if(n == 1): # n이 1이면 회전을 할 수 없을거라는 가설
        print(0) 
    else:
        sp_idx = n-1
        s_idx = 0
        cnt = 0
        
        while(True):
            sp_idx = (sp_idx + 1) % n
            cnt += 1
            
            if(spin[sp_idx] == s[s_idx]):
                s_idx += 1
            
                if(s_idx == m):
                    print(cnt)
                    break
            
            