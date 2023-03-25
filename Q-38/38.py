words = ["tae", "aet", "tea", "eat", "rac", "bat", "ate", "arc", "car" ]
def anagram(words):
    output1 = []
    output2 = []
    for word in words:
        words_list = []
        for w in words:
            if "".join(sorted(word)) == "".join(sorted(w)):
                words_list.append(w)
        for w in words_list:
            words.remove(w)
        output1.append(words_list)
        output2.append([words_list[0]])
    return output1, output2
print(anagram(words))