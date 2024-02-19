'''

'''


def can_finish(sizes, limits, tasks):
    result = []
    for i in range(len(sizes)):
        k, t = int(tasks[i][0]), tasks[i][1:]
        time_needed = k * (sizes[i] ** len(t))
        if time_needed <= limits[i]:
            result.append(1)
        else:
            result.append(0)
    return result

sizes = [100, 100, 100]
limits = [1000000000, 100, 3]
tasks = ['9tttt', '1t', '4']
print(can_finish(sizes, limits, tasks))