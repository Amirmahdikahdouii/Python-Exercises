while True:
    a = int(input())
    if a == 0:
        break
    if a <= 1000000:
        print(a)
    elif a <= 5000000:
        print(int(a - (a * 0.1)))
    elif a > 5000000:
        print(int(a - (a * 0.2)))