'''
직원은 15분 배수로 운동을 예약하고 최대 운동 예약 시간은 90분 넘길수 없다. 
새로산 로봇에게 예약을 많이 배정하여 다른 로봇 노후화를 막으려고 한다.
한번 운동하면 로봇은 반드시 충전해야하고 연속된 운동 예약 지도 불가
충전만 되면 로봇은 무제한 지도 가능
운동 예약 시간은 서로 겹치지 않음, 한번 예약되면 시간 변경 불가능

1. 모경수(prt, n=1)
1) 백으로 탐색(start)

* 예약 스케줄
출 : 새로 구매한 로봇이 예약 시간 스케줄 중에서 조건에 맞게 가장 길에 운동을 지도할 수 있는 예약 순서를 찾아라
'''

def back(chose, start, l):
    global res
    
    if(start >= l):
        print(chose)
        res = max(res, sum(chose))
    
    for i in range(start, l):
        chose.append(sch[i])
        back(chose, i+2, l)
        chose.pop()

sch = [45, 15, 30] # 총길이가 8인데 start가 6보다 크거

res = 0
back([], 0, len(sch))
print(res)