'''
화분 : n개에 k만큼의 수분이 있다.
일 : 
1] 연속된 A개의 화분에 물을 B만큼 준다.
2] 모든 화분의 수분이 1씩 감소
3] 수분이 0이 된 화분에 잎은 죽음

n = 6 / k = 3 / a = 5 / b = 2

3   3   3   3   3   3
5   5   5   5   5   3
4   4   4   4   4   2

4   6   6   6   6   4
3   5   5   5   5   3


가장 작은 인덱스 2
a = 3

0   1   2   3
4   4   3   4


1. 모경수
1) 첫날 = 1일
2) k로 채워진 크기 n배열을 만듦
3) 일을 반복
    1] 물 주기
        1] 수분이 가장 작은 idx 찾기
        2] 가장 작은 idx부터 a번 오른쪽으로 물 주기
            1] 물 준 횟수를 기록하고 물을 줄 때마다 횟수를 차감
            2] 배열 크기를 넘으면 끝
        
        3] a번 다 못 주면 왼쪽으로 물 주기
            1] 횟수가 0이 아니면
            2] 왼쪽으로 물주기
    
    2] 전체에 1빼기
    3] 요소가 0이 있으면 날짜 출력하고 끝
    4] 날짜 ++


* n, k, a, b
출 : 모든 잎이 살아있는 기간이 최대한 길게 물을 줄 때, 첫 잎이 죽는 날짜 (첫 날은 1일)

2. n^3
'''

n, k, a, b = map(int, input().split())

day = 1
plants = [k] * n
# plants = [4, 4, 3, 4]

su = 1
# while(su != 2):
while(True):
    min_water = min(plants)
    min_idx = plants.index(min_water)
    cnt = a
    
    # 오른쪽 물주기 / idx 4, cnt 2라면 4 5
    for i in range(min_idx, min_idx + a):
        if(i == n):
            break
        
        plants[i] += b
        cnt -= 1
    
    # 왼쪽 / idx 4, cnt 2라면 3, 2
    temp_cnt = cnt
    for i in range(min_idx-1, min_idx-1-temp_cnt, -1):
        plants[i] += b
        cnt -= 1
        
    plants = list(map(lambda x: x-1, plants))
    
    print(plants)
    
    if(0 in plants):
        print(day)
        break
    
    day += 1
    
    
    su += 1