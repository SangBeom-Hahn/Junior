'''
방금그곡 서비스
1]  제목, 재생 시작 + 끝 시간, 악보
2] 악보 음 = 12가지 #도 포함
3] 각 음은 1분에 1개 재생함 = 음의 총 길이가 재생 시간
4] 반복재생 : 원본길이 < 재생시간
5] 끊김 : 원본길이 > 재생시간
6] 출력 : 조건 일치 음악 여러개/ 재생시간이 제일 긴 순, 먼저 입력된 음악 순 / 없으면 None

라디오
1] 반복재생 [노래][노래] : 끝과 앞이 이어진 걸수도 있음
2] 끊김 [노] : 끊길수도 있음

ex) 기억 = ABCDEFG
노래  재생시간    악보원본길이  반복 OR 끊김                    실제재생곡               기억이 실제재생곡에 포함?
1번      14      7           재생시간 > 원본길이 = 반복        CDEFGABCDEFGAB          0
2번      5       6           <   = 끊김                        ABCDE                   X

# 실제 재생곡
1) 몫, 나머지로 악보원복 * 몫 + 악보원몬[:나머지]
2) 악보원본[:재생시간]


1. 모경수(prt, n=1)
ok 0) 기억음을 #까지 포함해서 list로 변환
    1] 모든 걸 다 나누고
    2] 순회하면서 뒤에가 #이면 앞에꺼에 붙임
    
1) 방금그곡 수록곡 순회
    0] 악보 원본을 # 까지 포함해서 list로 변환
    1] 재생시간, 악보원본길이 구함
        1] #은 빼고 구해야함
    2] 재생시간 > 악보원본길이 -> 실제재생곡 구함
        0] 실제 재생곡 #까지 포함해서 list로 변환
        1] 기억음을 실제재생곡과 비교
    3] 재생시간 < 악보원본길이 -> 실제재생곡 구함
        1] 기억음을 실제재생곡과 비교
    
    4] 포함시 (제목, 재생시간, 입력 순서) APPEND

* m : 기억 멜로디
music : 방송된 곡 정보 (시작시간, 끝시간, 제목, 악보)

출력 : 조건 일치 음악 여러개/ 재생시간이 제일 긴 순, 먼저 입력된 음악 순 / 없으면 None

2. nlogn
'''

def convert_list(m):
    real_m = []
    for i in range(len(m)):
        if(i+1 == len(m) and m[i] != '#'):
            real_m.append(m[i])
            break
        
        if(m[i] != '#'):
            if(m[i+1] == '#'):
                real_m.append(m[i] + m[i+1])
                continue
            else:
                real_m.append(m[i])
                continue
            
        if(m[i] == '#'):
            continue
    return real_m

def check(real_m, real_play_m):
    # 1] 기억음을 실제재생곡과 비교
    pt_idx = 0
    real_idx = 0
    while(pt_idx != len(real_m) and real_idx != len(real_play_m)):
        if(real_m[pt_idx] == real_play_m[real_idx]):
            pt_idx += 1
            real_idx += 1
        else:
            pt_idx = 0
            real_idx = real_idx - pt_idx + 1

    # 포함
    if(pt_idx == len(real_m)):
        return "포함"
    else:
        return "비포함"

def solution(m, musicinfos):
    m = list(m)
    # 기억한 음
    real_m = convert_list(m)
    
    print("기억한 음", real_m)
    
    
# 1) 방금그곡 수록곡 순회
#     ok 0] 악보 원본을 # 까지 포함해서 list로 변환
#     ok 1] 재생시간, 악보원본길이 구함
#         1] #은 빼고 구해야함

#     ok 2] 재생시간 > 악보원본길이 -> 실제재생곡 구함
            # 1) 몫, 나머지로 악보원복 * 몫 + 악보원몬[:나머지]
            # 2) 악보원본[:재생시간]

#         0] 실제 재생곡 #까지 포함해서 list로 변환
#         1] 기억음을 실제재생곡과 비교
#     3] 재생시간 <= 악보원본길이 -> 실제재생곡 구함
#         1] 기억음을 실제재생곡과 비교
    
#     4] 포함시 (제목, 재생시간, 입력 순서) APPEND
    ans = []
    num = 0
    for musicinfo in musicinfos:
        num += 1
        start, end, title, save_m = musicinfo.split(',')
        
        # 악보 원본
        save_m = convert_list(save_m)
        
        end_t, end_m = map(int, end.split(':'))
        start_t, start_m = map(int, start.split(':'))
        
        
#         # 재생시간, 악보원본길
        play_time = end_t * 60 + end_m - (start_t * 60 + start_m)
        save_m_leng = len(save_m)
        
        if(play_time > save_m_leng):
            mok = play_time // save_m_leng
            nmg = play_time % save_m_leng
            
#             # 실제 재생 곡
            real_play_m = save_m * mok + save_m[:nmg]
            print("실제 제생 음", real_play_m)
            
        
            # 1] 기억음을 실제재생곡과 비교
            check_result = check(real_m, real_play_m)
            if(check_result == "포함"):
                ans.append([title, play_time, num])
            
        else:
            #     3] 재생시간 <= 악보원본길이 -> 실제재생곡 구함
#         1] 기억음을 실제재생곡과 비교
            real_play_m = save_m[:play_time]
            print("실제 제생 음", real_play_m)
            check_result = check(real_m, real_play_m)
            if(check_result == "포함"):
                ans.append([title, play_time, num])        

    print(save_m in real_play_m)

    print(*ans, sep = '\n')
    # 조건 일치 음악 여러개/ 재생시간이 제일 긴 순, 먼저 입력된 음악 순 / 없으면 None
    if(len(ans) == 0):
        return "(None)"
    else:
        ans.sort(key = lambda x : (-x[1], x[2]))
        return ans[0][0]

















