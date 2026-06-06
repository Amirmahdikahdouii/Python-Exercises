number = int(input())
flag = True
for i in range(2, number // 2 + 1):
    if number % i == 0:
        flag = False
        break

if flag and not (number <= 1):
    print(f"{number} is Prime")
else:
    print(f"{number} is'nt prime")
