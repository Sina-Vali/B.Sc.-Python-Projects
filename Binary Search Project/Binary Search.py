L = []
A = input("").split(' ')
m = int(A[0])
n = A[1]
for i in range(m):
    L.append(input(""))


def f(L, m, n, left = 0, right = len(L)):
    if left == right:
        return left - 1
    mid = left + (right - left)//2
    if L[mid] == n:
        return mid
    if L[mid] > n:
        return f(L, m, n, left, mid)
    return f(L, m, n, mid+1, right)


print(f(L, m, n, left = 0, right = len(L)))