from string import ascii_letters

def encrypt(string:str, key:int):
    encrypt_code = ""
    for char in string:
        if char not in ascii_letters:
            encrypt_code += char
            continue
        encrypt_code += ascii_letters[(ascii_letters.index(char) + key) % len(ascii_letters)]
    return encrypt_code

def decrypt(string: str, key: int):
    return encrypt(string, key * -1)

while True:
    user_choose = input("1. Enter 1 for encrypte sentense: \n2. Enter 2 for decrypte sentense: 3. Enter \"end\" for exit program\n")
    if user_choose.lower() == "end":
        print("Thanks!")
        break
    try:
        if int(user_choose) == 1:
            string = input("Please enter your sentense: ")
            key = input("Please Enter your key shift: ")
            print(encrypt(string, key))
        elif int(user_choose) == 2:
            string = input("Please enter your sentense: ")
            key = input("Please Enter your key shift: ")
            print(decrypt(string, key))
        else:
            raise ValueError
    except ValueError:
        print("Something Wrong happend, please try again!")