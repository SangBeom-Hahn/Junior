'''
땅 고르기 : 땅의 높이를 모두 동일하게 만들기
n, m 크기의 집터에 높이를 일정하게 바꾸자
작업 : 
1) i, j 좌표의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다. -> 2초걸림
2) 인벤에서 블럭 하나를 꺼내서 i, j 좌표 가장 위에 있는 블록 위에 놓는다. ->1초걸림

조건 : 
집터 밖에서 블록을 가져올 수 없음. 
작업 시작시 B개의 블록이 인벤에 있음
땅의 높이는 256블럭 초과 X, 음수 X

ex) 
0 0 0 0
0 0 0 0
0 0 0 1 -> 작은거 11개, 큰거 1개 = 큰게 더 적으면 = 적은거 제거

1 1 1 1
1 1 1 1
1 1 1 0 -> 큰거 11개, 작은거 1개 = 작은게 더 적으면 = 적은거 채움
-> 작은게 적으면 채움, 그때 작은거 개수가 B보다 크면 못 채움 = 큰거 제거해야함

1 2
3 4

1로 맞추기  
B       작업    상태        초
1                           6 제거 = 12초
2       2 제거  1 1
                3 4

        3 제거
        3 제거
        4제거
        4제거
        4제거    
        
2로 맞추기                    
작업    상태    B   초                
1 채움              1채움 3제거 = 7초
3제거
4제거
4제거

3로 맞추기
작업    상태    B   초
1채움               3채움 1제거 = 5초
1채움
2채움
4제거

4로 맞추기
작업    상태    B   초
1채움               6채움 = 6초
1채움
1채움
2채움
2채움
3채움

1. 모경수
1) 모든 땅의 높이 0 ~ 256까지 순회해서 보자
2) 현재 땅의 높이와 집터의 높이를 비교
    1] 땅 > 집터 : 인벤에서 빼서 집터를 채워야 함 / 블록 1개당 1초 걸림
    2] 땅 < 집터 : 인벤에 넣어야 함 / 1개당 2초 걸림
3) 현재 땅에서의 시간을 저장함
4) 최소 시간을 구함



* n, m, B : n, m 크기 집터, 최초 B개의 블럭
땅의 높이 상태
출 : 땅을 고르는데 걸리는 최소 시간과 땅의 높이(여러개일 경우 최대높이)

2. nlogn
'''
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
house = [list(map(int, input().split())) for _ in range(n)]

# print(*house, sep = '\n')
time = [0 for _ in range(257)]
result_h = 0
for ground in range(257):
# for ground in range(63, 64):
    inven = b
    for i in range(n):
        for j in range(m):
            
            house_hei = house[i][j]
            
            if(ground > house_hei):
                inven -= ground-house_hei
                time[ground] += ground-house_hei
            elif(ground < house_hei):
                inven += house_hei-ground
                time[ground] += 2 * (house_hei-ground)
    if(inven >= 0 and time[result_h] >= time[ground]):
        result_h = ground
    

print(time[result_h], result_h)
                
