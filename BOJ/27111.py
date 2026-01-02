'''
출입기록 일부 누락
출입기록 :
1] 총 n개
2] 출입자가 출입한 시간순으로 기록함.
3] ai, bi = 출입하는 사람의 번호, 유형 (1 = 부대로 들어감, 0 = 부대에서 나옴)
4] 기록을 시작하지 전, 기록을 끝낸 후엔 부내 내 사람 수 = 0명

ex) n = 8
1   1
2   1 -> 들어가고 나온 기록이 없음
1   1 -> 1번 사람이 나온 기록이 없는데 들어감.
4   1

3   0 -> 들어가는거 없이 나옴
5   1
4   0
1   0

0. 뭘 구함?
1) 누락되는 유형을 구하면 될 듯

1. 모경수
0) 번호 : 유형 형태의 키, 벨류를 저장하고 수정하면 되겠다.
1) 기록 전, 후엔 부내 내 사람 0명이라서 들어가면 꼭 나와야함
1) 누락되는 유형
    1] 들어감
        1] 나오는거 없이 또 들어감 : 해당 번호 사람의 출입 유형이 부대로 들어감(1)인데 또 1임 -> 나옴 누락
        2] 안나옴 : 전부 다 순회했는데 유형이 아직 1임 -> 나옴 누락
    2] 나옴
        1] 들어가는게 없었는데 나옴 : dic에 이 번호가 없는데, 현재 유형이 0임 -> 들어감 누락
        2] 나왔는데 또 나옴 : 유형이 0인데 현재 유형이 또 0임 -> 들어감 누락
2) 정상 유형
    1] ok dic에 없는데 1이면 dic에 넣음
    2] ok dic에 있는데 0이면 0으로 수정


* n 
n개의 ai, bi

출 : 누락된 출입 기록의 최소 개수
2. nlogn
'''
import sys

input = sys.stdin.readline

n = int(input())
dic = {}
result = 0

for _ in range(n):
    num, t = map(int, input().split())
    
    # dic에 없는데 1이면 dic에 넣음
    if(num not in dic and t == 1):
        #print(1)
        dic[num] = 1
        continue
    
    # dic에 있는데 0이면 0으로 수정
    if(num in dic and dic[num] == 1 and t == 0):
        #print(2)
        dic[num] = 0
        continue
    
    if(num in dic and dic[num] == 0 and t == 1):
        #print(2)
        dic[num] = 1
        continue
        
# 1) 누락되는 유형
#     1] 들어감
#         1] 나오는거 없이 또 들어감 : 해당 번호 사람의 출입 유형이 부대로 들어감(1)인데 또 1임 -> 나옴 누락
    if(num in dic and dic[num] == 1 and t == 1):
        #print(3)
        result += 1


#     2] 나옴
#         1] 들어가는게 없었는데 나옴 : dic에 이 번호가 없는데, 현재 유형이 0임 -> 들어감 누락
    if(num not in dic and t == 0):
        #print(4)
        result += 1
#         2] 나왔는데 또 나옴 : 유형이 0인데 현재 유형이 또 0임 -> 들어감 누락    
    if(num in dic and dic[num] == 0 and t == 0):
        #print(5)
        result += 1


#         2] 안나옴 : 전부 다 순회했는데 유형이 아직 1임 -> 나옴 누락

#print(dic)
for k, v in dic.items():
    if(v == 1):
        result += 1

print(result)