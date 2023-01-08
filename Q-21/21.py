# Pandigital Prime Number
counter = int(input())
for number in range((10**counter)-1, 10**(counter-1), -2):
    flag = True
    for i in range(2, number//2+1):
        if number % i == 0:
            flag = False
            break
    if not flag:
        continue
    c_number = number
    while c_number != 0:
        r = c_number % 10
        c_number //= 10
        c_num = c_number
        while c_num != 0:
            nr = c_num % 10
            c_num //= 10
            if nr == r:
                flag = False
                break
    if flag:
        print(number)
        break