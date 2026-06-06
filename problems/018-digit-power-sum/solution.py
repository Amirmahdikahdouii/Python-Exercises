# Dighit Power Sum
number = int(input())
c_number = number
sum_of_nums = 0
while c_number != 0:
    r = c_number % 10
    c_number //= 10
    sum_of_nums += r
i = 0
flag = True
while flag:
    if sum_of_nums ** i == number:
        break
    if sum_of_nums ** i > number:
        flag = False
    i += 1
if flag:
    print("YES")
else:
    print("NO")
