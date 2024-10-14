'''
n개의 수열이 있음.
오등큰수 = ngf(i) = 오른쪽에 있으면서 등장횟수가 fai보다 큰수 중 가장 왼쪽에 있는 수
fai = ai가 수열 a에 등장한 횟수
그런게 없으면 -1이다.

a = 1 1 2 3 4 2 1 / f(1) = 3, f(2) = 2
nfg(A1) = A1의 오른쪽에 있으면서 등장횟수가 f(A1) = f(1) 보다 큰 수 중에서 가장 왼쪽에 있는 수
= -1 그런수가 없다.

nfg(A3) = A3의 오른쪽에 있으면서 등장횟수가 f(A3) = f(2) 보다 큰 수 중에서 가장 왼쪽에 있는 수
= A7이다.

f(1) = 3, f(2) = 2, f(3) = 1, f(4) = 1
idx     값      스택
0       1       1 = 스택이 비면 넣음
1       1       1 1 = 현재 오등큰수가 스택 오등큰수보다 작거나 같으면 넣음
2       2       1 1 2 = 현재 오등큰수가 스택 오등큰수보다 작거나 같으면 넣음
3       3       1 1 2 3 
4       4       1 1 2 3 4
5       2       1 1 2 3 팝 = 현재 오등큰수가 스택 오등큰수보다 크면 팝, 해당 idx에 현재 값

1. 모경수(prt, n=1)
1) 각 등장횟수를 구함
2) stack을 할 때, 현재 등장횟수를 고려함

* n = 수열의 크기 
수열의 원소
출 : 각 원소의 오등큰수를 구하라

2. nlogn
'''
from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
cnt = Counter(arr)
result = [-1] * n

print(cnt)
stack = []
for i in range(n):
    while(stack and cnt[arr[i]] > cnt[stack[-1][0]]):
        value, idx = stack.pop()
        result[idx] = arr[i]
        
    stack.append((arr[i], i))
    
print(result)    