'''
길이가 N인 수식이 0~9 정수와 연산자로 이루어짐.
수식 계산은 왼쪽에서 순서대로 계산한다.
수식에 괄호를 추가하면, 괄호 안에 식을 먼저 계산해야 한다.
단 괄호 안에는 연산자가 하나만 있다. (1+2) O
중첩 괄호는 안된다. ((1+2)-3) X
수식이 있을 때 괄호를 적절히 추가해 만들 수 있는 식의 결과의 최대값을 구해라
추가 괄호 개수 제한은 없고 추가하지 않아도 됨

# visit 버전
3 + 8 * 7 - 9 * 2면 이 사이사이 갈호를 붙인 곳을 visit + 백트래킹

0 1 2 3 4 5 6 7 8
3   8   7   9   2

0 1 2 3 4 5 6 7 8 9 10
1   2   3   4   5   6
  
1. 한번의 재귀에서 열괄호 닫괄호를 둘 다 true로 만듬, (3+8)이면 숫자의 자리에 t를 하자
0 1 2 3 4 5 6 7 8
t   t

(8 + 7)이면
0 1 2 3 4 5 6 7 8
    t   t

2. for문에서 재귀를 0 2 4 8 10처럼 짝수로만 하면 될 듯, for문은 0부터 +2씩 증가함
3. 한 번 재귀를 하면 다음 인덱스는 +4? 0 -> 4에서 2씩 증가 start를 두자
0 1 2 3 4 5 6 7 8
t   t

0 1 2 3 4 5 6 7 8
t   t
        t   t
t   t       t   t        

4. 매 재귀마다 결과 계산함
back(start, )일때 재귀 맨 위에서 visit 순회해서 
1) 인덱스 0에서 t이면 flag t, 다음 인덱스 순회 
2) 인덱스 1에서(인덱스가 홀수이면 연산자) flag가 t면 패스
3) 인덱스 2에서 flag가 t면 -2해서 인덱스 0, 1, 2계산해서 결과에 더함, flag f
4) 인덱스 3에서 flag f면 패스, 
5) 인덱스 4에서 visit이 false이면 결과에 바로 인덱스 3에 있는 연산자로 결과에 연산함

1. 모경수(prt, n=1)
1) visit을 수식 길이만큼 f로 초기화
2) visit f면 열괄호 닫괄호를 둘 다 true
3) 한번의 재귀에서 for문은 0부터 2씩 증가해서 짝수만 보는데, start를 둬서 다음 재귀는 인덱스는 +4
4) 매 재귀마다 결과 계산함
        
* n : 수식의 길이
수식
출 : 괄호를 적절히 추가해서 얻을 수 있는 결과의 최대값
2. 시복 b^3
'''

answer = 0
def back(start):
    global answer
    
    flag = False
    semi_result = 0
    for i in range(len(visit)):
        if(i%2 == 0 and visit[i] == True and flag == False):
            flag = True
        elif(i%2 == 0 and visit[i] == True and flag == True):
            one = int(calc[i-2])
            oper = calc[i-1]
            two = int(calc[i])
            final_oper = '+'
            if(i-3 >= 0):
                final_oper = calc[i-3]
            
            if(oper == '+'):
                hab = (one + two)
                if(final_oper == '+'):
                    semi_result += hab
                elif(final_oper == '-'):
                    semi_result -= hab
                elif(final_oper == '*'):
                    if(semi_result == 0):
                        semi_result += hab
                    else:
                        semi_result *= hab
                
                
            elif(oper == '-'):
                cha = (one - two)
                if(final_oper == '+'):
                    semi_result += cha
                elif(final_oper == '-'):
                    semi_result -= cha
                elif(final_oper == '*'):
                    if(semi_result == 0):
                        semi_result += cha
                    else:
                        semi_result *= cha
            else:
                gob = (one * two)
                if(final_oper == '+'):
                    semi_result += gob
                elif(final_oper == '-'):
                    semi_result -= gob
                elif(final_oper == '*'):
                    if(semi_result == 0):
                        semi_result += gob
                    else:
                        semi_result *= gob
                
            flag = False
        elif(i%2==0 and visit[i] == False):
            one = int(calc[i])
            
            if(i == 0):
                oper = calc[i+1]
                if(oper == '+'):
                    semi_result += one
                elif(oper == '-'):
                    semi_result -= one
                else:
                    if(semi_result == 0):
                        semi_result += one
                    else:
                        semi_result *= one
                
            else:
                oper = calc[i-1]
                if(oper == '+'):
                    semi_result += one
                elif(oper == '-'):
                    semi_result -= one
                else:
                    if(semi_result == 0):
                        semi_result += one
                    else:
                        semi_result *= one
        # print(calc[i])
        # print(semi_result)
        
        
    # print(visit)    
    # print(semi_result)
    answer = max(answer, semi_result)
    # return
    
    for i in range(start, leng, 2):
        # print(i)
        if(not visit[i] and i < leng-1):
            visit[i] = True
            visit[i+2] = True
            back(i+4)
            visit[i] = False
            visit[i+2] = False
        

n = int(input())
calc = input()
leng = len(calc)

visit = [False] * leng
# visit = [False, False, False, False, False, False, True, False, True]

back(0)
print(answer)