c = int(input())
string = input()
flag = True
while flag:
    flag = False
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            string = string[:i] + string[i+2:]
            flag = True
            break
print(string)