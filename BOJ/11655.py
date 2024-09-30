'''
카드 n장이 있다. 숫자는 정수, 음수포함이다.
가장 많이 가지고 있는 정수를 구하고, 그런게 여러개라면 작은 것을 출력하라

1. 모경수(prt, n=1)
1) dic으로 카운트 셈
2) 정렬을 갯수로 해서 내림차순하고, 숫자를 기준으로 오름차순한 후 맨앞 요소 출력

* 준규가 가진 숫자 카드의 개수
숫자에 적힌 정수
출 : 가장 많이 가지고 있는 정수, 여러개라면 작은 것

2. nlogn
'''

dic = {}
n = int(input())
for _ in range(n):
    num = int(input())
    if(num in dic):
        dic[num] += 1
    else:
        dic[num] = 1
        
# print(dic)        
result = sorted(dic.items(), key = lambda x: (-x[1], x[0]))
print(result[0][0])