animal = list(map(int, input().split()))
count = 0

while (1):
    if (animal[0] + 1 == animal[1] and animal[0] + 2 == animal[2]):
        print(count)
        break

    if (animal[1] - animal[0] > animal[2] - animal[1]):
        animal[2] = animal[1] - 1
        count += 1
        animal[2], animal[1] = animal[1], animal[2]
    else:
        animal[0] = animal[1] + 1
        count += 1
        animal[0], animal[1] = animal[1], animal[0]