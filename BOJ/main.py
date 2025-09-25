'''
n일 동안 최대한 많은 상담을 하려고 한다.

상담
1] 하루에 하나씩 다른 상담
2] t : 완료하는데 걸리는 시간 / p : 상담하고 받는 금액

3] 완료하는데 걸리는 시간이 3일이면 당일, 다음날, 다다음날 이렇게 다른 상담을 할수없다.
4] n+1을 넘어가는 상담도 할 수 없다.

ex)
0  1  2  3  4  5  6
3  5  1  1  2  4  2
10 20 10 20 15 40 200

상담한 날       이익
1               10 -> 2 , 3일 못함 / 4, 5, 6, 7 중에서 4를 안하고 5를 할수도 있음

4  5  6  7
1  2  4  2
20 15 40 200

4 -> 567도 가능 30

1. 모경수
1) 백, start
2) 재귀 할때마다 최대 수익을 갱신한다.
3) 재귀할 때 수익을 더함
4) 상담하려고하는날 + 소요시간 > n 면 못함.


* n : 계획 n개
n개의 t와 p

출 : 백준이가 얻을 수 있는 최대 이익
2. n^2

'''

n = int(input())
works = [list(map(int, input().split())) for _ in range(n)]

# print(*works, sep='\n')

max_hab = 0

def back(hab, start):
    # print(hab, "start=", start)
    
    global max_hab
    
    semi_hab = 0
    for _, num in hab:
        semi_hab += num
    
    if(max_hab < semi_hab):
        max_hab = semi_hab
    
    for i in range(start, n):
        if(i + works[i][0] <= n):
            hab.append([i, works[i][1]])
            back(hab, i + works[i][0])
            hab.pop()

back([], 0)
print(max_hab)