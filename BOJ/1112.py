'''
알파벳 대문자와 숫자로만 이뤄진 문자열이 있따. 모든 알파벳을 오름차순 정렬하고
그 뒤에 모든 숫자를 더한 값을 이어서 출력

1. 모경수(prt, n=1)
0] 정렬
1) 알파벳인지 체크하고 
    1] 알파벳이면 붙이고
    2] 숫자면 더함

* s : 문자열
출력 : 

2. 시복 nlogn
'''

s = input()
s = sorted(s)

result = ""
hab = 0
for ele in s:
    if(ele.isalpha()):
        result += ele
    else:
        hab += int(ele)
        
if(hab != 0):
    result += str(hab)
    
print(result)