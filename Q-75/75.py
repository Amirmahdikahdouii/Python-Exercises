def sort_numbers(numbers: list):
    if any(num < 0 or not isinstance(num, int) for num in numbers):
        raise ValueError("please give non negetive entegers")
    for _ in range(len(numbers)):
        for i, (number1, number2) in enumerate(zip(numbers, numbers[1:])):
            if number1 > number2:
                numbers[i] -= number1 - number2
                numbers[i+1] += number1 - number2
    return numbers


numbers = list(map(int, input().split()))
print(sort_numbers(numbers))
