'''
ex)
1개 = 1
2개 = 2, 3, 4, 5, 6, 7 = 6개
3개 = 8, 9, 10, ,,, , 19 = 12개
4개 = 20, ,,, , 37 = 18개


37

1. 모경수(prt, n=1)
1) 1번도 지나는 방의 개수에 포함 = 시작은 1개
2) 1 ~ 1000000000까지 n이 들어올때 몇 개지나는지 해시 만듬
    1] 1 해시에 넣어둠
    2] 2 ~ 1000000000 순회
    2-1] 현재 개수 cnt, 최초는 1
    2-2] 현재 v = 1
    2-3] value = v + 1
    3] cnt가 6 * 1개(v)가 되면 / v++ / 현재 개수 = 1
    
    4] 6 * 2개 / v = 2개+1
    
    
    
3) n이 들어오면 해시 검색해서 출력

* n : 가려고 하는 방의 번호
출 : 1에서 n까지 가려고 할 때 몇 개의 방을 지나는지 출력

2. n
'''

import sys
input = sys.stdin.readline

n = int(input())  

if(n == 1):
    print(1)
else:
    cnt = 0
    v = 1
    for i in range(2, n+1):
    # for i in range(2, 40):
        if(i == n):
            print(v+1)
            
        cnt += 1
        
        if(cnt == 6 * v):
            v += 1
            cnt = 0
        