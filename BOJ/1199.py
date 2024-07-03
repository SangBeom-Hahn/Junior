'''
외벽의 총 둘레 : n미터
외벽에 취약한 지점이 있다. 친구들이 1시간 동안 이동할 수 있는 거리는 제각가깅고 최소한의 친구들을 투입해 취약 지점을 점검한다.
레스토랑 정북 방향을 0으로 나타내며, 취약 지점의 위치는 정북 방향으로부터 시계 방향으로 떨어진 거리다.
친구들은 출발지점부터 시계, 혹은 반시계 방향으로 외벽을 따라서만 이동한다.

weak    pos = weak[i] + perm[무언가]
1       2 = weak[0] + perm[0] -> 내가 weak[0]를 커버할 수 있으니 난 증가 안해
5       2 -> 내가 커버 못함 cnt 증가 

pos = weak[1] + perm[1]로 갱신, 다음 친구는 perm[0]이 본 다음부터 하는게 아니라 다음 취약점부터 봄
        7


1.모경수(prt, n=1)
1) 벽을 선형으로 펼치기
2) 각 취약지점을 전부다 훑어서 시작 위치를 바꾸기
3) 그때마다 모든 친구 순열을 봐서 출발 순서를 바꾸기
4) 

n : 외벽길이
weak : 취약 지점 위치
dist : 각 친구가 이동할 수 있는 거리
출 : 취약 지점을 점검하기 위해 보내야 하는 친구 수 최소값(친구를 전부 투입해도 전부 점검할 수 없는 겨우 -1)
n^3
'''
from itertools import permutations

def solution(n, weak, dist):
    # 벽을 선형으로 펼치기
    leng = len(weak)
    answer = len(dist) + 1
    
    for i in range(leng):
        weak.append(weak[i]+n)
        
# weak    pos = weak[i] + perm[무언가]
# 1       2 = weak[0] + perm[0] -> 내가 weak[0]를 커버할 수 있으니 난 증가 안해
# 5       2 -> 내가 커버 못함 cnt 증가 

# pos = weak[1] + perm[1]로 갱신, 다음 친구는 perm[0]이 본 다음부터 하는게 아니라 다음 취약점부터 봄
#         7        
        
    # 각 취약지점을 전부다 훑어서 시작 위치를 바꾸기
    for start in range(leng):
        # 그때마다 모든 친구 순열을 봐서 출발 순서를 바꾸기
        for friends in list(permutations(dist, len(dist))):
            pos = weak[start] + friends[0]
            cnt = 1
            
            # start가 0이라면 취약지점1을 시작점으로 했을 때 start가 1라면 취약지점 5를 시작점으로 했을 때
            # 어떠한 친구 순열에서 해당 시작점부터 leng개의 취약지점을 다 커버할 수 있나 보겠다.
            for idx in range(start, start+leng):
                if(weak[idx] > pos):
                    cnt += 1
                    if(cnt > len(dist)):
                        break
                    
                    pos = weak[idx] + friends[cnt-1]
            
            answer = min(answer, cnt)
    if(answer == len(dist) + 1):
        return -1
            
            
    return answer
        