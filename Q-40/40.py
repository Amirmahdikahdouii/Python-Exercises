def calculator(number1, number2, opt="+"):
    if opt == "+":
        return number1 + number2
    elif opt == "-":
        return number1 - number2
    elif opt == "*":
        return number1 * number2
    elif opt == "/":
        return number1 / number2
    elif opt == "%":
        return number1 % number2
    elif opt == "**":
        return number1 ** number2


while True:
    opt = int(input(""" 0. Exit \n 1. + Addition \n 2. - Subtraction \n 3. * Multiplication \n 4. / Division \n 5. % Divide remaining \n 6. ** Exponentiation \n operation Number: """))
    if opt == 0:
        break
    elif opt not in range(7):
        print("Please Enter currect!")
        print("-----------------------")
        continue
    number1 = float(input("First Number: "))
    number2 = float(input("Second Number: "))
    if opt == 1:
        print(f"{number1} + {number2} = {calculator(number1, number2)}")
        print("----------------------------------------------")
    elif opt == 2:
        print(f"{number1} - {number2} = {calculator(number1, number2, '-')}")
        print("----------------------------------------------")
    elif opt == 3:
        print(f"{number1} * {number2} = {calculator(number1, number2, '*')}")
        print("----------------------------------------------")
    elif opt == 4:
        print(f"{number1} / {number2} = {calculator(number1, number2, '/')}")
        print("----------------------------------------------")
    elif opt == 5:
        print(f"{number1} % {number2} = {calculator(number1, number2, '%')}")
        print("----------------------------------------------")
    elif opt == 6:
        print(f"{number1} ** {number2} = {calculator(number1, number2, '**')}")
        print("----------------------------------------------")
