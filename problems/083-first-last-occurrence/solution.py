def sort_numbers(numbers: list):
    length = len(numbers) - 1
    for i in range(length - 1):
        is_sorted = True
        for j in range(length - i - 1):
            if numbers[j] > numbers[j+1]:
                is_sorted = False
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        if is_sorted:
            return numbers
    return numbers


def first_occurrence(numbers: list, num: int):
    low, high = 0, len(numbers) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if low == high:
            break
        elif numbers[mid] < num:
            low = mid + 1
        else:
            high = mid
    return low if numbers[low] == num else None


def last_occurrence(numbers: list, num: int):
    low, high = 0, len(numbers) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if (numbers[mid] == num and mid == len(numbers) - 1) or\
                (numbers[mid] == num and numbers[mid+1] > num):
            return mid
        elif numbers[mid] <= num:
            low = mid + 1
        else:
            high = mid - 1
    if numbers[high] == num:
        return high
    return None

numbers = list(map(int, input().split()))
numbers = sort_numbers(numbers)
num = int(input())
print(numbers)
print(first_occurrence(numbers, num))
print(last_occurrence(numbers, num))
