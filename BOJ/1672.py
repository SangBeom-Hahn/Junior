'''
n개의 염기 서열이 있다.
염기서열을 표로 해독할 거다.

방법
1] n-1 : 제일 끝에서 하나 앞
2] n : 제일 끝
3] 표에 대응하는 하나의 염기로 바꾸는 방식을 반복

ex) AAGTCG > AAGTT > AAGT > AAA > AA > A

CG > T
TT > T
GT > A
AA > A
AA > A

1. 모경수(prt, n=1)
0) 표를 dic으로 만듦
1) 뒤에서부터 맨 앞까지 순회
2) 변환
    1] 최초엔 n-1, n 뽑아서 변환
    2] for문 돌면서 n-2부터 최초에 변환한거랑 붙여서 2개씩 묶어서 변환함
        1] n-2 + 변환결과를 붙여서 > 변환
        3] 쭉쭉쭉
    

* N : 염기 서열
염기 서열

출 : 최종 염기 출력

2. nlogn

'''

dic = {
    "AA" : "A",
    "AG" : "C",
    "AC" : "A",
    "AT" : "G",
    "GA" : "C",
    "GG" : "G",
    "GC" : "T",
    "GT" : "A",
    "CA" : "A",
    "CG" : "T",
    "CC" : "C",
    "CT" : "G",
    "TA" : "G",
    "TG" : "A",
    "TC" : "G",
    "TT" : "T"
}

# 1) 뒤에서부터 맨 앞까지 순회
n = int(input())
arr = input()

# 2) 변환
#     1] 최초엔 n-1, n 뽑아서 변환
#     2] for문 돌면서 n-2부터 최초에 변환한거랑 붙여서 2개씩 묶어서 변환함
#         1] n-2 + 변환결과를 붙여서 > 변환
#         3] 쭉쭉쭉

if(n == 1):
    print(arr)
else:
    change = dic[arr[n-2:]]

    # print(change)

    for i in range(n-3, -1, -1):
        # 2) 변환결과 붙여가면서 ㄱㄱ ex) AAGTCG > AAGTT > AAGT > AAA > AA > A
        
        result = arr[i] + change
        change = dic[result]
        # print(change)
        # print(f"헤드 {head}")
        # print(f"테일 {tail}")
        # print(f"변환결과 {dic[tail]}")
        
    print(change)