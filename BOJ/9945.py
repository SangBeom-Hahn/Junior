'''
도시 : 깊이 k 완전 이진 트리
노드 : 2**k - 1개
k       노드
1       1
2       3
3       7

노드에 번호가 있음, 상근이가 방문한 번호 순서가 있음
순서 : 전위순회 방법으로 들어감
ex)
순서 1 6 4 3 5 2 7
트리 3 6 2 1 4 5 7
3
6 2
1 4 5 7

-> 재귀
배열            mid idx     결과 인덱스     
1 6 4 3 5 2 7   3           0               

-> 왼 재귀
배열            mid idx     결과 인덱스
1 6 4           1           1

1               0           3

-> 오른 재귀
4               0           4

1. 모경수(prt, n=1)
1) 전위 순회를 재귀로 층위 순회로 만들 수 있다.
2) 재귀
    1] 종료 조건 : 길이가 1이면 종료
    2] 인자 : arr, 결과에 어디에 넣을 지 idx
    3] 재귀(arr, 결과에 어디에 넣을 지 idx * 2 + 1) = 왼재귀
    (arr, 결과에 어디에 넣을 지 idx * 2 + 2) = 오른 재귀

* k : 깊이
빌딩 방문 순서
출 : 각 레벨에 있는 빌딩의 번호 k 가 3이면 1, 2, 3레벨 빌딩 번호

2. n^3
'''
k = int(input())
arr = list(map(int, input().split()))
result = [0] * len(arr)

def div(arr, result_idx):
    if(len(arr) == 1):
        result[result_idx] = arr[0]
        return
    
    mid = len(arr) // 2
    result[result_idx] = arr[mid]
    
    div(arr[:mid], result_idx*2 + 1)
    div(arr[mid+1:], result_idx*2 + 2)
    
    
div(arr, 0)
print(result)