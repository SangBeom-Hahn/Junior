n = int(input())
arr = list(map(int, input().split()))
arr.sort()

if(n % 2 == 0):
    sumA = sumB = 0
    for i in arr:
        sumA += abs(arr[(len(arr)-1)//2] - i)

    for i in arr:
        sumB += abs(arr[(len(arr))//2] - i)
    # print(sumA, sumB)

    print(arr[(len(arr)-1)//2] if(sumA <= sumB) else arr[(len(arr))//2])
else:
    print(arr[len(arr)//2])