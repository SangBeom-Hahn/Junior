'''
7개 led로 0-9까지를 표시할 수 있다. 7개의 led는 A~G로 표현되고 스위치를 연결해서
led를 점등한다.

 A
F  B
 G
E  C
 D


---
|  |
|  |
---
|  |
|  |
---

led를 최대 1개의 스위치에 연결할 수 있다. 여러 led를 같은 스위치에 연결하면
필요한 스위치 개수를 줄일 수 있다.

ex) 3839

3 : "ABCDG"
8 : "ABCDEFG"
3 : "ABCDG"
9 : "ABCDFG"

3 : "ABCDG"
7 : "ABCF"
9 : "ABCDFG"

-> ABCDG / E / F 조합
AF / CDGE / B
ABCDF / EF

ABC / DG / EF
ABC / DG / E / F 

1. 모경수(prt, n=1)
1) 1 ~ 7 짜리 조합을 구함
2) 조합을 순회하면서 가능한 조합만 남김
    -> 가능
    1] ABCDG처럼 모두 속하면 OK
    
    -> 불가능
    1] CDGE처럼 8에는 속하고 3에는 안 속하면 
    2] AF처럼 8, 9에는 속하는데 3에는 안속하면
        1] 8, 9는 AF를 전부 가져
        2] 3은 A는 속하는데 F는 안속함 -> 이러면 안됨
        
    -> 가능
    1] ABC처럼 모두 속하면 OK
    2] DG처럼 어디엔 속하고 어디엔 아예 안속해도 OK
    
    -> 불가능
    1] EF처럼 어디에 F는 속하는데 E는 안속하면  
    2] 아무대도 안속하면 그 조합은 패스
    
    -> 가능
    1] 모두 속하는 거 OK
    2] 어딘가엔 속하는데, 어딘가엔 아예 안속하면 
    
    -> 불가능
    1] 아무 숫자에도 안속하면 그 조합은 패스 -> 어딘가엔 무조건 속해야함
    2] 어딘가엔(8) 속하지만, 어딘가엔(3) 일부만 속하면 안됨
    
3) 가능한 조합을 모두 찾음
4) 조합을 순회하면서 조합의 요소가 다른 조합 요소에 속하면 뺌 ex) A가 AC에 속함
5) 마지막 남은 조합이 결과임

* arr : 표시하려는 숫자 조합 = 3839
출 : 필요한 스위치의 최소 개수
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
    9 : "ABCDFG",
}

nums = "3839"
arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
from itertools import combinations

combs = []
for i in range(1, 8):
    for comb in list(combinations(arr, i)):
        combs.append(comb)
            
        
print(*combs, sep = '\n')        

# -> 가능
#     1] 모두 속하는 거 OK
#     2] 어딘가엔 속하는데, 어딘가엔 아예 안속하면 
    
# -> 불가능
#     1] 아무 숫자에도 안속하면 그 조합은 패스 -> 어딘가엔 무조건 속해야함
#     2] 어딘가엔(8) 속하지만, 어딘가엔(3) 일부만 속하면 안됨
can_comb = []
for comb in combs: # 가능한 조합인지 봄
    can_flag = False

    for digit in nums: # nums = 3839
        some_contain_flag = False
        some_not_contain_flag = False
        each_num = dic[int(digit)] # 3 : "ABCDG"
        
        # 일부만 속하냐, 안속하냐 flag를 구함
            # 속하냐만 있으면 속하는 거임
            # 안속하냐만 있으면 만약 모든 숫자에 안속하면 뺴야함, 어떤 숫자는 속하면 암뺌
            # 속하고 안속하고 둘다 있으면 빼야함
            
        for ele in comb:
            if(ele in each_num): # A는 ABCDG에 속함
                some_contain_flag = True
                
            if(ele in each_num): # AF는 ABCDG에 속하는 것도 있고 아닌 것도 있음
                some_not_contain_flag = True
        
    
        # 속하냐만 있으면 속하는 거임
        if(some_not_contain_flag != True and some_contain_flag != True):
            can_flag = True
            
    if(can_flag == True):
        can_comb.append(comb)
        
            
print(*can_comb, sep = '\n')