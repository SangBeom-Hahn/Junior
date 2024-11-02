'''
k개의 글자를 가르친다 = k개의 글자로만 이루어진 단어만 읽을 수 있음
남극어 = 시작 anta, 끝 tica

1. 모경수(prt, n=1)
1) a, n, t, i, c는 무조건 필요함 k가 4보다 작거나 같으면 0리턴
2) k가 5보다 크거가 같으면
    1] 가르칠 글자 = [a, n, t, i, c] 포함해야함
    2] 가르칠 글자를 [a, n, t, i, c]로 시작해서 k개가 될때까지 계속 추가함
    3] 모든 단어를 순회해서 가지고 있는 글자를 구하고 [a, n, t, i, c] 빼고
    단어들이 가지고 있는 글자를 하나씩 가르칠 글자에 추가해서 길이가 k가 되었을때
    4] 현재 가르칠 글자들로 가르칠 수 있는 단어의 개수를 구함 -> 최대 단어의 개수 갱신
3) 백으로 탐색(start)

* n, k : 단어의 개수, k개의 글자(0 ~ 26)
남극단어 n개 (길이가 8~15)
출 : k개의 글자를 가르칠때, 학생들이 읽을 수 있는 단어 개수의 최대값

2. n^3
'''
import sys
input = sys.stdin.readline

max_cnt = 0
def back(teach_digit, start):
    global max_cnt
    
    if(len(teach_digit) == k):
        
        t = set(teach_digit)
        cnt = 0
        for word in words:
            for digit in word:
                if(digit not in t):
                    break
            else: # 속하면
                cnt += 1
        if(max_cnt < cnt):
            max_cnt = cnt
            
        return

    for i in range(start, len(words_have_digit)):
        teach_digit.append(words_have_digit[i])
        back(teach_digit, i+1)
        teach_digit.pop()

n, k = map(int, input().split())
words = []
words_have_digit = []
teach_digit = ["a", 'n', 't', 'i', 'c']
for _ in range(n):
    ele = input().strip()
    words.append(ele)

    for digit in ele:
        if(digit not in teach_digit and digit not in words_have_digit):
            words_have_digit.append(digit)

# print(words_have_digit)    

if(len(words_have_digit) + 5 < k):
    k = len(words_have_digit) + 5
    
if(k <= 4):
    print(0)
else:
    
    
    back(teach_digit, 0)
    print(max_cnt)