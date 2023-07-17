def fibbo(number):
    if number <= 1:
        return number
    return fibbo(number-1)+fibbo(number-2)

number = int(input())
nums = []
i = 1
f = 0
while True:
    f = fibbo(i)
    if f > number:
        break
    nums.append(f)
    i += 1
new_number = []
nums.reverse()
if number in nums:
    nums.pop(nums.index(number))
num = number
for i in nums:
    if number < i:
        continue
    number -= i
    new_number.append(i)
print(f"{num} = " + " + ".join([str(x) for x in new_number]))