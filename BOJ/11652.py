n = int(input())
arr = [int(input()) for i in range(n)]
# print(arr)
arr2 = []
arr.append(2**62+1)
# print(arr)
arr.sort()
# print(arr)

# print(arr)
currentCnt = 1
maxCnt = 0
maxNum = 0 # 해설에서는 이것을 -2^62 -1로 했는데 비교는 maxCnt로 하니 그냥 아무거나 초기화해도 상관없다고 생각했다

if(n == 1):
    print(arr[0])
else:
    for i in range(n):
        if(arr[i] == arr[i+1]):
            currentCnt += 1
        else:
            arr2.append(currentCnt)
            if(maxCnt < currentCnt):
                maxCnt = currentCnt
                maxNum = arr[i]
            currentCnt = 1
        # print(currentCnt)
    print(maxNum)

# print(arr2)