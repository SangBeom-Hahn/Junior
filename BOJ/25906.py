'''
10개 중 9개 망치 선택
i망치로 x강 강화 성공 확률 = pi/x

강  확률
1   pi / 1
2   pi / 2

1. 모경수(prt, n=1)
1) 10개 중 9개를 가장 작은거 빼고 고름
2) 확률 다 곱하고 1 ~ 9 곱한거로 나눔
3) 출력

* 10개의 pi
출 : 9강에 도달할 확률ㄹ의 최대값에 10 ** 9 곱하고 , 오차는 10**-6까지 허용

2. n^3
'''

ps = [float(input()) for _ in range(10)]

boonja = 1
for ele in ps:
    boonja *= ele

# print(boonja)
    
boonja /= min(ps)    

# print(boonja)

boonmo = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9

result = boonja / boonmo * 10 ** 9

print(round(result, 6))