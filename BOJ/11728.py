'''
정렬된 두 배열 a, b가 있다.

ex)
a = 3 5
b = 2 9
결과 2, 3, 5, 9


1. 모경수(prt, n=1)
1) 두 배열을 앞에서부터 순회한다.
2) 각 배열의 포인팅 요소를 비교한다
    1] 더 작은 것을 배열에 넣는다
    4] 넣은 배열은 포인팅을 ++한다
    5] 배열의 끝을 본 배열이 있으면 끝을 안 본 배열을 다 넣는다


* n : a의 크기, m
a의 요소
b의 요소

출 : 두 배열을 합친 후 정렬한 결과 출력
2. n
'''

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_idx = 0
b_idx = 0
result = []

while(True):
    print(result, a_idx, b_idx)
    if(a[a_idx] <= b[b_idx]):
        result.append(a[a_idx])
        a_idx += 1
    else:
        result.append(b[b_idx])
        b_idx += 1
    
    if(a_idx == n):
        for idx in range(b_idx, m):
            result.append(b[idx])
        
        break
    elif(b_idx == m):
        for idx in range(a_idx, n):
            result.append(a[idx])
        
        break
        
print(*result)