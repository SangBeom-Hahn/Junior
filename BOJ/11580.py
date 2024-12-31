'''
재윤이 : 
1] 2차원 좌표 평면 원점에 있음
2] 방향을 외치면 그 뱡향으로 이동
3] 발자국을 남김, 똑같은 좌표는 발자국 x / 원점도 발자국 있음

1. 모경수(prt, n=1)
1) 발자국 원점을 가지고 set으로 만듦
2) 시작 발자국은 0, 0
3) 명령에 따라 이동함, 명령을 dic으로 말들어 둠
4) 명령에 따라 이동을 하면서 set에 넣음
5) set의 길이가 결과

* L : 명령어의 길이
명령어 E=동쪽, W=서쪽, S=남쪽, N=북
출 : 발자국의 개수

2. n^2
'''

L = int(input())
talk = input()

result = set()
result.add(tuple([0, 0]))
x = 0 # 시작
y = 0

print(result)

dic = {
    'E' : [0, -1],
    'W' : [0, 1],
    'S' : [-1, 0],
    'N' : [1, 0]
}

for ele in talk:
    x = x + dic[ele][0]
    y = y + dic[ele][1]
    
    result.add((x, y))

print(result)
print(len(result))    