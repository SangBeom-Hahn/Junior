'''
N개의 카드에 앞, 뒷면에 숫자
명령에 따라 카드를 뒤짚는다.
명령
1] K : 보이는 면의 숫자가 K이하인 카드를 모두 뒤집는다.

1. 모경수(prt, n=1)
ok 1) 카드의 앞, 뒤를 배열에 dic으로 저장 ex) [{앞: 9, 뒤: 2}]
2) 각 카드의 앞, 뒤 상태를 나타내는 배열 둠
    1] 카드에 적힌 수 : 인덱스 접근 -> 상태 접근
3) 명령에 따라서 K이하이면 상태를 수정한다.
4) 맨 마지막에 상태를 보고 배열 순회해서 합 구하기

* N, M : M개의 명령
N개의 카드의 앞면과 뒷셤
M개의 명령

출 : 명령이 끝나고 보이는 카드들의 합

2. nlogn
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    f, b = map(int, input().split())
    arr.append({'앞' : f, '뒤' : b})

# 2) 각 카드의 앞, 뒤 상태를 나타내는 배열 둠
status = ['앞'] * n

for _ in range(m):
    k = int(input())
    
    for i in range(n):
        if(arr[i][status[i]] <= k):
            if(status[i] == '앞'):
                status[i] = '뒤'
            else:
                status[i] = "앞"

hab = 0
for i in range(n):
    hab += arr[i][status[i]]

print(hab)    
            