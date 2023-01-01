start = int(input())
end = int(input())
number = int(input())
new_number = 0
p = 0
i = 1
while number != 0:
    r = number % 10
    number //= 10
    if i >= end and i <= start:
        i += 1
        continue
    new_number = (r*(10**p)) + new_number
    p += 1
    i+=1
print(new_number)