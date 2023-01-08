number = int(input())
flag = True
while number != 0:
    r = number %10
    number //= 10
    if r != 7 and r!=4:
        flag = False
        break
if flag:
    print("YES")
else:
    print("NO")