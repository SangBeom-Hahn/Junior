'''
게임
1] n명이 각각 k개의 카드를 가짐
2] 혜민이부터 반시계 방향으로 1 ~ N번 배정
3] 모두 바닥에 카드를 일렬로 내려 놓음.
4] 1번 사람의 제일 왼쪽 카드부터 선택해서 시작
    1] 카드 제거
    2] 해당 카드 숫자 기준 반시계 방향으로 해당 숫자 번째 위치한 카드를 선택해서 다시 시작
    (해당 카드 제거하고 번째를 세어야 함.)
5] 마지막 한 장의 카드 주인이 승리

ex) 
0 1 2 3 4 5
9 5 1 2 3 10

선택 인덱스     제거인덱스 모음     순회 인덱스                     원하는번째                  번째
0               0               1 -> 선택인덱스 + 1부터 순회        arr[선택인덱스] = 9         1
                                2                                                           2
                                3
                                4
                                5                                                           5
                                0 -> 제거인덱스 모임에 속하면 pass
                                1                                                           6
                                2
                                3
                                4                                                           9

4               [0, 4]          5                                3                          1
                                0 -> 무시
                                1                                                           2
                                2                                                           3


ex) n = 2, k = 1
0 1
1 2

선택 인덱스     제거인덱스 모음     순회 인덱스                     원하는번째                  번째
0               0               1 -> 선택인덱스 + 1부터 순회        arr[선택인덱스] = 1         1

1               [0, 1]          0

---

ex) n = 1, k = 1
0 
1

선택 인덱스     제거인덱스 모음     순회 인덱스                     원하는번째                  번째
0               0               1 -> 선택인덱스 + 1부터 순회        arr[선택인덱스] = 1         1


1. 모경수
1) 제거 인덱스 모음의 길이가 n * k와 같으면, 종료
    1] 맨마지막에 추가한 인덱스의 숫자와 주인번호 출력
2) 초기화
    ok 1] 배열에 (숫자, 주인번호)
    ok2] 선택인덱스 = 0
    ok3] 제거 인덱스 모음 []
    
3) 위 종료 조건이 만족할 때까지 반복
    0] 선택인덱스를 제거인덱스에 넣음
    1] while
        1] 순회 인덱스 : 선태 인덱스 + 1
        2] 원하는 번째 : 선택 인덱스의 숫자 배열 요소 값
        3] 현재 번째 : 1
        3] 배열 순회
            1] 순회 인덱스를 증가하면서 순회
            2] 순회 인덱스가 제거인덱스에 속하면 무시
            3] 안 속하면 현재 번째 ++
            4] 현재 번째 == 원하는 번째
                1] 해당 인덱스가 선택인덱스가 되고 반복
                2] 현재 번째 : 1


* n, k
1번부터 각 사람이 내려놓는 순서대로 바닥에 놓은 카드 번호

출 : 이긴 사람 번호, 마지막 남은 카드에 적힌 수

2. n^2
'''

n, k = map(int, input().split())
arr = []
master_num = 1

for _ in range(n):
    num_list = list(map(int, input().split()))
    for num in num_list:
        arr.append((num, master_num))
        
    master_num += 1

# print(arr)    

choose_idx = 0
remove_idx_list = []

# 1) 제거 인덱스 모음의 길이가 n * k와 같으면, 종료
#     1] 맨마지막에 추가한 인덱스의 숫자와 주인번호 출력

# 3) 위 종료 조건이 만족할 때까지 반복
#     0] 선택인덱스를 제거인덱스에 넣음
#     1] while
#         ok1] 순회 인덱스 : 선태 인덱스 + 1
#         ok2] 원하는 번째 : 선택 인덱스의 숫자 배열 요소 값
#         ok3] 현재 번째 : 1
#         3] 배열 순회
#             1] 순회 인덱스를 증가하면서 순회
#             2] 순회 인덱스가 제거인덱스에 속하면 무시
#             3] 안 속하면 현재 번째 ++
#             4] 현재 번째 == 원하는 번째
#                 1] 해당 인덱스가 선택인덱스가 되고 반복
#                 2] 현재 번째 : 1


su = 1
while(True):  
    
    #print("---")
    
    su += 1  
    remove_idx_list.append(choose_idx)
    
    #print(f"현재 선택한 숫자 {arr[choose_idx][0]}")
    #print(f"제거 인덱스 리스트 {remove_idx_list}")
    
    if(len(remove_idx_list) == n * k):
        print(arr[choose_idx][1], arr[choose_idx][0])
        break
    
    # 원하는 번째
    want_step = arr[choose_idx][0]
    
    #print("현재 원하는 번째", want_step)
    
    curr_step = 1
    # 순회 인덱스
    circle_idx = (choose_idx + 1) % (n * k)
    
    #print(f"최초 순회 인덱스 {circle_idx}")
    
    while(True):
        if(circle_idx in remove_idx_list):
            circle_idx = (circle_idx + 1) % (n * k)
            continue
        
        if(curr_step == want_step):
            choose_idx = circle_idx
            break
        
        circle_idx = (circle_idx + 1) % (n * k)
        curr_step += 1
            
        #print(f"순회 인덱스= {circle_idx}, 현재 단계= {curr_step}")
        
        
        
        
        
        