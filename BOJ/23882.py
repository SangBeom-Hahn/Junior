'''
A : n개의 서로 다른 양의 정수가 있다. 
선택 정렬로 A를 오름차순 정렬할 경우 K번 교환이 발생한 직후의 배열 A를 출력해보자.

선택 정렬
1] 가장 큰수부터 맨 뒤로 보내는 정렬 방식

ex)

3 1 2 5 4

횟수    배열
1       3 1 2 5 4 -> 5와 4 교환
        3 1 2 4 5
        
2       3 1 2 4 5 -> 3과 2 교환
        2 1 3 4 5 -> 2번째 교환 끝
        
1. 모경수(prt, n=1)        
ok1) 순화하는 맨 마지막 요소 idx = n-1
ok2) 맨 첫 요소 idx = 0
3) 순회하는 맨 마지막 요소 idx를 1씩 감소시키면서 선택 정렬
    ok 1] 첫 ~ 마지막 중 가장 큰 수 찾음
    ok 2] max의 idx가 맨 마지막 요소 idx가 아니면 교환
    ok 3] 교환 횟수 ++ -> 교환 횟수가 k면 배열 출력
    ok 4] 맨 마지막 요소면 무시
    5] 맨 마지막 요소 idx를 ++ 하고 교환 반복
    6] 맨 마지막 요소 idx가 0이 되면 끝

* n, k : n개의 정수, 교환 횟수 k
a의 원소
출 : k번 교환 발생 직후의 배열 a
교환 횟수가 k보다 작으면 -1

2. nlogn
'''

n, k = map(int, input().split())
arr = list(map(int, input().split()))

last_idx = n-1
first_idx = 0
cnt = 0

for _ in range(n-1):
    max_v = 0
    max_idx = 0
    for i in range(first_idx, last_idx+1):
        
        # 1] 첫 ~ 마지막 중 가장 큰 수 찾음
        if(arr[i] > max_v):
            max_v = arr[i]
            max_idx = i
            
    if(max_idx != last_idx):
        arr[last_idx], arr[max_idx] = arr[max_idx], arr[last_idx]
        cnt += 1
        
        if(cnt == k):
            print(*arr)
            break
    
    last_idx -= 1
else:
    print(-1)