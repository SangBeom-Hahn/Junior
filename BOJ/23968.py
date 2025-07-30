'''
a = n개의 양의 정수 배열

버블정렬
1] 끝 점은 맨 뒤부터 시작하여 반복
2] 1번의 반복에서 1 ~ 끝 점까지 비교하여 a[i] > a[i+1]이면 교환
3] 끝점을 -1 / 끝점은 맨 앞 원소보다 하나 큰 값이 최소 점

ex)         
끝  시작    배열            현재        교환
5   0       4 6 5 1 3 2     0, 1        x
                            1, 2        o
            4 5 6 1 3 2
                            2, 3        o
            4 5 1 6 3 2     
                            3, 4        o
            4 5 1 3 6 2
                            4, 5        o
            4 5 1 3 2 6
            
4   0

1. 모경수(n=1, prt)
1) 시작점 0, 끝점 n-1
2) 끝점이 0이 될때까지 반복
    1] 시작점 ~ 끝점-1을 순회
    2] a[i] > a[i+1] 이면 교환, 교환수 ++
    3] 교환수 == k이면 출력하고 끝 break
    4] 끝점 -1
3) 반복이 끝나고 교환수가 k보다 작으면 -1 출력

* n, k : n개의 정수, 교환 횟수
원소 n개
출 : k번째 교환되는 두 개의 수를 작은수부터 출력
교환 횟수가 k보다 작으면 -1 출력

2. n^2
'''

n, k = map(int, input().split())
arr = list(map(int, input().split()))

st = 0
end = n-1
cnt = 0
flag = False

for end in range(n-1, 0, -1) :
    for idx in range(st, end):
        if(arr[idx] > arr[idx+1]):
            cnt += 1
            arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
            # print(arr)
            
        if(cnt == k):
            print(arr[idx], arr[idx+1])
            flag = True
            break
    
    if(flag == True):
        break
else:
    print(-1)
        