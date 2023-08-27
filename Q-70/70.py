from string import ascii_letters
is_lowercase_char = lambda char: True if ord(char) >= 97 and ord(char) <= 122 else False
is_uppercase_char = lambda char: True if ord(char) >= 65 and ord(char) <= 90 else False

def saesar_encode(string: str):
    encoded_string = ""
    for char in string:
        if is_lowercase_char(char):
            if ord(char) + 3 > 122:
                char = chr(ord(char) - 23)
            else:
                char = chr(ord(char) + 3)
        elif is_uppercase_char(char):
            if ord(char) + 3 > 90:
                char = chr(ord(char) - 23)
            else:
                char = chr(ord(char) + 3)
        encoded_string += char
    return encoded_string

def seasar_decode(string: str):
    decoded_string = ""
    for char in string:
        if is_lowercase_char(char):
            if ord(char) - 3 < 97:
                char = chr(ord(char) + 23)
            else:
                char = chr(ord(char) - 3)
        elif is_uppercase_char(char):
            if ord(char) - 3 < 65:
                char = chr(ord(char) + 23)
            else:
                char = chr(ord(char) - 3)
        decoded_string += char
    return decoded_string

while True:
    user_choose = input("1. Enter 1 for encode sentense: \n2. Enter 2 for decode sentence: \n3. Enter \"end\" for decode sentence:\n")
    if user_choose.lower() == "end":
        print("Thanks!")
        break
    try:
        if int(user_choose) == 1:
            string = input("Enter your sentence: ")
            print(f"The encode sentense is: \n{saesar_encode(string)}")
            print('--------------------------------------------------')
        elif int(user_choose) == 2:
            string = input("Enter your sentence: ")
            print(f"The decode sentense is: \n{seasar_decode(string)}")
            print('--------------------------------------------------')
        else:
            raise ValueError
    except ValueError:
        print("Input choose is not correct!")
