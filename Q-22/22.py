# Nearly Lucky Number
number = int(input())
countOfLuckyNumbers = 0
while number != 0:
    r = number % 10
    number //= 10
    if r == 7 or r == 4:
        countOfLuckyNumbers += 1
if countOfLuckyNumbers == 0:
    flag = False
else:
    flag = True
while countOfLuckyNumbers != 0:
    r = countOfLuckyNumbers % 10
    countOfLuckyNumbers //= 10
    if r != 7 and r != 4:
        flag = False
        break
if flag:
    print("YES")
else:
    print("NO")
