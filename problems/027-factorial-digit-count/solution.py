number = int(input())
fact = 1
for i in range(1, number+1):
    fact *= i
counter = 0
print(fact)
while fact!=0:
    r = fact %10
    fact//=10
    counter += 1
print(counter)