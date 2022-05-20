dp = []
loc = []
x_y = []

N, M = map(int, input().split()) #테이블의 크기, M개의 치즈

for i in range(N):
    dp_sub = [0 for j in range(N)]
    dp.append(dp_sub)

for i in range(M):
    xy_list = []
    y, x = map(int, input().split())
    ex_X = N-x
    ex_Y = y-1

    # x_y = list(map(int, input().split()))
    loc.append([ex_X, ex_Y])

print(loc)

#베이스 가장 밑에 행 0으로, 가장 왼쪽 열 0으로
dp[N-1][0] = 0 # 가장 베이스

#가장 밑에 행 베이스 채우기
for j in range(1, N):
    sig = 0

    for x in range(M):
        if(loc[x][0] == N-1 and loc[x][1] == j):
            sig = 1
            break
        else:
            sig = 0

    if (sig == 1):
        dp[N-1][j] = dp[N-1][j-1]+1
    else:
        dp[N-1][j] = dp[N-1][j - 1]
    sig = 0


# 가장 왼쪽 열 베이스 채우기
for i in range(N-2, -1, -1):
    sig = 0

    for x in range(M):
        if(loc[x][0] == i and loc[x][1] == 0):
            sig = 1
            break
        else:
            sig = 0

    if (sig == 1):
        dp[i][0] = dp[i + 1][0] + 1
    else:
        dp[i][0] = dp[i + 1][0]
    sig = 0

# 여기서부터는 4행 1열부터 다룸 -> 더하기만 하면 됨

for i in range(N-2, -1, -1):
    for j in range(1, N):
        sig = 0
        for x in range(M):
            if (loc[x][0] == i and loc[x][1] == j):
                sig = 1
                break
            else:
                sig = 0

        if (sig == 1):
            dp[i][j] = max(dp[i+1][j], dp[i][j - 1])+1
        else:
            dp[i][j] = max(dp[i+1][j], dp[i][j - 1])
        sig = 0
print(dp)

















# stairs = [0, 10, 20, 15, 25, 10, 20] # 1, 2, 3, 4, 5, 6으로 6층이 마지막 층으로 계단 값
#
# dp = [0 for i in range(7)]
#
# dp[0] = 0
# dp[1] = stairs[1]
# dp[2] = stairs[1] + stairs[2]
#
# for i in range(3, 7):
#     dp[i] = stairs[i] + max(stairs[i-1]+dp[i-3], dp[i-2])
#
# print(dp[6])