def factorial(number):
    if number <= 1:
        return number
    return factorial(number-1) + factorial(number - 2)


number = int(input("Enter Number: "))
[print(factorial(num), end=" ") for num in range(number+1)]
print()
