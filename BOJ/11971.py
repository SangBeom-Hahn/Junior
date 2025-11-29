'''
도로 : 
1] 100KM
2] n개 구간에 제한속도가 있다. 각 구간에 도로 길이와 제한속도가 주어진다.

연정
1] m개의 구간에 (도로 길이와 연정이가 달린 속도)가 있다.

ex) 

도로
40 75
50 35
10 45

연정
40 76
20 30
40 40

달린구간    해당 구간의 제한속도    연정이 달린 속도    속도위반한 값
40          75                      76              76-75=1
20          35                      30
30          35                      40              5
10          45                      40  

연정 달린 속도 배열
1 ~ 40      76
41 ~ 60     30
61 ~ 100    40

도로 제한 속도 배열
1 ~ 40      75
41 ~ 90     35
91 ~ 100    45

1. 모경수(prt, n=1)
ok 1) 연정 배열을 만듦
ok 2) 도로제한 속도 배열을 만듦
3) 처음부터 100까지 순회해서 연정 - 제한의 최대값을 구함.
4) 최대값 최초를 0으로 하면 연정이 위반을 안하면 연정 - 제한값이 전부 음수라서 최대값이 0이 유지되겠다.


* n, m
n개의 구간의 길이와 해당 구간의 제한 속도
m개의 여정이가 달린 각 구간의 길이와 해당 구간에서 달린 속도

출 : 속도 위반한 최댓값
'''

n, m = map(int, input().split())

fact_value = [] # 실제 제한속도 배열
run_value = [] # 연정 달린 배열
for _ in range(n):
    part_range, pase = map(int, input().split())
    for _ in range(part_range):
        fact_value.append(pase)

for _ in range(m):
    part_range, pase = map(int, input().split())
    for _ in range(part_range):
        run_value.append(pase)
        


max_v = 0
for i in range(100):
    fact = fact_value[i]
    run = run_value[i]
    
    if(max_v < run - fact):
        max_v = run - fact

print(max_v)