'''
x에 할 수 있는 연산은 다음과 같다.
1) 3으로 나눠 떨어지면 3으로 나눈다.
2) 2로 나눠 떨어지면 2로 나눈다
3) 1을 뺀다.

정수 n이 있을 때 연산 3개를 적절히 사용해서 1을 만드려고 한다. 

1. 모경수
1) 결과값
2) 점화식
3) base
    1] 0 dp 배열, -1 저장소 배열
    2] 2부터 시작

* n
출력 : 연산을 사용하는 횟수의 최소값, 1f로 만드는 방법에 포함되어 있느 수

2. 시복 : nlogn
'''

n = int(input())
dp = [0] * (10**6+1)
store = [-1]* (10**6+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    store[i] = i-1
    
    if(i % 3 == 0):
        if(dp[i] > dp[i//3]+1):
            dp[i] = min(dp[i], dp[i//3] + 1)
            store[i] = i//3
        
    if(i % 2 == 0):
        if(dp[i] > dp[i//2]+1):
            dp[i] = min(dp[i], dp[i//2] + 1)
            store[i] = i//2
        
# print(dp[:11])
# print(store[:11])

print(dp[n])

want = n
while(True):
    print(want, end = ' ')
    want = store[want]
    
    if(want == -1):
        break