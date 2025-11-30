'''
게임
1] 0, x를 번갈아 그린다
2] o x가 직선으로 이어지게 하면 승리
3] 이어지는 직선이 없고, 더 그릴 빈칸도 없으면 무승부

1. 모경수(prt, n=1)
ok1) 4 by 4 행렬
2) 좌표 입력을 받고 플레이어 번호가 1이면 0, 2이면 x를 입력한다
3) 입력할 때마다 반복을 봐서 한 번의 케이스라도 모든 위치가 현재 좌표 입력을 한 플레이어의 모양과 같다면 거기서 승리!
    1] 1x1 / 1x2 / 1x3
    2] 2x1 / 2x2 / 2x3
    3] 3x1 / 3x2 / 3x3
    4] 1x1 / 2x1 / 3x1
    1x2 / 2x2 / 3x2
    1x3 / 2x3 / 3x3
    1x1 / 2x2 / 3x3
    1x3 / 2x2 / 3x1

4) 9번을 모두 봤는데 승부가 안나면 0출력

0x0
x0x
x0x

2
1 2
1 1
2 1
1 3
2 3
2 2
3 1
3 2
3 3


* 게임을 먼저 시작하는 플레이어 번호 1=o or 2=x
9개의 그림 좌표 (행, 열) / 인덱스 1부터 시작
출 : 승자가 결정되는 즉시 이긴 플레이어 번호를 출력하라 1, 2 / 무승부면 0

2. n^3

'''

num = int(input()) # 1=o or 2=x
graph = [[0] * 4 for _ in range(4)]
finish_flag = False
for _ in range(9):
    x, y = map(int, input().split())
    curr_moyang = "" # 현재 플레이어의 모양
    if(num == 1):
        curr_moyang = 'O'
    else:
        curr_moyang = 'X'
        
    graph[x][y] = curr_moyang
    
    arr = [
        [[1, 1], [1, 2], [1, 3]],
        [[2, 1], [2, 2], [2, 3]],
        [[3, 1], [3, 2], [3, 3]],
        [[1, 1], [2, 1], [3, 1]],
        [[1, 2], [2, 2], [3, 2]],
        [[1, 3], [2, 3], [3, 3]],
        [[1, 1], [2, 2], [3, 3]],
        [[1, 3], [2, 2], [3, 1]]
    ]
    
    for ele in arr:
        for x, y in ele:
            if(graph[x][y] != curr_moyang):
                break
        else:
            # 전부 같아.
            finish_flag = True
            break
    
    if(finish_flag == True):
        print(num)
        break
        
    if(num == 1):
        num = 2
    else:
        num = 1
else:
    print(0)


