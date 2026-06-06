encoder = lambda string: [ord(char.lower()) - 96 for char in string]
decoder = lambda numbers: "".join(chr(num + 96) for num in numbers)

while True:
    user_choose = int(input("1. To encode string Enter 1: \n2. To Decode string Enter 2\n0. To exit Enter 0:\n"))
    if user_choose == 0:
        break
    elif user_choose == 1:
        print(encoder(input()))
    elif user_choose == 2:
        numbers = list(map(int, input("seprate numbers by , and numbers should be 1 <= x <= 26 !:").split(",")))
        print(decoder(numbers))
    else:
        print("Try Again!")
    print("----------------------------------")