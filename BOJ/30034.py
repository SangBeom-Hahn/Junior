'''
규칙 : 
1) 문자열을 규칙에 따라 나누는 게임
2) 문자열을 공백과 구분자로 나눔
3) 문자 구분자 : 영어 대소문자
4) 숫자 구분자 : 0~9
5) 병합자 : 구분자로 취급 X
6) 기준 문자열 : 나눌문자열 

구분자 a, b, 3
병합자 a
기준 abcdefg 1234

결과
a
cdefg
12
4

구분자 b c d 1
병합자 e
기준 abcde1bcd

1. 모경수(prt, n=1)
1) 구분자에서 병합자 뺌
2) 기준 문자열 순회하면서 구분자면 \n내림
3) 구분자가 여러개면
    0] 첫 시작 flag f
    1] 구분자가 아닌 경우 출력했다는 flag t
    2] 구분자가 맞음
        1] f이면 아무것도 안함
        2] t면 \n app


* n : 문자 구분자 개수
n개의 문자 구분자
m : 숫자 구분자 개수
m개의 숫자 구분자
k : 병합자 개수
k개의 병합자
s : 기준 문자열 길이
기준 문자열
출 : 적용한 결과

2. n
'''

n = int(input())
word_splits = list(set(input().split()))
m = int(input())
num_splists = list(set(input().split()))
k = int(input())
sum_word = input().split()

s = int(input())
str = input()

# 1) 구분자에서 병합자 뺌
total_split = set(word_splits + num_splists)
for ele in sum_word:
    total_split.discard(ele)
    
# print(total_split)

# 2) 기준 문자열 순회하면서 구분자면 \n내림
# 3) 구분자가 여러개면
#     0] 첫 시작 flag f
#     1] 구분자가 아닌 경우 출력했다는 flag t
#     2] 구분자가 맞음
#         1] f이면 아무것도 안함
#         2] t면 \n app

flag = False
result = []
for ele in str:
    if(ele in total_split or ele == " "):
        if(flag == True):
            result.append("\n")
            flag = False
    else:
        flag = True
        result.append(ele)
        
print("".join(result))        