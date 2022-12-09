# A는 자기보다 크기가 작은 먹이만 먹을 수 있다. 같아도 못먹는다.
# A의 크기가 B보다 큰 쌍이 몇개나 있는지 구하는 프로그램 작성하라
# 아 그러면 와 함수 구현은 찾고자하는 타겟이 뚜렷하면 써야하고 얘는 뚜렷하지 않고 없어도 돼!! 그러면 bisect
import bisect

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split())) # 1 3 6

    B.sort()
    # A가 오름차순이니 들어갈 수 있는 곳을 left를 찾아라 근데 오름차순 상관없이 같은 것도 보니 right를 찾아야하네
    # ㄴㄴ ㅋㅋ left를 찾고 왼쪽을 다 세라
    sum = 0
    for i in A:
        idx = bisect.bisect_left(B, i)
        sum += idx
    print(sum)