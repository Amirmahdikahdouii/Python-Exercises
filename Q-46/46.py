def fibonacci(number):
    a, b = 0, 1
    while a <= number:
        print(a)
        a, b = b, a+b
number = int(input())
fibonacci(number)