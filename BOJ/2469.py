'''
k명의 참가자가 알파벳 순서대로 사다리 탐/ 세로 막대를 타고 내려오다가
가로 막대를 만나면 옮겨가면서 끝까지 내려온다.
가로 막대가 세로 줄 연속해서 있지는 않음
가로 줄 하나가 감추어진 사다리를 받아서 가로막대를 적절히 넣어서 최종 수서가
원하는 순서대로 나오도록 만들고 싶다.

ex) k = 10
1. 모든 경우의 수
1) 사람은 항상 가로줄 수 + 1개의 배열에 저정된다.

2) 모든 사람 말고 한명씩 이동하는데 어차피 가로줄 하나만 바꾸는 것이므로
A부터 봐서 그 줄에 놨는데 최종 결과의 위치로 가면 놓고 안되면 놓지마라

근데 안돼서 안놨는데 안 놔도 최종 결과가 안나오면 x


ㅁaㅁbㅁcㅁ -> join
ㅁㅁ-ㅁ-ㅁㅁ

* k : 사람수
n : 가로 줄 수
사다리를 타고 난 후 최종 순서
사다리 상태(*가로막대가 없음, - 있음, ? 감추어진 가로 줄)

출력 : 감추어진 가로 줄의 상태를 *과 -로 재구성해야한다.
못하면 x로 출력

2. n^2
'''
import string

# 1) 사람은 항상 가로줄 수 + 1개의 배열에 저정된다.
k = int(input()) # 사람수
n = int(input()) # 가로 줄 수 
peoples = string.ascii_uppercase[:k]
peoples = 'ㅁ'.join(peoples)
peoples = 'ㅁ'+peoples+'ㅁ' # 입력 단계 알파벳

results = input() # 최종 결과
results = 'ㅁ'.join(results)
results = 'ㅁ'+results+'ㅁ' # 입력 단계 알파벳

bridges = []
for _ in range(n):
    line = input()
    line = 'ㅁ'+'ㅁ'+'ㅁ'.join(line)+'ㅁ'+'ㅁ'
    bridges.append(line)

import copy
# 시작에서 ? 만나기 전까지 변경
for ele in bridges:
    temp = ['ㅁ'] * len(peoples)
    # temp = ['ㅁ' for _ in range(len(peoples))]
    if(ele[2] == '?'):
        break
    
    for idx, people in enumerate(peoples):
        # print(idx, people)
        if(people != 'ㅁ'):
            # print(1)
            if(ele[idx+1] == '-'):
                # print(2)
                temp[idx+2] = people
            elif(ele[idx-1] == '-'):
                # print(3)
                temp[idx-2] = people
            else:
                temp[idx] = people
                
    peoples = copy.deepcopy(temp)
    # print(peoples)


for ele in bridges[::-1]:
    temp = ['ㅁ'] * len(results)
    # temp = ['ㅁ' for _ in range(len(peoples))]
    if(ele[2] == '?'):
        break
    
    for idx, results in enumerate(results):
        # print(idx, people)
        if(results != 'ㅁ'):
            # print(1)
            if(ele[idx+1] == '-'):
                # print(2)
                temp[idx+2] = results
            elif(ele[idx-1] == '-'):
                # print(3)
                temp[idx-2] = results
            else:
                temp[idx] = results
                
    results = copy.deepcopy(temp)
    
newLine = ""
flag = False
for i in range(len(peoples)-2):
    if(peoples[i] != 'ㅁ'):
        if(peoples[i] == results[i]):
            newLine += '*'
        elif(peoples[i] == results[i+2] and peoples[i+2] == results[i]):
            newLine += '-'
            peoples[i], results[i+2] = peoples[i+2], results[i]
        else:
            flag = True

results = ''.join(results)
results = results.replace('ㅁ', '')

# print(results)
if(flag == True)            :
    print('x' * len(results))
else:
    print(newLine)