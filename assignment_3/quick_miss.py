def quick_miss(C, D, p, r, miss_left=None):
    if p < r:
        q = partition(C, p, r)
        if C[q] == D[q]:
            print(f'{C[q]} == {D[q]}, q = {q}, p = {p}, r = {r}')
            print(f'quick_miss(C, D, {q+1}, {r}, False)')
            return quick_miss(C, D, q+1, r, False)
        else:
            print(f'{C[q]} != {D[q]}, q = {q}, p = {p}, r = {r}')
            print(f'quick_miss(C, D, {p}, {q-1}, True)')
            return quick_miss(C, D, p, q-1, True)
    # else:
    if miss_left:
        print(f'\nmiss_left = {miss_left}, p = {p}, r = {r}, D {D}')
        print(f'D[p] = {D[p]}')
        return D[p]
    else:
        print(f'\nmiss_left = {miss_left}, p = {p}, r = {r}, D {D}')
        print(f'D[r+1] = {D[r+1]}')
        return D[r+1]

def partition(A, p, r):
    print(f'\n\nbefore: C {A}, p = {p}, r = {r}')
    q = p
    for i in range(p, r):
        if A[i] < A[r]:
            A[i], A[q] = A[q], A[i]
            q += 1
    A[q], A[r] = A[r], A[q]
    print(f'after : C {A}, q = {q}, C[q] = {A[q]}')
    return q


# C = [1, 2, 3, 6, 5]
# D = [1, 2, 3, 4, 5, 6]

C = [1, 2, 3, 6, 5]
D = [1, 2, 3, 4, 5, 6]

result = quick_miss(C, D, 0, 4)

print(f'result is: {result}')