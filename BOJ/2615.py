'''
5알이 연속적이면 이긴건데 6알 이상은 이긴게 아니다. 바득ㅂ판의 상태가 주어질 때
검이 이겼나 흰이 이겼나 아직 승부가 ㄱㄹ정되지 않았나 판단하는 프로그래믈 ㄱㄱ

1. 모든 경우의 수
1) 조합으로 좌표 5개의 조합을 구함
2) 조합을 돌면서 그 조합에 해당하는 바둑판의 상태를 봤는데 다 1이거나 다
2다?? 그럼 출력 그게 모든 조합이 다 안되면 0출력 -> 이거 메모리 초과

3) 모든 좌표 다 돌면서 한 좌표에서 오, 오른쪽 아래 대각선, 아래를 6번 보는데
중간에 틀리면 pass 다 맞는데 6까지 맞으면 pass 5까지 맞으면 여기다.


* 검 1, 흰 2 알이 없는 곳 0
바둑판의 상태
출력 : 검이 이기면 1, 흰이 이기면 2 아직 승부 x면 0
검이나 흰이 이기면 가장 왼쪽 바둑알 좌표 ㄱㄱ

2. n^3
'''
from itertools import combinations

n = 19
loc = []
graph = [list(map(int, input().split())) for _ in range(19)]

def main():
    for i in range(19):
        for j in range(19):
            if(graph[i][j] == 0):
                continue
            
            # 오른쪽
            cnt = 0
            for k in range(1, 6):
                if(j+k >= 19):
                    continue
                # print(i, j+k)
                if(graph[i][j+k] == graph[i][j]):
                    cnt += 1
                    continue
                else: # 다르면 다음 칸을 처음부터 시작
                    break
            if(cnt == 4): # 5개가 똑같단 소리
                # 가장 오른쪽 열이면 체크 안해도 됨
                if(j == 0):
                    print(graph[i][j])
                    print(i+1, j+1)
                    return
                
                if(graph[i][j-1] != graph[i][j]):
                    print(graph[i][j])
                    print(i+1, j+1)
                    return
            
            # 오른쪽 아래 대각선
            cnt = 0
            for k in range(1, 6):
                if(i+k >= 19 or j+k >= 19):
                    continue                
                
                if(graph[i+k][j+k] == graph[i][j]):
                    cnt += 1
                    continue
                else: # 다르면 다음 칸을 처음부터 시작
                    break
            if(cnt == 4): # 5개가 똑같단 소리
                if(i == 0 or j == 0):
                    print(graph[i][j])
                    print(i+1, j+1)
                    return
                
                if(graph[i-1][j-1] != graph[i][j]):
                    print(graph[i][j])
                    print(i+1, j+1)
                    return
                
            # 오른쪽 위 대각선
            cnt = 0
            for k in range(1, 6):
                if(j+k >= 19 or i-k < 0):
                    continue                
                if(graph[i-k][j+k] == graph[i][j]):
                    cnt += 1
                    continue
                else: # 다르면 다음 칸을 처음부터 시작
                    break
            if(cnt == 4): # 5개가 똑같단 소리
                if(i == 18 or j == 0):
                    print(graph[i][j])
                    print(i+1, j+1)
                    return                    
                
                if(graph[i+1][j-1] != graph[i][j]):
                    print(graph[i][j])
                    print(i+1, j+1)
                    return
            
            # 아래
            cnt = 0
            for k in range(1, 6):
                if(i+k >= 19):
                    continue                
                
                if(graph[i+k][j] == graph[i][j]):
                    cnt += 1
                    continue
                else: # 다르면 다음 칸을 처음부터 시작
                    break
            if(cnt == 4): # 5개가 똑같단 소리
                if(i == 0):
                    print(graph[i][j])
                    print(i+1, j+1)
                    return         
                       
                if(graph[i-1][j] != graph[i][j]):
                    print(graph[i][j])
                    print(i+1, j+1)
                    return
    print(0)
main()