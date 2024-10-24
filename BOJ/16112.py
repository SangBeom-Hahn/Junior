'''
시그널
1) .과 #로
2) 항상 5의 배수
3) 숫자와 숫자 사이에는 1열 이상의 공백 = (열의 성분이 모두 .)
4) 숫자는 #을 검은색, .을 흰색으로 표시했을때 나타남

###..#..
#.#..#..
###..#..
#.#..#..
###..#..



1. 모경수(prt, n=1)
1) 5개로 쪼갬 = 무조건 5행, 최대 2만 열
    1] 열은 규칙이 똑같음 -> 0은 무조건 첫 열이 다 #임
    (아닌가 일단 그냥 해봄) 2] 행은 다를 수 있음 0의 윗 획이 #이 쭉 늘어설 수 있음 
    = 한 글자가 차지하는 가로 구해야함, 공백 고려해서

2) .이 0, 1, 2행까지 나오면 공백으로 봐서 다음 열 봄
    1] 숫자와 숫자 사이에는 1열 이상의 공백이 있다.
3) 0 = 앞 열이 전부 # 뒤 열 0행, 4행이 #, 2행이 .
4) 1 = 앞 열이 전부 #, 하나 + 1 열에 0행, 4행이 .
5) 2 = 앞 열에 0, 2, 3, 4행 #, 1행 .
6) 3 = 앞 열에 0, 2, 4행 #
7) 4 = 앞에 0, 1, 2행 #, 3, 4열 .
8) 5 = 앞에 0, 1, 2, 4행 #, 3행 ., 뒤에 열에 1행 .
6 = 앞에 열이 전부 #, 뒤 열 1행이 .
7 = 앞에 열에 0행만 #
8 = 뒤 열 0행, 2행, 4행이 #
9 = 앞에 0, 1, 2, 4행 #, 3행 ., 뒤에 열에 1행 #

* n : 시그널 길이
출 : 숫자 출력


'''

# 5개로 쪼갬 = 무조건 5행, 최대 2만 열
n = int(input())
inp = list(input())
signal = []
row = 5
col = n // 5
visit = [False] * col

roww = []
for i in range(n):
    roww.append(inp[i])
    
    # print(i, i+1 % col)
    if((i+1) % col == 0):
        signal.append(roww)
        roww = []
        
# print(*signal, sep = '\n')
        
        
# 2) .이 0, 1, 2행까지 나오면 공백으로 봐서 다음 열 봄
#     1] 숫자와 숫자 사이에는 1열 이상의 공백이 있다.        

# 3) 0 = 앞 열이 전부 # 뒤 열 0행, 4행이 #, 2행이 .
# 4) 1 = 앞 열이 전부 #, 하나 + 1 열에 0행, 4행이 .
# 6 = 앞에 열이 전부 #, 하나+1열에 2행이 #, 하나+2열에 1행이 .
# 8 = 뒤 열 0행, 2행, 4행이 #

result = ""
leng = len(signal[0])
for i in range(leng):
    if(visit[i]):
        continue
    
    if(signal[0][i] == '.' and signal[1][i] == '.' and signal[2][i] == '.'):
        # print("HI")
        visit[i] = True
        continue
    
    if(signal[0][i] == '#' and signal[1][i] == '#' and signal[2][i] == '#' and
       signal[3][i] == '#' and signal[4][i] == '#'):
        
        if(signal[0][i+1] == '#' and signal[4][i+1] == '#' and signal[2][i+1] == '.'):
            result += "0"
            visit[i] = True
            visit[i+1] = True
            visit[i+2] = True
            continue
            
        if(signal[0][i+1] == '.' and signal[4][i+1] == '.'):
            result += "1"
            visit[i] = True
            continue
    
        if(signal[2][i+1] == '#' and signal[1][i+2] == '.'):
            result += "6"
            visit[i] = True
            visit[i+1] = True
            visit[i+2] = True
            continue
        
        if(signal[0][i+1] == '#' and signal[2][i+1] == '#' and signal[4][i+1] == '#'):
            result += "8"
            visit[i] = True
            visit[i+1] = True
            visit[i+2] = True
            continue
# 5) 2 = 앞 열에 0, 2, 3, 4행 #, 1행 .
# 6) 3 = 앞 열에 0, 2, 4행 #
# 7) 4 = 앞에 0, 1, 2행 #, 3, 4열 .
# 8) 5 = 앞에 0, 1, 2, 4행 #, 3행 ., 뒤에 열에 1행 .
# 7 = 앞에 열에 0행만 #
# 9 = 앞에 0, 1, 2, 4행 #, 3행 ., 뒤에 열에 1행 #
    else:
        if(signal[0][i] == "#" and signal[2][i] == "#" and signal[3][i] == "#" 
           and signal[4][i] == "#" and signal[1][i] == "."):
            result += "2"
            visit[i] = True
            visit[i+1] = True
            visit[i+2] = True
            continue
            
        if(signal[0][i] == '#' and signal[2][i] == '#' and signal[4][i] == '#'):
            result += "3"
            visit[i] = True
            visit[i+1] = True
            visit[i+2] = True
            continue
        
        if(signal[0][i] == '#' and signal[1][i] == '#' and signal[2][i] == '#'
           and signal[3][i] == "." and signal[4][i] == "."):
            result += "4"
            visit[i] = True
            visit[i+1] = True
            visit[i+2] = True
            continue
        
        if(signal[0][i] == '#' and signal[1][i] == '#' and signal[2][i] == '#'
           and signal[4][i] == '#' and signal[3][i] == "." and signal[1][i+2] == "."):
            result += "5"
            visit[i] = True
            visit[i+1] = True
            visit[i+2] = True
            continue
        
        # 7 = 앞에 열에 0행만 #
# 9 = 앞에 0, 1, 2, 4행 #, 3행 ., 뒤에 열에 1행 #
        if(signal[0][i] == '#' and signal[1][i] == '.' and signal[2][i] == '.' and
           signal[3][i] == '.' and signal[4][i] == '.'):
            result += "7"
            visit[i] = True
            visit[i+1] = True
            visit[i+2] = True
            continue
        
        if(signal[0][i] == '#' and signal[1][i] == '#' and signal[2][i] == '#'
           and signal[4][i] == '#' and signal[3][i] == "." and signal[1][i+2] == "#"):
            result += "9"
            visit[i] = True
            visit[i+1] = True
            visit[i+2] = True
            continue

print(result)
            