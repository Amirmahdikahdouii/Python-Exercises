data = input()
count_of_students, classes, questions = list(map(lambda x: int(x), data.split()))
classes_data = {}
for i in range(1, classes+1):
    data = input()
    data = list(map(lambda x: int(x), data.split()))
    classes_data[i] = data[1:]
for i in range(questions):
    data = input()
    data = list(map(lambda x: int(x), data.split()))
    counter = data.pop(0)
    for i in range(counter):
        if i == 0:
            common_students = set(classes_data[data[i]])
            continue
        common_students = common_students & set(classes_data[data[i]])
    print(len(common_students))