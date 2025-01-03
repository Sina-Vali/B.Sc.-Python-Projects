m = int(input(""))
L = []
for i in range(m):
    L.append(input(""))


def power_set(L):
    E = []
    if len(L) == 0:
        return [[]]
    else:
        F = []
        for item in power_set(L[:-1]):
            F.append(item + [L[-1]])
        return power_set(L[:-1]) + F


E = power_set(L)
for i in range(len(E)):
    E[i].sort()
E.sort()
E.sort(key=len)
print(E)
