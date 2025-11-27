'''
돈세탁 감지 관련 정보 : 주인, 저번달, 이번달 거래내역

감지 작동기준 :
1] 하루를 4시간 단위로 나눴을 때 저번달에 가장 적은 거래수를 기록한 시간대에 거래 발생. 
ex) 저번달 3시에 거래가 젤 적은데, 이번달에 3시에 거래 발생

2] 저번달 거래 총액보다 큰 금액을 1건에 거래함. 

ex) 

지난 달
시  분  src dst 금액
0   30  0   1   500
8   0   0   2   100

지난달 정리
계좌번호    시간 0  1   2   3   4   5   총금액
0           1     0   1   0   0   0     600

현재
시  분  src dst 금액
7   10  1   0   1500 
-> dst인 거래번호 0이 지난달 거래액 회수가 가장 적었던 2번 시간대에 총금액 600보다 큰 1500원을 거래했다.

---

계좌의 주인이 같은 사람이면
0 : catch
1 : olive
3 : olive

최종 결과 dic을 이름을 key로 하면 됨. src가 0이면 0으로 catch 찾고 catch로 최종 결과 찾는다.





설계 :
1) 저번달 거래 총액보다 큰 금액을 저번달에 가장 적은 거래수를 기옥한 시간대에 거래한다.
2) 1번의 거래에서 src, dst 모두 저번달과 비교를 해야한다.


1. 모경수
ok 0) 각 계좌주인마다 저번달 거래의 총액과 가장 적은 거래수를 기록한 시간대를 구해야함.
ok 1) owner를 순회해서 키 : 번호 / value : 사람이름 dic을 만듦
    1] 나중에 src로 owner dic 접근해서 사람이름 찾고 사람이름으로 최종 dic만든다.
1) previous를 순회
    1] 거래 1건에서
    2] src와 dst에 해당하는 계좌번호의 거래 총액을 누적한다. -> 각 인원마다 dic로 키 : 사람이름 / 벨류 : 총액
    3] src와 dst의 가장 적은 거래수를 기록한 시간대 구하기
        1] 각 인원마다 요소 6의 배열을 만들고 0으로 초기화하고 > 속하는 시간대의 배열에 ++
        2] 가장 적은 거래수는 0번 거래한 시간대는 제외해야해서  0이 아닌 것 중에서 최소값에 해당하는 시간대를 구한다.
    4] 시간대는 previous를 전부 순회한 후에 dic에 저장한다.
        1] 키 : 사람이름 / 벨류 : 가장 적은 거래수를 기록한 시간대 번호
2) now를 순회
    1] src
        1] src의 작년 내역을 봐서
        2] 가장 적은 거래수를 기록한 시간대의 거래이고
        3] 저번달 거래 총액 보다 큰 건이면 결과에 ++
    2] dst도 동일



* owners : 계좌의 주인 명 (인덱스 0 = 0번 계좌), 동일한 사람이 여러 개 계좌 가능
previ : 저번달 거래 내역
h, m : 시 분
a : src 계좌의 번호
b : dst 계좌의 번호
c : 거래 금액

now : 이번달

출 : 이번달 거래 내역 중 감지동작 거래가 몇개인지 구하라

2. nlogn

'''

owners = ["c", "a", "d", "e", "b"]
prev = [
    [14, 19, 2, 1, 200],
    [21, 14, 4, 3, 1500],
    [17, 58, 4, 3, 2900],
    [18, 47, 3, 4, 2700],
    [0, 46, 1, 0, 300],
    [12, 57, 0, 1, 2700],
    [7, 48, 2, 4, 1800],
    [9, 20, 0, 1, 2200],
    [8, 41, 3, 0, 3000],
    [23, 31, 3, 0, 2900]
]

now = [
    [3, 53, 2, 4, 900],
    [14, 36, 2, 0, 2000],
    [6, 38, 2, 0, 75100],
    [22, 6, 1, 0, 3800],
    [14, 4, 4, 2, 47700],
    [19, 8, 4, 3, 3300],
    [9, 13, 0, 2, 1400],
    [6, 27, 4, 3, 63800],
    [1, 22, 2, 0, 2000],
    [8, 1, 3, 1, 79200]
]

# 0) 각 계좌주인마다 저번달 거래의 총액과 가장 적은 거래수를 기록한 시간대를 구해야함.
total_dic = {} # 과거 총 거래 량
cnt_dic = {} # 과거 거래 젤 적은 시간대
cnt_semi_result = {} # 거래 횟수를 구하기 위한 dic
final = 0

