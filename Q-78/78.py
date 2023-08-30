from random import randint
class OneTimePadCipher:
    def __init__(self, string):
        self.string = string
        self.key = {chr(i): randint(100, 999) for i in range(97, 123)}
        self.cipher = [randint(100, 999) for i in range(len(string))]
        
    
    def encrypt(self):
        cipher_code = []
        for i, char in enumerate(self.string):
            cipher_code.append((self.key[char] + self.cipher[i]) * self.cipher[i])
        return cipher_code
    
    def decrypt(self, cipher_code: list):
        string = ""
        decrypt_keys = dict(zip(self.key.values(), self.key.keys()))
        for i, num in enumerate(cipher_code):
            key = num / self.cipher[i] - self.cipher[i]
            string += decrypt_keys[key]
        return string
    
cipher = OneTimePadCipher("amir")
print(cipher.encrypt())
print(cipher.decrypt(cipher.encrypt()))