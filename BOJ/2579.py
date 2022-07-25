n = int(input())
stairs = [0 for i in range(301)]

for i in range(n):
    stairs[i] = int(input())

dp = [0 for i in range(301)]

dp[1] = stairs[0]
dp[2] = stairs[0] + stairs[1]

for i in range(3, n+1):
    dp[i] = stairs[i-1] + max(stairs[i-2]+dp[i-3], dp[i-2])

print(dp[n])

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