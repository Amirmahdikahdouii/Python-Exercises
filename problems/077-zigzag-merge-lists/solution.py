def zigzag_iterator(numbers1, numbers2):
    zigzag_list = []
    for i in range(min(len(numbers1), len(numbers2))):
        zigzag_list.extend([numbers1.pop(0), numbers2.pop(0)])
    else:
        if numbers1:
            zigzag_list.extend(numbers1)
        elif numbers2:
            zigzag_list.extend(numbers2)
    return zigzag_list


numbers1 = list(map(int, input().split()))
numbers2 = list(map(int, input().split()))
print(zigzag_iterator(numbers1, numbers2))
