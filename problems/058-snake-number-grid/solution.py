x, y = list(map(int, input().split()))
number = 1
for i in range(x):
    line = []
    for j in range(y):
        line.append(number)
        number += 1
    if i % 2 != 0:
        line.reverse()
    [print(num, end=" ") for num in line]
    print()
