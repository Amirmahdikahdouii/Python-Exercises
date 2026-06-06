def symmetric(items):
    r_i = -1
    for i in range(len(items) // 2):
        if items[i] != items[r_i]: return False
        r_i += -1
    return True
print(symmetric([1,2,3,4,3,2,1])) # True
print(symmetric([1,2,3,4,5])) # False