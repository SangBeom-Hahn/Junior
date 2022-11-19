N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(input()))
maximum = 1

for i in range(N):
    for j in range(M):
        ac = 1
        while(i+ac <= N-1 and j+ac <= M-1):
            if(arr[i][j] == arr[i][j+ac] and arr[i][j] == arr[i][j+ac]\
                   and arr[i][j] == arr[i+ac][j] and arr[i][j] == arr[i+ac][j+ac]):
                maximum = max(maximum, ac+1)
            ac += 1

print(maximum ** 2)
