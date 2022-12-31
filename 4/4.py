price = int(input())
speed_limit = int(input())
armins_speed = int(input())
difference = armins_speed - speed_limit
if difference > 0:
    number = 0
    while difference != 0:
        r = difference % 10
        difference //= 10
        if r > number:
            number = r
    number_fact = 1
    for i in range(1, number+1):
        number_fact *= i
    print(price + number_fact)
else:
    print(0)
