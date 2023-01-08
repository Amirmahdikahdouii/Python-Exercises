number = int(input())
new_number = 0
p = 0
while number != 0:
    r = number % 2
    number //= 2
    new_number = (r*(10**p)) + new_number
    p += 1
c_new_number = new_number
palindNum = 0
while c_new_number != 0:
    r = c_new_number%10
    c_new_number //= 10
    palindNum = (palindNum*10) + r
if palindNum == new_number:
    print("YES")
else:
    print("NO")