'''
모든 자리수가 같지 않은 수의 각 자리의 숫자를 재배열해서 만들 수 있는 가장 큰수와 가장 작은 수의 차이를 계산해서 반복한다.

ex) 2008
최대    최소
8200    28 = 8172
8721    1278 = 7443

ex) 0001
최대    최소
1000    0001 = 999 -> 결과가 4자리가 안될수도 있으니 결과 앞에 0채우기 해야겠다.
9990    0999 = 


1. 모경수(prt, n=1)
0) 이 과정을 반복한다.
1) 입력을 배열에 넣고
    1] 최대 : 내림차순
    2] 최소 : 오름차순
2) 둘의 차이를 구해서 결과를 구함
    0] 차이를 구할 때마다 횟수 ++
    1] 결과가 6174면 끝
    2] 아니라면 앞에 0을 채우고, 입력에 대입



* t : 테케수
네자리수

출 : 몇 단계만에 6174가 되는지 출력하라.

2. n^3
'''

t = int(input())
for _ in range(t):
    # 입력 값
    value = input()
    result = 0
    su = 1
    
    while(True):
    # while(su != 10):
        if(value == "6174"):
            print(result)
            break
        
        # 입력에 0 채우기
        value = value.zfill(4)
        # print("입력", value, len(value))
        
        # 1) 입력을 배열에 넣고
        #     1] 최대 : 내림차순
        #     2] 최소 : 오름차순
        
        max_v = list(value)
        min_v = list(value)
        
        max_v.sort(reverse=True)
        min_v.sort()
        
        # print(max_v, min_v)
        # 2) 둘의 차이를 구해서 결과를 구함
        #     0] 차이를 구할 때마다 횟수 ++
        #     1] 결과가 6174면 끝
        #     2] 아니라면 앞에 0을 채우고, 입력에 대입
        max_int_v = int("".join(max_v))
        min_int_v = int("".join(min_v))
        
        result += 1
        semi_result = max_int_v - min_int_v
        value = str(semi_result)
        
        su += 1