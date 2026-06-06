number = int(input())
new_number = 0
p = 0
while number != 0:
    r = number % 10
    number //= 10
    if r % 2 == 0:
        new_number = (r*(10**p)) + new_number
        p += 1
print(new_number)