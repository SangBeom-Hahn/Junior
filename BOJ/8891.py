'''
트럭
1] n개, 순서 변경 불가

다리
1] 길이 W
2] 다리 위 트럭 무게 합은 최대하중 보다 작거나 같아야 함
3] 트럭은 1초에 1칸씩만 이동 가능

ex) w = 2 / 최대하중 10 / 트럭 무게 7 4 5 6

초      다리    트럭인덱스
0       []      0
1       [, 7]   1
2       [7, ]   
3       [, 4]   2
4       [4, 5]  3
5       [5, ]   
6       [, 6]   4
7       [6, ]
6       []

w = 100 / 최대하중 100 / 트럭 무게 100

초      다리    트럭인덱스
0       []      0
1       [100]   1



1. 모경수(prt, n=1)
ok 1) w 길이의 큐를 만듦
ok 2) 큐를 1칸 보내고 , 새로운 트럭을 태운 후 1초 증가
ok 3) 큐를 1칸 보내고 -> 큐와 새롭게 타려는 트럭의 무게 총합이 <= L 면 탑승
    1] 탑승하면 트럭 인덱스 += 1
ok 4) 아니면 탑승 못함
5) 다리 sum이 0이고 트럭 인덱스가 n과 같으면 끝


n, w, l 
건너는 순서대로 트럭 무게
출 : 모든 트럭이 다리를 건너는 최단 시간

2. n^2
'''

n, w, l = map(int, input().split())
tons = list(map(int, input().split()))

q = [0] * w
time = 0
idx = 0
# print(q)

while(True):
    if(sum(q) == 0 and idx == n):
        break
    
    q.pop(0)
    
    if(idx < n and sum(q) + tons[idx] <= l):
        q.append(tons[idx])
        idx += 1
    else:
        q.append(0)
    
    time += 1
    
    # print(q)

print(time)