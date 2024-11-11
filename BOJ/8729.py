'''
7개의 led를 사용해서 0-9까지 숫자를 표시한다.

LED : 
 --
|  |
|  |
 --
|  |         스위치 1
|  |
 --
 
  A
F   B
  G
E   C
  D

ex) 숫자 조합 3 8 3 9
    3 : "ABCDG",
    8 : "ABCDEFG",
    3 : "ABCDG",
    9 : "ABCDFG"
    
숫자 조합 3
    3 : "ABCDG",

1) 최대 1개의 스위치에 연결할 수 있다.
2) 1개의 스위치에 LED를 여러개 연결할 수도 있다.

1. 모경수(prt, n=1)
1) abcdefg로 길이 1-7 조합을 구함
2) 길이 2 = AB BC EF
    1] 조합을 순회함
    2] 하나의 조합에서 숫자를 순회함
        1] 하나의 숫자에서 이 조합의 일부는 포함하는데 일부는 비포함이면 다른 숫자는 볼 필요
        없이 이 조합은 불가함
        2] 하나의 숫자에서 전체가 포함하면 가능한 조합
        3] 하나의 숫자에서 전체가 비포함 가능한 조합
            1] 다만 모든 숫자가 이 조합을 다 비포함 하면 불가한 조합

3) 조합을 순회하면서 현재 선택한 요소가 다른 요소에 속하면 pass
    1] 안 속하면 최종 결과에 넣음

* arr : 표시하려는 숫자 조합 ex 3, 8, 3, 9
출 : 숫자 조합에 필요한 스위치의 최소 개수

2. n^2

'''

dic = {
    0 : "ABCDEF",
    1 : "BC",
    2 : "ABDEG",
    3 : "ABCDG",
    4 : "BCFG",
    5 : "ACDFG",
    6 : "ACDEFG",
    7 : "ABCF",
    8 : "ABCDEFG",
    9 : "ABCDFG"
}

# 1) abcdefg로 길이 1-7 조합을 구함
# 2) 길이 2 = AB BC EF
#     1] 조합을 순회함
#     2] 하나의 조합에서 숫자를 순회함
#         1] 하나의 숫자에서 이 조합의 일부는 포함하는데 일부는 비포함이면 다른 숫자는 볼 필요
#         없이 이 조합은 불가함
#         2] 하나의 숫자에서 전체가 포함하면 가능한 조합
#         3] 하나의 숫자에서 전체가 비포함 가능한 조합
#             1] 다만 모든 숫자가 이 조합을 다 비포함 하면 불가한 조합

arr = [3]
digit = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
from itertools import combinations

combs = []
for i in range(1, 8):
    for comb in list(combinations(digit, i)):
        combs.append(comb)

# 2] 하나의 조합에서 숫자를 순회함
#         1] 하나의 숫자에서 이 조합의 일부는 포함하는데 일부는 비포함이면 다른 숫자는 볼 필요
#         없이 이 조합은 불가함
#         2] 하나의 숫자에서 전체가 포함하면 가능한 조합
#         3] 하나의 숫자에서 전체가 비포함 가능한 조합
#             1] 다만 모든 숫자가 이 조합을 다 비포함 하면 불가한 조합

semi_result = []
for comb in combs:
    # ex) 숫자 조합 3 8 3 9
    # 3 : "ABCDG",
    # 8 : "ABCDEFG",
    # 3 : "ABCDG",
    # 9 : "ABCDFG"
    can_flag = False
    for num in arr: # 3 : ABCDG
        include = False
        exclude = False
        for ele in comb: # A, E
            if(ele in dic[num]):
                include = True
            
            elif(ele not in dic[num]):
                exclude = True
        
        if(include == True and exclude == True):
            break
    
        if(include == True): # 하나의 숫자에서 전체가 포함하면 가능한 조합
            can_flag = True
    
    else: # break를 안하면! 전체가 포함해서 break을 안하거나 전체가 비포함해서 break을 안한거겠지?
         if(can_flag == True): # 어떤 숫자는 한번이라도 이 조합을 포함하면 
            semi_result.append(comb)

# print(semi_result)            
result = []
# 3) 조합을 순회하면서 현재 선택한 요소가 다른 요소에 속하면 pass
#     1] 안 속하면 최종 결과에 넣음

for comb in semi_result:
    for another in semi_result:
        if(comb != another):
            
            for ele in comb:
                if(ele not in another):
                    break
            else: # 다 속하면
                break
    else:
        result.append(comb)
print(result)

# for d in digit:
#     for comb in 