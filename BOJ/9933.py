'''
텍스트 파일 하나를 자신의 메일로 전송함. 파일에는 단어가 한줄ㄹ에 하나씩 있고
그중 하나는 비밀번호다.
1) 모든 단어 길이: 홀수
2) 비밀번호를 뒤집어서 쓴 문자열도 포함되어 있다.

1. 모경수(prt, n=1)
1) 비밀번호를 순회함
2) 하나 선택해서 뒤집고 그게 비밀번호에 속하면, 길이와 가운데 글자 출력

* n : 단어의 수
단어들
출 : 비밀번호를 찾고, 비밀번호의 길이와 가운데 글자를 출력하라

2. n^3
'''

n = int(input())
password = set()
for _ in range(n):
    ele = input()
    password.add(ele)

for ele in password:
    rev = ele[::-1]
    if(rev in password):
        leng = len(rev)
        print(leng, rev[leng // 2])
        break