from header_file import a, b

def smTranspose(a, b):
    m = a[0][0] #일반행렬 행
    n = a[0][1] #일반행렬 열
    v = a[0][2] #일반행렬 값 개수
    b[0][0] = n #전치행렬 행
    b[0][1] = m #전치행렬 열
    b[0][2] = v #전치행렬 값 개수

    if(v > 0):
        p = 1
        for i in range(n+1):
            for j in range(1, v+1):
                if(a[j][0] == i): # 조건을 만족할 때만 switch 하겠다
                    b[p][0] = a[j][1]
                    b[p][1] = a[j][0]
                    b[p][2] = a[j][2]
                    p+=1

    for i in b:
        print(i)




if(__name__ == '__main__'):
    smTranspose(a(), b())