'''
송신    수신
4       7
7       9
5       9
9       x
6       x

선택    스택탑      스택    결과
4       []          []

스택탑이 더 작으면 pop해서 막힌거니 결과를 현재 선택으로 갱신
7       4           4       7
        []          []
        7           7
        
스택탑이 더 크면 append        
5       7           7        
        5           5 7

스택탑이 더 작으면 pop해서 막힌거니 결과를 현재 선택으로 갱신
9       5           5 7     9
        7           7       9
        []          []
        9           9
        
6       9           9
        6           6 9

for문 다 훑고 남아있는 애들은 0으로 채움

1. 모경수(prt, n=1)
0) for로 방향대로 훑음
1) 스택이 비면 넣음
2) 스택탑이 더 작으면 pop해서 막힌거니 결과를 현재 선택으로 갱신, 그러다 스택이 비면 넣음
3) 스택탑이 더 크면 append
4) for문 다 훑고 남아있는 애들은 0으로 채움(이미 0넣고 시작해서 pass)

* n : 탑의 수
탑의 높이
출 : 주어진 탑 순서대로 각 탑에서 발사한 레이저 신호를 수신한 탑들의 번호(수신하는탑이 없으면0)
2. 시복 : nlogn
'''

n = int(input())
stack = []
res = [0] * n

tops = list(map(int, input().split()))
for i in range(n-1, -1, -1):
    # print(stack)
    while(stack and stack[-1][0] < tops[i]):
        pop_item = stack.pop()
        res[pop_item[1]] = i+1
    
    stack.append([tops[i], i])
    
# print(res)    

for ele in res:
    print(ele, end=' ')