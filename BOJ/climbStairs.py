N = int(input())
stair = [0 for i in range(300)]
dp = [0 for i in range(300)]

for i in range(1, N+1):
    stair[i] = int(input())

print(stair)
dp[0] = 0
dp[1] = stair[1]
dp[2] = stair[1]+stair[2]

for i in range(3, N+1):
    dp[i] = max(dp[i-2], dp[i-3]+stair[i-1]) + stair[i]

print(dp[N])

#문제를 잘 안 읽은 버전
# stair = [10, 20, 15, 25, 10, 20]
#
# dp = [0 for i in range(6)]
#
# dp[0] = stair[0]
# dp[1] = stair[0]+stair[1]
# dp[2] = max(stair[0], stair[1]) + stair[2]
#
# for i in range(3, 6):
#     dp[i] = max(dp[i-2], dp[i-3]+stair[i-1]) + stair[i]
#
# print(dp)