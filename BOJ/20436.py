'''
한글 자음 : 왼손
모음 : 오른손

a에 위치한 손가락이 b로 이동하는데 걸리는 시간 : 택시 거리
키를 누르는데 1의 시간이 걸림
두 손을 동시에 움직일 수 없음.

문자열  타이핑  왼  오  초      최종 초(걸린 초의 총합)
zoac    z       z   o   1
        o       z   o   1
        a       a   o   2
        c       c   0   4

1. 모경수(prt, n=1)
1) 알파벳과 자음, 모음을 매칭
2) 알파벳과 좌표를 매칭
3) 문자열 순회
    1] 자음이면 -> 왼쪽 손으로 타이핑
    2] 모음이면 -> 오른 손으로 타이핑
4) 현재 손가락 위치는 타이핑 칠때마다 갱신
5) 시간은 이동거리 + 누르는 시간 1초

* 왼쪽 검지 손가락, 오른쪽 손가락 처음 위치
문자열
출 : 문자열을 출력하는데 걸리는 시간의 최소값

2. n^2
'''

jaumm_dic = {
    'q' : (0, 0),
    'w' : (0, 1),
    'e' : (0, 2),
    'r' : (0, 3),
    't' : (0, 4),
    
    'a' : (1, 0),
    's' : (1, 1),
    'd' : (1, 2),
    'f' : (1, 3),
    'g' : (1, 4),
    
    'z' : (2, 0),
    'x' : (2, 1),
    'c' : (2, 2),
    'v' : (2, 3)
}

moumm_dic = {
    'y' : (0, 5),
    'u' : (0, 6),
    'i' : (0, 7),
    'o' : (0, 8),
    'p' : (0, 9),
    
    'h' : (1, 5),
    'j' : (1, 6),
    'k' : (1, 7),
    'l' : (1, 8),
    
    'b' : (2, 4),
    'n' : (2, 5),
    'm' : (2, 6)
}

# 3) 문자열 순회
#     1] 자음이면 -> 왼쪽 손으로 타이핑
#     2] 모음이면 -> 오른 손으로 타이핑
# 4) 현재 손가락 위치는 타이핑 칠때마다 갱신
# 5) 시간은 이동거리 + 누르는 시간 1초

left, right = input().split()
left = jaumm_dic[left]
right = moumm_dic[right]    
    
# print(left, right)

str = input()
time = 0
for ele in str:
    if(ele in jaumm_dic):
        time += (
            abs(left[0] - jaumm_dic[ele][0]) + abs(left[1] - jaumm_dic[ele][1])
        )
        left = jaumm_dic[ele]
    else:
        time += (
            abs(right[0] - moumm_dic[ele][0]) + abs(right[1] - moumm_dic[ele][1])
        )
        right = moumm_dic[ele]
        
    time += 1
        
    
print(time)
    # print(left, right)