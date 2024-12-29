'''
단어 순서 우선순위
1) 자주 나오는 단어
2) 길이가 길수록
3) 알파벳 사전 순
4) 길이가 M 미만이면 안 씀

ex) m = 4
apple sand apple append sand sand

횟수    길이    단어    
3       4       sand
2       5       apple
1       6       append

1. 모경수(prt, n=1)
1) 길이가 M 미만이면 conti
2) dic에 단어 : [횟수, 길이] 넣음
3) items로 뽑고 정렬
    1] 1, 2, 0 순으로

* n : 단어 개수
m : 길이
외울 단어
출 : 우선순위에 맞게 하나씩 출력

2. nlogn
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
for _ in range(n):
    word = input().strip()
    leng = len(word)
    if(leng < m):
        continue
    
    if(word in dic):
        dic[word][1] = dic[word][1]-1
    else:
        dic[word] = [word, -1, -leng]
        
# print(dic)
results = list(dic.values())
results.sort(key = lambda x:(x[1], x[2], x[0]))

for ele in results:
    print(ele[0])