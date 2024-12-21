'''
n명의 친구 1 ~ n번
에어르랍 : 보내는 휴대폰과 받는 폰의 버전 차이가 t이하, 거리가 k이하만 가능
버전 차이가 커도 간접 경로로는 가능하다.

* n, k, t = 친구수, 최대러기, 버전차이
x, y, v = 푸앙이 좌표, 버전
x, y, v, p = n개의 좌표, 버전, 사진여부(0 = 안찍음, 1 = 찍음)

1. 모경수(prt, n=1)
1) bfs로 방문 탐색
2) 버전 차이가 커도 갈 수는 있다.

출 : 에어드랍 가능한 친구들 번호(없다면 0)
2. nlogn
'''
result = []
def dfs(i): # 거리, 버전이 가능한 친구 번호
    visit[i] = True
    f_x, f_y, f_v, _ = graph[i]
    
    for nuw_f_num in range(n):
        if(nuw_f_num != i and not visit[nuw_f_num]):
            new_f_x, new_f_y, new_f_v, new_p = graph[nuw_f_num]
            
            dis = abs(f_x - new_f_x) + abs(f_y - new_f_y)
            v_diff = abs(f_v - new_f_v)
            
            if(dis <= k):
                if(new_p == 1 and v_diff <= t):
                    result.append(nuw_f_num+1)
                dfs(nuw_f_num)

from collections import deque

def bfs(p_x, p_y, p_v):
    q = deque()
    q.append((p_x, p_y, p_v, False, "푸앙"))
    
    while(q):
        x, y, v, p, num = q.popleft()
        # print(num, x, y, v, p)
        for i in range(n):
            if(not visit[i] and num != i):
                f_x, f_y, f_v, f_p = graph[i]
                dis = abs(x - f_x) + abs(y - f_y)
                v_diff = abs(v - f_v)
                
                # print(i, dis, v_diff, f_p)
                # print()
                
                if(dis <= k):
                    if(v_diff <= t and f_p == 1):
                        # print("들어감!")
                        result.append(i+1)
                    

                    q.append((f_x, f_y, f_v, f_p, i))
                    visit[i] = True
            
            
    

    
n, k, t = map(int, input().split())
p_x, p_y, p_v = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visit = [False] * n

bfs(p_x, p_y, p_v)

if(len(result) == 0):
    print(0)
else:
    print(*result)