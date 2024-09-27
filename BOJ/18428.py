'''
nxn 복도, 선생님, 학생, 장애물이 있다. 
선생님 : 상하좌우 4가지 방향으로 감시를 진행함, 장애물 뒤편은 볼 수없음, 장애물 없으면
멀리까지 볼수있음

학생 : 빈칸중에서 정확히 3개의 장애물을 설치함

1. 모경수(prt, n=1)
5) 선생님들 좌표 구함
6) 학생들 좌표 구함
1) 빈칸의 좌표를 배열에 저장
2) 그걸로 조합을 구함
3) 모든 조합을 순회함
4) 각 조합에서 장애물 설치함
5) 선생님들 좌표에서 상하좌우 dfs 돌림
6) visit 배열에서 학생들의 좌표가 모두 false면 yes하고 게임 끝냄
7) 모든 조합을 다봤는데 게임 안 끄탄면 no


* n : nxn
복도 정보(s, t, x = 학생, 선생님, 빈칸)
출 : 3개를 설치해서 모든 학생들을 감시로부터 피하도록 할 수있는지 여부를 출력함

2. 시복 n^3
'''

n = int(input())
graph = [input().split() for _ in range(n)]
tempGraph = [ele[:] for ele in graph]
visit = [[False] * n for _ in range(n)]
tempVisit = [ele[:] for ele in visit]

teachers = []
students = []
observes = []
# print(*graph, sep='\n')

# 5) 선생님들 좌표 구함
# 6) 학생들 좌표 구함
for i in range(n):
    for j in range(n):
        if(graph[i][j] == "T"):
            teachers.append((i, j))
        if(graph[i][j] == "S"):
            students.append((i, j))
        if(graph[i][j] == "X"):
            observes.append((i, j))
            
# 1) 빈칸의 좌표를 배열에 저장
# 2) 그걸로 조합을 구함
combs = []
def comb(chose, start):
    if(len(chose) == 3):
        combs.append(chose[:])
        return
    
    for i in range(start, len(observes)):
        chose.append(observes[i])
        comb(chose, i+1)
        chose.pop()
comb([], 0)

# print(*combs, sep='\n')
# 3) 모든 조합을 순회함
# 4) 각 조합에서 장애물 설치함            

def dfsUp(x, y):
    visit[x][y] = True
    
    nx = x-1
    if(nx < 0 or graph[nx][y] == 'O'):
        return
    dfsUp(nx, y)
    
def dfsDown(x, y):
    visit[x][y] = True
    
    nx = x+1
    if(nx >= n or graph[nx][y] == 'O'):
        return
    dfsDown(nx, y)
    
def dfsRight(x, y):
    visit[x][y] = True
    
    ny = y+1
    if(ny >= n or graph[x][ny] == 'O'):
        return
    dfsRight(x, ny)
    
def dfsLeft(x, y):
    visit[x][y] = True
    
    ny = y-1
    if(ny < 0 or graph[x][ny] == 'O'):
        return
    dfsLeft(x, ny)

# combs = [[[0, 0], [0, 2], [0, 3]], [[1, 1], [0, 3], [2, 2]]]
for c in combs:
    for x, y in c:
        graph[x][y] = 'O'
    # print(*graph, sep='\n')
    
    # 5) 선생님들 좌표에서 상하좌우 dfs 돌림
    for x, y in teachers:
        dfsUp(x, y)
        dfsDown(x, y)
        dfsRight(x, y)
        dfsLeft(x, y)
    
    # 6) visit 배열에서 학생들의 좌표가 모두 false면 yes하고 게임 끝냄
    # 7) 모든 조합을 다봤는데 게임 안 끄탄면 no
    allFalse = True
    for x, y in students:
        if(visit[x][y] == True):
            allFalse = False
            break
        
    if(allFalse == True):
        print("YES")
        break
        
        
    # print(*visit, sep='\n')
    # print()
    graph = [ele[:] for ele in tempGraph]
    visit = [ele[:] for ele in tempVisit]
else:
    print("NO")