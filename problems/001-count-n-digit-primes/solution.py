n = int(input())
count = 0
for i in range(10**(n-1)+1, 10**n):
    flag = True
    for j in range(2, i//2+1):
        if i % j == 0:
            flag = False
            break
    print(i)
    if flag:
        count += 1
print(count)