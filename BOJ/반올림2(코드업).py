N , M = map(float, input().split())
nanum = N/M
n_list = list(str(nanum))
count = -2

print(N%M)
for i in range(len(n_list)):
    if (i == count):
        break

    print(n_list[i], end='')
    if(n_list[i] == '.'):
        count = i+4
        if(int(n_list[count]) >= 5):
            n_list.insert(count-1, int(n_list[count])+1 )

