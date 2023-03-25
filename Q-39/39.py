def passed_numbers(numbers) -> list:
    passed_nums = []
    for num in range(min(numbers), max(numbers)+1):
        if num not in numbers:
            passed_nums.append(num)
    return passed_nums
print(passed_numbers([1, 3, 5, 6, 7, 8, 9, 10, 13, 14, 16, 17, 20, 21, 25]))