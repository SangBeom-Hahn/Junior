'''
길이 L미터의 롤 케이크, N명에게 나눠 줄 거다.
1미터씩 잘라서 1 ~ L 번 조각
방청객 1 ~ N번

나누기 :
1] 각 방청객은 p번 ~ k번을 쓰고 그 번호에 해당하는 케이크에 방청객 번호를 씀
2] 이미 번호가 적혀있으면 못 적음

ex) 
ㅁㅁㅁㅁㅁㅁㅁㅁㅁㅁ

1번 : 2 ~ 4
ㅁ111ㅁㅁㅁㅁㅁㅁ

2번 : 7 ~ 8
ㅁ111ㅁㅁ22ㅁㅁ

3번 : 6 ~ 9
ㅁ111ㅁ3223ㅁ

1. 모경수 (prt, n=1)
ok 1) 1 ~ n번 사람까지 순회해서 p, k에 해당하는 자리에 visit 처리
ok 2) 최초 visit 배열은 False, 번호를 쓰면 T
ok 3) 1~n 번호를 쓰면 각 갯수 cnt
ok 4) p, k를 다 보면 
    1] 그 갯수를 배열의 인덱스를 그 사람 번호로 하여 그 인덱스에 갯수 저장
    2] 최대값 갱신
5) 맨 마지막에 배열 순회하면서 최대값인 사람 번호 출력
6) 기대값은 k-p+1이 가장 큰 사람


* L : 롤 케익 길이
n : 방청객 수
n개의 p, k

출 : 가장 많은 조각을 받기를 기애하는 번호, 실제로 가장 많이 받은 번호
그런 번호가 겹치면 가장 번호가 작은 사람

2. n^2
'''

l = int(input())
n = int(input())

visit = [False] * (l+1)
max_cnt = 0 # 최대값 최초는 가장 작은 값으로 해야함.
cnt_arr = [0] * (n+1)

respect = 0
res_num = 0

# 1) 1 ~ n번 사람까지 순회해서 p, k에 해당하는 자리에 visit 처리
for num in range(n):
    p, k = map(int, input().split())
    
    if(respect < k-p+1):
        respect = k-p+1
        res_num = num+1
    
    # 각 갯수
    cnt = 0
    for i in range(p, k+1):
        if(not visit[i]):
            cnt += 1
            visit[i] = True
        
    # print("HI", cnt)
    cnt_arr[num+1] = cnt
    if(max_cnt < cnt):
        max_cnt = cnt

# print(max_cnt, cnt_arr, res_num)
            
# 5) 맨 마지막에 배열 순회하면서 최대값인 사람 번호 출력            

print(res_num)
for idx in range(1, n+1):
    if(cnt_arr[idx] == max_cnt):
        print(idx)
        break