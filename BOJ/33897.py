'''
진행
1] 수열의 첫 원소부터 시작
2] 현재 원소를 베고 다음 원소로 이동
3] 현재 <= 다음원소 : 현재 사용중인 벽력일섬 이어서 사용
4] > : 다음원소부터 새로운 벽력일섬 사용
5] 마지막 원소를 베면 : 벽력일섬 자동 종료

ex) 6 7 8 9 3 4 5 1 2

6 7 8 9
3 4 5
1 2


1. 모경수(prt, n=1)
1) 순회 (현재가 더 크면 결과 갱신을 하므로 맨 뒤에 -1 추가)
2) 전체 횟수 1으로 시작
2) 새로운 벽력일섬 시작할때마다 각각 베어낸 원소의 개수 1로 시작
2) 현재, 현재+1 원소 비교
      1] <= : 각각 베어낸 원소의 개수 + 1
      2] > : 
            각각 베어낸 원소의 개수 = 1
            각각 베어낸 최대 개수 갱신

3) 고민
1] 전체 횟수 시작 값
2] 전체 횟수 ++ 언제할지


* n : 수열의 길이
수열
출 : 사용 횟수, 한번의 벽력일섬 중 베어낸 원소의 개수 중 최댓값


2. nlogn
'''

n = int(input())
arr = list(map(int, input().split()))
arr.append(-1)

total = 0 # 전체 횟수
each_cnt = 1
max_cnt = 0

for i in range(n):
      print(arr[i], each_cnt, max_cnt, total)
      if(arr[i] <= arr[i+1]):
            each_cnt += 1
      else:
            if(max_cnt < each_cnt):
                  max_cnt = each_cnt
            
            each_cnt = 1
            total += 1
            
print(total, max_cnt)            