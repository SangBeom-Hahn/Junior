'''
폭발
1] 모든 폭발 문자열이 폭발함
2] 남은 문자열을 순서대로 이어 붙여 새로운 문자열을 만듦
3] 폭발 문자열이 없을 때까지 계속한다.

남은 문자가 없는 경우도 있음 = FRULA 출력

1. 모경수(PRT, N=1)
1) 앞에서부터 순회해서 스택에 넣는다.
2) 스택에 넣을때마다 슬라이싱 폭발 문자열 길이만큼해서 헤드가 폭발 문자열과 같은지 비교
3) 같으면 폭발 문자열 길이만큼 팝, 안 같으면 패스
4) 남은 스택 문자열 출력, 길이가 0이면 frula 출력

* 문자열
폭발 문자열 (알파벳 대소문자 구분)
출 : 모든 폭발이 끝나고 남은 문자열, 없으면 FRULA

2. nlogn
'''

s = input()
bombstr = input()
stack = []
leng = len(bombstr)

cnt = 0 # 전체 길이
for ele in s:
    stack.append(ele)
    cnt += 1
    
    if(cnt >= leng): # 전체 길이가 폭발 문자열 길이보다 크거나 같을때만
        head = ''.join(stack[cnt - leng : ]) # 전체 길이 - 폭발 = 헤드
        if(head == bombstr):
            for _ in range(leng):
                stack.pop()
                cnt -= 1

if(cnt == 0)             :
    print("FRULA")
else:
    print(''.join(stack))                