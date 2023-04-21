def calculate_floor(chars):
    floor = 0
    for char in chars:
        if char == "U":
            floor += 1
        else:
            floor -= 1
    return floor