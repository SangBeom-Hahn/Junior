'''
수열을 어떤 규칙에 의해 여러 가지 항으로 나누었을 때, 
각각의 항으로 이루어진 수열을 군수열이라고 한다.

규칙 : 
1. n번째 군에느 1~n까지의 자연수가 크기 순서대로 있음
2. 수열의 k번쨰 항은 군 상관없이 맨 앞부터 셈

ex) 4번째 항은 1임

군      군의 길이       항의 번째       항      군의 길이만큼 돌기위한 개수(goon_tmp)
1       1               1               1       1
                                                0
12      2               2               1       2
                        3               2       1
                                                0


1       1
12      2
123     3
1234    4

1. 모경수(prt, n=1)
1) 군의 길이가 1부터 시작, goon_tmp의 시작은 군의 길이, 항은 1로 시작
2) 처음에 항의 번째와 k 비교 후 안 똑같으면, goon_tmp - 1, 항+1
3) goon_tmp가 0이 되면 군의 길이 + 1하고 goon_tmp에 재대입, 항에 1 대입
3) 항의 번째 1부터 시작, 매 반복마다 1씩 증가 k랑 같아지면?? 그때의 항이 답


* k : k번째 항
출 : 수열 s에서 k번쨰 항의 수를 구하라
2. 시복 n
'''
k = int(input())
goon_leng = 1
goon_tmp = goon_leng
hang = 1
hang_cnt = 1
su = 1

# while(su != 5):
while(True):
    if(k == hang_cnt):
        print(hang)
        break
    
    su += 1
    goon_tmp -= 1
    hang += 1
    hang_cnt += 1
    
    if(goon_tmp == 0):
        goon_leng += 1
        goon_tmp = goon_leng
        hang = 1
