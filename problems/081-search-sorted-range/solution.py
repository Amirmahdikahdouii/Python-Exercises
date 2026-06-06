def search_range(numbers: list, num: int):
    """
    This Function is Used to get first and last index of number in a numbers list.
    for example:
        search_range([1,2,2,2,3,4], 2) -> [1, 3]
    """
    start, end = None, None
    flag = False
    for i, number in enumerate(numbers):
        if number == num and flag is False:
            start = i
            flag = True
        elif flag and number != num:
            end = i - 1
            break
    return [start, end]


def sort_numbers(numbers: list):
    length = len(numbers)
    for i in range(length-1):
        is_sorted = True
        for j in range(length-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                is_sorted = False
        if is_sorted:
            return numbers
    return numbers

numbers = list(map(int, input().split()))
num = int(input())
numbers = sort_numbers(numbers)
print(numbers)
print(search_range(numbers, num))