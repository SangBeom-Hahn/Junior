'''
자신보다 높거나 같은 빌딩이 있으면 그 다음은 보지 못한다.

10 3 7 4 12 2라면
선택    스택탑  스택
10      x       [] = 스택이 비면 넣음
                10
3       10      10,3 = 스택탑보다 선택이 작으면 넣음
7       3       10 = 선택이 더 크면 pop
        10      10, 7 = 스택탑보다 선택이 작으면 넣음

4       7       10,7,4 = 스택탑보다 선택이 작으면 넣음
12      4       10, 7 = 선택이 더 크면 pop
        7       10 = 선택이 더 크면 pop
        10      [] = 선택이 더 크면 pop
        x       12 = 스택이 비면 넣음
2       12      12, 2 = 스택탑보다 선택이 작으면 넣음        

배열을 다 보면 끝

1. 모경수(prt, n=1)
1) 스택이 비면 넣음
2) 스택탑보다 선택이 작으면 넣음
3) 선택이 더 크면 pop

* n : 빌딩의 개수
빌딩의 높이
출 : 볼 수 있는 빌딩의 수의 합

2.시복 : nlogn
        
'''

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
    
stack = []
res = 0
for i in range(n):
    while(stack and stack[len(stack)-1] < arr[i]):
        stack.pop()
    
    stack.append(arr[i])
    res += (len(stack) - 1)
print(res)