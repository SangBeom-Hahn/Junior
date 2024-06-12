'''
선택    스택탑      스택        결과
스택에 아무것도 없으면 append
6                  6             [0] : 맨 마지막 인덱스라서 0

스택탑이 선택보다 작으면 싹다 pop 어차피 현재 선택에 막혀서 더 오른쪽 애들은 못 봄
9       6           []          [0, 0] : 스택이 비어지면 0
                    9
         
스택 탑이 더 크면 결과를 스택 탑을 하고 더 오른쪽 애들은 현재 선택한 걸 볼테니 스택에 append                    
5       9           5 9         [0, 0, 2]         

작으면 pop
7       5           9

크면 결과를 스택 탑을 하고 더 오른쪽 애들은 스택에 append  
7       9           7 9         [0, 0, 2, 2]
'''

n = int(input())
tops = list(map(int, input().split()))
stack = []
result = []

for i, ele in enumerate(tops):
    while(stack and stack[-1][0] < ele):
        stack.pop()
    
    if(not stack):
        result.append(0)
    else:
        result.append(stack[-1][1]+1)
        
    stack.append([ele, i])
    
    # print(stack)    
    # print(result)

for ele in result:    
    print(ele, end=" ")