s = set()
min_num = 0
first_num = True
output = ""
for i in range(int(input())):
    query = input()
    if query == "?":
        if len(s) == 0:
            print("EMPTY")
        else:
            print(min_num)
    else:
        num = int(query.split()[1])
        if first_num:
            first_num = False
            min_num = num
        elif num < min_num:
            min_num = num
        s.add(num)
