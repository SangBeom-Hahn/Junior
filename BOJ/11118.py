'''
N개의 물건이 있다. 각 물건은 무게 w, 가치 v/ 최대 k만큼 무게를 넣을 수 있는 배낭이 있다. 배낭에 넣을 수 잇는
물건들의 가치의 최대값

* nk : 물품의 수, k만큼 버팀
각 물건의 무게와 가치(w, v)
출력 : 물건들의 가치합의 최대값
'''

n, k = map(int, input().split())
dp = [0] * (k+1)

for _ in range(n):
    w, v = map(int, input().split())
    
    for i in range(k, -1, -1):
        if(w+i <= k):
            dp[w+i] = max(dp[w+i], dp[w] + v)