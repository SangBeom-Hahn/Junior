''''
배열, 참조, 포인터가 있고 혼합가능 int&&[]*
int& a*[]&에서 a의 타입 = int&&[]* 오른쪽에 있는거 순서 뒤집어서 왼쪽에 붙임

1. 모경수(prt, n=1)
1) 기본 변수형 구함 [0]
2) 변수 선언 리스트 구함
    1] 맨 마지막 변수 선언에서 ; 제거
    2] 변수 선언을 변수명 (1글자 이상) + 추가적 변수형[없을수도 있음]으로 나눔
3) 변수 선언 리스트 훑으면서 기본 변수형 + 추가적 변수형[없을수도 있음] 뒤집은거 + 공백 + 변수명 + ; 출력

* 변수 선언문 (변수가 여러개 포함되어 있을수 있음)
기본 변수형+추가 변수형(추가는 없을수도 있음) 
-> 공백 이후에 변수 선언이 하나씩 (,와 공백으로 나뉨, ;로 끝남)
변수 선언(기본 변수명, 추가적인 변수형[없을수도 있음])

출 : 오른쪽에 있는 변수형을 모두 왼쪽으로 옮기고 한줄에 하나씩 출력 (형과 명 사이 공백)
;로 끝
'''

inp = list(input().split(' '))
basic_v_type = inp[0]
v_call_list = inp[1:] # 변수 선언 리스트 구함
for i in range(len(v_call_list)):
    v_call_list[i] = v_call_list[i][:-1]
    
# print(basic_v_type)
# print(v_call_list)

v_names = []
extra_v_type = []

# 2] 변수 선언을 변수명(1글자 이상)+ 추가적 변수형[없을수도 있음]으로 나눔
    # 1] 변수명 : 변수 선언을 순회하면서 *, [, &가 나오기 전까지
    # 2] 변수형 : 나온 이후, 없으면 "" 넣음
for ele in v_call_list:
    meet_flag = False
    for i in range(len(ele)):
        if(ele[i] == '*' or ele[i] == '[' or ele[i] == '&'):
            v_names.append(ele[:i])
            extra_v_type.append(ele[i:])
            break
    else:
        # conti를 못 만났어 = b만 있어
        
        v_names.append(ele)
        extra_v_type.append("")

# print(v_names)
# print(extra_v_type)

# 변수 선언 리스트 훑으면서 기본 변수형 + 추가적 변수형[없을수도 있음] 뒤집은거 + 공백 + 변수명 + ; 출력
for i in range(len(v_call_list)):
    # 추가적 변수형[없을수도 있음] 뒤집은거
    ele = extra_v_type[i][::-1]
    reverse = []
    for digit in ele:
        if(digit == '['):
            reverse.append(']')
        elif(digit == ']'):
            reverse.append('[')
        else:
            reverse.append(digit)
    
    print(f"{basic_v_type}{''.join(reverse)} {v_names[i]};")