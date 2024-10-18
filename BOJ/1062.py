'''
k개의 글자로만 이루어진 단어만 읽을 수 있다.
단어 : anta, tica

ex)
a, n, t, i, c는 공통

1. 모경수(prt, n=1)
1) k가 5보다 작으면 0개 가르칠 수 있음
2) k가 5보다 크거나 같으면
    0] 단어들의 알파멧을 counter로 구하고
    1] 알파벳을 [a, n, t, i, c]에서 하나씩 추가하면서
    2] 현재 모은 알파벳의 길이가 k일때, 만들 수 있는 단어 개수를 매번 세고 개수를 갱신함
    3] 현재 모은 알파벳으로 만들 수 있는지 = counter의 키들이 현재 모은 알파벳에 모두 
    포함되면 만들 수 있음

* n, k : 남근 단어의 개수, k개의 글자만 가르침(0~26)
남극 언어의 단어
출 : k개의 글자를 가르치고, 읽을 수 있는 단어 개수의 최대값

2. n^3
'''
import sys
input = sys.stdin.readline
from collections import Counter

n, k = map(int, input().split())
words = [set(input().rstrip()) for _ in range(n)]

# print(words)

# print(*words, sep='\n')

# 1) k가 5보다 작으면 0개 가르칠 수 있음
# 2) k가 5보다 크거나 같으면
#     0] 단어들의 알파멧을 counter로 구하고
#     1] 알파벳을 [a, n, t, i, c]에서 하나씩 추가하면서 -> 백으로 탐색 used
#     2] 현재 모은 알파벳의 길이가 k일때, 만들 수 있는 단어 개수를 매번 세고 개수를 갱신함
#     3] 현재 모은 알파벳으로 만들 수 있는지 = counter의 키들이 현재 모은 알파벳에 모두 
#     포함되면 만들 수 있음

max_r = 0

def back(st):
    global max_r
    
    if(len(alphas) == k):
        al = set(alphas)
        cnt = 0
        for word in words:
            for digit in word:
                if(digit not in al):
                    break
            else:
                cnt += 1
        
        if(max_r < cnt):
            max_r = cnt
        return

    for i in range(st, 26):
        if(not used[i]):
            alphas.append(chr(97+i))
            used[i] = True
            back(i+1)
            alphas.pop()
            used[i] = False

alphas = ["a", "n", "t", "i", "c"]
used = [False] * 26
for ele in alphas:
    used[int(ord(ele)) - int(ord("a"))] = True

if(k < 5):
    print(0)
else:
    back(0)
    print(max_r)