counter = int(input())
output = {"person": "", "amount": 0}
for i in range(counter):
    data = input()
    person, amount = data.split()
    amount = int(amount)
    if amount > output['amount']:
        output = {"person": person, "amount": amount}
print(output['person'])