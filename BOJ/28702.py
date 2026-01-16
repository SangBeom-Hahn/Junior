'''
규칙
1] 3의 배수, 5의 배수이면 FizzBuzz
2] 3의 배수이면 Fizz
3] 5의 배수이면 Buzz
4] 전부 다니면 숫자 그대로 출력

1. 뭘구해?
1) 3개를 보고 4번째 출력을 구해야한다.

2. 모경수
1) 3개가 전부 문자열인 경우는 없을 것 같아.
2) 숫자를 찾고
    1] 첫 번째라면, 3 더해서 결과
    2] 두번째라면, 2더해서
    3] 세번째라면, 1 더해서 결과 ㄱㄱ


* 연속으로 출력된 3개의 문자열
출 : 다음에 올 문자열 (여러개가 가능하면 아무거나 출력)
2. n^3

'''

one = input()
two = input()
three = input()

step = 1

for ele in [one, two, three]:
    try:
        int(ele)
        break
    except:
        step += 1



if(step == 1):
    result = int(one) + 3
    
    if(result % 3 == 0 and result % 5 == 0):
        print("FizzBuzz")
    elif(result % 3 == 0):
        print("Fizz")
    elif(result % 5 == 0):
        print("Buzz")
    else:
        print(result)
elif(step == 2):
    result = int(two) + 2
    
    if(result % 3 == 0 and result % 5 == 0):
        print("FizzBuzz")
    elif(result % 3 == 0):
        print("Fizz")
    elif(result % 5 == 0):
        print("Buzz")
    else:
        print(result)
else:
    
    result = int(three) + 1
    
    if(result % 3 == 0 and result % 5 == 0):
        print("FizzBuzz")
    elif(result % 3 == 0):
        print("Fizz")
    elif(result % 5 == 0):
        print("Buzz")
    else:
        print(result)