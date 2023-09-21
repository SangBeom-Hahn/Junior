'''
문자열 s가 있을 때 여기서 단어만 뒤집으려고 한다. 
규칙 : 
1) <>는 무조건 <> 순서로 나오고 개수는 같다 열대, 닫괄호가 됨
2) 태그 : <로 시작, > 로 끝나는 길이 3이상 문자열이고 사이에는 알파벳
소문자와 공백만 있음 = 숫자, 특수문자 <> 없음

3) 단어 : 알파벳 소문자와 숫자로 이루어진 부분 문자열 
4) 연속하는 두 단어는 공백 하나로 구분 = 즉 연속하는 단어는 공백이 있어서 단어X
각각이 단어지 하나의 단어가 아님
5) 태그는 단어 X, 태그와 단어사이에는 공백 없음

1. 모든 경우의 수
1) 단어를 찾는다.
2) 단어는 알파와 숫자로만 되어있으니 <가 나오면 >나올 떄까지 태그고
3) 알파벳 소문자로 시작하거나 숫자로 시작하면 공백이나 <나올 때까지 단어임

4) 태그를 찾는 순간인지 단어를 찾는 순간인지 구분을 해서
태그였으면 그냥 더하고 단어였으면 역순으로 더하자

* s : 문자열
출력 : s의 단어만 뒤집어라

2. 시복 nlogn
'''

s = input() + ' '
result = []
stack = []
tagFlag = False

for ele in s:
    # 태그이면 그냥 더함
    if(tagFlag == False):
        if(ele == '<'):
            # <만나면 기존 것은 뒤집어서 더한다.
            while(stack):
                result.append(stack.pop())
            
            tagFlag = True # 태그를 찾는 다는 얘기임
            stack.append(ele)
        elif(ele != ' '):
            if(ele.isalpha() or ele.isdigit()):
                stack.append(ele)
        else: # 공백이면
            while(stack):
                result.append(stack.pop())
            result.append(' ')
    
    # 태그를 시작하는 건 아니고 태그 찾는 순간일 때    
    elif(tagFlag == True):
        if(ele == '>'):
            stack.append(ele)
            
            while(stack):
                result.append(stack.pop(0)) # 안 뒤집고 더함
            tagFlag = False
        else:
            stack.append(ele)
            
# 3) 알파벳 소문자로 시작하거나 숫자로 시작하면 공백이나 <나올 때까지 단어임

# 4) 태그를 찾는 순간인지 단어를 찾는 순간인지 구분을 해서
# 태그였으면 그냥 더하고 단어였으면 역순으로 더하자

print("".join(result))