counter = int(input())
number = int(input())
m_reverse = 0
p = 0
while number != 0:
    num = number % (10**counter)
    number //= (10**counter)
    new_num = 0
    while num != 0:
        r = num % 10
        num //= 10
        new_num = (new_num * 10) + r
    m_reverse = (new_num*(10**p)) + m_reverse
    p += counter
print(m_reverse)