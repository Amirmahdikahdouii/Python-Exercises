number1 = int(input())
number2 = int(input())
gcd = 1
lcm = 1
if number2 > number1:
    c_number1 = number1
    number1 = number2
    number2 = c_number1
for i in range(number1, 1, -1):
    if number1 % i == 0 and number2 % i == 0:
        gcd = i
        break
i = 1
while True:
    if (number2 * i) % number1 == 0:
        lcm = number2 * i
        break
    i += 1
print(gcd)
print(lcm)
