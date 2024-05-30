'''
전체 종이가 모두 같은 색이 아니면 4개로 나눈다. 나눈 것도 전체 종이로 봐서 모두 같은 색이 아니면 다 나눈다.
이를 자른 종이가 모두 하얀색 혹은 모두 파란색으로 칠해져있거나 길이가 1이되어 더이상 못자를때까지 반복한다.

1. 모경수(prt, n=1)
1) 4개로 나눈다.
2. 4개를 모두 검사하고 모두 동일 숫자가 아니면 재귀한다.
3) 모두 동일 숫자면 전역 변수를 cnt 한다.
4) 길이가 1이면 0번요소로 전역 변수 cnt 한다.

* n : 한변의 길이
상태(흰 = 0, 파 = 1)
출 : 잘라진 하얀과 파란의 개수 출력
2. 시복 : nlogn
'''

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def check(graph):
    # print("검사")
    # print(*graph, sep = '\n')
    
    
    stand = graph[0][0]
    
    leng = len(graph)
    for i in range(leng):
        for j in range(leng):
            if(graph[i][j] != stand):
                return False
    return True

def rec(graph):
    n = len(graph)
    # print(*graph, sep = '\n')
    # print()
    global w_cnt, b_cnt
    
    # 4) 길이가 1이면 0번요소로 전역 변수 cnt 한다.
    if(len(graph) == 1):
        stand = graph[0][0]
        if(stand == 0):
            w_cnt += 1
        else:
            b_cnt += 1
        return
    
    if(check(graph)): # 모두 동일 숫자면 전역 변수를 cnt 한다.
        stand = graph[0][0]
        if(stand == 0):
            w_cnt += 1
        else:
            b_cnt += 1
        return
    
    # 왼 위
    l_t = []
    for i in range(n//2):
        tmp = []
        for j in range(n//2):
            tmp.append(graph[i][j])
        l_t.append(tmp)
        
    # print(*l_t, sep = '\n')
    # print()
    
    # 오른 위
    r_t = []
    for i in range(n//2):
        tmp = []
        for j in range(n//2, n):
            tmp.append(graph[i][j])
        r_t.append(tmp)
        
    # print(*r_t, sep = '\n')
    # print()
    
    # 왼 아래
    l_b = []
    for i in range(n//2, n):
        tmp = []
        for j in range(n//2):
            tmp.append(graph[i][j])
        l_b.append(tmp)
        
    # print(*l_b, sep = '\n')
    # print()
    
    # 오른 아래    
    r_b = []
    for i in range(n//2, n):
        tmp = []
        for j in range(n//2, n):
            tmp.append(graph[i][j])
        r_b.append(tmp)
        
    # print(*r_b, sep = '\n')
    # print()
    
    # 2. 4개를 모두 검사하고 모두 동일 숫자가 아니면 재귀한다.
    for ele in [l_t, r_t, l_b, r_b]:
        # print(1)
        if(check(ele)): # 모두 동일 숫자면 전역 변수를 cnt 한다.
            stand = ele[0][0]
            if(stand == 0):
                w_cnt += 1
            else:
                b_cnt += 1
        else:
            rec(ele)

w_cnt = 0
b_cnt = 0
rec(graph)

print(w_cnt)
print(b_cnt)