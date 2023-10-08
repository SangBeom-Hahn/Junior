'''
금 > 은 > 동이 많은 나라순으로 순위를 정함

각 나라가 1 ~n 사이의 정수로 표현된다. 
등수 : 자신보다 더 잘한 나라의 수 + 1
두 나라의 금,은,동 수가 모두 같다면 두 나라의 둥스누는 간ㅌ다.
어느나라가 몇등함?

1. 모경수
1) 정렬
2) 현재 인덱스+1 출력

* n, k : 국가의 수, 등수를 알고 싶은 국가 번호
각 국가를 나타내는 정수와 금, 은, 동 수
출력 : k국가의 등수

2. 시봇 n^2
'''

n, k = map(int, input().split())
eachCountryMedalsCnt = []
for _ in range(n):
    countryNum, g, s, dong = map(int, input().split())
    eachCountryMedalsCnt.append([g, s, dong, countryNum])
    
# print(eachCountryMedalsCnt)

# 정렬
eachCountryMedalsCnt.sort(key = lambda x : (-x[0], -x[1], -x[2]))

# print(eachCountryMedalsCnt)
wantG, wantS, wantD = 0, 0, 0
for i in range(len(eachCountryMedalsCnt)):
    if(eachCountryMedalsCnt[i][3] == k):
        wantG = eachCountryMedalsCnt[i][0]
        wantS = eachCountryMedalsCnt[i][1]
        wantD = eachCountryMedalsCnt[i][2]
        
for i in range(len(eachCountryMedalsCnt)):
    if(eachCountryMedalsCnt[i][0] == wantG and
       eachCountryMedalsCnt[i][1] == wantS and
       eachCountryMedalsCnt[i][2] == wantD):
        print(i+1)
        break