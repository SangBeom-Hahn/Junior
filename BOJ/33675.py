'''
규칙
1] D일 동안 별이 떨어짐
2] 1 ~ N개의 점에 별이 떨어짐
3] 첫날엔 점에 각 0개의 별들
4] i번 점 = Si개의 별이 떨어짐
5] 각 점에 쌓인 별의 개수가 K개를 초과하지 않도록 별이 떨어지기 전 낮에 청소를 해야함
6] 청소를 하면 모든 점에 쌓인 별이 0개가 됨

1. 모경수(prt, n=1)
1) 가장 별이 많이 내리는 점 때문에 k가 초과할 것이기 때문에 그 점에만 si를 더함
2) 그 점이 k를 넘으면 청소하고 횟수를 셈
3) 총서를 하면 그 점엔 별이 0개임

* n, d, k : n개의 점, d일 동안, k 초과 x
각 점에 내리는 별의 개수

출 : 별이 폭발하지 않도록 할 수 있는 최소 청소 횟수

2. n^2
'''

n, d, k = map(int, input().split())
point = 0 # 별이 가장 많이 내리는 점의 현재 별의 개수
stars = list(map(int, input().split()))
max_star = max(stars)
cnt = 0

for _ in range(d):
    # 낮에 청소
    if(point + max_star > k):
        point = 0
        cnt += 1
    
    # 밤에 별 내림
    point += max_star
    
print(cnt)
        