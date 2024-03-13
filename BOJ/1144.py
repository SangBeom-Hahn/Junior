'''
n개의 정수로 이루어진 수열이 있다. 그 수열의 원소를 다 더한 값이 s가 되는 경우의 수 ㄱ

1. 모경수
1) 백으로 탐색 + 시작점

* n, s
출력 : 합이 s가 되는 부분 수열의 개수
2. 시복 : nlogn
'''

def back(chose, start):
    global cnt
    
    if(len(chose) > 0 and sum(chose) == s):
        cnt += 1
        
    
    for i in range(start, n):
        chose.append(eles[i])
        back(chose, i+1)
        chose.pop()

cnt = 0
n, s = map(int, input().split())
eles = list(map(int, input().split()))

back([], 0)
print(cnt)