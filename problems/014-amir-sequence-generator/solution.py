counter = int(input())
prev_num = 0
for i in range(1, counter+1):
    if i % 2 == 0:
        prev_num *= 2
    else:
        prev_num = (prev_num*2) + 1
    print(prev_num)
