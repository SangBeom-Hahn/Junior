'''
설정에 {db} 환경변수에 실제 값이 들어가야 한다.
참조 = {db}
치환 = 참조를 실제 값으로 바꿈

db-test = 위에 {db}와 password 벨류 값인 test=123으로 되어있음
참조가 없을 수도 있고 = 참조가 모두 치환된 것임
참조가 아닌 경우에도 벨류에 {, }이 포함될수 있음 = 괄호가 있는데 키에는 없는 경우가 있음
한 벨류에 참조 쌍이 여러개 있을 수 있음

ex) [key1 , {key2}, key2, hi] = [key1 , hi, key2, hi]
문자        스택
{           { = 열갈호면 스택에 넣음
k
e
y
2
}           []팝 = 닫갈호면 뺌 -> 열갈호가 되면 그 이후 문자를 저장하고 닫갈호가 됐을 때 문자를 모아서 키에서 찾음, 키에 없으면 
                                    ""로 치환

ex) [key1, {value]
문자        스택
{           {
v
a
l
u
e -> 올바르지 않은 스택 3가지에 해당하면 원본으로 그냥 둠

ex) key1, {key2} is {key3}, key2, hi, key3, hello

문자        스택
{           {
k
e
y
2
}           [] 팝 = 치환 = 치환하면 결과 문자열을 어딘가에 저장하고 있음
blank
i
s = 열갈호가 나오기 전의 문자도 결과에 저장함
{
k
e
y
3
} = 전체 치환


1. 모경수
1) 배열에서 짝수가 다 키고, 홀수가 다 벨류임
2) 벨류에 갈호 쌍이 맞았을때 내부 문자열을 키에서 찾아서 벨류로 치환함
    0] 열갈호가 나오기 전의 문자도 결과에 저장함
    1] 스택 쌍이 맞을 때
        1] 열갈호면 스택에 넣음, 그 이후 문자를 따로 저장하고
        2] 닫갈호가 됐을 때 문자를 모아서 키에서 찾음
        3] 키에 없으면 ""로 치환
    
    2] 안 맞을 때
        1] 문자열이 다 끝났는데 스택에 {가 남아있으면 { + 저장한 문자열을 벨류에 넣음
        2] 스택이 비었는데 }가 나오면 그냥 결과에 저장
3) 중복 치환
    1] 
    
4] 서로 참조하면 빈배열


* 
출 : 참조가 모두 치환된 설정 mpa을 반환하라 (키를 사전순 정렬)
{{test}} 처럼 중첩 치환도 가능하다.
{}가 있는데 키에 없으면 ""로 치환
서로 참조하는 경우가 하나라도 발견되면 빈배열 반환
중첩 치환하다가도 서로 참조하면 빈배열 반환

2. n^3
'''

# arr = ["db", "testdb:localhost:12345", "password", "test", "db-test", "{db}?test=123"]
# arr = ["key1", "value}"]
# arr = ["key1", "{key2} is {key3}", "key2", "hi", "key3", "hello"]
# arr = ["key2", "{{test}}", "test", "hi", "hi", "hello"]
arr = ['key1', "{key2}", 'key2', "{key1}"]

keys = []
values = []
value_to_key = {}
key_value = {}
for i in range(0, len(arr), 2):
    value = arr[i+1].lstrip("{")
    value = value.rstrip("}")
    key = arr[i]
    value_to_key[value] = key
    key_value[key] = value
print(value_to_key)

for i in range(len(arr)):
    if(i % 2 == 0):
        keys.append(arr[i])
    else:
        values.append(arr[i])
        
for idx, value in enumerate(values):
    stack = []
    semi_result = ""
    chihwan = ""
    open_flag = False
    for digit in value:
        # print(1, semi_result, chihwan)
        # print(stack)
        if(digit == '{'):
            stack.append('{')
            open_flag = True
        
        elif(digit == '}'):
            # 2] 스택이 비었는데 }가 나오면 그냥 결과에 저장
        
            if(len(stack) == 0):
                semi_result = semi_result + "}"
            else:
                # print(3, semi_result, chihwan)
                stack.pop()
            
                open_flag = False
                # 문자를 모아서 키에서 찾음
                for i, ele in enumerate(keys):
                    '''
                    여기서 치환이 ""이 되어서 중첩이 안됨
                    1] 무작정 아직 열괄호가 있으면 치환을 유지하는게 맞나?
                    {{{test}}
                    '''
                    if(ele == chihwan): 
                        # print("hihi", ele, value_to_key[ele])
                        if(ele == key_value[value_to_key[ele]]):
                            print(1, 1, 1, [])
                            exit()
                        
                        if(len(stack) == 0):
                            semi_result = semi_result + values[i]
                            chihwan = ""
                            break
                        else:
                            chihwan = values[i]
                            break
                else:
                    semi_result = semi_result + ""
            
        else:
            if(open_flag == True):
                chihwan += digit
            else:
                semi_result += digit # 열갈호가 나오기 전의 문자도 결과에 저장함
    #  1] 문자열이 다 끝났는데 스택에 {가 남아있으면 { + 저장한 문자열을 벨류에 넣음
    else:
        if(len(stack) != 0):
            values[idx] = "{" + chihwan
        
        else:
            values[idx] = semi_result
        
        # print(2, semi_result, chihwan)
    
    
    
    
    
    
    
    
    
    
    
    
# print(values)
    