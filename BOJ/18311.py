'''
그룹 : 단어에 존재하는 모든 문자에 대해서 각 문자가 연속해서 나타나는 경우

ex) 그룹단어
a\n = 뒤에 문자랑 다르면 현재 나온 문자들 보관소에서 검사
ab = 뒤에 문자랑 다르면 
aabb
aabbccc
abbccc

그룹 X
aabbbccb = b가 연속하지 않고 떨어져서 나와서 그룹 단어가 아님

1. 모경수(prt, n=1)
1) 맨 뒤에 'A' 추가
1) 뒤에 문자랑 다르면 현재 나온 문자들 보관소에서 검사
    1] 보관소에 없으면 보관소에 추가
    2] 보관소에 있으면 그룹 단어 X, 다음 문자 봄
2) 뒤에 문자랑 같으면 다음 문자 봄
3) 모든 문자 다 보면 그룹 단어임 

* n : 단어의 개수
n개의 단어
출 : 그룹 단어의 개수

2. nlogn
'''

n = int(input())
cnt = 0
for _ in range(n):
    word = input()
    leng = len(word)
    word += 'A'
    dic = {} # 보관소
    
    for i in range(leng):
        if(word[i] != word[i+1]):
            if(word[i] not in dic):
                dic[word[i]] = 1
            else:
                break
    else:
        cnt += 1
        # print(dic)
print(cnt)