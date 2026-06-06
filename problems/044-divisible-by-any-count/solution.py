data = input()
number, *nums = list(map(lambda x: int(x), data.split()))
counter = 0
for i in range(1, number+1):
    if True in [i % num == 0 for num in nums]: counter += 1
print(counter)