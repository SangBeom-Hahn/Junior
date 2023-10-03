'''

1. 모든 경우의 수
1) 끝시간이 빠른 순서대로 추가하기

* n : 회의의 수
회의의 상태(시작, 끝)
출력 : 회의의 최대 개수
'''

n = int(input())
meets = []
for _ in range(n):
    meets.append(list(map(int, input().split())))
    
meets.sort(key = lambda x: (x[1], x[0]))

# print(meets)
result = []

end = 0
for ele in meets:
    if(ele[0] >= end):
        result.append(ele)
        end = ele[1]
        
# print(result)        
print(len(result))