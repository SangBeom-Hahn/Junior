'''
n개의 정수를 오름차순 정렬함.
k번째 교환되는 수를 구하자

선택
1] 가장 큰수를 골라
2] 맨뒤로 보내 (맨 뒤와 가장 큰수 -> 교환)
3] 다음은 맨뒤가 하나 앞이 되겠지

ex) 
k = 2
배열
3 1 2 5 4 -> 5랑 4교환

3 1 2 4 5 -> 이미 4가 맨뒤

3 1 2 4 5 -> 2랑 3

2 1 3 4 5

1 2 3 4 5

1. 모경수(prt, n=1)
ok 1) 맨앞 idx, 맨 뒤 idx를 만듦
ok 2) 맨앞 ~ 뒤를 훑어서 가장 큰거 찾음
ok 3) 가장 큰게 이미 맨뒤가 아니면 교환, 교환 횟수 ++
ok 4) 맨뒤 idx를 -1을 함
5) 교환 횟수랑 k랑 같으면 그때 교환한 거 2개 출력 (맨뒤가 더 작은거였겠지)

* n : 배열의 크기
k : 교환 횟수
배열 원소

출 : k번째 교환되는 두 개의 수를 작은 수부터 한 줄에 출력
교환 횟수가 k보다 작으면 -1 출력 (5 1 2 3 4 -> 1번 교환으로 정렬이 끝날수도 있으니)
'''

n, k = map(int, input().split())
arr = list(map(int, input().split()))

front = 1 # 최초 최대 값을 arr[0]으로 할거라서 1로 잡음
back = n
cnt = 0

flag = False

for _ in range(n-1): # 총 n-1번 가장 큰 것을 찾을 거임
    # 맨앞 ~ 뒤를 훑어서 가장 큰거 찾음
    max_v = arr[0]
    max_idx = 0
    for idx in range(front, back):
        if(max_v < arr[idx]):
            max_v = arr[idx]
            max_idx = idx
    
    # print("최대", max_v)
    if(max_v != arr[back-1]): # 3) 가장 큰 게 이미 맨뒤가 아니면 교환, 교환 횟수 ++
        arr[back-1], arr[max_idx] = arr[max_idx], arr[back-1]
        cnt += 1
        
        if(cnt == k):
            print(arr[max_idx], arr[back-1])
            flag = True
            break
    
    if(flag == True):
        break
        
    back -= 1    # 맨 뒤 인덱스는 교환을 하든 안하든 바뀌어야 함.
    # print("arr", arr)
    
    # 교환 횟수랑 k랑 같으면 그때 교환한 거 2개 출력 (맨뒤가 더 작은거였겠지)
else:
    print(-1) # break로 안 끝나면 k를 못 만난거, 즉 교환 횟수가 k 이하임