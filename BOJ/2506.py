'''
갈호 값 : 
1) () = 2
2) [] = 3
3) (x) = 2 * 값(x)
4) [x] = 3 * 값(x)
5) xy = 값(x) + 값(y)

ex) ()[[]] = 2 + 3*3 = 11
(x) = 2 * 11 = 22

( () [[]] )
요소    스택        중간        최종
(       (           2*
(       ( (         2 * 2
)       ( 팝        2 *         4
[       ( [         2 * 3
[       ( [[        2 * 3 * 3
]       ( [ 팝      


1. 모경수(prt, n=1)
ok 1) 중간, 최종 결과를 둠
ok 2) 열갈호면 중간에 * 를 함
3) 닫 갈호면
    ok 1] 하나 앞이 열갈호면 최종에 중간 더함
    ok 2] 중간 // 
4) 스택
    1] 열갈호면 넣음
    2] 닫갈호면 
        1] 스택이 비어있으면 올바르지 않음 끝
        2] 스택 헤드랑 쌍이 다르면 끝
        3] 팝
    3] 갈호열이 끝났는데 스택이 남아있으면 끝


* 괄호열
출 : 갈호값(올바르지 않으면 0)

2. n^3
'''

inputs = input()
semi = 1
final = 0
stack = []

for idx in range(len(inputs)):
    if(inputs[idx] == '('):
        semi *= 2
        stack.append('(')
    elif(inputs[idx] == '['):
        semi *= 3
        stack.append('[')
        
    elif(inputs[idx] == ']'):
        if(not stack or stack[-1] != '['):
            final = 0
            break
        
        if(inputs[idx-1] == '['):
            final += semi
        
        semi //= 3
        stack.pop()
        
    elif(inputs[idx] == ')'):
        if(not stack or stack[-1] != '('):
            final = 0
            break
        
        if(inputs[idx-1] == '('):
            final += semi
        
        semi //= 2
        stack.pop()
        
if(stack):
    final = 0

print(final)