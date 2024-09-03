'''
nxn 도시가 있다. 도시는 빈칸0, 치킨집2, 집1 중 하나임
치킨 거리 : 집과 가장 가까운 치킨집 사이의 거리다.
도시 치킨 거리 : 모든 집의 치킨 거리의 합이다.
(a, b), (c, d) 거리 : |a-c| + |b-d|이다.

치킨집의 최대 개수는 M개다. 
치킨집 중 M개를 골라서 도시의 치킨 거리가 가장 작게 될지 구하라



1. 모경수(prt, n=1)
1) 치킨 집의 모든 좌표를 하나의 배열에 넣음 조합 m을 돌림
2) 각 조합마다 도시 치킨 거리를 구함
  1] 하나의 조합에서 도시 치킨 거리 구하는 법
    1] 하나의 집이 들어오고
    2] 그 집과 가장 가까운 치킨 집과의 거리를 구함 = 그게 그 집의 치킨 거리임
    3] 모든 집의 치킨 거리를 구함
    4] 그것을 합함
3) 하나의 조합에서 구한 도시 치킨 거리의 최소값을 구함

* n, m : nxn과 치킨집 조합의 수
도시 상태(0, 1, 2) = (빈, 집, 치킨)
출 : 최대 M개의 집을 골랐을 때 치킨 거리의 최소값

2. n^2
'''

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

all_chick_loc = []
all_home_loc = []
for i in range(n):
  for j in range(n):
    if(graph[i][j] == 2):
      all_chick_loc.append((i, j))
    elif(graph[i][j] == 1):
      all_home_loc.append((i, j))
      
# 치킨 집의 모든 좌표를 하나의 배열에 넣음 조합 m을 돌림      
from itertools import combinations

result = int(1e9)
for comb in list(combinations(all_chick_loc, m)):
  print(comb)
  
  # 2) 각 조합마다 도시 치킨 거리를 구함
  # 1] 하나의 조합에서 도시 치킨 거리 구하는 법
  #   1] 하나의 집이 들어오고
  #   2] 그 집과 가장 가까운 치킨 집과의 거리를 구함 = 그게 그 집의 치킨 거리임
  #   3] 모든 집의 치킨 거리를 구함
  #   4] 그것을 합함
  each_comb_city_chick_dis = 0
  for home_x, home_y in all_home_loc:
    min_each_chick_dis = int(1e9)
    
    for chick_x, chick_y in comb:
      dis = abs(home_x - chick_x) + abs(home_y - chick_y)
      min_each_chick_dis = min(min_each_chick_dis, dis)
    
    each_comb_city_chick_dis += min_each_chick_dis
  result = min(result, each_comb_city_chick_dis)
      
    # print(home_x, home_y, min_each_chick_dis)
print(result)
    
  