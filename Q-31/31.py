data = input()
a,b = list(map(lambda x: int(x), data.split()))
if a < b:
    c_b = b
    b = a
    a=c_b
print(b)