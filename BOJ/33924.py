

'''
8개의 밥 그릇 중 하나에 햄버거
처음 위치는 안다.
밥그릇 4행 2열

요술
1] a : 1, 2행 과 3, 4행 위치 switch
2] b : x자 교환
3] c : 이상한 교환
4] d : 시계방향 회전

1. 모경수(prt, n=1)
ok-1) 처음위치는 12 34 56 78로 되어있음
ok0) 처음 공을 숨긴 위치의 밥그릇 번호를 기억함.
ok1) a : 1행과 3행, 2행과 4행을 스위치함. 열은 동일
ok2) b : 
행    열    행    열
0     0     1     1
0     1     1     0

2     0     3     1
3     0     2     1

3) c : 
행    열    행    열
0     0     3     1
0     1     3     0
1     0     2     1
2     0     1     1

ok4) : 2차원을 1차원으로 만들어서 회전하고 2차원으로 만들기
      1] 0, 0에서 시작
      2] 가로로 증가, 가로가 1이되면 끝
      3] 세로로 증가, 세로가 3이되면 끝
      4] 가로 감소, 가로가 0이 되면 끝
      5] 세로감소, 가로가 1이되면 끝
      
      6] 인덱스 7을 보관하고, 인덱스 6 ~ 0까지 1개 증가시키고, 인덱스 0에 보관한거 넣기
      
      7] 1차원을 2차원으로
            1] 1차원은 인덱스 0부터 시작하여 계속 1씩 증가
            2] 2차원은 인덱스 0, 0 시작
            3] 위와 동일

12
34
56
78

1246 8753

31246 875



* n, m : 처음 숨긴 위치
k : 기술 사용 횟수
s : 기술

출 : 행, 열

2. n^2
'''

n, m = map(int, input().split())
k = int(input())
s = input()

# -1) 처음위치는 12 34 56 78로 되어있음
# 0) 처음 공을 숨긴 위치의 밥그릇 번호를 기억함.
# 1) a : 1행과 3행, 2행과 4행을 스위치함. 열은 동일

arr = [
      [1, 2],
      [3, 4],
      [5, 6],
      [7, 8]
]

num = arr[n-1][m-1]

for ele in s:
      if(ele == 'A'):
      # a 
            arr[0][0], arr[2][0] = arr[2][0], arr[0][0]
            arr[1][0], arr[3][0] = arr[3][0], arr[1][0]
            arr[0][1], arr[2][1] = arr[2][1], arr[0][1]
            arr[1][1], arr[3][1] = arr[3][1], arr[1][1]

      # b
      # 행    열    행    열
      # 0     0     1     1
      # 0     1     1     0

      # 2     0     3     1
      # 3     0     2     1
      elif(ele == 'B'):
            arr[0][0], arr[1][1] = arr[1][1], arr[0][0]
            arr[0][1], arr[1][0] = arr[1][0], arr[0][1]
            arr[2][0], arr[3][1] = arr[3][1], arr[2][0]
            arr[3][0], arr[2][1] = arr[2][1], arr[3][0]

      # 행    열    행    열
      # 0     0     3     1
      # 0     1     3     0
      # 1     0     2     1
      # 2     0     1     1
      elif(ele == 'C'):
            arr[0][0], arr[3][1] = arr[3][1], arr[0][0]
            arr[0][1], arr[3][0] = arr[3][0], arr[0][1]
            arr[1][0], arr[2][1] = arr[2][1], arr[1][0]
            arr[2][0], arr[1][1] = arr[1][1], arr[2][0]

      # 4) : 2차원을 1차원으로 만들어서 회전하고 2차원으로 만들기
      #       1] 0, 0에서 시작
                  # 1] garo_cnt : 가로로 2차원 배열 요소를 추가할 횟수 변수 / 최초에 2
                  # 2] for문을 cnt만큼 함
                  # 3] for문동안 1차원 배열에 추가함.
                  # 4] for문이 끝나면 cnt -= 1
                  
                  # 5] sero_cnt : 최초에 3
                  # 6] for문이 끝나면 cnt -= 1
                  # 7] garo_cnt가 0이 되면 끝

      # 2차원을 1차원으로 만들기
      else:
            x = 0
            y = -1

            garo_cnt = 2
            sero_cnt = 3
            semi_arr = []
            buho = 1

            while(garo_cnt != 0):
                  for _ in range(garo_cnt):
                        y += buho
                        semi_arr.append(arr[x][y])
                        
                  garo_cnt -= 1
                  
                  for _ in range(sero_cnt):
                        x += buho
                        semi_arr.append(arr[x][y])
                  sero_cnt -= 1
                                          
                  buho *= -1
            
            #       6] 인덱스 7을 보관하고, 인덱스 6 ~ 0까지 1개 증가시키고, 인덱스 0에 보관한거 넣기

            last_num = semi_arr[7]
            for i in range(6, -1, -1):
                  semi_arr[i+1] = semi_arr[i]

            semi_arr[0] = last_num

            #print("1차원으로 만들기", semi_arr)
                  
            #       7] 1차원을 2차원으로
            #             1] 1차원은 인덱스 0부터 시작하여 계속 1씩 증가
            #             2] 2차원은 인덱스 0, 0 시작
            #             3] 위와 동일      

            x = 0
            y = -1

            semi_idx = 0
            garo_cnt = 2
            sero_cnt = 3
            buho = 1

            while(garo_cnt != 0):
                  for _ in range(garo_cnt):
                        y += buho
                        arr[x][y] = semi_arr[semi_idx]
                        semi_idx += 1
                        
                  garo_cnt -= 1
                  
                  for _ in range(sero_cnt):
                        x += buho
                        semi_arr.append(arr[x][y])
                        arr[x][y] = semi_arr[semi_idx]
                        semi_idx += 1
                  sero_cnt -= 1
                        
                  
                  buho *= -1

            #print("2차원으로 만들기")
            #print(*arr, sep = '\n')

f = False
# 5) 이동 완료 후 원하는 밥그릇의 위치를 찾음
for x_idx in range(4):
      for j in range(2):
            if(arr[x_idx][j] == num):
                  print(x_idx+1, j+1)
                  f = True
                  break
      
      if(f == True):
            break