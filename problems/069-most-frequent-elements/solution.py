from collections import Counter
# Top-One algorithm


def get_top_one(numbers):
    max_count = 0
    top_ones = []
    """
    You can do this instead of creating data:
    data = Counter(numbers)
    the Counter object, make a dictionary with key of elements and value is count of elements in iterable
    """
    data = {}
    for number in numbers:
        if number in data:
            data[number] += 1
        else:
            data[number] = 1
    max_count = max(data.values())
    for key in data.keys():
        if data[key] == max_count:
            top_ones.append(key)
    return top_ones


numbers = list(map(int, input().split(",")))
print(get_top_one(numbers))
