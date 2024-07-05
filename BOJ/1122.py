'''
2차원 배열 z 모양 탐색한다. 2x2 보다 큰 4x4, 8x8의 경우 4등분한 후 재귀적으로 
순서대로 방문한다. r행, c열을 몇 번째로 방문하는지 구해라

1. 모경수(prt, n=1)
1) 4등분으로 재귀
2) mid를 방문 순서로 활용
3) 재귀하면 좌상단으로 모는 기술

* n, r, c : 2^n x 2^n (n=1이면 2x2), r행 c열
출 : r행 c열을 몇 번째로 방문하는지
2.시복 : 4^15
'''

def rec(n, r, c):
    if(n==0): return 0
    
    mid = 2**n // 2
    if(r < mid and c < mid): return rec(n-1, r, c)
    if(r < mid and c >= mid): return mid * mid + rec(n-1, r, c-mid)
    if(r >= mid and c < mid): return 2* mid * mid + rec(n-1, r-mid, c)
    return 3 * mid * mid + rec(n-1, r-mid, c-mid)

n, r, c = map(int, input().split())
print(rec(n, r, c))