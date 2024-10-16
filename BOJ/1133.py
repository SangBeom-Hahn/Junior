'''
n x m 직사각형이 있다. k개의 카메라
cctv
    1] cctv는 5가지 종류
    2] 벽을 못 통과함, cctv는 통과할 수 있음
    3] 90도 방향으로 회전 가능
사각지대 : cctv가 감시할 수 없는 영역
지도 : 0, 6, 1~5 / 빈칸, 벽, 카메라 종류 번호

1. 모경수(prt, n=1)
1) 카메라를 다 돌리면서 모든 경우의 수를 다 봐야할 것 같다.
2) 카메라 총 대수가 최대 8대니깐 뭐 카메라 대수 대만큼 for문 돌려야지 뭐
3) 카메라 좌표를 구함
4) [1, 2, 5] 총 3대라고 쳤을 때 재귀
    1] 첫번째 카메라 봐서 ↑ 로 감시함
    2] for문으로 2번쨰 카메라로 재귀
    3] 2번째 카메라로 <- ->로 감시함
    4] 5번 감시함
    5] 마지막 카메라까지 감시를 했을 때마다 visit이 f인 부분 개수를 셈, 최소 개수 갱신
    6] 다시 2번 카메라로 와서 위/아래 감시함
    7] 5번 감시함, 반복


* n, m 사무실 크기, 
상태
출 : cctv의 방향을 적절히 정해서, 사각 지대의 최소 크기를 구하라

2. 시복 n^3
'''

def back():
    for i in range(len(cam)):
        

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
cam = []

for i in range(n):
    for j in range(m):
        if(graph[i][j] != 0 and graph[i][j] != 6):
            cam.append((i, j))
            
back()