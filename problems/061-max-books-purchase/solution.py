count, money = list(map(int, input().split()))
prices = list(map(int, input().split()))
count = 0
for book in prices:
    if book <= money:
        money -= book
        count += 1
    else:
        break
print(count)