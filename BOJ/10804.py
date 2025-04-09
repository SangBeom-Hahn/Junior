'''
규칙
1] 인덱스 a, b 구간에서 카드를 역순으로 둠

1. 모경수(prt, n=1)
1) 총 구간 짝수
    0] 구간 길이 절반만큼 순회
    1] 양끝부터 가운데로 모으면서 switch
2) 홀수
    0] 구간 길이 절반만큼 순회, 맨 가운데는 뺌
    1] swap

* 10개의 구간 (1부터 시작)
출 : 마지막 카드 배치

2. n^3
'''

l = list(range(1, 21))
for _ in range(10):
    x, y = map(int, input().split())
    # 총길이
    leng = y - x + 1
    x -= 1
    y -= 1
    
    for i in range(leng // 2):
        l[x + i], l[y - i] = l[y - i], l[x + i]
    
    # print(l)
    
print(*l)    