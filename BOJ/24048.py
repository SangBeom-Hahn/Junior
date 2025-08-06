'''
n, m 정원

규칙
1] 정원의 왼쪽, 위쪽 가장자리에도 격자와동일한 간격으로 n, m개 꽃이 있다.
2] 위에서 아래로, 왼에서 오른 순으로 꽃을 심음.
3] 왼, 위쪽 칸에 꽃의 색을 보고 두 꽃 색이 같으면 노랑, 다르면 빨강 심음.

1. 모경수(prt, n=1)
1) n+1, m+1 크기 배열
2) 0열, 0행을 가장자리로 채움
3) 1, 1부터 오른->왼 / 위->아래로 심음

* n, m
왼쪽 가장자리 꽃의 정보 (0 = 노랑, 1 = 빨강)
위 가장자리 꽃 정보

출 : n, m에 심어야 하는 꽃의 색깔

2. nlogn
'''

n, m = map(int, input().split())
left = list(map(int, input().split()))
top = list(map(int, input().split()))

arr = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    arr[i][0] = left[i-1]
    
for i in range(1, m+1):
    arr[0][i] = top[i-1]    
    
# print(*arr, sep = '\n')

for i in range(1, n+1):
    for j in range(1, m+1):
        if(arr[i-1][j] == arr[i][j-1]):
            arr[i][j] = 0
        else:
            arr[i][j] = 1
            
print(arr[n][m])            