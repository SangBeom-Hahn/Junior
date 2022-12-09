n = int(input())
dp = [[0] * n for i in range(3)]
arr = [[0] * n for i in range(3)]

# print(arr)

for j in range(n):
    l = list(map(int, input().split()))
    for i in range(3):
        arr[i][j] = l[i]

for i in range(3):
    dp[i][0] = arr[i][0]

for j in range(1, n):
    for i in range(3):
        dp[i][j] = min(dp[(i+1) % 3][j-1], dp[(i+2) % 3][j-1]) + arr[i][j]

mini = 99999999
for i in range(3):
    if(mini > dp[i][n-1]):
        mini = dp[i][n-1]

print(mini)
# print(dp)