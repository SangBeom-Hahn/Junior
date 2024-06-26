'''
n개의 원소를 포함하는 뎈이 있다. 여기서 몇 개의 원소를 뽑을 것이다.

연산 :
1) 첫번째 원소를 뽑음
2) 왼쪽으로 한칸 이동 rotate
3) 오른쪽 한칸 이동 rotate

ex) 큐 1 2 3 4 5 6 7 8 9 10
연산 1 1 1 -> 1 2 3

원하는 수   연산    큐                      나온 수 인덱스  0과 인덱스의 차     큐길이와 인덱스의 차
                    1 2 3 4 5 6 7 8 9 10            1       1
2 9 5       2       2 3 4 5 6 7 8 9 10 1            
            1       3 4 5 6 7 8 9 10 1      2       6                           3
            
            3       1 3 4 5 6 7 8 9 10
            3       10 1 3 4 5 6 7 8 9
            3       9 10 1 3 4 5 6 7 8
            1       10 1 3 4 5 6 7 8        1
            
2 8 10      2       2 3 4 5 6 7 8 9 10 1
            1       3 4 5 6 7 8 9 10 1      2
            3       1 3 4 5 6 7 8 9 10
            3       10 1 3 4 5 6 7 8 9
            3       9 10 1 3 4 5 6 7 8            
            3       8 9 10 1 3 4 5 6 7
            1       9 10 1 3 4 5 6 7        8
            
            
1. 모경수(prt, n=1)
1) 원하는 수가 큐의 맨 앞과 가까운지, 규의 맨 뒤와 가까운지 체크
    1] 원하는 수의 인덱스를 구함
    2] 큐의 길이가 짝수이면 큐의 길이 //2 보다 작으면 왼쪽 rot, 길이와 같아도 왼쪽 rot, 크면 오른쪽 rot / cnt+1
    3] 큐의 길이가 홀수이면 큐의 길이 //2 보다 작으면 왼쪽 rot, 길이와 같아도 왼쪽 rot, 크면 오른쪽 rot
2) 인덱스 만큼 rotate를 한 번에 돌린다.
    1] 왼쪽으로 돌려야 하면 0과 인덱스 차 횟수만큼 돌리고
    2] 오른쪽으로 돌려야 하면 큐 길이와 인덱스의 차 만큼 돌린다.
3) 돌린 다음 q[0]를 뺀다.

n, m : 큐의 크기, 뽑으려고 하는 수의 개수
뽑으려고 하는 수의 위치(가장 처음 큐에서의 위치)
출 : 원소를 주어진 순서대로 뽑아내는데 드는 2, 3번 연산의 최소 횟수를 구하라

2. 시복 : n^3
'''

n, m = map(int, input().split())
locs = list(map(int, input().split()))

from collections import deque
nums = deque(list(range(1, n+1)))
res = 0

for loc in locs:
    # 1] 원하는 수의 인덱스를 구함
    idx = nums.index(loc)
    leng = len(nums)
    
    # 왼쪽으로 돌려야 하면 0과 인덱스 차 횟수만큼 돌리고
    
    # print(nums)
    if(idx <= leng // 2):
        cnt = idx - 0
        for _ in range(cnt):
            nums.rotate(-1) # -1이 왼쪽
            res += 1
            # print(nums)
    else:
        # 오른쪽으로 돌려야 하면 큐 길이와 인덱스의 차 만큼 돌린다.
        cnt = leng - idx
        for _ in range(cnt):
            nums.rotate(1) # 1이 오른쪽
            res += 1
            # print(nums)
            
    nums.popleft()
    # print(nums)

print(res)

