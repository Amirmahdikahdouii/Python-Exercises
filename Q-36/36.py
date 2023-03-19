counter = int(input())
states = []
while counter != 0:
    counter -= 1
    cards = input()
    c = 0
    if cards[0] == "0":
        flag = False
    else:
        flag = True
    for char in cards:
        if char == '1':
            if flag == False:
                c += 1
            flag = True
        else:
            flag = False
    else:
        if cards[-1] == "0":
            c += 1
    states.append(c)
[print(i) for i in states]