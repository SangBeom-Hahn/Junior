'''
nxn에 사탕, 은 모두 색이 같이 않을 수 있음, 사타으이 색이 다른 인접한 두칸을 교환함
가장 긴 같은 색으로 연속된 사탕을 먹음

ex) 
ccp
ccp
pcp 

1. 모경수(prt, n=1)
1) 모든 칸을 돌면서 왼쪽, 오른쪽으로 인접한 두칸 색이 같은지 체크
2) 같다면 교환하고 그 칸에서 행, 열 연속 칸의 개수 세서 최대값 구함
3) 모든 칸에서 최대값 구하고 계속 갱신함

* n : 보드크기
보드상태 c, p, z, y

출력 : 먹을 수 있는 사탕의 최대 개수
2. ㅣ복 n^2
'''

def counting():
    global max_cnt
    
    # 행의 연속한 거 개수 -> 지금 구하는 것이 행이라는 것을 인지하는 게 필요
    cnt = 1
    for y in range(n-1):
        if(bo[i][y] == bo[i][y+1]):
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 1
    # ccppp 같이 p는 다르지 않고 끝나서 그때를 위해 마지막에 갱신 한 번 더
    max_cnt = max(max_cnt, cnt)
    
    # 열의 연속한 거 개수
    cnt = 1
    for x in range(n-1):
        if(bo[x][j] == bo[x+1][j]):
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 1
    max_cnt = max(max_cnt, cnt)


n = int(input())
bo = [list(input()) for _ in range(n)]
max_cnt = 0

# print(*bo, sep='\n')

for i in range(n):
    for j in range(n):
        #  바꾸기 전에도 카운트 한번 함
        counting()
        if(j == n-1 and i == n-1): # -> 맨 마지막 행과 열은 비교 대상이 아니고
            break
        
        # 끝 열
        elif(j == n-1):
            # 아래랑만 교환
            # 행, 열 연속 칸의 개수 셈
            if(bo[i][j] != bo[i+1][j]):
                bo[i][j], bo[i+1][j] = bo[i+1][j], bo[i][j] # -> 교환하면 다시 돌려 놓는 거 필요
                counting()
                # print('a', i, j, max_cnt)
                bo[i][j], bo[i+1][j] = bo[i+1][j], bo[i][j]
        
        # 끝 행
        elif(i == n-1):
            # 오른쪽이랑만 교환
            # 행, 열 연속 칸의 개수 셈
            if(bo[i][j] != bo[i][j+1]):
                bo[i][j], bo[i][j+1] = bo[i][j+1], bo[i][j]
                counting()
                # print('b', i, j, max_cnt)
                bo[i][j], bo[i][j+1] = bo[i][j+1], bo[i][j]
            
        # 그 외 (오른쪽이랑도 교환하고 개수세고, 아래랑 교환하고도 개수셈)
        else:
            # 행교환
            if(bo[i][j] != bo[i+1][j]):
                bo[i][j], bo[i+1][j] = bo[i+1][j], bo[i][j]
                counting()
                # print('c', i, j, max_cnt)
                bo[i][j], bo[i+1][j] = bo[i+1][j], bo[i][j]
            
            # 열교환
            if(bo[i][j] != bo[i][j+1]):
                bo[i][j], bo[i][j+1] = bo[i][j+1], bo[i][j]
                counting()
                # print('d', i, j, max_cnt)
                bo[i][j], bo[i][j+1] = bo[i][j+1], bo[i][j]

print(max_cnt)