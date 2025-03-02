'''
탁자에 컵 4개, 가장 왼쪽= 작은 공 / 가장 오른쪽 = 큰공

A = 0, 1
B = 0, 2
C = 0, 3
D = 1, 2
E = 1, 3
F = 2, 3

작 빈 빈 큰

1. 모경수(prt, n=1)
o0) 컵 내부를 크기 4 배열로 두고 작 빈 빈 큰
o1) 컵 섞는 순서 순회
2) A라면 A의 인덱스 2개를 스위치
3) 모두 섞고 컵 내부를 순회해서 작과 큰의 위치 출력

* 컵을 섞는 순서 : ABCEDF 중 한게
출 : 작은 공의 위치, 큰 공의 위치 (가장 왼쪽부터 1, 2, 3, 4)

2. n^3
'''

sunsu = input()

dic = {
    'A' : [0, 1],
    'B' : [0, 2],
    'C' : [0, 3],
    'D' : [1, 2],
    'E' : [1, 3],
    'F' : [2, 3]
}

cup_in = ['작', '빈', '빈', '큰']

for ele in sunsu:
    idx1, idx2 = dic[ele][0], dic[ele][1]
    cup_in[idx1], cup_in[idx2] = cup_in[idx2], cup_in[idx1]

s_loc = 0
b_loc = 0

for i in range(len(cup_in)):
    if(cup_in[i] == '작'):
        s_loc = i
    if(cup_in[i] == '큰'):
        b_loc = i
        
print(s_loc+1)        
print(b_loc+1)        