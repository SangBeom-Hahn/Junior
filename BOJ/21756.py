'''
1 ~ N의 수

작업
1] 수가 하나 남을 때까지 반복
    1] 수가 하나 남았나 확인 -> 하나라면 끝
    2] 홀수번 칸의 수를 모두 지워 (홀수번 칸!!을 지우는 거임)
    3] 남은 수를 모두 왼쪽으로 모아
    
    
ex) 1 -> 1

n = 2
1 2
1번 작업 후 : 2
2번 작업 후 : 2

n = 5
1 2 3 4 5
1번 작업 후 : 2 4
2번 : 2 4
1번 : 4

1. 모경수(prt, n=1)
ok 1) 1 ~ n을 가지는 배열
2) 작업
    1] 종료조건
        1] 배열의 0의 개수를 셈
        2] 0의 개수 == n-1이면 끝
    ok 2] idx 짝수 0 2 4 이 자리의 요소를 0으로 바꿔
    ok 3] 배열 순회해서 0이 아닌 애들을 new 배열에 넣어

* n
출 : 마지막 남은 수

2. n^3

'''

n = int(input())
arr = list(range(1, n+1))

while(True):
    leng = len(arr)
    cnt = arr.count(0)
    if(cnt == leng-1):
        print(arr[0])
        break
    
    
    # 2] idx 짝수 0 2 4 이 자리의 요소를 0으로 바꿔
    
    for i in range(0, leng, 2):
        arr[i] = 0
        
    # 3] 배열 순회해서 0이 아닌 애들을 new 배열에 넣어
    new_arr = []
    for ele in arr:
        if(ele != 0):
            new_arr.append(ele)
            
    arr = new_arr