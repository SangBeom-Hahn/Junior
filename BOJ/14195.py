'''
각 계란에는 내구도와 무게가 있다. 계란으로 계란을 치면 각 계란의 내구도는 상대
계란의 무게만큼 깎인다. 내구도가 0이하가 되면 깨진다.
ex)
계란 1 내구도 7, 무게 5
계란 2 내구도 3, 무게 4

계란1로 2를 치면 계란이1의 내구도 7-4(계란 2의 무게)가 되고 
계란 2의 내구도 3 - 5(계란 1의 무게)가 된다. 결과적으로 1은 깨지지 않고 
2는 깨진다.

일렬로 놓여있는 계란에 왼쪽부터 차례로 들어서 한번씩 다른계라능ㄹ 쳐서
최대한 많은 계란을 깨는 문제이다.

1. 가장 왼쪽 계란을 든다. 깨지지 않은 다른 계란 중 하나를 친다.
손에 든 계란이 깨졌거나 깨지지 않은 다른 계란이 없으면 치지 않고 넘어간다.
2. 가자 ㅇ최근에 든 계란의 한 칸 오른쪽 게란을 손에 들고 2번 과정을 반복한다.
3. 가장 최근에 든 계란이 가장 오른쪽 위치한 게란이면 게임 종료

최대 몇개의 계라능ㄹ 꺨 수 있는지 알아맞춰봐라

1. 모든 경우의 수
1) 백으로 탐색

* n : 계란의 수
게란의 내구도와 무게
출력 : 인범이가 깰 수 있는 계란의 최대 개수
'''
def back(stand, eggs):
    # print(stand, eggs)
    global maxCnt
    
    if(stand == n): # 가장 최근에 든 계란이 가장 오른쪽 위치한 게란이면 게임 종료
        cnt = 0
        for egg in eggs:
            if(egg[0] <= 0):
                cnt += 1
                
        maxCnt = max(maxCnt, cnt)
        # print("one", 1)
        return
    
    if(eggs[stand][0] <= 0):
        # 다음 계란으로 넘어감
        back(stand + 1, eggs)
        return
    
    for i in range(len(eggs)):
        if(stand == i):
            continue
        else: # 깨지지 않은 다른 계란 중 하나를 친다.
            if(eggs[i][0] > 0):
                eggs[stand][0] -= eggs[i][1]
                eggs[i][0] -= eggs[stand][1]
                back(stand + 1, eggs)
                eggs[stand][0] += eggs[i][1]
                eggs[i][0] += eggs[stand][1]
    else:
        cnt = 0
        for egg in eggs:
            if(egg[0] <= 0):
                cnt += 1
                
        maxCnt = max(maxCnt, cnt)
        # print("two", 2)
        return
            

n = int(input())
inputEggs = [list(map(int, input().split())) for _ in range(n)]
# print(inputEggs)
maxCnt = 0

back(0, inputEggs)
print(maxCnt)