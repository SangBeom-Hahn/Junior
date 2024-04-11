'''
숫자 야구 : 
1] 1~9 서로 다른 숫자 3자리수 생각
2] 민역이가 그 세자리 수를 묻는다
3] 민혁이가 말한 수가 영수의 수와 동일한 위치면 스트라이크 1번, 숫자가 있긴하나 다른 위치면 볼한번
4] 영수는 민혁이가 말한 수를 스트와 볼로 답한다.
5] 민혁이가 맞출때까지 묻고 맞추면 겜 끝

ex) 
영수    
324     

429         1스트 1볼
241         0스트 2볼 (0스트도 셈)
924         2스트 0볼 (0볼도 셈)

민혁    영수        정답
123     1스트1볼    324, 328
356     1스트0볼

가능성이 있는 수 : 324, 328

1. 모경수(prt, n=1)
1) 1~9로 순열만듦
2) 민혁이가 물은 수에 대해 모든 수열을 훑어서 영수와 같은 대답이 안나오면 제거
    1] 스트라이크일 조건 : for문으로 0~2까지 훑는데 같은 인덱스의 요소 값이 같으면 스트+1
    2] 볼 조건 : 민혁이 수를 0~2로 훑으면서 해당 요소가 후보에 속하는 데 그 둘의 인덱스 값은 다른 경우 +1
3) 민혁이의 질문의 수만큼 ㄱㄱ


* 민혁이의 질문 수
민혁이가 어떤 수를 물었는지
각각의 물음에 대한 영수의 대답
출력 : 영수가 생각하고 있을 가능성이 있는 수가 총 몇개인지

2. 시복 : n^3
'''

# 1~9로 순열만듦
from itertools import permutations
perms = list(permutations(list(range(1, 10)), 3))
# print(perms)


n = int(input())
import copy
# tmp = copy.deepcopy(perms)

for _ in range(n):
# for _ in range(2):
    tmp = []
    # 민혁이가 물은 수에 대해 모든 수열을 훑어서 영수와 같은 대답이 안나오면 제거
    asks, strike, ball = map(int, input().split())
    # 3자리 요소의 배열로 만들고
    asks = list(map(int, list(str(asks))))
    # print(asks, strike, ball)
    
    for perm in perms:
        st_cnt = 0
        ba_cnt = 0
        # 스트 조건
        for i in range(3):
            if(asks[i] == perm[i]):
                st_cnt += 1
        
            elif(asks[i] in perm and asks[i] != perm[i]):
                ba_cnt += 1
        
        # print(strike, st_cnt, ball, ba_cnt)
        if(strike == st_cnt and ball == ba_cnt):
            tmp.append(perm)
    # print(tmp)
    perms = copy.deepcopy(tmp)
    
print(len(perms))