count = 0
for number in range(499, 2, -2):
    flag = True
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            flag = False
            break
    if not flag:
        continue
    for i in range(5, -1, -1):
        if number > (10**i):
            p = i
            break
    remind_number = number // 10
    result = number
    while number != 0 and flag:
        r = number % 10
        number //= 10
        if r == 5 or (r % 2 == 0):
            flag = False
            break
        elif number == 0:
            break
        c_number = (r*(10**p)) + remind_number
        remind_number = c_number // 10
        for i in range(2, c_number//2+1):
            if c_number % i == 0:
                flag = False
                break
    if flag:
        count += 1
        print(result)
print(count)
