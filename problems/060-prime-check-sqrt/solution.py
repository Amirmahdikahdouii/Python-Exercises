def prime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    for i in range(2, int(number**.5)+2):
        if number % i == 0:
            return False
    return True
number = int(input())
print("YES" if prime(number) else "NO")