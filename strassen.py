
def mul(A, B):
    result = []
    for i, r in enumerate(A):
        result.append([])
        for j in range(len(B[i])):
            result[i].append(0)
            for k, a in enumerate(r):
                result[i][j] += (a * B[k][j])    
    return result


def add(A, B):
    result = []
    for i in range(len(A)):
        result.append([])
        for j in range(len(A)):
            result[i].append(A[i][j] + B[i][j])
    return result


def sub(A, B):
    result = []
    for i in range(len(A)):
        result.append([])
        for j in range(len(A)):
            result[i].append(A[i][j] - B[i][j])
    return result


def submatrix(A, r, c):
    return [r[c[0]:c[1]] for r in A[r[0]:r[1]]]


def strassen(A, B, n_min = 2):

    n = len(A)

    if n <= n_min:
        return mul(A, B)
    else:
        m = n / 2
        u = (0, m)
        v = (m, n)

        P_1 = strassen(
            add(submatrix(A, u, u), submatrix(A, v, v)),
            add(submatrix(B, u, u), submatrix(B, v, v)),
            n_min
        )

        P_2 = strassen(
            add(submatrix(A, v, u), submatrix(A, v, v)),
            submatrix(B, u, u),
            n_min
        )

        P_3 = strassen(
            submatrix(A, u, u),
            sub(submatrix(B, u, v), submatrix(B, v, v)),
            n_min
        )

        P_4 = strassen(
            submatrix(A, v, v),
            sub(submatrix(B, v, u), submatrix(B, u, u)),
            n_min
        )

        P_5 = strassen(
            add(submatrix(A, u, u), submatrix(A, u, v)),
            submatrix(B, v, v),
            n_min
        )

        P_6 = strassen(
            sub(submatrix(A, v, u), submatrix(A, u, u)),
            add(submatrix(B, u, u), submatrix(B, u, v)),
            n_min
        )

        P_7 = strassen(
            sub(submatrix(A, u, v), submatrix(A, v, v)),
            add(submatrix(B, v, u), submatrix(B, v, v)),
            n_min
        )

        return merge(
            add(sub(add(P_1, P_4), P_5), P_7),
            add(P_3, P_5),
            add(P_2, P_4),
            add(sub(add(P_1, P_3), P_2), P_6)
        )


def merge(A, B, C, D):
    result = []

    for i in range(len(A)):
        result.append(A[i] + B[i])

    for i in range(len(A)):
        result.append(C[i] + D[i])

    return result

A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2],
    [3, 4, 5, 6]
]

print(strassen(A, A))
print(strassen(A, A, n_min=4))
print(strassen(A, A, n_min=1))