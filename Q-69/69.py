# Top-One algorithm
def get_top_one(numbers):
    data = {}
    max_count = 0
    top_ones = []
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
