'''
n개의 기차가 은하수를 건넘(1 ~ N번 기차)
1개 기차 20개의 1열로 된 좌석

명령:
1] i번 기차에 x번 좌석에 사람을 태움, 이미 사람이 있다면 아무런 행동 X
2] i번 기차에 x번 좌석에 앉은 사람은 하차, 아무도 없었다면 아무런 행동 x
3] i번 기차에 앉아있는 승객들이 모두 한칸씩 뒤로 이동, 20번째 좌석에 사람은 하차
4] i번 기차 모두 한칸씩 앞으로 이동 1번사람 하차

m개의 명령 후 1번부터 기차가 순서대로 은하수를 건넌다. 
조건 : 
1] 이미 지나간 기차 상태라면 은하수 못 건넘

ex)(명령번호, i번기차, x번 칸)
명령        기차                최종 기차 상태
1 1 1       1번                 1번[, 1, 1]
1 1 2       1번                 2번[, 1, 1]
1 2 2       2번 
1 2 3       2번
3 1         1번

1. 모경수(prt, n=1)
1) 기차 수만큼 길이 20짜리 deque 기차 목록을 만듦
2) 명령 수만큼 명령 순회
    1] 명령수행
3) 명령이 다 끝나고 기차 상태를 set에 저장
4) set의 길이가 답

* n : 기차의 수
m : 명령의 수
m개의 명령(명령번호, i번기차, x번 칸)
출 : 은하수를 건널 수 있는 기차의 수

2. nlogn
'''
n, m = map(int, input().split())

# 1) 기차 수만큼 길이 20짜리 deque 기차 목록을 만듦
from collections import deque
trains = []
for _ in range(n):
    trains.append(deque([0] * 20))

# print(trains)    

# h = deque([1, 2, 3])
# h.rotate(1)

# print(h)

# 2) 명령 수만큼 명령 순회
#     1] 명령수행

# 1] i번 기차에 x번 좌석에 사람을 태움, 이미 사람이 있다면 아무런 행동 X
# 2] i번 기차에 x번 좌석에 앉은 사람은 하차, 아무도 없었다면 아무런 행동 x
# 3] i번 기차에 앉아있는 승객들이 모두 한칸씩 뒤로 이동, 20번째 좌석에 사람은 하차
# 4] i번 기차 모두 한칸씩 앞으로 이동 1번사람 하차
for _ in range(m):
    ele = list(map(int, input().split()))
    num = i = x = 0
    if(ele[0] == 1 or ele[0] == 2):
        num = ele[0]
        i = ele[1]
        x = ele[2]
        
        i -= 1
        x -= 1
    else:
        num = ele[0]
        i = ele[1]
        i -= 1
        
    if(num == 1):
        trains[i][x] = 1 # 1은 사람을 의미
    
    elif(num == 2):
        trains[i][x] = 0 # 1은 사람을 의미
        
    elif(num == 3):
        trains[i].rotate(1)
        trains[i][0] = 0
        
    elif(num == 4):
        trains[i].rotate(-1)
        trains[i][19] = 0
        
# print(*trains, sep = '\n')

result = set()
for ele in trains:
    result.add(tuple(list(ele)))
    
print(len(result))    