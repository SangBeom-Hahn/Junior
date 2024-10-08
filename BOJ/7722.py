'''
동작 : 
1. 직접 방문
1) 이전 방문 종목을 뒤로 가기 목록에 추가 (이전 방문 종목이 없으면 무시)
2) 앞으로 가기 목록 비움
3) 최근 방문 종목에 직접 방문 종목 id를 넣음(스택으로 해야할듯)

2. 뒤로가기
1) 뒤로가기 목록에 종목이 없으면 수행 x
2) 이전 방문 종목은 앞으로 가기 목록에 추가
3) 뒤 목록에 가장 최근에 추가된 종목을 방문하고(뒤로 가기 목록에 탑)
뒤로 가기 목록에서 제거 
4) 최근 방문 목록에 지금 뒤로 가는 목록 추가, 추가할때는 중복된거 제거

3. 앞으로 가기
1) 앞로가기 목록에 종목이 없으면 수행 x
2) 이전 방문 종목은 뒤로 가기 목록에 추가
3) 앞 목록에 가장 최근에 추가된 종목을 방문하고, 앞으로 가기 목록에서 제거
4) 최근 방문 목록에 지금 앞으로 가는 목록 추가, 추가할때는 중복된거 제거

필요한거 : 이전 방문 종목(최근 방문 종목의 탑일듯), 직접 방문 종목
, 앞, 뒤 목록(스택), 최근 방문 목록(스택)

ex) 1, 2, 3, 4, 3
최근
1
2
4
3

* maxSize : 최근 방문 목록 최대 개수
actions : 동작 배열
출 : 최근 방문 목록 (그냥 스택으로 쭉쭉 넣고 출력할때만 뒤에서 maxSize만큼 훑음)
2. nlogn
'''

maxSize = 3
actions = ["1", "2", "B", "F"]
last_visit_list = [] # 최근 방문 목록
# 이전 방문 종목(최근 방문 종목의 탑일듯)
# 직접 방문 종목 = 지금 들어오는 거
front_list = []
back_list = []

# 3. 앞으로 가기
# 1) 앞로가기 목록에 종목이 없으면 수행 x
# 2) 이전 방문 종목은 뒤로 가기 목록에 추가
# 3) 앞 목록에 가장 최근에 추가된 종목을 방문하고, 앞으로 가기 목록에서 제거
# 4) 최근 방문 목록에 지금 앞으로 가는 목록 추가, 추가할때는 중복된거 제거

for ele in actions:
    if(ele == "B"):
        if(len(back_list) == 0):
            pass
        else:
            last = last_visit_list[len(last_visit_list)-1]
            front_list.append(last)
            back = back_list.pop()
            if(back in last_visit_list):
                last_visit_list.remove(back)
            last_visit_list.append(back)
            # print("hi")
            
    elif(ele == "F"):
        if(len(front_list) == 0):
            pass
        else:
            last = last_visit_list[len(last_visit_list)-1]
            back_list.append(last)
            front = front_list.pop()
            if(front in last_visit_list):
                last_visit_list.remove(front)
            last_visit_list.append(front)
            # print("hi")
    else:
        # 1) 이전 방문 종목을 뒤로 가기 목록에 추가 (이전 방문 종목이 없으면 무시)
        if(len(last_visit_list) != 0):
            back_list.append(last_visit_list[len(last_visit_list)-1])
        front_list = []
        last_visit_list.append(ele)

print(last_visit_list)