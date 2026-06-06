names = {}
count = 0
for i in range(int(input())):
    f_name, l_name = input().split()
    if f_name in names:
        names[f_name].append(l_name)
    else:
        names[f_name] = [l_name]
else:
    for value in names.values():
        if len(value) > count:
            count = len(value)
print(count)