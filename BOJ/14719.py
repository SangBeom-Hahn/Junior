'''
세계 : 바닥이 막혀있음, 비가 오면 블럭 사이에 고임

ex) 

ㅡㅡㅡㅡ
ㅁ  ㅁㅁ
ㅁ    ㅁ
ㅁ    ㅁ
      ㅁ

ㅡㅡㅡㅡ 3 0 1 4 -> 2 -1 0 3행 까지 있다.
3 0 1 4 0행
3 0 0 4 1행
3 0 0 4 2행
0 0 0 4 3행

행      행보다 작은열
0       1
1       1, 2
2       1, 2
3       0, 1, 2 -> 0열이나 w-1열이 포함되면 안됨

      
ㅡㅡㅡㅡㅡㅡㅡㅡ 3 1 2 3 4 1 1 2 -> 2 0 1 2 3 0 0 1
ㅁㅁㅁㅁㅁㅁㅁㅁ 
ㅁ  ㅁㅁㅁ    ㅁ
ㅁ    ㅁㅁ    
        ㅁ       
        
행      행보다 작은열        
0       x
1       1, 5, 6
2       1, 2, 5, 6, 7
3       0 1 2 3 5 6 7 -> 0열부터 연속되는 열 다 뺌, 7열부터 연속되는 열 다 뺌

ㅡㅡㅡㅡㅡ
      ㅁ
      ㅁ    
      
1. 모경수(prt, n=1)
ok 1) H행 번 반복함
ok 2) 입력 값에 싹다 -1함
3) 해당 행보다 작은 열 구함
    1] 0열이 포함되어 있다면 0열 부터 연속되는 열 다 뺌
    2] W-1열이 포함되어 있다면 7열부터 연속되는 열 다 뺌
    3] 남은 개수만큼 결과에 더함

* H, W : 행, 열
왼쪽부터 차례대로 블럭의 높이
출 : 고이는 빗물의 총량 (전혀 안고이면 0)

2. nlong
'''

h, w = map(int, input().split())
heights = list(map(int, input().split()))
heights = list(map(lambda x: x-1, heights))

# print(heights)
result = 0

for x in range(h):
    small_col = []
    for y in range(w):
        # print(heights[y], x)
        if(heights[y] < x):
            small_col.append(y)
    print(small_col)
    leng = len(small_col)
    zero_serize_cnt = 0
    w_serize_cnt = 0
    all_flag = False
    
    # 1] 0열이 포함되어 있다면 0열 부터 연속되는 열 개수 셈
    if(0 in small_col):
        zero_serize_cnt = 1
        for i in range(leng-1):
            if(small_col[i] + 1 == small_col[i+1]):
                zero_serize_cnt += 1
            else:
                break
        else:
            all_flag = True
            
        
        # 0 1 2 3 5 6 7
    if(w-1 in small_col):
        w_serize_cnt = 1
        for i in range(leng-1, 0, -1):
            if(small_col[i] - 1 == small_col[i-1]):
                w_serize_cnt += 1
            else:
                break
    
    if(all_flag == True):
        w_serize_cnt = 0
            
    print(f"zero_serize_cnt = {zero_serize_cnt}")
    print(f"w_serize_cnt = {w_serize_cnt}")
    
    
    result += (leng - zero_serize_cnt - w_serize_cnt)
print(result)