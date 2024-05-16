'''
n개의 정수로 된 수열, 
자연수 x : ai + aj (i < j)
x가 주어졌을 때 ai, aj의 쌍의 수를 구하라

1 2 3 5 7 9 10 11 12
x       ai      aj
13      1       12
        2       11
        3       10
        
5 

1. 모경수(prt, n=1)
1) 백트래킹 불가, 2중for 불가
2) 중복이 있을 수 없음
3) 정렬
4) 현재 인덱스부터 그 이후 인덱스의 값들을 다 순회해서 더해보고 같으면 break
5) 현재 인덱스부터 그 이후 인덱스까지 훑는데 합이 x보다 크면 break
6) ai가 x의 절반보다 크면 break
x 13이면 x의 절반 6 그니깐 절반까지는 가능

i j 가능 하니
6 7

7이면 6밖에 안되는데 7뒤에는 다 7보다 큰 것들이니 절반까지만 보자는 거임


* n : 수열의 크기
수열
x
출력 : 쌍의 개수

2.시복: nlogn
'''

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
arr = set(arr)


res = 0
cnt_arr = [0] * (max(arr) + 1)

# 계수 정렬처럼 개수 셈
for ele in arr:
    cnt_arr[ele] += 1

# print(arr)
# print(cnt_arr)

'''
x   x//2
13  6
10  5
11  6
'''

# for ele in arr:
#     if(ele > x//2):
#         break
    
#     if(cnt_arr[x-ele] == 1):
#         print(ele, x-ele)
#         res += 1

# print(res)


for ele in arr:
    if(x-ele in arr):
        # print(ele, x-ele)
        res += 1
        
print(res // 2)