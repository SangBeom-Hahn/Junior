'''
ac는 정수 배열에 연산을 하는 언어다. 
함수 R : 배열에 있는 수의 순서를 뒤집는 함수
D : 첫번쨰 수를 버리는 함수, 배열이 비어있는 데 D를 하면 에러

Rdd : 뒤집고 처음 두수를 버리는 함수로 함수는 조합해서 한번에 사용 가능

ex)
함수    배열        r의 개수(홀, 짝)
rdd     1 2 3 4

r       4 3 2 1
d       3 2 1
d       2 1

함수    배열            r의 개수(홀, 짝)
rdd     1 2 3 4     0 = 짝일때 d가 나오면 왼팝
r                   1
d       1 2 3            1 = 홀일때 d가 나오면 뒤집고 빼는 거잖아? 그래서 오른팝
d       1 2            1 = 홀일때 d가 나오면 뒤집고 빼는 거잖아? 그래서 오른팝

r의 개수가 홀이면 끝나고 딱한번 리버스

rrd     1 1 2 3 5 8     0
r                       1 r이 나오면 아무것도 안하고 r의 개수 증가
r                       2
d                       2 = 짝일때 d가 나오면 왼팝

ddr      1 2 3 4        0
d        2 3 4          0 = 짝일때 d가 나오면 왼팝
d        3 4            0 = 짝일때 d가 나오면 왼팝
r                       1

r의 개수가 홀이면 끝나고 딱한번 리버스



1. 모경수
1) r = 뒤집기
이게 p의 길이도 10만이라서 뒤집기를 하면 n^2이 될거 같아 따라서 뒤집는 걸 채크해서 왼쪽에서 빼고 오른쪽에서 빼자

2) r이 나오면 그냥 개수를 셈
3) r이 홀일때 d가 나오면 그래서 오른팝
4) r이 짝일때 d가 나오면 왼팝
5) r의 개수가 홀이면 끝나고 딱 한번 리버스
6) 빈거에 d나오면 err 출력 끝

*  t : 테케수
p : 수행할 함수 조합
n : 배열에 있는 수의 개수
배열에 있는 정수
출 : 정수 배열에 함수를 수행한 결과, 에러가 있으면 error

2. 시복 : nlogn
'''
from collections import deque
t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    nums = input()
    leng = len(nums)
    nums = nums[1:leng-1].split(',')
    nums = deque(nums)
    # print(nums)

    # 2) r이 나오면 그냥 개수를 셈
    # 3) r이 홀일때 d가 나오면 그래서 오른팝
    # 4) r이 짝일때 d가 나오면 왼팝
    # 5) r의 개수가 홀이면 끝나고 딱 한번 리버스
    # 6) 빈거에 d나오면 err 출력 끝
    # 7) 처음부터 비어있는데 D가 나오면 error, 처음부터 비어있는데 r나오면 그냥 [] 출력
    # 첫번째꺼를 꺼내서 ''면 flag를 t로 하고 for문 돌려서 ele가 d이면 error
    # ''가 아니면 다시 appendleft함
    
    flag = False
    first = nums.popleft()
    if(first == ''):
        flag = True
    else:
        nums.appendleft(first)
    
    r_cnt = 0
    for ele in p:
        if(flag == True and ele == 'D'):
            
            print("error")
            break

        if(ele == 'R'):
            r_cnt += 1
        elif(ele == 'D'):
            if(not nums):
                print("error")
                break
            else:
                if(r_cnt % 2 == 1):
                    nums.pop()
                else:
                    nums.popleft()

    else:
        if(r_cnt % 2 == 1):
            nums = list(reversed(nums))
        
        print('[' + ','.join(list(nums)) + ']')