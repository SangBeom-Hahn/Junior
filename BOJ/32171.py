'''
1 ~ N번 친구
에어드랍
1] src와 dst의 버전 차이가 T 이하
2] 거리가 최대 K만큼 떨어진 거리의 기기에만 전송 가능


ex) n = 5, 최대거리 = 4, 버전차이 = 3
푸앙이 x,y = (5, 2) / v = 3

친구 5명                        유클리드 거리       버전차이            에어드랍 가능 여부
(2, 2) / 버전 1 -> 없음         5-2 + 2-2 = 3       3-1 = 2             최대거리 ok, 버전차이 ok
(2, 5) / 버전 4 -> 있음         5-2 + 5-2 = 6       4-3 = 1             거리 xx, 버전차이 ok
(2, 8) / 버전 7 -> 있음
(4, 9) / 버전 11 -> 있음
(7, 6) / 버전 4 -> 있음

1. 모경수
1) bfs로 방문 탐색
    ok0] visit을 친구 사이즈로 만듦
    1] 방문 조건
        1] 푸앙이와 친구의 버전 차이가 t 이하
        2] 푸앙이와 친구의 거리 차이가 k이하
    2] 내부 for
        1] 매번 모든 친구를 전부 다 순회해서 방문 x, 방문 조건 만족하는 곳으로 간다.
    3] 큐 : 좌표, v, 친구 번호 idx
    4] 팝했는데 p가 1이면 친구 목록에 idx+1을 넣음

* n : 친구 수
k : 최대 거리
t : 버전 차이

x, y, v : 푸앙이 좌료, 푸앙이 폰 버전
x, y, v, p : n명의 친구의 좌표 / 버전 / p = 0이면 푸앙이와 사진 찢지 않음, 1이면 찍음.

출 : 푸앙이리아 사진 찍은 친구들의 번호를 오름차순 출력
사진을 못 받으면 0 출력

2. n^2
'''
from collections import deque

def bfs(xp, yp, vp):
    q = deque()
    q.append((xp, yp, vp, -1, -1)) # 푸앙이는 p, idx가 의미가 없음
    
    while(q):
        print(q)
        x, y, v, p, idx = q.popleft()
        if(p == 1):
            result.append(idx+1)
        
        for friend_idx in range(n):
            if(not visit[friend_idx]):
            
                xf, yf, vf, pf = friends[friend_idx]
                
                print(f"중심 {x} {y} / 주변 번호 : {friend_idx} 좌표 : {xf} {yf}")
                
                check_dis = abs(x-xf) ** 2 + abs(y-yf) ** 2
                check_version = abs(v - vf)
                
                print("거리", check_dis, "버전", check_version)
                
                if(check_dis <= k**2 and check_version <= t):
                    q.append((xf, yf, vf, pf, friend_idx))
                    visit[friend_idx] = True
            

n, k, t = map(int, input().split()) #최대 거리, t=최대버전 차이

xp, yp, vp = map(int, input().split()) # 푸앙이 좌표, 버전
visit = [False] * n # 0부터 시작

friends = [list(map(int, input().split())) for _ in range(n)]
result = []
bfs(xp, yp, vp)

if(result):
    print(*sorted(result))
else:
    print(0)