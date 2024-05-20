'''
1~n까지 수를 ㅅ택에 넣었다가 빼서 늘어노아서 하나의 수열을 만들 수 있다. 
push 순선느 반드시 오름차순을 지킬 것이다. 임의의 수열이 주어졌을 떄
스택을 활용해 그 수열을 만들 수 있는지 없는지 있다면 어떤 순서로 push pop 해야 하는지
알아내라

1. 모경수(prt, n=1)
1) 
수열
43687521
41

스택    숫자    연산
[]
1        1       push
1,2        2       push
1,2,3        3       push
1,2,3,4        4       push
1,2,3                pop = 4
1,2                    pop = 3
1,2,5      5       push
1,2,5,6        6       push
1,2,5                pop = 6

12534

스택    숫자    연산
[]
1       1       push
[]              pop = 1
2       2      push
[]              pop = 2
3       3       push
34      4       push
345     5       push
34              pop = 5


1. 모경수
1) su = 1 
2) su가 수열의 포인트값보다 작으면 push
2) su가 더 크면? 

2) 스택의 탑이 수열의 포인트값과 같으면 pop
3) 스택의 탑이 수열의 포인트값보다 크면 break no
4) 수열의 포인트가 n과 같으면 연산자 출력

* n
임의의 수열
출 : 임의의 수열을 만들기 위해 필요한 연산을 한 줄에 한개씩 출력 push +, -/ 불가하면 no
2. 시복 : nlogn
'''

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
    
su = 1
idx = 0
stack = []
opers = []

while(idx != n):
    if(stack):
        if(stack[len(stack)-1] == arr[idx]):
            stack.pop()
            opers.append('-')
            idx += 1
            continue
        
        if(stack[len(stack)-1] > arr[idx]):
            print("no")
            break
        
    stack.append(su)
    opers.append('+')
    su += 1
    
else:
    print(opers)