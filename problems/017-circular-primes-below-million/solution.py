# Circular Primes
count = 2
# Count is one because we do not check '2' and '5' Numbers
# Note That we should just check odd numbers so dont forget to start with odd numbers because count of range is -2!
for number in range((10**6)-1, 2, -2):
    flag = True
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            flag = False
            break
    if not flag:
        continue
    for i in range(6, -1, -1):
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
        c_number = (r*(10**p)) + remind_number
        remind_number = c_number // 10
        for i in range(2, c_number//2+1):
            if c_number % i == 0:
                flag = False
                break
    if flag:
        count += 1
        print(result)
print(f"Count Of Circular Number: {count}")
