'''
8개의 톱니를 가진 톱니 바퀴 4개가 있따. 톱니는 N,S극 중 하나이다.
1) 왼쪽부터 1,2,3,4번 톱니바퀴
2) 톱니바퀴를 k번 회전시킬 건데 회전시키려면, 회전시킬 톱니바퀴와 회전시킬 방향을 결정해야한다.
3) A를 회전시킬 때 B와 맞닿은 톱니의 극이 다르면 B는 A의 회전방향과 반대로 회전한다.
최종 톱니 상태를 구해라

1. 모경수
0) 모든 톱니 상태를 보고 한번에 돌아감
1) 선택한 톱니의 오른쪽 회전은 선택 톱니 = 2인덱스, 오른쪽 톱니 6번 인덱스 비교
2) 선택한 톱니의 왼쪽 회전은 선택 톱니 = 6인덱스, 왼쪽 톱니 2번 인덱스 비교
3) 왼쪽 싹 보고 오른쪽 싹 보는데 체크할 톱니(동반으로 돌아가는 톱니는 주인톱니가 돌아가나
안 돌아가나 체크 후 돈다.)

0) 톱니 4개가 돌아가냐 안돌아가냐 배열만듬
1) 주인 톱니의 왼쪽 싹 봐서 돌아가나와 방향 저장
2) 오른쪽
3) 회전을 k번 반복

* 1번 톱니 바퀴 상태(12시 방향부터 시계방향 순으로 N극 = 0, S극 = 1)
2
3
4
k : 회전횟수
톱니번호, 방향(1 = 시계, -1 = 반시계)
출력 : 최종 상태를 구해라ㄴ
'''
from collections import deque

wheels = []
for _ in range(4):
    wheels.append(deque(list(input())))

# 돌아가냐 안돌아가냐 배열
k = int(input())
for _ in range(k):
# for _ in range(1):
    yesOrNo = [0, 0, 0, 0]
    num, d = map(int, input().split())
    num -= 1
    yesOrNo[num] = d

    # 주인 톱니의 왼쪽을 싹 봄
    idx = num-1
    while(True):
        if(idx == -1):
            break

        # 주인 톱니가 안돌면 나도 안돔
        if(yesOrNo[idx + 1] == 0):
            break

        # 주인이 돌면
        # 선택한 톱니의 왼쪽 회전은 선택 톱니 = 6인덱스, 왼쪽 톱니 2번 인덱스 비교
        # 1) 주인 톱니의 왼쪽 싹 봐서 돌아가나와 방향 저장
        if(wheels[idx + 1][6] != wheels[idx][2]):
            yesOrNo[idx] = yesOrNo[idx+1] * -1
        else:
            pass
        idx -= 1

    # 주인 톱니의 오른쪽을 싹 봄
    idx = num+1
    while(True):
        if(idx == 4):
            break

        if(yesOrNo[idx-1] == 0):
            break

        #  선택한 톱니의 오른쪽 회전은 선택 톱니 = 2인덱스, 오른쪽 톱니 6번 인덱스 비교
        if (wheels[idx - 1][2] != wheels[idx][6]):
            yesOrNo[idx] = yesOrNo[idx - 1] * -1
        else:
            pass
        idx += 1

    for idx, ele in enumerate(wheels):
        ele.rotate(yesOrNo[idx])


    # print(yesOrNo)
result = 0
stack = 1
for ele in wheels:
    # print(ele, ele[0])
    if(ele[0] == '0'): # N극
        result += 0
    else:
        # print(stack)
        result += stack
    stack *= 2

print(result)