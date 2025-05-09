'''
N명, 1번부터N명, 반시계방향 원모양

7 6 5 4 3 2 1

룰
1] 자신의 차례예 K를 외침
2] 번호를 부른 사람이 3모, 시계방향으로 1감소(번호가 작아짐), 반시계로 1증가(번호가 커짐)
3] K인 사람이 게임 이어감
4] 술 : 
    1] 자신의 차레인데 K안 외침
    2] 자신의 차례가 아닌데 K를 외침


-> K-3 양수
ex) 7명, 현재 2번, K=4
현재 3모
K=4 (K-3 = 1증가 = 번호커짐)
다음 = 3

K=9
K-3 = 6 
다음=0

7 6 5 4 3 2 1

K=1
K-3=-2 = 절대값 수 만큼 번호가 작아짐
다음=7

K=-1
K=-4 = 절대값 수 만큼 번호가 작아짐
다음5


1. 모경수
0) K=3이면 현재 번호가 답
1) K-3이 양수면 그 수만큼 +1 = 2 3 4 5 6 7
2) K-3이 음수면 = 2 1 7 6 5 4 3 2 1 ,,,


* N, M, K - 게임하는 사람수, 현재 차례사람 번호, ㅎㄴ재 부른 K
출 : 다음 자례인 사람 번호    

2. nlogn
'''

n, m, k = map(int, input().split())
if(k == 3):
    print(m)
else:
    su = k-3
    # print(su)
    
    if(su > 0):
        for _ in range(su):
            m = (m+1) % n
            if(m == 0):
                m = n
            # print(m)
        
    else:
        for _ in range(abs(su)):
            m = (m-1+n) % n
            if(m == 0):
                m = n
            # print(m)
    
    print(m)