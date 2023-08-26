from itertools import combinations


def combine_elements(collection):
    return [list(combinations(collection, r)) for r in range(1, len(collection)+1)]


collection = list(map(lambda x: x, input().split(",")))

for combination_list in combine_elements(collection):
    for combination in combination_list:
        print(combination)
