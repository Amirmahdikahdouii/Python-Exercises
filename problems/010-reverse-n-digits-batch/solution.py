counter = int(input())
number = int(input())
new_number = 0
p = 0
while number != 0:
    num = number % (10**counter)
    number //= (10**counter)
    new_num = 0
    c = 0
    while num != 0:
        r = num % 10
        num //= 10
        new_num = (new_num*10) + r
        c+=1
    if number == 0:
        p += (counter - c)
        new_number = (new_num*(10**p)) + new_number
    else:    
        new_number = (new_num*(10**p)) + new_number
    p += counter
print(new_number)