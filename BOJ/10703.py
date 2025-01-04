''''
계란
1] 네구도와 무게
2] 내구도는 상대 무게만큼 깍임
3] 내구도 0 = 깨짐

퍼즐
1] 가장 왼쪽에 계란을 들어
2] 깨지지 않은 다른 계란 중 하나를 침
    1] 손에 든계 깨졌거나 깨지지 않은 다른 계란이 없으면 넘어감(애초에 더이상 못함 return)
3] 하나 오른쪽 계란으로 다시 침
4] 모든 계란을 하나씩 다 치면 끝

1. 
1) 백으로 탐색(기준)


* n : 계란의 수
내구도와 무게
출 : 깰 수 있는 계란의 최대 개수

2. n^3
'''

def back(eggs, stand):
    # print(eggs, stand)
    global max_cnt
    
    if(stand == n):
        cnt = 0
        for i in range(n):
            if(eggs[i][0] <= 0):
                cnt += 1
        
        if(max_cnt < cnt):
            max_cnt = cnt
        return
    
    if(eggs[stand][0] <= 0):
        back(eggs, stand+1)
        return
    
    for i in range(n):
        
        if(i != stand and eggs[i][0] > 0):
            eggs[stand][0] -= eggs[i][1]
            eggs[i][0] -= eggs[stand][1]
            back(eggs, stand+1)
            eggs[stand][0] += eggs[i][1]
            eggs[i][0] += eggs[stand][1]
    else:
        cnt = 0
        for i in range(n):
            if(eggs[i][0] <= 0):
                cnt += 1
        
        if(max_cnt < cnt):
            max_cnt = cnt
        
max_cnt = 0
n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]

back(eggs, 0)
print(max_cnt)