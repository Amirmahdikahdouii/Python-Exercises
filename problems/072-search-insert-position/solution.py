def sort_numbers(numbers: list):
    """
        Function to sort the numbers.
    """
    length = len(numbers)
    for i in range(length - 1):
        swapped = True
        for j in range(length - i - 1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swapped = False
        if swapped:
            break
    return numbers


def search_insert(numbers: list, value: int):
    low = 0
    high = len(numbers) - 1
    mid = high // 2

    while low <= high:
        if numbers[mid] < value:
            mid += 1
            low = mid
        else:
            mid -= 1
            high = mid
    return low


numbers = list(map(int, input().split(",")))
value = int(input())
numbers = sort_numbers(numbers)
print(search_insert(numbers, value))
