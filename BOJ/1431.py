n = int(input())
serial = []
for i in range(n):
    serial.append(input())

# print(serial)

addLen = [[len(i), i]for i in serial]
# print(addLen)

for i in addLen:
    sum = 0
    for j in i[1]:
        if(j.isdigit()):
            sum += int(j)
    i.append(sum)

addLen = sorted(addLen, key=lambda x:(x[0], x[2], x[1]))
for i in addLen:
    print(i[1])