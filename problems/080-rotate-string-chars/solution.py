def rotate(string: str, count: int):
    double_string = string + string
    if count <= len(string):
        return double_string[count:count+len(string)]
    count = count % len(string)
    return rotate(string, count)


string = input()
count = int(input())
print(rotate(string, count))
