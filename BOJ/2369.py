'''
k명이 알파벳으로 표시되고 알파벳 순서로 사다리 탐
사다리(점섬 = 가로 막대 없음, 가로 실선 = 가로 막대)
1] 하나의 가로줄 전체가 감추어져 있음, 줄의 각 칸에 가로 막대를 적절히 넣어서
게임 결과가 원하는 순서가 나오게 할 것이다.

사람 A B C
사다리
*-
-*

A B C
|*|-| 사다리 0행
-----
|-|*| 사다리 1행
C A B

        행      열
A       0       0 = 시작
        좌, 우를 살핌 -> '-' 없음 = 열 고정, 행을 그냥 계속 증가함

        1       2
        좌우를 살핌 -> 우에 - 있음 = 우로 이동
        
        2       2
        
B       0       2 = 시작        
        우에 -
        
        1       4
        없음
        
        2       4
        
C       0       4 = 시작    
        좌웨 -
        
        1       2
        좌에 -
        
        2       0
        
최종 열 C A B
0 2 4

1. 모경수(prt, n=1)
1) ???에 [*, -]로 이루어진 길이 k-1짜리 순열을 구함
2) 순열을 순회해서 사다리에 ???에 넣어보고 실제로 사다리를 타서 결과를 만듬
    0) 사다리 사이 사이와 양 끝에 |를 추가함 = 사람 10명 가로 칸 9개 = 19(K+K-1)이 나와야 함
    0) 사람도 사이 사이에 공백 추가해서 길이 19(K+K-1) 맞춤
    1) 사람을 0행에서 시작해서 2(N+1)행까지 가자 = 각 사람마다 n+1행으로 가면 끝
    2) 현재 행에서 좌, 우 봐서 -가 있는 곳으로 열 +2 / OR 열 -2, 행은 변화 없음
    3) K+K-1 길이 결과 배열 만들고 사람의 열에 해당하는 인덱스에 삽입
    
3) 원하는 순서가 나오면 그 순열 출력
4) 안 나오면 -1

* 
k = 참가한 사람 수
n = 전체 가로 줄의 수
원하는 최종 순서
사다리 전체 모양 (가로 줄의 유무로 표현)
있는 경우 - / 없는 경우 * / 감추어진 특정 가로 줄 ?

ex) *-***-*** = k-1개의 칸으로 이루어진 가로줄 1개

출 : 최종 순서로 도착할 수 있도록 감추어진 가로 줄을 구성해서 출력하라
절대로 최종 순서가 나오도록 감추어진 가로 줄을 구성할 수 없다면 x로 구성된 길이 k-1 문자열

2. 
'''

# 0) 사다리 사이 사이와 양 끝에 |를 추가함 = 사람 10명 가로 칸 9개 = 19(K+K-1)이 나와야 함
# 0) 사람도 사이 사이에 공백 추가해서 길이 19(K+K-1) 맞춤
#     1) 사람을 0행에서 시작해서 2(N+1)행까지 가자 = 각 사람마다 n+1행으로 가면 끝
#     2) 현재 행에서 좌, 우 봐서 -가 있는 곳으로 열 +2 / OR 열 -2, 행은 변화 없음
#     3) K+K-1 길이 결과 배열 만들고 사람의 열에 해당하는 인덱스에 삽입


k = int(input())
n = int(input())
order = input()
graph = [input() for _ in range(n)]
col_leng = k+k-1

loc = 0
for i in range(n):
    if(graph[i][0] == '?'):
        loc = i
        break

start_order = [chr(97+ele).upper() for ele in range(0, k)]
start_order = '|'.join(start_order)
for i in range(n):
    graph[i] = '|'.join(graph[i])
    graph[i] = '|' + graph[i] + '|'

# print(order)    
# print(*graph, sep = '\n')


# 1) ???에 [*, -]로 이루어진 길이 k-1짜리 순열을 구함
    # 1] -가 연속된 건 빼야함
# 2) 순열을 순회해서 사다리에 ???에 넣어보고 실제로 사다리를 타서 결과를 만듬

from itertools import product, permutations

candis = []
for cand in list(product(['*', '-'], repeat=k-1)):
    for i in range(k-2):
        if(cand[i] == cand[i+1] and cand[i] == '-'):
            break
    else:
        candis.append(cand)

# print(*candis, sep = '\n')

# ?의 위치를 구함

# print(candis)
# 2) 순열을 순회해서 사다리에 ???에 넣어보고 실제로 사다리를 타서 결과를 만듬
for cand in candis:
    result = [''] * (k+k-1)
    
    ttttemp = ''.join(cand)
    
    # if(ttttemp == '**-*-***-'):
    #     # print(cand)
        
    cand = '|'.join(cand)
    cand = '|' + cand + '|'
    
    # if(ttttemp == '**-*-***-'):
    #     print(cand)
    
    graph[loc] = cand
    
    
    # if(ttttemp == '**-*-***-'):
    #     # print(cand)
    #     print(*graph, sep = '\n')
    
    for j in range(0, col_leng, 2):
    # for j in range(0, 1):
        col = j
        # print(order[j])
        # print(col)
        
        # 2) 현재 행에서 좌, 우 봐서 -가 있는 곳으로 열 +2 / OR 열 -2, 행은 변화 없음
        for row in range(0, n):
        # for row in range(0, 2):
        
            if(col == 0): #우만 봄
                if(graph[row][col+1] == '-'):
                    col += 2
                
            elif(col == col_leng-1): # 좌만 봄
                if(graph[row][col-1] == '-'):
                    col -= 2
                
            else: # 좌우봄
                if(graph[row][col+1] == '-'):
                    col += 2
                    
                elif(graph[row][col-1] == '-'):
                    col -= 2

        # print(col)
        result[col] = start_order[j]
    
    # print(result)    
    tmp = ''.join(result)
    
    # if(ttttemp == '**-*-***-'):
    #     print(*graph, sep = '\n')
    #     print(tmp)
        
    if(tmp == order):
        print()
        print(cand)
        print(tmp)
        
    # print()