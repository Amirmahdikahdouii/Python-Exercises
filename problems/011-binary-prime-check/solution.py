number = int(input())
new_number = 0
p = 0
while number != 0:
    r = number % 2
    number //= 2
    new_number = (r*(10**p)) + new_number
    p += 1
for i in range(2, new_number//2+1):
    if new_number % i == 0:
        print("N")
        break
else:
    print("Y")