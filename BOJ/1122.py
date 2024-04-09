'''
마음을 읽는 기계, 각 사람들이 누구를 찍을지 미리 읽을 수 있어 국회 선거 조작할거다.
어떤 사람이 누구를 찍을지 정하면 반드시 선거때 그 사람을 찍음
후보 n명, 다솜이는 기호1번, 마을 주민 m명, m명의 마음을 읽어서 자신을 찍지 않은 사람을
돈으로 매수해서 조작할거임
다른 모든 사람의 득표수보다 많은 득표수를 가질때 당선됨
다솜이가 매수해야 하는 사람의 최소값을 ㄱ

ex) 기호 1  2   3
    5       7   7
    7(5+1+1)       6(7-1)   6(7-1)

1. 모경수(prt, n=1)    
1) 백으로 탐색, 그냥 배열 훑기 유형
    
* n : 후보의 수
기호 1~n번을 찍으려는 사람의 수

2. 시복 : n^3
'''

def back(candis, cnt): # 매수자 수
    global min_cnt
    # print(candis)
    me = candis[0]
    for i in range(1, len(candis)):
        if(me <= candis[i]): # 작거나 같으면 다시 재귀 ㄱ
            break
    else: # 전부 다 크면
        if(cnt != 0 and min_cnt > cnt):
            min_cnt = cnt # 현재가 최소값이라 추가 재귀 안함
            return 

    for i in range(1, len(candis)):
        if(candis[i] > 0): # 한 개라도 있다면
            candis[0] += 1
            candis[i] -= 1
            back(candis, cnt+1)
            candis[0] -= 1
            candis[i] += 1
            # print(i, candis)

min_cnt = 50000
n = int(input())
candis = [int(input()) for _ in range(n)]
# print(candis)

if(n == 1):
    print(0)
else:
    back(candis, 0)
    print(min_cnt)