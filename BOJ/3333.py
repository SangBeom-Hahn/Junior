'''
규칙
1] 1~N개의 점에 별이 떨어짐
2] 첫날 낮에 모든 점에 쌓인 별의 개수는 각 0개
3] i번 점에 매일 밤 si개의 별이 떨어진다.

폭발
1] 점에 쌓인 별의 개수 > K
2] 청소 : 모든 점에 쌓인 별의 개수 0개

ex) 
1 2 3 4 점
2 3 1 2
4 6 2 4

0 0 0 0
2 3 1 2
4 6 2 4

0 0 0 0
2 3 1 2

1. 모경수(prt, n=1)
1) 폭발은 무조건 별이 많이 내리는 점 때문임
    1] 가장 많이 내리는 별 찾음
    2] d일 동안 누적함
    3] 그날 내릴건데
        1] k 초과하면 청소 > 내림
        2] 초과 안하면 내림

* n d k : n개의 점, d일동안 내림, k 초과
각 점에 내린는 별의 개수

출 : 별이 폭발하지 않도록 할 수 있는 최소 청소 횟수

2. n^2
'''

n, d, k = map(int, input().split())
stars = list(map(int, input().split()))

# 가장 많이 내리는 별 찾음
max_star = max(stars)
point = 0
cnt = 0

for _ in range(d):
    if(point + max_star > k):
        point = 0
        cnt += 1
        
    point += max_star
    
print(cnt)