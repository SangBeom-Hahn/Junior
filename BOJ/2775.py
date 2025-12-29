'''
a 층 b 호에 살 거임.
1] a-1층의 1 ~ b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다.
2] 0층에 i호에는 i명이 산다.

ex) 

층      호 (3호까지 있다고 치자)

0       1   2   3
1       1   3   6
2       1   4   10
3       1   5   15



1. 모경수(prt, n=1)
1) k+1행, n-1열짜리 배열에 0으로 채움
2) 0행에는 1, 2, 3,,,,으로 채움
3) 1~k행 순회
    1] 전체 열 순회
    2] 이전행의 합을 구함
        1] 현재행, 현재열의 이전행 값을 누적해서 더하면 될 듯

4) k행 n열 요소가 답

* T : 테케 수
k, n

출 : k층, n호에 몇 명이 살고 있는지 출력
2. n^3
'''

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    
    # k+1행, n-1열짜리 배열에 0으로 채움
    arr = [[0] * (n) for _ in range(k+1)]
    
    # 0행에는 1, 2, 3,,,,으로 채움
    for i in range(n):
        arr[0][i] = i+1
        
    for i in range(1, k+1):
        hab = 0
        for j in range(n):
            hab += arr[i-1][j]
            arr[i][j] = hab
    
    print(arr[k][n-1])