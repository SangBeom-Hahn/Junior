'''
계란은 내구도와 무게가 있다. 게게치하면 내구도가 상대 계란 무게만큼 깎인다.
내구도가 0이면 깨진다.
계란1 7, 5
2     3, 4

왼쪽부터 차례로 들어서 한번씩만 다른 계란을 쳐 최대한 많은 계란을 깨는 문제다.
1. 가장 왼쪽 계란을 듬
2. 깨지지 않은 다른 계란 중 하나를 침 손에 든 계란이 깨졌거나 깨지지 않은 다른 계란이 없으면 치지 않고 넘어감, 이후 계란을 내려놓음
3. 가장 최근에 든 계란의 한칸 오른쪽 계란을 손에 들고 2번 과정을 함, 가장 오른쪽 계란까지 치면 종료

1. 모경수
1) 백으로 탐색, 기준

* n : 계란수
계란의 내구도와 무게
출 : 깰 수 있는 계란의 최대 개수
2. 시복 : n^3
'''

def back(stand):
    # print(eggs)
    
    global max_cnt
    if(stand >= n):
        cnt = 0
        for i in range(n):
            if(eggs[i][0] <= 0):
                cnt += 1
        
        max_cnt = max(max_cnt, cnt)
        return
    
    # 손에 든 계란이 깨졌거나
    if(eggs[stand][0] <= 0):
        back(stand + 1)
        return
    
    for i in range(n):
        if(stand != i and eggs[i][0] > 0): # 깨지지 않은 다른 계란 중 하나를 침
            eggs[i][0] -= eggs[stand][1]
            eggs[stand][0] -= eggs[i][1]
            back(stand + 1)
            eggs[i][0] += eggs[stand][1]
            eggs[stand][0] += eggs[i][1]
    
    else:
        cnt = 0
        for i in range(n):
            if(eggs[i][0] <= 0):
                cnt += 1
        
        max_cnt = max(max_cnt, cnt)
        return
        
            
max_cnt = 0
n = int(input())
eggs = []

for _ in range(n):
    eggs.append(list(map(int, input().split())))
    
# print(eggs)

back(0)

print(max_cnt)