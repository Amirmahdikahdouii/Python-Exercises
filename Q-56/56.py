def get_count_digits(number):
    """
        Function to get count of number digits.
    """
    digits = 0
    while number != 0:
        number //= 10
        digits += 1
    return digits


n1, n2 = list(map(int, input().split()))
if n1 % 2 == 0:
    # For check just Odd Numbers
    n1 += 1

digits = get_count_digits(n1)
circular_primes = []
for number in range(n1, n2 + 1, 2):
    if number in circular_primes:
        continue
    if number >= n2:
        digits = get_count_digits(n2)
    flag = True
    primes = []
    for i in range(digits):
        for j in range(2, number//2+1):
            if number % j == 0:
                flag = False
                break
        if not flag:
            break
        if number >= n1:
            primes.append(number)
        r = number % 10
        number //= 10
        number = r * 10 ** (digits - 1) + number
    if flag and number not in circular_primes:
        circular_primes.extend(primes)
circular_primes.sort()
[print(i) for i in circular_primes]
