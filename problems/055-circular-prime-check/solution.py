def get_count_digit(number: int):
    """
    Function to get count of number digits.
    """
    digits = 0
    while number != 0:
        number //= 10
        digits += 1
    return digits


number = int(input())
digits = get_count_digit(number)
flag = True
for i in range(digits):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            flag = False
            break
    r = number % 10
    number //= 10
    number = r * 10 ** (digits - 1) + number
    if not flag:
        print("False")
        break
else:
    print("True")
