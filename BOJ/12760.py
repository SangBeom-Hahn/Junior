'''
n명이 각 m장씩 카드를 가짐
n명이 각자 가진 카드 중 가장 큰 카드를 뽑아서 비교
가장 큰 수를 가진 플레이어가 1점 획득 가장 큰 수를 가진 플레이어가 여러 명일수 있다.
사용된 카드는 버린다.

플레이어 1      2           3           4           5
5 4 3           2 5 1       3 3 3       2 2 2       1 1 1

5               5           3           2           1
4               2           3           2           1

세트        최종 결과
1           1 1 0 0 0
2           2 1 0 0 0


1. 모경수
0) 결과 배열은 플레이어 수만큼 0으로 초기화

1) m번 반복
    0) 최종 최대값은 0으로 초기화, 최종 최대값의 플레이어 번호 0으로 초기화
    1) 플레이어 순회
        1] 최대값, 플레이어 번호 = idx를 뽑읍
        2] 배열에 저장함.
    3] 그 배열에서 진짜 최대값을 찾음
    4] 배열을 순회하면서 진짜 최대값과 최대값을 비교해서 같은 애들의 플레이어 번호에 result를 ++       
    
        
2) 최종 결과에서 max값 추출
3) 결과를 순회해서, 요소가 max와 같은 경우의 idx에 +1해서 출력

* n : 플레이어 수
m : 가진 카드 수
n줄에 각 플레이어가 가진 카드

출: m번 경기후 가장 점수가 높은 플레이어 번호, 여러명이면 오름차순 출력
플레이어 번호 : 1 ~ n번까지 입력 받은 순서로 

2. n^3

'''

n, m = map(int, input().split())
cards = []
for _ in range(n):
    cards.append(list(map(int, input().split())))

# print(cards)

# 1) m번 반복
#     0) 최종 최대값은 0으로 초기화, 최종 최대값의 플레이어 번호 0으로 초기화
#     1) 플레이어 순회
#         1] 최대값, 플레이어 번호 = idx를 뽑읍
#         2] 배열에 저장함.
#     3] 그 배열에서 진짜 최대값을 찾음
#     4] 배열을 순회하면서 진짜 최대값과 최대값을 비교해서 같은 애들의 플레이어 번호에 result를 ++  

result = [0] * n
for _ in range(m):
    final_max_v = 0
    final_idx = 0
    semi_max_v = []
    semi_idx = []
    
    for i in range(n):
        each_max_v = max(cards[i])
        semi_max_v.append(each_max_v)
        semi_idx.append(i)
        
        cards[i].remove(each_max_v)
    
    final_max_v = max(semi_max_v)
    for i in range(n):
        if(final_max_v == semi_max_v[i]):
            result[semi_idx[i]] += 1
            
#             2) 최종 결과에서 max값 추출
# 3) 결과를 순회해서, 요소가 max와 같은 경우의 idx에 +1해서 출력


max_ele = max(result)
for idx in range(n):
    if(max_ele == result[idx]):
        print(idx+1, end = ' ')