# 1) owner를 순회해서 키 : 번호 / value : 사람이름 dic을 만듦
#     1] 나중에 src로 owner dic 접근해서 사람이름 찾고 사람이름으로 최종 dic만든다.

owner_dic = {} # 번호, 사람이름 dic
for num, owner in enumerate(owners):
    owner_dic[num] = owner
    total_dic[owner] = 0 # 토탈 거래량 누적을 위해 초기화 해두기
    cnt_semi_result[owner] = [0, 0, 0, 0, 0, 0]
    

# 1) previous를 순회
#     1] 거래 1건에서
#     2] src와 dst에 해당하는 계좌번호의 거래 총액을 누적한다. -> 각 인원마다 dic로 키 : 사람이름 / 벨류 : 총액

for h, m, src, dst, money in prev:
    total_dic[owner_dic[src]] += money
    total_dic[owner_dic[dst]] += money
    
#     3] src와 dst의 가장 적은 거래수를 기록한 시간대 구하기
#         1] 각 인원마다 요소 6의 배열을 만들고 0으로 초기화하고 > 속하는 시간대의 배열에 ++
    src_owner = owner_dic[src]
    dst_owner = owner_dic[dst]
    time_num = 0
    
    if(0 <= h <= 3):
        time_num = 0
    elif(4 <= h <= 7):
        time_num = 1
    elif(8 <= h <= 11):
        time_num = 2
    elif(12 <= h <= 15):
        time_num = 3
    elif(16 <= h <= 19):
        time_num = 4
    elif(20 <= h <= 23):
        time_num = 5
    
    cnt_semi_result[src_owner][time_num] += 1
    cnt_semi_result[dst_owner][time_num] += 1

#         2] 가장 적은 거래수는 0번 거래한 시간대는 제외해야해서  0이 아닌 것 중에서 최소값에 해당하는 시간대를 구한다.
#     4] 시간대는 previous를 전부 순회한 후에 dic에 저장한다.
#         1] 키 : 사람이름 / 벨류 : 가장 적은 거래수를 기록한 시간대 번호

print("주인 별 저번달 모든 거래 시간대", cnt_semi_result)

for key in cnt_semi_result.keys():
    value = cnt_semi_result[key]
    
    min_time_range = 0
    min_time_range_value = 100001
    
    for idx, ele in enumerate(value):
        if(ele < min_time_range_value):
            min_time_range = idx
            min_time_range_value = ele
    
    # 여기 set으로 한거 너무 잘했고
    cnt_result = set()
    
    # 최소값 찾고 다시 순회해서 전부 찾은거 너무 잘했다. 이 문제는 전체적으로 dic을 잘 구상했다 복기 씨게 해보자!
    # 주석도 잘 썼다. 변수 하나하나에 프린트 좋았다.
    for idx, ele in enumerate(value):
        if(ele == min_time_range_value):
            cnt_result.add(idx)
    
    print("주인별 거래량이 가장 적은 시간대 인덱스 번호", key , " = " , cnt_result)
    cnt_dic[key] = cnt_result

print(cnt_dic)
print(total_dic)   


# 2) now를 순회
#     1] src
#         1] src의 작년 내역을 봐서
#         2] 가장 적은 거래수를 기록한 시간대의 거래이고
#         3] 저번달 거래 총액 보다 큰 건이면 결과에 ++
#     2] dst도 동일

for h, m, src, dst, money in now:
    src_owner = owner_dic[src]
    dst_owner = owner_dic[dst]
    
    time_num = 0
    
    if(0 <= h <= 3):
        time_num = 0
    elif(4 <= h <= 7):
        time_num = 1
    elif(8 <= h <= 11):
        time_num = 2
    elif(12 <= h <= 15):
        time_num = 3
    elif(16 <= h <= 19):
        time_num = 4
    elif(20 <= h <= 23):
        time_num = 5
        
    src_min_cnt = cnt_dic[src_owner]
    src_total = total_dic[src_owner]
    dst_min_cnt = cnt_dic[dst_owner]
    dst_total = total_dic[dst_owner]
    
    
    print(time_num , src_min_cnt , money , src_total)
    
    if(time_num in src_min_cnt and money > src_total):
        print("잡았다.", src_owner)
        final += 1
        continue
    
    if(time_num in dst_min_cnt and money > dst_total):
        print("잡았다.", dst_owner)
        final += 1
        continue
        
    
print(final)