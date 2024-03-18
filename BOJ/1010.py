'''
n개의 수로 이루어진 수열이 주어진다. 수와수 사이에 넣을 수 있는 n-1개 연산자가 있다.
식의 계산은 우선순위 무시하고 앞에서부터 진행한다. 나눗셈은 몫만 취하고
음수를 양수로 나눈ㄹ때는 양수로 바꾸고 몫을 취하고 그 몫을 음수로 바꾼다.
만들 수 있는 식의 결과의 최대 최소를 구하라

1. 모경수(prt, n=1)
1) 백으로 탐색 + 방문

* n : 수의 개수
수열
덧셈, 뺼셈, 곱셈, 나눗셈 개수
출력 : 최대 최소

2. 시복 : n^3
'''

max_r = int(1e9) * -1
min_r = int(1e9)

def back(calc, arrs_idx):
    global min_r,max_r
    
    if(arrs_idx == n):
        # print(max_r)
        max_r = max(max_r, calc)
        min_r = min(min_r, calc)
        return
    
    for i in range(n-1):
        # 연산자 종류를 훑음
        if(not visit[i]):
            visit[i] = True
            if(calcs_arr[i] == '+'):
                back(calc + arrs[arrs_idx], arrs_idx+1)
            elif(calcs_arr[i] == '-'):
                back(calc - arrs[arrs_idx], arrs_idx+1)
            elif(calcs_arr[i] == '*'):
                back(calc * arrs[arrs_idx], arrs_idx+1)
            elif(calcs_arr[i] == '//'):
                # 음수이면 
                if(calc < 0):
                    calc *= -1
                    calc //= arrs[arrs_idx]
                    calc *= -1
                else:
                    calc //= arrs[arrs_idx]
                back(calc, arrs_idx+1)
            visit[i] = False

n = int(input())
arrs = list(map(int, input().split()))
calcs_cnt = list(map(int, input().split()))
calc_type = ['+', '-', '*', '//']
calcs_arr = []
for i in range(4):
    for _ in range(calcs_cnt[i]):
        calcs_arr.append(calc_type[i])

# print(calcs_arr)
visit = [False] * len(calcs_arr)

back(arrs[0], 1)

print(max_r)
print(min_r)