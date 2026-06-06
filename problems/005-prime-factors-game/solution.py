number1 = int(input())
number2 = int(input())
s1 = s2 = 0
def getPrimeConstSum(number):
    s = 0
    flag = True
    for i in range(2, number//2+1):
        if number % i == 0 and (i == 2 or i == 3 or i == 5 or i == 7):
            flag = False
            s += i
    if flag:
        return number
    return s
s1 = getPrimeConstSum(number1)
s2 = getPrimeConstSum(number2)
if s1 > s2:
    print("M")
elif s1 < s2:
    print("S")
else:
    print("E")
