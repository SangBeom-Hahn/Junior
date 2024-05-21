'''
빌딜ㅇ이 일렬로 서있고 오른쪽만 보기 가능
자신 빌딩보다 높거나 같은 빌딩이 있으면 그 이후 오른쪽은 더 못본다.

= 나보다 작으면 넣고로 하면 2중 for라서 안됨
스택탑  선택      볼 수 있냐      스택
x       10                      [] 
                                10 = 스택이 비어있으면 그냥 넣음
10      3         ㅇ            10,3 = 스택탑이 더 크면 볼수있는 거니 스택에넣기
3       7         x             10 = 스택탑이 더 작으면 못보니 pop
10                ㅇ            10,7 = 스택탑이 더 크면 볼수있는 거니 스택에넣기
7       4           ㅇ          10,7,4 = 스택탑이 더 크면 볼수있는 거니 스택에넣기
4       12          x           107 = 스택탑이 더 작으면 못보니 pop
7                               10  = 스택탑이 더 작으면 못보니 pop
10                              [] = 스택탑이 더 작으면 못보니 pop
                                12 = 스택이 비어있으면 그냥 넣음
12      2                       12,2 = 스택탑이 더 크면 볼수있는 거니 스택에넣기

for문 다 돌면 끝내기
'''

n = int(input())
arr = []
stack = []
for _ in range(n):
    arr.append(int(input()))

print(arr)    
res = 0

for i in range(n):
    while(stack and stack[len(stack)-1] < arr[i]):
        stack.pop()
        
    stack.append(arr[i])
    res += (len(stack) - 1)
    
    print(stack, len(stack) - 1)