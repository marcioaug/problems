
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

def main():
    n, m, o = map(int, raw_input().split())
    
    A = []
    B = []

    for i in range(n):
        A.append(map(int, raw_input().split()))

    for i in range(m):
        B.append(map(int, raw_input().split()))

    C = mul(A, B)

    for r in C:
        for i, c in enumerate(r):
            sys.stdout.write(str(c))
            if i < len(r):
                sys.stdout.write(' ')
        sys.stdout.flush()
        print('')

if __name__ == '__main__':
    main()
