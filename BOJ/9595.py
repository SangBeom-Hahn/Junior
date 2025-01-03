'''
n개의 옵션, 옵션의 기능을 설명하고 있다.
옵션에 단추키 대표 알파벳을 지정하자

알파벳
0] 이 방법은 첫번째부터 N번쨰까지 차례대로 지정
1] 왼쪽에서 오른쪽 순서로 옵션 설명 기능 단어의 첫 글자가 단축키로 지정되었는지 보고
안 되어있으면 그 알파벳을 단축키 지정
2] 1번 불가하면 왼쪽에서부터 차례로 봐서 단축키로 지정 안된 것 단축키 지정
3] 2번도 안되면 그냥 놔둠 

ex) 
Save = S
Save As = S가 되어있으니 A

1. 모경수(prt, n=1)
1) 단축키 모음 집 set (전부다 소문자로 비교함)
2) 단어 - 단축키 dic

3) 첫번째 옵션부터 순회
    1] 지정1 : split해서 단어 순회
        2] 단어의 첫 글자만 봐서 단축키 모음집에 있는 지 확인 (소문자 비교)
        3] 있으면 다음 단어
        4] 없으면 단축키 모음집에 그 알파멧 소문자 넣고, 단어 - 단축키 알파벳 dic
    2] 지정 2 : 1번 다 안됨
        1] 왼쪽에서 부터 전부 순회해서 단축키 모음집에 있는 지 확인 (소문자 비교)
        2] 있으면 다음
        3] 없으면 단축키 모음집에 그 알파멧 소문자 넣고, 단어 - 단축키 알파벳 dic
    3] 지정 3 : 2번도 안 되면 그냥 dic에 그 단어가 없을 거임, 

4) 출력
    1] dic 단어봐서 단어를 한글자씩 출력하는데 단축키면 [, ]
    2] dic에 단어가 없으면 그냥 그 단어 출력
        

* n : 옵션의 개수
옵션의 기능을 설명하는 문자열 (단어는 공백 1칸)
출 : n개의 옵션 출력, 단축키 좌우에 []

2. n^3
'''

n = int(input())
funcs = [input() for _ in range(n)]
shorts = set()
dic = {}

# 3) 첫번째 옵션부터 순회
#     1] 지정1 : split해서 단어 순회
#         2] 단어의 첫 글자만 봐서 단축키 모음집에 있는 지 확인 (소문자 비교)
#         3] 있으면 다음 단어
#         4] 없으면 단축키 모음집에 그 알파멧 소문자 넣고, 단어 - 단축키 알파벳 dic

# 2] 지정 2 : 1번 다 안됨
#         1] 왼쪽에서 부터 전부 순회해서 단축키 모음집에 있는 지 확인 (소문자 비교)
#         2] 있으면 다음
#         3] 없으면 단축키 모음집에 그 알파멧 소문자 넣고, 단어 - 단축키 알파벳 dic

for i in range(n):
    fin_flag = False
    opt = funcs[i]
    split = opt.split(' ')
    for ele in split:
        first_ele = ele[0]
        if(first_ele.lower() not in shorts):
            shorts.add(first_ele.lower())
            dic[opt] = first_ele
            fin_flag = True
            break
    
    if(fin_flag == True): # 다음 단어
        continue
    
    for ele in opt:
        # 공백이면 패스
        if(ele == ' '):
            continue
        
        if(ele.lower() not in shorts):
            shorts.add(ele.lower())
            dic[opt] = ele
            fin_flag = True
            break
    
    # 3] 지정 3 : 2번도 안 되면 그냥 dic에 그 단어가 없을 거임, 
    
# 4) 출력
#     1] dic 단어봐서 단어를 한글자씩 출력하는데 단축키면 [, ]
#     2] dic에 단어가 없으면 그냥 그 단어 출력    
    

# print(shorts)            
# print(dic)            

for ele in funcs:
    if(ele not in dic):
        print(ele)
    else:
        for digit in ele:
            if(digit == dic[ele]):
                print(f"[{digit}]", end = '')
            else:
                print(digit, end = '')
        print()