'''
배열의 앞엔 짝수, 뒤엔 홀수가 위치하도록 배열의 요소 위치를 이동시킬 것이다.

ex) 8 1 4 7 = 1번 이동
1 2 2 2 2 8 = 1번
1 2 2 1 2 8 = 2

홀수 인덱스 = 0 2 4 6 8 / 짝 idx = 7 5 3 1 / 가장 뒤에 있는 짝수 인덱스 = 7
1 2 3 4 5 6 7 8 9 / 

홀수 인덱스 = 2 4 6 8 / 짝 idx = 5 3 1 / 가장 뒤에 있는 짝수 인덱스 = 5
8 2 3 4 5 6 7 1 9

홀수 인덱스 = 4 6 8 / 짝 idx = 3 1 / 가장 뒤에 있는 짝수 인덱스 = 3
8 2 6 4 5 3 7 1 9 = 2번

1. 모경수(prt, n=1)
-> while로 실제 swap 하는 버전
1) 홀수 인덱스를 전부 다 구해 0 2 4 6 8
2) 짝수 인덱스를 전부 다 구해 7 5 3 1
2) 가장 뒤에 있는 짝수 인덱스를 구해 -> 현재 짝수 인덱스의 idx 0 / 값 = 7
3) 홀에 가장 앞에 있는 걸 짝의 가장 뒤에 있는 거랑 바꿈
4) 현재 바꾸려는 홀 수 인덱스가 짝수 인덱스보다 크면 끝
5) 길이 나가도 끝


-> 수식이 있는 버전


* 배열
출 : 모든 짝수가 홀수보다 앞에 있는 배열을 만드는데 필요한 최소 이동 횟수

2. nlogn
'''
# [8, 1, 4, 7]
# 1 2 2 2 2 8 = 1번
# 1 2 2 1 2 8 = 2

arr = [1, 2, 2, 1, 2, 8]
odd = []
jjack = []

for i in range(len(arr)):
    if(arr[i] % 2 == 0):
        jjack.append(i)
    else:
        odd.append(i)
        
jjack.reverse()        
# 2) 가장 뒤에 있는 짝수 인덱스를 구해 -> 현재 짝수 인덱스의 idx 0 / 값 = 7
# 3) 홀에 가장 앞에 있는 걸 짝의 가장 뒤에 있는 거랑 바꿈

odd_point = 0
jjack_point = 0
cnt = 0
odd_leng = len(odd)
jjack_leng = len(jjack)

while(odd[odd_point] < jjack[jjack_point]):
    cnt += 1

    odd_point += 1
    jjack_point += 1
    
    if(odd_point == odd_leng or jjack_leng == jjack_point):
        break
    
print(cnt)