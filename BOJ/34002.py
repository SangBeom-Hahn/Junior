'''
레벨업
1] 250 레벨을 목표로 한다.
2] 이벤트맵 : 1분마다 A만틈 경험치
심신 : B / 입장권 필요, 30분 동안만 있을 수 있음
사우나 : C / 입장권 필요, 30분 동안만 있을 수 있음

3] 레벨을 1 올리려면 100 경험치가 필요 / 현재 경험치 = 0
4] 100을 초과한 경험치는 레벨업때 이월됨

목표 경험치 = 25000
ex) 10, 20, 30 / 입장권 1, 2개
들어간 곳   경험치      레벨              분
            100        1
사우나       900                          30
사우나       1800                          60
심신        2400                          90
이벤트      22600                         2350 (+ 2260 )

25000 - 2400 = 22600

1. 모경수(prt, n=1)
ok 1) 현재 레벨 * 100이 현재 경험치이다.
2) 분 당 경험치가 가장 큰 경험치의 인덱스를 찾음
      1] 0이면 계속 거기 있음
      2] 1이면 1에 입장권 개수만큼 30분 씩 있고, 여기서 250레벨 안되면 다음으로 큰 인덱스를 찾음
      3] 2이면 2에 입장권 개수만큼 30분 씩 있고, 여기서 250레벨 안되면 다음으로 큰 인덱스를 찾음
      4] 경험치가 큰 순으로 배열에 인덱스를 app하고 그 인덱스를 사용하면 됨.
      
3] 경험치 더하기
      1] 0에서는 현재 경험치에 a를 더하고 분을 ++함
      2] 1에서는 현재 경험치에 b를 더하고 분을 ++함, 이방 분도 따로 세서 30 * 입장권 개수분 뒤에 나가야 함      
      3] 2에서는 현재 경험치에 c를 더하고 분을 ++함, 이방 분도 따로 세서 30 * 입장권 개수분 뒤에 나가야 함

4] 끝내기
      1] 경험치가 25000보다 크거나 같으면 끝, 총 분이 답이다.


* a, b, c 경험치
s, v = 심신 입장거ㅜㄴ, 사우나 입장권 개수
l : 현재 레벨
출 : 레벨 250을 달성하는 소요되는 최단 시간을 분 단위로 

2. n^3
'''

each_map_streagth = list(map(int, input().split()))
s, v = map(int, input().split())
l = int(input())

current_strength = l * 100
max_streagth_soonsu = []

# 몇개를 append 해쓴ㄴ지 세는 변수
append_cnt = 0
visit = [False] * 3
while(False in visit):
      max_idx = 0
      max_streanth = 0
      for i in range(3):
            if(not visit[i] and max_streanth < each_map_streagth[i]):
                  max_streanth = each_map_streagth[i]
                  max_idx = i
           
      max_streagth_soonsu.append(max_idx)
      visit[max_idx] = True

#print("순서", max_streagth_soonsu)

# 경험치가 큰 순으로 배열에 인덱스를 app하고 그 배열을 바라볼 inx를 최초에 0으로 둬서 1, 2로 증가시킴
max_idx = 0

# 3] 경험치 더하기
#       1] 0에서는 현재 경험치에 a를 더하고 분을 ++함
#       2] 1에서는 현재 경험치에 b를 더하고 분을 ++함, 이방 분도 따로 세서 30 * 입장권 개수분 뒤에 나가야 함      
#       3] 2에서는 현재 경험치에 c를 더하고 분을 ++함, 이방 분도 따로 세서 30 * 입장권 개수분 뒤에 나가야 함

su = 0
total_min = 0
each_min = 0
while(True):
# while(su != 100):
      if(current_strength >= 25000):
            print(total_min)
            break

      room_idx = max_streagth_soonsu[max_idx]
      
      if(room_idx == 0):
            current_strength += each_map_streagth[0]
            total_min += 1
      elif(room_idx == 1):
            current_strength += each_map_streagth[1]
            total_min += 1
            each_min += 1
            
            if(each_min == 30 * s):
                  max_idx += 1
                  each_min = 0
      elif(room_idx == 2):
            current_strength += each_map_streagth[2]
            total_min += 1
            each_min += 1
            
            if(each_min == 30 * v):
                  max_idx += 1
                  each_min = 0

      #print(current_strength, total_min)
      su += 1