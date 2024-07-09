'''
길이 n인 수식이 있다. 수식은 0~9 정수와 연산자로 이뤄짐. 연산자 우선순위가 없어서, 왼쪽부터 순서대로 계산한다.
괄호를 추가하면 괄호 안 식을 먼저 계산해야한다. 괄호안에 연산자 하나만 있어야 함 1 + (2+3)
중첩 괄호도 안됨 (1 + (2+3)) X

(3+8)×7-9×2 (num[i-1] oper[i-1] num[i])

(3+8)×(7-9)×2 (num[i-1] oper[i-1] num[i]) oper[i-2] (num[i-1] oper[i-1] num[i])

(3+8)×7-(9×2) (num[i-1] oper[i-1] num[i]) oper[i-1] num[i] 

3+(8×7)-9×2 num[i] oper[i-2] (num[i-1] oper[i-1] num[i])

3+(8×7)-(9×2)

012345678910
 3 8 7 9 2 

01234 
38792

+*-*

ttfff  (3+8)
ttttf

ttftt





1. 모경수(prt, n=1)
1) 백으로 탐색()
2) i가 uesd로 방문 안했으면 i, i+1 둘 다 방문처리
3) 그 다음 재귀는 +2로 
4) start도 둠
5) 매 재귀마다 visit을 봐서 t일때
    1] 첫 flag = f
    2] flag가 f면 t로 변환 끝
    3] flag가 t면 
        1] i가 1이면 그냥 결과에 (num[i-1] oper[i-1] num[i])
            1] first_flag = t면, 그냥 대압
            
        2] i가 i이 아니면 oper[i-2] (num[i-1] oper[i-1] num[i])
            2] f면 oper[i-2]의 기호로 (num[i-1] oper[i-1] num[i]) eval 결과를 result에 연산함
        
        3] flag = f로
        
6) visit이 f면
    1] i가 0이 아니면 oper[i-1] num[i]
        1] result에 oper[i-1]의 부호로 num[i] eval 결과를 result에 연산
    2] i가 0이면 num[i]
        1] first_flag = t면 result에 num[i] 대입, first_flag false로
        
            
            
7) 결과를 바로바로 더해야함
0] first_flag를 둬서, 맨 앞에 있는 건 그냥 대입, 아니면 그 괄호 앞에 연산자까지 고려함
1]    first_flag가 true면 result에 그 계산값 대입, first_flag를 false로
2] first_flag가 false면 

* n : 수식의 길이
수식
출 : 괄호를 적절히 추가해 만들 수 있는 식의 결과의 최대ㅏㄱㅄ, 추가안해도 된다.
2. 시복 n^3
'''

max_hab = 0

def back(start):
    global max_hab
    
    result = ""
    flag = False
    first_flag = True
    for i in range(len(used)):
        if(used[i]): # t일때
            if(flag == False):
                flag = True
            else:
                if(i == 1):
                    result = eval(f"({nums[i-1]} {opers[i-1]} {nums[i]})")
                        
                    # result += f"({nums[i-1]} {opers[i-1]} {nums[i]})"
                else:
                    middle_calc = eval(f"({nums[i-1]} {opers[i-1]} {nums[i]})")
                    oper = opers[i-2]
                    
                    if(oper == '+'):
                        result += middle_calc
                    elif(oper == '-'):
                        result -= middle_calc
                    else:
                        result *= middle_calc

                flag = False  
        else:
            if(i != 0):
                oper = opers[i-1]
                if(oper == '+'):
                    result += int(nums[i])
                elif(oper == '-'):
                    result -= int(nums[i])
                else:
                    result *= int(nums[i])
                
            else:
                result = int(nums[i])
    
    max_hab = max(max_hab, result)
        
    
    for i in range(start, len(nums)-1):
        if(not used[i]):
            used[i] = True
            used[i+1] = True
            back(i+2)
            used[i] = False
            used[i+1] = False

n = int(input())
calc = input()

nums = []
opers = []

for ele in calc:
    if(ele.isdigit()):
        nums.append(ele)
    else:
        opers.append(ele)

used = [False] * len(nums)

back(0)
print(max_hab)