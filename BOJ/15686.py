'''
알파벳을 오름차순으로 정려라여 이어서 출력하고, 그 뒤에 모든 숫자를 더한 값을 이어서 출력하라

1. 모경수
1) for문으로 훑어서 알파벳이면 배열에 저장
2) 숫자면 더함
3) 알파벳을 소트 > 조인하고 숫자도 더함

* s : 문자열
출력 : 

2. nlogn
'''

n = input()
alphas = []
num = 0

for digit in n:
    if(digit.isalpha()):
        alphas.append(digit)
    else:
        num += int(digit)
        
alphas.sort()        
result = "".join(alphas)
result += str(num)
print(result)