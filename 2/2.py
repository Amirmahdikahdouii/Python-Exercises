count = int(input())
sumOfNumbers = 0
while count > 0:
    count -= 1
    num = int(input())
    number = num
    new_number = 0
    while num != 0:
        r = num % 10
        new_number = (new_number*10) + r
        num //= 10
    if new_number == number:
        sumOfNumbers += new_number
print(sumOfNumbers)
