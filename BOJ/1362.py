'''


콘솔
1] E와 숫자 : 운동하여 펫의 실제 체중이 숫자만큼 감소
2] F와 숫자 : 먹이줘서 실제 체중이 n 증가
3] 팻이 중간에 죽으면 이후 콘솔은 무시

ex) 
콘솔    숫자    적정    실제
                100     100
F       10              110
F       10              120
E       20              100

                50      30
F       5               35
E       20              15


1. 모경수(prt, n=1)
ok 1) 적정, 실제 기록함
    1] 0 0이 아닌 숫자 2개가 들어오면 New 시나리오임

2) 콘솔에 따라서 실제 체중을 수정함
    ok 0] 펫이 모든 콘솔 다 처리하고 # 때 죽으면 다른 상태와 동일하게 처리
    1] 펫이 중간에 죽으면 
        ok 2] 죽었나 여부 flag
        ok 3] E를 했는데 실제 체중이 0이면 flag = True
        ok 3] flag가 true일 때 나오는 콘솔은 무시
        4] # 0이 나오면 다시 flag True
        
ok 3) # 0를 만나면 한개 시나리오 종료 + 개 상태 출력
ok 4) 0 0이면 아예 종료

* o, w : 적정, 실제 체중
펫에 가할 콘솔이 한줄에 하나씩
# 0를 하면 각 시나리오 종료 -> 0 0을 안만나면 다음 시나리오 시작 가능
0 0을 하면 아예 게임 종료

출 : 시나리오 번호와 펫의 상태(행복, 슬픔, 사망)

'''
#적정, 실제
good, real = 0, 0
num = 1
flag = False

while(True):
    # print(f"적정 {good} / 실제 {real}")
    a, b = input().split()
    
    # 시나리오 시작을 알리는 적정과 실제
    if(a.isdecimal() and b.isdecimal()):
        if(a != "0" and b != "0"):
            good = int(a)
            real = int(b)
            continue
        elif(a == "0" and b == "0"):
            #  아예 게임 종료
            break
        
    # 이 밑은 전부 다 콘솔 혹은 #    
    if(flag == False and a == 'F'):
        real += int(b)
    elif(flag == False and a == 'E'):
        real -= int(b)
        # E를 했는데 실제 체중이 0이면 flag = True
        if(real <= 0):
            flag = True
        
    elif(a == '#'):
# 행복 : 적정 1/2 < 실제 체중 < 적정 * 2
# 사망 : 실제 <= 0
# 슬퍼 : 그 외        
        if(good * 0.5 < real and real < good * 2):
            print(f"{num} :-)")
        elif(real <= 0):
            print(f"{num} RIP")
        elif(0 < real <= good * 0.5 or good * 2 <= real):
            print(f"{num} :-(")
            
        num += 1 # 다음 시나리오 번호
        flag = False
        