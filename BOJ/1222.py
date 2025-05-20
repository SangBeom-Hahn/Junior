'''
N개의 곡
L초 : 모든 노래의 길이
노래와 노래 사이 : 5초 동안 텀
시작 : 0초
전화 : 0초부터 D초에 1번씩 1초동안 울림
노래가 나오는 중에는 전화를 못 들음
1] 노래가 시작할 때 울리면
2] 노래가 끝날때 끝나면

들음
1] 앨범을 다 들으면 들을 수 있음

ex) 
개수    노래 길이   전화 울리는 텀
2       5           7

초      노래 여부       전화 여부
0       o               o
1       o               x
2       o               x
3       o               x
4       o               x
5       x               x
6       x               x
7       x               o
8       x
9       x
10
11
12
13
14

개수    노래 길이   전화 울리는 텀
4       5           20

초      노래 여부       전화 여부
0       o               o
1       o               x
2       o               x
3       o               x
4       o               x
5       x               x
6       x               x
7       x               x
8       x               x
9       x               x
10      o               x
11      o               x
12      o               x
13      o               x
14      o               x
15      x               x
16      x               x
17      x               x
18      x               x
19      x               x
20      o               o

1. 모경수(prt, n=1)
ok 1) N * L + 5 * (L-1) -1만큼 for문을 돔
ok 2) 0초부터 시작 초는 게속 증가
ok 3) 노래 여부 t
ok 4) 노래가 나오는 횟수를 cnt해서 cnt가 노래의 길이와 같으면 노래 여부 f
ok 5) 노래 여부 f일 땐 텀 5초 cnt
6) 0초부터 D초마다 전화 울림
    1] 노래 여부가 t이면 pass
    2] f이면 그 초가 정답
    3] for문이 끝나면 d에 d를 계속 더하다가 s보다 클 때 끝

* N L D : 곡의 개수, 모든 노래의 길이, D초에 1번 전화 울림
출 : 전화 받을 수 있는 가장 빠른 시간

2. n^2
'''

n, l, d = map(int, input().split())
second = n * l + 5 * (n - 1) - 1

# print(second)
sing = True
sing_cnt = 0
term_cnt = 0

for s in range(second+1):
    # 6) 0초부터 D초마다 전화 울림
    if(s % d == 0):
        if(sing == True):
            pass
        else:
            print(s)
            break
    
    if(sing == True):
        # 노래가 나오는 횟수를 cn
        sing_cnt += 1
        
        if(sing_cnt == l):
            sing_cnt = 0
            sing = False
    else:
        term_cnt += 1
        
        if(term_cnt == 5):
            sing = True
            term_cnt = 0
else:
    # 3] for문이 끝나면 d에 d를 계속 더하다가 s보다 클 때 끝
    result = 0
    while(True):
        if(result > s):
            print(result)
            break
        
        result += d