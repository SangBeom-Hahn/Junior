'''
오름차순 정렬하라

ex) 5 2 3 1 4

선택    비교    선택한게 더 작음
2       5       o -> 2 5 3 1 4
3       5       o -> 2 3 5 1 4
        2       x
1       5       o




1. 모경수 (prt, n=1)
1) 삽입정렬
1] 길이가 1이면 하나 출력하고 끝
2] 길이가 2이상이면
    ok 1] 인덱스 1부터 ~ 맨뒤까지 봐서
    2] 선택한 것보다 앞을 역순회해서
    3] 선택한게 더 클때까지 계속 swap

2) 계차정렬
ok 1] 입력 최대값을 수용할 수 있을 만큼 0으로 초기화된 배열 만듦
2] 입력값을 순회하면서 값을 인덱스로 배열에 개수 ++
3] 배열을 순회하면서 배열 요소 개수만큼 인덱스 출력

* n : 수의 개수
n개의 수

출 : 오름차순 정렬

2. n
'''

import sys
input = sys.stdin.readline

n = int(input())

zero_arr = [0] * (10001)
for _ in range(n):
    ele = int(input())
    zero_arr[ele] += 1
    
for idx in range(10001):
    for _ in range(zero_arr[idx]):
        print(idx)


# if(n == 1):
#     print(arr[0])
# else:
#     for i in range(1, n): # 1 ~ 맨 뒤까지
#         stand = arr[i] # 삽입 기준값
#         for j in range(i-1, -1, -1):
#             if(stand < arr[j]):
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
        
#     for ele in arr:
#         print(ele)