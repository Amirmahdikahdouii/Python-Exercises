numbers = []
for i in range(5):
    word = input()
    for word_index in range(len(word)):
        if word[word_index: word_index+6] == "MOLANA":
            numbers.append(i + 1)
            break
        elif word[word_index: word_index+5] == "HAFEZ":
            numbers.append(i + 1)
            break
        if len(word[word_index: word_index+5]) < 5:
            break
if len(numbers) == 0:
    print("NOT FOUND!")
else:
    [print(i, end=" ") for i in numbers]
