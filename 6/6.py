number = int(input())
counter = int(input())
numToBePalindrom = number % (10**counter)
number = number // (10**counter)
new_number = 0
while numToBePalindrom != 0:
    r = numToBePalindrom % 10
    new_number = (new_number*10) + r
    numToBePalindrom //= 10
number = (number * (10**counter)) + new_number
print(number)