import random


def bubble_sort(collection):
    length = len(collection)
    for i in range(length - 1):
        sorted = True
        for j in range(length - 1 - i):
            if collection[j] > collection[j+1]:
                sorted = False
                collection[j], collection[j+1] = collection[j+1], collection[j]
        if sorted:
            break
    return collection


collection = [random.randint(0, 1000) for i in range(10)]
print(f"unordered list: {collection}")
print(f"ordered list: {bubble_sort(collection)}")
