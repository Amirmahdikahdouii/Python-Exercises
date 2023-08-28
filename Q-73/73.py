def is_isomorphic(string1: str, string2: str):
    if len(string1) != len(string2):
        return False
    pairs = {}
    for i in range(len(string1)):
        if string1[i] not in pairs:
            if string2[i] not in pairs.values():
                pairs[string1[i]] = string2[i]
            else:
                return False
        else:
            if pairs[string1[i]] != string2[i]:
                return False
    return True


string1, string2 = list(map(lambda x: x, input().split()))
print(is_isomorphic(string1, string2))
