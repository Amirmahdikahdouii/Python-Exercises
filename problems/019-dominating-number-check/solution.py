# Dominating Number
number = int(input())
halfOfCountDigits = 0
for i in range(10, 0, -1):
    if number > (10**i):
        halfOfCountDigits = (i+1)//2
        break
while number != 0:
    r = number % 10
    number //= 10
    count = 1
    c_number = number
    new_number = 0
    while c_number != 0:
        nr = c_number % 10
        c_number //= 10
        if nr == r:
            count += 1
        else:
            new_number = (new_number*10) + nr
    if count > halfOfCountDigits:
        print("YES")
        break
    number = new_number
else:
    print("NO")