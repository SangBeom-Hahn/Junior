'''
게임판의 상태가 주어지면, 그 상태가 게임에서 발생할 수 있는 최종 상태인지를 
판별하라

1. 모든 경우의 수
1) 만족하는 경우와 불만족하는 경우를 구해보자
va :
1) .이 없을 때 x의 개수가 1개 더 많음
2) .이 있을 때 x의 개수가 1개 더 많음 > 그 때 행/열/대각 조건을 만족하면
3) .이 있을 떄 o의 개수가 x의 개수와 같음

inva : 
1) va가 아닌 경우
2) 둘 다 승리 조건을 만족하는 경우(.이 있을 때 o의 개수가 x의 개수와 같을 때
둘 다 열에 3개 거나 행에 3개)


* 테케
출력 : 가능하면 va/ 불가하면 inva

2. 시복 : n^3
'''

while(True):
    graph = input()
    if(graph == 'end'):
        break
    
    xCnt = graph.count('X')
    oCnt = graph.count('O')
    result = "invalid"

    if('.' not in graph):
        if(xCnt == oCnt+1):
            result = "valid"
            
    else:
        # x만 봐서 조건을 만족하나 봐야함
        if(xCnt == oCnt+1):
            # 행조건
            for i in range(0, 7, 3):
                if(graph[i] == graph[i+1] == graph[i+2] == 'X'):
                    result = "valid"
                    break
            
            xElement = []
            # 열/대각 조건
            for i in range(9):
                if(graph[i] == 'X'):
                    xElement.append(i)
                    
            subsets = [[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
            for subset in subsets:
                if(set(subset).issubset(xElement)):
                    result = "valid"
                    break
                
        elif(xCnt == oCnt):
            # 행조건
            for i in range(0, 7, 3):
                if(graph[i] == graph[i+1] == graph[i+2] == 'O'):
                    result = "valid"
                    break
                
            for i in range(0, 7, 3):
                if(graph[i] == graph[i+1] == graph[i+2] == 'X'):
                    result = "invalid"
                    break
            
            oElement = []
            # 열/대각 조건
            for i in range(9):
                if(graph[i] == 'O'):
                    oElement.append(i)
                    
            subsets = [[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
            for subset in subsets:
                if(set(subset).issubset(oElement)):
                    result = "valid"
                    break
                
            xElement = []
            # 열/대각 조건
            for i in range(9):
                if(graph[i] == 'X'):
                    xElement.append(i)
                    
            subsets = [[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
            for subset in subsets:
                if(set(subset).issubset(xElement)):
                    result = "invalid"
                    break
                
    print(result)