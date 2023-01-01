counter = int(input())
greatest_number = 0
number = 0
while counter > 0:
    counter -= 1
    num = int(input())
    c_num = num
    sumOfDivisiors = 0
    while c_num != 0:
        r = c_num % 10
        c_num //= 10
        if r == 2 or r == 3 or r == 5 or r == 7:
            sumOfDivisiors += r
    if sumOfDivisiors > greatest_number:
        greatest_number = sumOfDivisiors
        number = num
print(number)
