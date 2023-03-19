def calculate_floor(actions):
    floor = 0
    for char in actions:
        if char == "U":
            floor += 1
        else:
            floor -= 1
    return floor
