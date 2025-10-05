'''
n x n에 퀀 n개를 서로 공격할 수 없게 놓는 문제이다.

  0 1 2 3
0 ㅁㅁㅁㅁ
1 ㅁㅁㅁㅁ
2 ㅁㅁㅁㅁ
3 ㅁㅁㅁㅁ

idx     x   y
0       0   3
1       0   2
        1   3
2       0   1
        1   2
        2   3 -> n - (y-x) - 1
        
3       0   0
        1   1
        2   2
        3   3
4       1   0 -> 4 - (0-1) - 1
        2   1 -> 4 - (1-2) - 1
        3   2

열 i
오른쪽 위 대각선 
왼쪽 위 대각선

1. 모경수(prt, n=1)
1) 백으로 탐색, used
2) 행을 인자로, for는 열을

* n : nxn
출 : 퀀 n개가 서로 공격할 수 없게 놓는 경우의 수

2. n^3
'''

def back(chose, row):
    global cnt
    
    if(len(chose) == n):
        cnt += 1
        return
    
    for i in range(n):
        if(not visit_col[i] and 
           not visit_right_cross[row + i] and
           not visit_left_cross[n - (i-row) - 1]
           ):
            visit_col[i] = True
            visit_right_cross[row + i] = True
            visit_left_cross[n - (i-row) - 1] = True
            chose.append(i)
            back(chose, row+1)
            visit_col[i] = False
            visit_right_cross[row + i] = False
            visit_left_cross[n - (i-row) - 1] = False
            chose.pop()
        
cnt = 0
n = int(input())
visit_col = [False] * n
visit_right_cross = [False] * (2 * n - 1)
visit_left_cross = [False] * (2 * n - 1)
back([], 0)

print(cnt)