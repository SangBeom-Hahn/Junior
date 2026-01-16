'''
n장의 카드에 정수가 있다.
k개를 선택해서 나란히 둬서 정수를 만들 거다. k1 k2 k3,,,

1. 모경수(prt, n=1)
1) 백으로 탐색, used




* n
k
n개의 카드에 적힌 수

출 : 만들 수 있는 정수의 개수

2. n^3

'''
result = set()

def back(chose):
    if(len(chose) == k):
        result.add(''.join(chose))
    
    for i in range(n):
        if(not used[i]):
            used[i] = True
            chose.append(arr[i])
            back(chose)
            chose.pop()
            used[i] = False

n = int(input())
k = int(input())
arr = [input() for _ in range(n)]
used = [False] * n

back([])
print(len(result))