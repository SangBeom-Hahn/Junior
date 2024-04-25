'''
설탕 N 키로그램을 배달한다. 설탕은 봉지에 담겨있고 봉지는 3, 5kg 봉지가 있다. 상근이는 최대한 적은 봉지를 들고
가려고 한다. 

ex) 
N   가능한것
18  3키로 봉지 6개
    5키로 봉지 3개와 3키로 1개 = 총 4개로 이게 더 적은 봉지
    
1. 모경수
1) dp로 풀기
2) 1로 만들기나 동전 문제랑 동일할 듯하다

* n
출력 상근이가 배달하는 봉지의 최소 개수를 구해라(못만들면 -1)

2. 시복 n^2
'''

n = int(input())
dp = [1000000] * (5001)
dp[0] = 0

for i in [3, 5]:
    for j in range(i, n+1):
        dp[j] = min(dp[j], dp[j-i] + 1)
        
# print(dp[:n+1])        
result = dp[n]
if(result == 1000000):
    print(-1)
else:
    print(result)