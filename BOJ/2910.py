# 이코테 방식
n, c = map(int, input().split())
cnt = []
arr = list(map(int, input().split()))
print(arr)

for i in range(c+1):
    print(cnt)
    cnt.append((i, arr.count(i)))

cnt = sorted(cnt, key=lambda x:(-x[1], x[0]))
print(cnt)

for su in cnt:
    for j in range(su[1]):
        print(su[0], end=" ")

# 계수정령



# 스웩 내 방식
n, c = map(int, input().split())
dic = {}
arr = list(map(int, input().split()))
# print(arr)

for i in arr:
    if(i in dic):
        dic[i] += 1
    else:
        dic[i] = 1
# print(dic)

cnt = sorted(dic.items(), key=lambda x:-x[1])
# print(cnt)

for i in cnt:
    for j in range(i[1]):
        print(i[0], end=" ")