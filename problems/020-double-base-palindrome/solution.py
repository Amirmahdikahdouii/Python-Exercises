# Double Based Palindromic
for number in range(1000, 0, -1):
    c_number = number
    palind_of_number = 0
    while c_number != 0:
        r = c_number % 10
        c_number //= 10
        palind_of_number = (palind_of_number * 10) + r
    if palind_of_number != number:
        continue
    numberInBinary = 0
    p = 0
    while number != 0:
        r = number % 2
        number //= 2
        numberInBinary = (r*(10**p)) + numberInBinary
        p += 1
    c_numberInBinary = numberInBinary
    palindNumberInBinary = 0
    while c_numberInBinary != 0:
        r = c_numberInBinary % 10
        c_numberInBinary //= 10
        palindNumberInBinary = (palindNumberInBinary*10) + r
    if palindNumberInBinary == numberInBinary:
        print(f"Number: {palind_of_number}, number in binary: {numberInBinary}")
