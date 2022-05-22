#배수가 됐을 때 dp의 중간 값들은 이용하지 않음 따라서 17이 13 111 아니면 77 111이 됨
# N = int(input())
# dp = [0 for i in range(N+1)]
# coin = [5, 2, 1]
#
# dp[1] = 1
# for i in range(1, N+1):
#     for j in coin:
#         if(i % j == 0):
#             mini = i//j
#             break #다른 코인 안 본다, 다음 숫자 본다는 아님
#
#     dp[i] = min(dp[i-1]+1, mini)
#
# print(dp)


# 이건 dp 중간 값들을 다 본 것
N = int(input())
dp = [0 for i in range(N+1)]
coin = [1,4,7,13,28,52,91,365]
coin.reverse()


dp[1] = 1
for i in range(2, N+1):
    t = i
    for j in coin:
        if(j <= i):
            dp[t]=dp[t]+i//j
            i=i%j

print(dp)
