from itertools import combinations, chain


def combine_elements(collection):
    return chain.from_iterable(combinations(collection, r) for r in range(1, len(collection)+1))
    return [list(combinations(collection, r)) for r in range(1, len(collection)+1)]


collection = list(map(lambda x: x, input().split(",")))

[print(combination) for combination in list(combine_elements(collection))]
