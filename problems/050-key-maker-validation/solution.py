while True:
    a = input()
    cut_c, keys_c = list(map(lambda x: int(x), a.split()))
    if cut_c == 0 and keys_c == 0:
        break
    a = input()
    a = list(map(lambda x: int(x), a.split()))
    c = 0
    for i in range(keys_c):
        key_depth = input()
        key_depth = list(map(lambda x: int(x), key_depth.split()))            
        if False in [False for j in range(len(key_depth)) if key_depth[j] > a[j]]:
            continue
        c += 1
    print(c)