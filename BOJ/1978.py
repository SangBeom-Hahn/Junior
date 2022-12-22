prime = [2, 3]
for i in range(5, 1001, 2):
    j = 1
    while(prime[j] * prime[j] <= i):
        if(i % prime[j] == 0):
            break
        j += 1

    else:
        prime.append(i)


# print(prime)

n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in arr: # 체크하려는 수 7 % 2, 3, 4
    if(i in prime):
        cnt += 1
print(cnt)