# 솔루션 내가 맥스보다 작으면 팔아 내가 맥스보다 크면 내가 맥스가 돼
# 근데 이걸 앞에서부터 하면 

import heapq
import sys
input = sys.stdin.readline
# 5       3 5 9 6 2
t = int(input())
for _ in range(t):
    n = int(input())
    moneys = list(map(int, input().split()))
    moneys.append(10001)
    max = 0
    result = 0
    stackMoney = []
    
    for i in range(n-1, -1, -1):
        if(moneys[i] >= max):
            max = moneys[i]
        else:
            result += (max-moneys[i])
            
    print(result)