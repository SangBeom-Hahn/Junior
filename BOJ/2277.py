'''
계계치
1) 계란에는 내구도와 무게가 있다.
2) 치면 각 계란의 내구도는 상대의 무게만큼 깎인다.
3) 내구도가 0이하가 되면 깨진다.
왼쪽부터 차례로 들어서 한번씩만 다른 계란을 쳐 최대한 많은 계란을 꺠는 문제
치는 과정
1) 가장 왼쪽의 계란을 듬
2) 깨지지 않은 계란 중 하나를 침 (손에 든 계란이 꺠졌거나 깨지지 않은 계란이 없으면 넘어감)
3) 그 오른쪽 계란을 들고 또 침
4) 가장 최근에 든 계란이 맨 오른쪽 계란이면 종료

1. 모경수(prt, n=1)
1) 백으로 탐색(기준을 둠)

* n : 계란의수
n개의 내구도와 무게
출 : 깰수있는 계란의 최대 개수

2. n^3

'''

max_cnt = 0
def back(stand):
    global max_cnt
    
    if(stand == n):
        # print(eggs)
        cnt = 0
        for i in range(n):
            if(eggs[i][0] <= 0):
                cnt += 1
        
        if(max_cnt < cnt):
            max_cnt = cnt
        return
    
    if(eggs[stand][0] <= 0):
        back(stand+1)
        return
    
    for i in range(n):
        # print(eggs)
        if(stand != i and eggs[i][0] > 0):
            eggs[stand][0] -= eggs[i][1]
            eggs[i][0] -= eggs[stand][1]
            back(stand+1)
            eggs[stand][0] += eggs[i][1]
            eggs[i][0] += eggs[stand][1]
    else:
        # print(eggs)
        cnt = 0
        for i in range(n):
            if(eggs[i][0] <= 0):
                cnt += 1
        if(max_cnt < cnt):
            max_cnt = cnt
            

n = int(input())
eggs = []
for _ in range(n):
    eggs.append(list(map(int, input().split())))
    
# print(eggs)    

back(0)
print(max_cnt)