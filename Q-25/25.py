counter = int(input())
count_of_odds = 0
while counter > 0:
    counter -= 1
    number = int(input())
    while number != 0:
        r = number % 10 
        number //= 10
        if r %2 == 0:
            count_of_odds += 1
print(count_of_odds)