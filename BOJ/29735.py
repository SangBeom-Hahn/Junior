'''
예상 도착 시간, 다른 집 택배 갯수

기사
1] 출근과 동시에 배송 시작
2] 지금 배송 택배 끝나는 시간 >= 퇴근 시간, 그 배송 안함. 다음날 출근해서 배송한다

ex)
출근    토근
7:30    12:30
450     750

먼저 100개
450 + 42 * 7 = 450 + 294 = 744 = 하루에 7개보내고 다음날 보내야 함
750 - 450 = 300
300 // 42 = 7 ... 6, 나머지가 0이면 몫 -1개 보낼 수 있음

14 * 7 = 98 = 14일에 거쳐 9개 보내고 15일에 2개 더 보내면 8:12 > 8:54
100 // 7 = 14

---

출근    토근
9:00    16:00
540     960
420 // 15 = 28개 - 1 하루에 27개 가능

3 // 27 = 0 ... 3


1. 모경수(prt, n=1)
ok 0) 시간에 60곱해서 분으로 본다.
ok 1) (퇴근시간 - 출근시간)  // 1건당 걸리는 시간
    1] 나머지가 0이면 몫-1개 하루에 배달 가능
    2] 나머지가 0이 아니면 하루에 몫개 배달 가능

4) 먼저 다 보내고, 브실이꺼 구하기
    1] 먼저 배송 수 // 하루에 배달 가능
        1] 나머지 0이면 전부다 보낸 거임
        2] 나머지 0아니면 나머지 개수만큼 출근 시간에 더해야함.
    2] 몫이 며칠 후 도착하는지
    3] 나머지가 0이면 출근시간 + 1건당 걸리는 시간이 브실이 시간
    4] 나머지가 0이 아니면 출근시간 + 나머지 개수만큼 출근 시간에 더하고 + 1건 더 더함.


* 출근 시각, 퇴근 시간 hh:mm
n 먼저 배송 택배 수
t 1건당 걸리는 시간 (단위 : 분)

출 : 택배 며칠 후 도착하는지, 몇시 몇분?

2. nlogn

'''

start, end = input().split()
start_time, start_min = start.split(':')
end_time, end_min = end.split(':')

# print(start_time, start_min)
start = int(start_time) * 60 + int(start_min)
end = int(end_time) * 60 + int(end_min)

# print(start, end)

n, t = map(int, input().split())
today_can_delivery = (end - start) // t
nmg = (end - start) % t

if(nmg == 0):
    today_can_delivery -= 1
    
# print(today_can_delivery)    


# 4) 먼저 다 보내고, 브실이꺼 구하기
#     1] 먼저 배송 수 // 하루에 배달 가능
#         1] 나머지 0이면 전부다 보낸 거임
#         2] 나머지 0아니면 나머지 개수만큼 출근 시간에 더해야함.
#     2] 몫이 며칠 후 도착하는지
#     3] 나머지가 0이면 출근시간 + 1건당 걸리는 시간이 브실이 시간
#     4] 나머지가 0이 아니면 출근시간 + 나머지 개수만큼 출근 시간에 더하고 + 1건 더 더함.

mok = n // today_can_delivery
nmg = n % today_can_delivery

# 며칠 후 도착하는지
print(mok)
# print(start_time, start_min)

if(nmg == 0):
    # 전부 다 보맨
    final_time = str((start + t) // 60)
    final_min = str((start + t) % 60)
    
    final_time = final_time.zfill(2)
    final_min = final_min.zfill(2)
    
    print(final_time + ":" + final_min)
    
else:
    final_time = str((start + (nmg * t) + t) // 60)
    final_min = str((start + (nmg * t) + t) % 60)
    
    final_time = final_time.zfill(2)
    final_min = final_min.zfill(2)
    
    print(final_time + ":" + final_min)