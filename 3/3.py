number1 = int(input())
number2 = int(input())
sum1, sum2 = 0, 0
def getSumOfDivisors(number):
    sumOfNum = 0
    for i in range(1, number):
        if number % i == 0:
            sumOfNum += i
    return sumOfNum
sum1 = getSumOfDivisors(number1)
sum2 = getSumOfDivisors(number2)
if sum1 == number2 and sum2 == number1:
    print("YES")
else:
    print("NO")
