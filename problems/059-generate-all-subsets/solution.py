number = int(input())
sets = [[]]
for i in range(1, number+1):
    newlists = []
    for lst in sets:
        newlst = lst.copy()
        newlst.append(i)
        newlists.append(newlst)
    sets += newlists
sets.sort()
[print("{" + ", ".join([str(num) for num in s]) +"}") for s in sets]