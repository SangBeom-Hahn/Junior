'''
nxn에 사탕이 있음, 사탕의 색은 모두 같지 않을수있음, 
색이 다른 인접한 두 칸을 골라서 교환한다. 이제 가장 긴 연속 행또는 열을 고른다음 먹는다.

1. 모경수(prt, n=1)
1) 2중 for로 오른쪽이랑 아래로 딱 한칸 비교하는 거니 -1만큼 순회함
2) 한칸에서 오른쪽이나 아래가 다르면 교체하고 원래칸에서 행, 열로 연속 한거 개수 셈
3) 최대값 구함

* n : 보드의 크기
사탕 색상
출력 : 상근이가 먹을 수 있는 사탕의 최대 개수 ㄱ
2. 시복 : n^2
'''

# 행, 열로 연속 한거 개수 셈
def count(x, y):
    global max_cnt
    
    # 연속한거 세기 위해서 맨 마지막에 하나 추가함
    temp = [[0] * (n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            temp[i][j] = candies[i][j]
    
    # 행에서 연속한 거 개수 셈 = 행 고정
    # print(*temp, sep='\n')
    # print()
    cnt = 1
    for i in range(n):
        if(temp[x][i] == temp[x][i+1]):
            cnt += 1
    
    max_cnt = max(max_cnt, cnt)        
    
    # 열 고정
    cnt = 1
    for i in range(n):
        if(temp[i][y] == temp[i+1][y]):
            cnt += 1
            
    max_cnt = max(max_cnt, cnt)
    
    



# 2중 for로 오른쪽이랑 아래로 딱 한칸 비교하는 거니 -1만큼 순회함
n = int(input())
candies = [list(input()) for _ in range(n)]
# print(*candies, sep='\n')
max_cnt = 0

for i in range(n):
    for j in range(n-1):
        # 기본으로 카운트도 한번은 셈
        count(i, j)
        
        # i=행이 맨 아래 일 때는 오른쪽만 봄
        if(i==n-1):
            if(candies[i][j] != candies[i][j+1]):
                # print(1, "오른쪽 바꿈", i, j)
                
                candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
                # print(*candies, sep='\n')
                count(i, j)
                # 원상 복구
                candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
        
        # j=열이 맨 오른쪽일때는 아래만 봄
        elif(j==n-1):
            if(candies[i][j] != candies[i+1][j]):
                # print(2, "아래바꿈", i, j)
                candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
                count(i, j)
                candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
        
        else:
            # 한칸에서 오른쪽이나 아래가 다르면 교체하고 원래칸에서 행, 열로 연속 한거 개수 셈
            # 오른쪽
            if(candies[i][j] != candies[i][j+1]):
                # print(3, "오른쪽바꿈", i, j)
                candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
                # print(*candies, sep='\n')
                count(i, j)
                # 원상 복구
                candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
            
            # 아래
            if(candies[i][j] != candies[i+1][j]):
                # print(4, "아래바꿈", i, j)
                candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
                count(i, j)
                candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
            
print(max_cnt)            