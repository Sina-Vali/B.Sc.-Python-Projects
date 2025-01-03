def splitter(string):
    from itertools import product
    all_comb = list(product([0, 1], repeat = len(string)-1))
    for comb in all_comb:
        string_ = [string]
        for i in range(len(string)-2, -1, -1):
            if comb[i]:
                save = string_[0]
                del string_[0]
                string_.insert(0, save[i+1:])
                string_.insert(0, save[:i+1])
        yield string_


string = input('')
L = []
for cut in splitter(string):
    if len(cut) == 4:
        x = 0
        for item in cut:
            if 0 <= int(item) <= 255:
                if item[0] == '0':
                    if item == '0':
                        x += 1
                else:
                    x += 1
            if x == len(cut):
                L.append('.'.join(cut))
L.sort()
for item in L:
    print(item)
