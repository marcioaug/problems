#! /usr/bin/python3
from math import ceil, log2

def build(A, tree):

    for i in range(len(A)):
        tree[len(A) + i] = A[i]

    for i in reversed(range(1, len(A))):
        tree[i] = max(tree[2 * i], tree[2 * i + 1])


def query(l, r, f, tree, n):
    l = l + n
    r = r + n

    res = f

    while l < r:
        if l & 1 > 0:
            res = max(tree[l], res)
            l += 1

        if r & 1 > 0:
            r -= 1
            res = max(tree[r], res)

        l = l // 2
        r = r // 2
    
    return res > f

def main():
    n = int(input())
    sections = []

    for _ in range(n):
        sections.append(int(input()))

    tree = [1 for _ in range(2 * len(sections))]
    
    build(sections, tree)

    count = 0
    for i in range(n): 
        if query(0, i, sections[i], tree, n) and query(i, n, sections[i], tree, n):
            count += 1

    print(count)

if __name__ == '__main__':
    main()