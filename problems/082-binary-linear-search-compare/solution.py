def binary_search(numbers: list, num: int):
    low = 0
    high = len(numbers) - 1
    steps = 0
    while low <= high:
        steps += 1
        mid = low + (high - low) // 2
        if numbers[mid] > num:
            high = mid - 1
        elif numbers[mid] < num:
            low = mid + 1
        elif numbers[mid] == num:
            return mid, steps
    return None, steps


def linear_search(numbers: list, num: int):
    steps = 0
    for i, number in enumerate(numbers):
        steps += 1
        if number == num:
            return i, steps
    return None, steps


numbers = range(100_000_000)
print(f"Binary Search: {binary_search(numbers, 514_112)}")
print(f"Linear Search: {linear_search(numbers, 514_112)}")
