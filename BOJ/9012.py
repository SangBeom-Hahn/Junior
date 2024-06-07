'''
()로만 이루어진 문자열이있다. 
올바른 괄호 문자열 vps : 괄호의 모먕이 바르게 구성된 문자열
기본 vps : g한쌍의 괄호 기호로된 문자열 ()
x = vps라면 (x)도 vps다.
x, y = vps라면 xy도 vps다.

1. 모경수(prt, n=1)
1) 괄호가 아닌 조건
    1] 쌍이 틀림
    2] 다 훑었는데 스택이 남음
    3] 닫괄호가 나왔는데 스택이 비어있음

* t :" 테케수
테케 수만큼의 괄호 문자열
출 : 올바른 vps면 yes, 아니면 no
2.시복 : n^3
'''

t = int(input())
for _ in range(t):
    word = input()
    stack = []
    for ele in word:
        if(ele == '('):
            stack.append('(')
        else:
            if(not stack):
                print("NO")
                break
            
            stack.pop()
            
    else:
        if(stack):
            print("NO")
        else:
            print("YES")
            
