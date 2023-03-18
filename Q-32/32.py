counter = int(input())
a = input()
b = input()
c = 0
while counter != 0:
    counter -= 1
    if a[counter] != b[counter]:
        c += 1
if c % 2 == 0:
    print(c//2)
else:
    print("NO")