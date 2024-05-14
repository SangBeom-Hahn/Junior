'''
흰=0, 검=1

ex) 
1111 (1 1 0 (0101))
1111
0001
0001 

11 1
11

01 (0101)
01

1111 1 1 1 1 -> 1
1111
1111
1111

1. 모경수(prt, n=1
0) 상하 좌우로 쪼개서 길이가 1일때까지 재귀
1) 재귀를 했는데 배열을 받았는데 길이가 1이면 리턴
2) 반환 받은게 모두 같으면 그 숫자 하나만 반환
3) 하나라도 다르면 ()로 묶어서 반환한다.


* n : 영상의 크기
상태

출력 : 압축 결과
2. 시복 : n^2
'''

# 0) 상하 좌우로 쪼개서 길이가 1일때까지 재귀
n = int(input())
graph = [list(map(int, list(input()))) for _ in range(n)]

# print(*graph, sep = '\n')

def checkOne(l):
    for i in range(len(l)):
        if(l[i] != 1):
            break
    else:
        return True
    
def checkZero(l):
    for i in range(len(l)):
        if(l[i] != 0):
            break
    else:
        return True
    
def rec(graph):
    if(len(graph) == 1):
        # print(graph[0][0])
        return graph[0][0]
    
    leng = len(graph)
    # 2중 for문을 4번 쓴다.
    # 위 왼
    top_left = []
    for i in range(leng//2):
        sub = []
        for j in range(leng//2):
            sub.append(graph[i][j])
        top_left.append(sub)
            
    # print(*top_left, sep = '\n')     
            
            
    # 위 오른
    top_right = []
    for i in range(leng//2):
        sub = []
        for j in range(leng//2, leng):
            sub.append(graph[i][j])
        top_right.append(sub)
    
    # print(*top_right, sep = '\n')     
    
    
    # 아래 왼
    bot_left = []
    for i in range(leng//2, leng):
        sub = []
        for j in range(leng//2):
            sub.append(graph[i][j])
        bot_left.append(sub)
    
    # print(*bot_left, sep = '\n')     
    
    
    
    # 아래 오른
    bot_right = []
    for i in range(leng//2, leng):
        sub = []
        for j in range(leng//2, leng):
            sub.append(graph[i][j])
        bot_right.append(sub)
    
    # print(*bot_right, sep = '\n') 
    
    # 위 왼 + 위 오른 + 아래 왼 + 아래 오른
    t_l = rec(top_left) 
    t_r = rec(top_right)
    b_l = rec(bot_left)
    b_r = rec(bot_right)
    
    # print(*graph, sep = '\n')
    # print(t_l, t_r, b_l, b_r)
    
    # 반환 받은게 모두 같으면 그 숫자 하나만 반환
    # ex) 1 1 1 1 = 1 /  0 1 0 1 (0101) 
    l = [t_l, t_r, b_l, b_r]
    if(checkOne(l)):
        return 1
    elif(checkZero(l)):
        return 0
        
    # 하나라도 다르면
    l = list(map(str, l))
    return '(' + ''.join(l) + ')'

print(rec(graph))