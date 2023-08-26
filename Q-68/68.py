def get_numbers(numbers, min_limit, max_limit):
    min_check = lambda val: True if min_limit is None else min_limit <= val
    max_check = lambda val: True if max_limit is None else max_limit >= val
    return sorted([num for num in numbers if min_check(num) and max_check(num)])

# import random
# print([random.randint(0, 1000) for i in range(10)])
numbers = list(map(int, input().split(",")))

min_limit = input()
min_limit = None if min_limit == "" else int(min_limit)

max_limit = input()
max_limit = None if max_limit == "" else int(max_limit)

print(get_numbers(numbers, min_limit, max_limit))
