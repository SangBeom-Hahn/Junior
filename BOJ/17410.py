'''
3x3 인 배열 A가 있다. 인덱스는 1부터 시작한다. 1초가 지날 때마다 배열에 연산이 적용된다.
R연산 : 행의 개수가 열의 개수보다 >= 경우 -> 배열 A의 모든 행에 대해서 정렬 수행
C연산 : 행의 개수가 < 열의 개수보다 경우 -> 배열 A의 모든 d열에 대해 정렬
정렬 조건 :
1) 각각의 수가 몇 번 나왔는지 알아야 하고 수의 등장횟수 기준 오름차순 정렬한다.couter()
그런게 여러개면 작은 숫자 먼저 오름차순
2) 정렬을 하고 그 다음 배열 A에 정렬된 결과를 다시 넣어야 하는데 그떄는 수와 등장횟수를 모두
덯으며, 수가 먼저이다.

ex) 3 1 1 > 3 : 1번 / 1 : 2번 > 3 1 1 2로 넣음
3 1 1 2 > 3 : 1번 / 1 : 2번 / 2 : 1번 > (2 1) (3 1) (1 2)

이걸 모든 행이나 모든 열에 대해 한다. 그러면 행이나 열의 길이가 달라질 수 있으니 0으로 패딩한다.
3) 행 또는 열의 크기가 100을 넘어가면 처음 100개를 제외한 나머지는 버린다.

1. 모경수
0) for문으로 100초를 세고 중간에 r,c = k와 같아지면 break, 아니면 -1
0) 최초에는 행과 열의 개수가 같아서 R 연산을 한다.
1) r이나 c 연산을 해서 (수, 갯수) (수, 갯수) (수, 갯수)로 만들고 새 배열로 저장하고
2) 수를 세는 방식은 counter()로 하자
3) 그 다음 다시 어떤 연산을 할지 고민한다. 언제까지? rc가 k일때 까지

* r, c, k(인덱스 1부터 시작)
배열 A의 상태
출력 : A[r][c]에 들어있는 값이 k가 되기 위해 몇 초가 걸리나 ㄱㄱ 100초가 지나도 k가 안되면
-1 출력

2. 시복 nlogn
'''
from collections import Counter

def R(graph):
    rowLeng = len(graph)

    # 최초에는 R 연산
    # R연산 : 행의 개수가 열의 개수보다 >= 경우 -> 배열 A의 모든 행에 대해서 정렬 수행
    # 정렬은 cnt를 세고 정렬하고 새 배열에 넣는 것임
    maxLeng = 0
    for i in range(rowLeng):
        eachRowEleCnt = Counter(graph[i])
        del eachRowEleCnt[0]
        newEachRow = sorted(eachRowEleCnt.items(), key= lambda x : (x[1], x[0]))

        if(len(newEachRow) > 50):
            newEachRow = newEachRow[:50]

        realRow = []
        # 새로운 가로가 확대된 배열을 만들고 넣어야 함
        for ele in newEachRow:
            realRow += ele

        graph[i] = realRow
        print(realRow)
        maxLeng = max(maxLeng, len(realRow))

    # # print(*graph, sep='\n')
    # print("a", maxLeng)
    # # 뒤에 0을 채움
    # for idx, ele in enumerate(graph):
    #     ele = list(map(str, ele))
    #     ele = ''.join(ele)
    #     ele = ele.ljust(maxLeng, '0')
    #     ele = list(map(int, ele))
    #     graph[idx] = ele

    for i in range(len(graph)):
        if len(graph[i]) < maxLeng:

            graph[i].extend([0] * (maxLeng - len(graph[i])))

    print(*graph, sep='\n')

# c연산
# C연산 : 행의 개수가 < 열의 개수보다 경우 -> 배열 A의 모든 d열에 대해 정렬
# c연산은 그래프 T > R연산 T하면 됨

# 0) for문으로 100초를 세고 중간에 r,c = k와 같아지면 break, 아니면 -1
# 0) 최초에는 행과 열의 개수가 같아서 R 연산을 한다.
# 1) r이나 c 연산을 해서 (수, 갯수) (수, 갯수) (수, 갯수)로 만들고 새 배열로 저장하고
# 2) 수를 세는 방식은 counter()로 하자
# 3) 그 다음 다시 어떤 연산을 할지 고민한다. 언제까지? rc가 k일때 까지

def main():
    r, c, k = map(int, input().split())
    r -= 1
    c -= 1
    graph = [list(map(int, input().split())) for _ in range(3)]

    for time in range(0, 101):
    # for time in range(0, 3):
        rowLeng = len(graph)
        colLeng = len(graph[0])
        # print(*graph, sep='\n')

        if(rowLeng > r and colLeng > c):
            if(graph[r][c] == k):
                print(*graph, sep='\n')
                print(time)
                break

        if(rowLeng >= colLeng):
            print('aa')
            R(graph)
        else:
            print('bb')
            graph = list(map(list, zip(*graph)))
            R(graph)
            graph = list(map(list, zip(*graph)))
    else:
        print(*graph, sep='\n')
        print(-1)

main()