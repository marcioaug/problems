import time
import sys


def mul(A, B):
    result = []
    for i in range(len(A)):
        result.append([])
        for j in range(len(B[0])):
            result[i].append(0)
            for k in range(len(A[0])):
                result[i][j] += (A[i][k] * B[k][j])    
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
    return [r[int(c[0]):int(c[1])] for r in A[int(r[0]):int(r[1])]]


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


def fill(A):
    result = []

    if len(A) > len(A[0]):
        increment = [0 for _ in range(len(A) - len(A[0]))]
        for r in A:
            result.append(r + increment[:])
    else:
        result = A[:]
        increment = [0 for _ in range(len(A[0]))]
        for _ in range(len(A[0]) - len(A)):
            result.append(increment[:])

    return result


def enlarge(A, n=None):

    q = 1

    if not n:
        n = len(A)

    while 2**q <= n: q += 1
    to_complete = 2**q - len(A)

    if to_complete > 0:
        diff_col = [0 for _ in range(to_complete)]
        complete_row = [0 for _ in range(n + to_complete)]

        for i in range(len(A)):
            A[i] += diff_col[:]

        for _ in range(to_complete):
            A.append(complete_row[:])
    
    return A


def Strassen(A, B, n_min = 2):

    i = len(A)
    j = len(B[0])

    if len(A) != len(A[0]):
        A = fill(A)

    if len(B) != len(B[0]):
        B = fill(B)

    max_len = max(len(A), len(B))
   
    return [r[:j] for r  in strassen(enlarge(A, max_len), enlarge(B, max_len), n_min=n_min)[:i]]