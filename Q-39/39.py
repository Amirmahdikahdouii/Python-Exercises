def passed_numbers(numbers) -> list:
    return [x for x in range(min(numbers), max(numbers)) if x not in numbers]
print(passed_numbers([1, 3, 5, 6, 7, 8, 9, 10, 13, 14, 16, 17, 20, 21, 25]))