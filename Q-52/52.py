def convert_to_binary(number):
    """ Convert Number from base 10 into base 2 """
    
    if number == 0:
        return ""
    return f"{convert_to_binary(number//2)}{number%2}"

a = int(input("Please Enter Records Count: "))
b = int(input("Please Enter Sells Count: "))
m_base_10, m_base_2 = [], []

for i in range(a):
    line, line_base_2 = [], []
    for j in range(b):
        number = int(input("Sell Number: "))
        line.append(number)
        line_base_2.append(convert_to_binary(number))
    print("---------------")
    m_base_10.append(line)
    m_base_2.append(line_base_2)

print(m_base_10)
print(m_base_2)