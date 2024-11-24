
'''
마라톤이 가능한 최장거리, 출발지의 방 번호, 도착지의 방번호를 구해라
마라톤
1] 1번 통과한 방은 다시 통과할 수 없다.
2] 최장 거리 = 개미 방이 이어진 경로들의 합
3] 출발지의 방번호 < 도착지의 방번호

* 개미방의 개수
개미방 번호, 개미방 번호, 개미방 사이의 거리
출 : 최장거리, 출발지, 도착지
서클 존재시 -1
'''





'''
조건이 2, 1, 3이면 나이, 성별, 노약자 순 우선순위임

조건
1] 성별 : F > M 순위로 우선순위가 높음
2] 나이 : 
    0] 무조건 7세 이하가 우선순위가 높아
    1] 7세 이하 -> 나이가 어릴수록 우선순위가 높음
    2] 7세 초과 : 나이가 많을수록 우선순위 높은
3] 노약자 ; 
    0] 노약자(3)은 조건에 없을수도 있음 ex) F 6
    1] PW > DP > P 순서로 우선순위가 높음
    2] M은 남자라서 PW가 될 수 없음

1) 모경수
0) 조건을 1개의 배열로 관리함
1) 조건 우선순위를 순회해서 각각을 쪼갬
    1] 우선순위가 1이면
        1] F인 애들 모으고
        2] M인 애들 모음
        3] 각 조건에서 쪼갠거의 길이가 1이면 출력
        4] 1이 아니면 배열을 1뺀 나머지로 새로 갱신함
    2] 우선순위가 2이면
        1] 7세 이하 모아
        2] 7세 초과 모아

3) 1이 아니면 다음 조건 봄 (최초엔 1로 해서 다음 조건을 보면 depth를 증가함)

4) 만약 depth가 3이면 그냥 순회하면서 출력

* 조건 우선순위(왼쪽이 가장 우선순위가 높음)
사람수
사람수만큼의 조건
    조건 1, 2, 3    
    조건 1, 2, 3
출 : 우선순위가 높은 사람부터 한 행으로 출력(행의 끝에 공백 없이 개행으로 끝나야 함)
'''