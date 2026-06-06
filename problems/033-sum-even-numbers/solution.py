def sumOfEvens(number):
    return sum([x for x in range(2, number+1, 2)])
number = int(input())
print(sumOfEvens(number))