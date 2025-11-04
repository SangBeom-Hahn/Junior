'''
n명의 국회의원, m명의 주민
당선 : 다른 모든 사람의 득표수보다 많을 때
다솜이 : 기호 1번

ex) 
1번   2     3
5표   7     7

1     2     3     4     5
5     10    7     3     8

6     9     7     3     8
7     8     7     3     8
8     7     7     3     8
9     7     7     3     7



1. 모경수(prt, n=1)
1) 최대 값이 기호 1번이 되도록 다른거에서 -1하고 1번에 +1을 한다.
2) 누구꺼를 까지? 가장 큰 녀석을 까면 되나?
      1] 1번빼고 나머지를 모음, 힙큐에 넣음
      2] 최대힙으로 만들어서 꺼냄
      3] 1번 <= 최대값 
            1] 1번에 더하고 최대값 -1해서 힙에 다시 넣음
            2] 1번이 더 크면 끝

*) n=1이면 0출력


* n : 후보의 수
1~n명의 후보의 찍힌 수
출 : 매수해야 하는 사람의 최솟값

2. n^3

'''

import heapq

n = int(input())
chooses = [-int(input()) for _ in range(n)]

if(n == 1):
      print(0)
else:
      one = -chooses[0]
      chooses = chooses[1:]

      heapq.heapify(chooses)

      print(chooses)

      cnt = 0
      while(True):
            print(one, chooses)
            max_value = -heapq.heappop(chooses)
            
            if(one > max_value):
                  print(cnt)
                  break
            
            one += 1
            max_value -= 1
            heapq.heappush(chooses, -max_value)
            cnt += 1