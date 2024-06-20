'''
1-2 / 2-3 이 침구면 1-3도 친구다
원래 알던 친구 5, 새롭게 알게된 친구 10원을 준다.
원래 알던 친구 : 친구 단계의 최소값이 1인 경우
새로알게된 친구 : 2이상이면서 최대 단계 이하인 경우

ex)
특정 사람 2, limit 3, 친구 [1, 2], [2, 3], [2, 6], [3, 4], [4, 5]
원래 알던 친구 1, 3, 6 = 3 * 5
새로 4, 5 2 * 10 + 새로 알게된 친구 수

1. 모경수
1) bfs로 방문 탐색
2) 큐에 타겟 넣고 시작해서 타겟의 촌수는 0하고 퍼질 떄 촌수 +1 해서 하면 되지?

* 관계, 특정사람, limit
출 : 보상을 받을 특정 사람이 새로  알게된 친구 수와 보상 금액의 합
2. 시복 nlogn
'''

from collections import deque

def bfs():
    q = deque()
    q.append((target, 0))
    visit[target] = True
    cnt = 0
    
    while(q):
        print(q)
        x, chon = q.popleft()

        # 결과 계산
        if(chon >= 2 and chon <= limit):
            print((x, chon))
            cnt += 1

        for ele in graph[x]:
            if(not visit[ele]):
                q.append((ele, chon+1))
                visit[ele] = True

    return cnt

rel = [[1, 2], [2, 3], [2, 6]]
target = 2
limit = 2

# 최대 사람 번호 찾기
max_num = 0
for ele in rel:
    max_num = max(max_num, max(ele))

# print(max_num)
graph = [[] for _ in range(max_num+1)]
visit = [False] * (max_num+1)
# print(visit)
# print(graph)

for x, y in rel:
    graph[x].append(y)
    graph[y].append(x)
    
print(graph)    

cnt = bfs()

res = 5 * len(graph[target]) + cnt * 10 + cnt
print(res)