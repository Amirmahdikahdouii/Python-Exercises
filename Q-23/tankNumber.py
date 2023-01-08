number = int(input())
countZero = 0
countNonZero = 0
while number != 0:
    r = number % 10
    number //= 10
    if r == 0:
        countZero += 1
        continue
    countNonZero += 1
if countZero > countNonZero:
    print("YES")
else:
    print("NO")