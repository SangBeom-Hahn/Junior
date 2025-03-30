'''
보드게임
1] 1에서 출발, N이 도착
2] 이동 (주사위 + 지시의 조합이 1세트)
    1] 주사위를 굴려 나온 눈의 수만큼 그 칸으로 이동
    2] 도착한 칸에 쓰인 지시만큼 말을 이동 (지시 사항으로 이동해서 도착한 칸의 지시는 안 따름)
3] 도착 : N칸에 도착했을 때와 그 칸을 넘는 경우모두 도착한 것이다.

ex) 시작 = 0 / 도착 = n-1
0 0 5 6 -3 8 1 8 -4 0

1. 모경수(prt, n=1)
1) 현재위치 = 0 / 도착 = n-1
2) 처음 주사위 던진 횟수 = 0
3) m개의 주사위 던진 것을 따라감
    1] 양수 : 현 위치 + 주사위 눈만큼 이동 > 현위치 + 주사위 눈만큼 이동한 곳에 써져있는 지시사항만큼 이동
    2] 음수 : 현 위치 - 주사위 눈만큼 이동 > 현 위치 - 주사위 눈만큼 이동한 곳에 써져있는 지시사항 만큼 뒤로 이동
    
4) 현재 위치가 n-1 이상이면 끝, 주사위 던진 횟수 출력

* n, m : 전체 칸수, 주사위를 던진 횟수
n개의 각 칸에 적혀있는 지시사항 (0 = 아무것도 안함, 양수=앞으로, 음수=뒤로)
m개의 주사위를 던졌을때 나온 눈의 수

출 : 주사위를 몇 번 던져서 도착할 수 있는지

2. n^2
'''

n, m = map(int, input().split())
# 지시사항 배열
cmds = []
for _ in range(n):
    cmds.append(int(input()))
    
curr_idx = 0
cnt = 0
    
# 주사위 던지기 진행    
for _ in range(m):
    # 나온 주사위
    play_num = int(input())
    
    # 이동 횟수 증가
    cnt += 1
    
    # 이동
    curr_idx = curr_idx + play_num
    
    # 이동 한 곳이 n-1이면 나감
    if(curr_idx >= n-1):
        print(cnt)
        break
    
    cmd = cmds[curr_idx]
    
    # 지시 사항이 0
    if(cmd == 0):
        pass
    
    # 양
    elif(cmd > 0):
        curr_idx = curr_idx + cmd
    
    # 음
    else:
        curr_idx = curr_idx + cmd
    
    if(curr_idx >= n-1):
        print(cnt)
        break