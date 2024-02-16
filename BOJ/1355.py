'''
숫자로만 이루어진 문자열 s가 입력으로 주어진다.(길이가 0이상 1000이하)
조건 : 
1) (길이간 N)인 (s의 substring)을 10진수로 읽은 숫자
2) 1~N까지의 숫자를 하나씩 사용하여 만든 N자리 수(N은 1이상 9이하)

1. 모경수(prt, n=1)
ex) s = 1451232125, n = 2
조건 : 1~2까지의 숫자를 하나씩 써서 길이가 2인 숫자 = 12, 21 > 그 중 큰 21

1) 구간을 무조건 미리 구해놓는게 빠름, 구간을 미리 다 구해서 배열에 저장
2) 각 구간을 set으로 관리하고 1~N까지 숫자가 각 구간에 in하는 지 체크(있으면 가장 큰수, 없으면 -1)
3) set으로 하니 각 part가 순서가 사라지네 dic로 관리해야 함 key로 보자

* s, n
출력 : 조건을 만족하는 수를 찾아라, 여러개라면 가장 큰 수, 존재 x면 -1

2. 시복 nlogn
'''

# s = "1451232125"
# n = 2

# s = "313253123"
# n = 3

s = "12412415"
n = 4

# 구간을 무조건 미리 구해놓는게 빠름, 구간을 미리 다 구해서 배열에 저장
# 인덱스 0~len(s)-n
part = []
for i in range(len(s)-n+1):
    part.append(s[i:i+n])
    
print(part)

# 각 구간을 dic로 관리하고 
# 1~N까지 숫자가 각 구간에 in하는 지 체크(있으면 가장 큰수, 없으면 -1)
set_part = {}
for ele in part:
    set_part[tuple([i for i in ele])] = "" # 리스트를 키로 보려면 튜플로 바꿔야 함
# print(set_part)

check_nums = [str(i) for i in range(1, n+1)]

results = []
for part in set_part.keys():
    # print(part)
    for digit in check_nums:
        if(digit not in part): #1~N 중 하나라도 없으면
            break
    else: #다 있으면
        results.append(part)
        
print(results)

