import sys

def back(start, store):
    global cnt

    if(sum(store) == s and len(store) > 0): # s와 같은 이후로도 다시 s와 같아질 수 있으므로 return 없음
        # print(store)
        cnt += 1


    for i in range(start, len(arr)):
        if(not used[i]):
            store.append(arr[i])
            back(i+1, store)
            store.pop()

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
used = [False] * n
cnt = 0

back(0, [])
print(cnt)