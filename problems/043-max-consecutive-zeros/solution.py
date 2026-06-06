data = input()
c = counter = 0
for char in data:
    if char == "0":
        c += 1
        if c > counter:
            counter = c
    else:
        c = 0
print(counter)