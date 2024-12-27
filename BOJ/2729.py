'''
이진수가 주어졌을 때 그 합을 구하라

ex) 
1001101
  10010
1011111
  
1011111

1001001 
  11001
1100010

1000111 
1010110

10011101


* 모경수(prt, n=1)
1) 두 이진수의 자리를 맞춰야 함
2) 각 자리수 합을 더할 높임수가 필요함 (시작은 그 수를 0으로 시작함)
3) 처음부터 3자리씩 더함
4) 합 결과에 따라서 출력할 것, 높임수에 넣을 것을 나눠야 함
    0] 2로 나눈 몫 = 높임수, 나머지 = 출력
    1] 10 = 1=높임수=몫, 0=나머지
    2] 1 = 0높임수=몫, 1출력=나머지
    3] 0 = 0높임수=몫, 0출력=나머지
    4] 11 = 1높임수=몫, 1출력=나머지
    
5) 마지막까지 훑고, 높임수가 1이면 그것 도 출력, 0이면 끝
    

    

* t:테케수
이진수 숫자 2개
출 : 이진수의 합(앞에 불필요한 0이 붙으면 안 됨)
01 이렇게 끝나면 1, 0+0 = 0이면 0은 출력하겠지 = 한번 10진수로 바꾸고 출력해야할듯

2.  n^3
'''

# 두 이진수의 자리를 맞춰야 함
t = int(input())
for _ in range(t):
    up, down = input().split()
    up_l = len(up)
    do_l = len(down)
    result = []

    leng = max(up_l, do_l)
    up = up.zfill(leng)
    down = down.zfill(leng)
    height_su = 0


    for i in range(leng-1, -1, -1):
        hab = int(up[i]) + int(down[i]) + height_su
        result.append(str(hab%2))
        height_su = hab // 2
        
    if(height_su == 1):
        result.append(str(1))
    else:
        pass

    result.reverse()
    print(int(''.join(result)))