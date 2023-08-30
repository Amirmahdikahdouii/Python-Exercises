def two_sum(numbers: list, target: int):
    """
    This Function is only useful when numbers list is sorted ascending!
    """
    i1 = 0
    i2 = len(numbers) - 1
    while i1 < i2:
        s = numbers[i1] + numbers[i2]
        if s == target:
            return [numbers[i1], numbers[i2]]
        elif s > target:
            i2 -= 1
        else:
            i1 += 1
    return None


def sort_ascending(numbers: list) -> list:
    length = len(numbers)
    for i in range(length - 1):
        is_sorted = True
        for j in range(length - 1 - i):
            if numbers[j] > numbers[j+1]:
                is_sorted = False
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        if is_sorted:
            return numbers
    return numbers


numbers = list(map(int, input().split()))
target = int(input())
sorted_numbers = sort_ascending(numbers)
print(two_sum(sorted_numbers, target))
