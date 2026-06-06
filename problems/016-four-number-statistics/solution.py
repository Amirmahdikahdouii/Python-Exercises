sum_numbers = 0
avg = 0
product = 1
max_number = -1000
min_number = 1000
for i in range(4):
    number = int(input())
    sum_numbers += number
    product *= number
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number
avg = sum_numbers / 4
print("Sum : %.6f" %sum_numbers)
print("Average : %.6f" %avg)
print("Product : %.6f" %product)
print("MAX : %.6f" %max_number)
print("MIN : %.6f" %min_number)